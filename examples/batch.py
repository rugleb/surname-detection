import asyncio
import csv
from argparse import ArgumentParser
from itertools import islice
from typing import Dict, Iterator

from aiohttp import ClientSession

URL = "https://surname-detection.herokuapp.com/detect"


def read_words(path: str) -> Iterator:
    with open(path) as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            yield i, row["Word"]


def read_words_group(words: Iterator, size: int) -> Dict[int, str]:
    group = {}
    for i, word in islice(words, size):
        group[i] = word
    return group


def create_tasks(queue: Dict[int, str], session: ClientSession):
    tasks = []
    for i, word in queue.items():
        coroutine = get_confidence(session, word, i)
        task = asyncio.create_task(coroutine)
        tasks.append(task)
    return tasks


async def get_confidence(session: ClientSession, word: str, i: int):
    params = {
        "surname": word,
    }
    async with session.get(URL, params=params) as r:
        json = await r.json()
        return json["status"], json["data"], word, i


async def run(words: Iterator, session: ClientSession, max_chunk_size: int):
    queue: Dict[int, str] = {}

    while words:
        chunk_size = max_chunk_size - len(queue)
        chunk = read_words_group(words, chunk_size)

        queue.update(chunk)
        if not queue:
            break

        tasks = create_tasks(queue, session)
        for feature in asyncio.as_completed(tasks):
            ok, data, word, i = await feature
            if ok:
                assert word == queue.pop(i)
                prediction = data.pop("confidence")
                yield i, prediction


async def main() -> None:
    arg_parser = ArgumentParser(
        prog="python batch.py",
    )
    arg_parser.add_argument(
        "--test_path",
        dest="test_path",
        help="Input file path (default: %(default)r)",
        default="test.csv",
    )
    arg_parser.add_argument(
        "--results_path",
        dest="results_path",
        help="Output file path (default: %(default)r)",
        default="results.csv",
    )
    arg_parser.add_argument(
        "--chunk_max_size",
        dest="chunk_max_size",
        help="TCP/IP port to serve on (default: %(default)r)",
        type=int,
        default=200,
    )

    args = arg_parser.parse_args()
    words = read_words(args.test_path)

    with open(args.results_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=("Id", "Prediction"))
        writer.writeheader()

        async with ClientSession() as session:
            async for data in run(words, session, args.chunk_max_size):
                row = dict(zip(writer.fieldnames, data))
                writer.writerow(row)


if __name__ == "__main__":
    asyncio.run(main())
