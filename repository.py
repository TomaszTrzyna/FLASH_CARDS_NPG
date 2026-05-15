import json
import os
from models import Flashcard


class FlashcardRepository:
    def __init__(self, filename="flashcards.json"):
        self.filename = filename
        self.flashcards = []
        self.load()

    def load(self):
        #Wczytanie fiszek z JSON jako obiekty typu Flashcard lub stworzenie bazowego w przypadku jego braku

    def save(self):
        #Zapis fiszek poprzez ich konwersję powrotną

    def add(self, pl, en, level):
        #Dodanie nowej fiszki o ile nie istnieje i zapis

    def get_all(self):
        #Zwrócenie wszystkich fiszek

    def get_by_level(self, level):
        #Zwrócenie tylko fiszek na danym levelu

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