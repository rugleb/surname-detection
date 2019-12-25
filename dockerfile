FROM python:3.7

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

RUN useradd -r -UM app
USER app

ENTRYPOINT [ "./entrypoint.sh" ]
