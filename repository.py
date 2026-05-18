import json
import os
from models import Flashcard


class FlashcardRepository:
    def __init__(self, filename="flashcards.json"):
        self.filename = filename
        self.flashcards = []
        self.load()

    def load(self):
        if not os.path.exists(self.filename):
            self._create_initial_data()
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.flashcards = [
                Flashcard(item['pl'], item['en'], item.get('level', 1)) for item in data
            ]

    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([fc.to_dict() for fc in self.flashcards], f, ensure_ascii=False, indent=4)

    def add(self, pl, en, level):
        pl_l = pl.lower()
        en_l = en.lower()
        for fc in self.flashcards:
            if fc.pl.lower() == pl_l and fc.en.lower() == en_l:
                return False

        self.flashcards.append(Flashcard(pl, en, level))
        self.save()
        return True

    def get_all(self):
        return self.flashcards

    def get_by_level(self, level):
        return [fc for fc in self.flashcards if fc.level == level]

    def _create_initial_data(self):

        #Generowanie bazy fiszek

        data = []
        easy = [
            ("pies", "dog")] #Stworzenie więcej fiszek bazowych
        medium = [
            ("pomarańcza", "orange"), ("pomarańczowy", "orange")]
        hard = [
            ("wyzwanie", "challenge")]

        for p, e in easy: data.append({"pl": p, "en": e, "level": 1})
        for p, e in medium: data.append({"pl": p, "en": e, "level": 2})
        for p, e in hard: data.append({"pl": p, "en": e, "level": 3})

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)