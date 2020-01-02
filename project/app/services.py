from typing import Dict

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
    def from_file(cls, path: str) -> "SurnameDetector":
        model = read_pickle_file(path)
        return cls(model)

    def predict(self, word: str) -> Prediction:
        words = pd.Series([word])
        data = self.extract_features(words)
        predict = self.model.predict_proba(data)
        confidence = predict[0, 1]
        return Prediction(confidence)

    def extract_features(self, words: pd.Series) -> pd.DataFrame:
        data = pd.DataFrame()
        data['word_len'] = words.str.len()

        is_first_letter_capital = words.str.slice(0, 1).str.isupper()
        data['is_first_letter_capital'] = is_first_letter_capital

        is_symbol_in_word = words.str.contains(r"\W")
        data['is_symbol_in_word'] = is_symbol_in_word

        last_letter = words.str.slice(-1, None).str.lower()
        data['last_letter'] = last_letter

        letter_before_last = words.str.slice(-2, -1).str.lower()
        data['letter_before_last'] = letter_before_last

        second_letter_before_last = words.str.slice(-3, -2).str.lower()
        data['second_letter_before_last'] = second_letter_before_last

        third_letter_before_last = words.str.slice(-4, -3).str.lower()
        data['third_letter_before_last'] = third_letter_before_last

        first_letter = words.str.slice(0, 1).str.lower()
        data['first_letter'] = first_letter

        n_vowels = words.str.lower().str.count(f'[{self.VOWELS}]')
        data['n_vowels'] = n_vowels

        n_consonants = words.str.lower().str.count(f'[{self.CONSONANTS}]')
        data['n_consonants'] = n_consonants

        return data
