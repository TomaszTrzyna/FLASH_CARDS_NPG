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
            ("pies", "dog"), ("kot", "cat"), ("dom", "house"), ("woda", "water"), ("chleb", "bread"),
            ("mama", "mother"), ("tata", "father"), ("syn", "son"), ("córka", "daughter"), ("brat", "brother"),
            ("siostra", "sister"), ("słońce", "sun"), ("księżyc", "moon"), ("dzień", "day"), ("noc", "night"),
            ("jeden", "one"), ("dwa", "two"), ("trzy", "three"), ("czerwony", "red"), ("niebieski", "blue"),
            ("zielony", "green"), ("żółty", "yellow"), ("biały", "white"), ("czarny", "black"), ("duży", "big"),
            ("mały", "small"), ("zimny", "cold"), ("gorący", "hot"), ("dobry", "good"), ("zły", "bad"),
            ("szkoła", "school"), ("książka", "book"), ("jabłko", "apple"), ("mleko", "milk"), ("herbata", "tea")
        ]
        medium = [
            ("pomarańcza", "orange"), ("pomarańczowy", "orange"), ("samochód", "car"), ("auto", "car"),
            ("pociąg", "train"), ("rower", "bicycle"), ("miasto", "city"), ("ulica", "street"), ("sklep", "shop"),
            ("praca", "work"), ("pieniądze", "money"), ("zegarek", "watch"), ("czas", "time"), ("rok", "year"),
            ("tydzień", "week"), ("miesiąc", "month"), ("dzisiaj", "today"), ("jutro", "tomorrow"),
            ("wczoraj", "yesterday"),
            ("niebo", "sky"), ("deszcz", "rain"), ("śnieg", "snow"), ("wiatr", "wind"), ("drzewo", "tree"),
            ("kwiat", "flower"), ("rzeka", "river"), ("morze", "sea"), ("góra", "mountain"), ("ptak", "bird"),
            ("ryba", "fish"), ("obiad", "dinner"), ("śniadanie", "breakfast"), ("kawa", "coffee"), ("sok", "juice")
        ]
        hard = [
            ("wyzwanie", "challenge"), ("sukces", "success"), ("wyobraźnia", "imagination"), ("wiedza", "knowledge"),
            ("środowisko", "environment"), ("społeczeństwo", "society"), ("rozwój", "development"),
            ("doświadczenie", "experience"),
            ("możliwość", "opportunity"), ("odpowiedzialność", "responsibility"), ("niezależność", "independence"),
            ("bezpieczeństwo", "security"), ("przyszłość", "future"), ("przeszłość", "past"), ("obecność", "presence"),
            ("równowaga", "balance"), ("umiejętność", "skill"), ("cel", "goal"), ("marzenie", "dream"),
            ("podróż", "journey"), ("odkrycie", "discovery"), ("nauka", "science"), ("sztuka", "art"),
            ("zdrowie", "health"), ("choroba", "disease"), ("lekarstwo", "medicine"), ("pamięć", "memory"),
            ("wrażenie", "impression"), ("zachowanie", "behavior"), ("decyzja", "decision"), ("wolność", "freedom")
        ]

        for p, e in easy: data.append({"pl": p, "en": e, "level": 1})
        for p, e in medium: data.append({"pl": p, "en": e, "level": 2})
        for p, e in hard: data.append({"pl": p, "en": e, "level": 3})

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)