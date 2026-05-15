class Flashcard:
    def __init__(self, pl, en, level):
        self.pl = pl
        self.en = en
        self.level = level

    def to_dict(self):
        return {"pl": self.pl, "en": self.en, "level": self.level}