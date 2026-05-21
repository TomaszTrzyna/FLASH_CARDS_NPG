import random
def ask_flashcard(fc, all_flashcards):
    direction = random.choice(['pl_to_en', 'en_to_pl'])
    if direction == 'pl_to_en':
        question = fc.pl
        valid_answers = [f.en.lower() for f in all_flashcards if f.pl.lower() == question.lower()]
        lang = "po angielsku"
    else:
        question = fc.en
        valid_answers = [f.pl.lower() for f in all_flashcards if f.en.lower() == question.lower()]
        lang = "po polsku"
    print(f"\nPytanie: {question} ({lang})")
    answer = input("Twoja odpowiedź (lub 'q' aby przerwać): ").strip().lower()
    if answer == 'q':
        return None
    if answer in valid_answers:
        print("BRAWO! To poprawna odpowiedź.")
        return True
    else:
        print(f"BŁĄD! Poprawne tłumaczenia to: {', '.join(set(valid_answers))}")
        return False