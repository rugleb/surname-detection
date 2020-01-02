import pathlib
import re
from typing import Any, Dict

import attr
import pandas as pd
from catboost import CatBoostClassifier

from project.abc import Dictable
from project.lib import read_pickle_file

__all__ = (
    "Prediction",
    "SurnameDetector",
)


@attr.s(slots=True, frozen=True)
class Prediction(Dictable):
    confidence: float = attr.ib()

    def to_dict(self) -> Dict:
        return attr.asdict(self)


@attr.s(slots=True, frozen=True)
class SurnameDetector:
    model: CatBoostClassifier = attr.ib()

    VOWELS = 'аеёиоуыэюя'
    CONSONANTS = 'бвгджзйклмнпрстфхчцшщъь'

    @classmethod
    def from_file(cls, path: pathlib.Path) -> "SurnameDetector":
        model = read_pickle_file(path)
        return cls(model)

    def predict(self, word: str) -> Prediction:
        features = self.extract_features(word)
        data = pd.DataFrame([features])
        probability = self.model.predict_proba(data)
        confidence = probability[0, 1]
        return Prediction(confidence)

    def extract_features(self, word: str) -> Dict[str, Any]:
        data = {
            'word_len': len(word),
            'is_first_letter_capital': word.istitle(),
            'is_symbol_in_word': re.match(r"\W", word) is not None,
            'last_letter': word[-1:].lower(),
            'letter_before_last': word[-2:-1].lower(),
            'second_letter_before_last': word[-3:-2].lower(),
            'third_letter_before_last': word[-4:-3].lower(),
            'first_letter': word[:1].lower(),
            'n_vowels': sum(map(word.lower().count, self.VOWELS)),
            'n_consonants': sum(map(word.lower().count, self.CONSONANTS)),
        }
        return data
