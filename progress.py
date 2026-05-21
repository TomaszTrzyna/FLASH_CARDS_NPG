import random
import time

from ask import ask_flashcard
from stats import print_stats

def progress_check_mode(repo):
    print("\nWybierz poziom trudności testu:")
    print("1. Łatwy (Podstawy)")
    print("2. Średni (Komunikacja)")
    print("3. Trudny (Zaawansowany)")

    choice = input("Wybór: ").strip()

    if choice not in ['1', '2', '3']:
        print("Nieprawidłowy poziom.")
        return

    level_f = repo.get_by_level(int(choice))
    all_f = repo.get_all()

    if not level_f:
        print("Brak fiszek na tym poziomie.")
        return

    random.shuffle(level_f)
    test_set = level_f[:15]
    correct, total = 0, 0
    start_time = time.time()

    print(f"\nRozpoczynasz sprawdzian z poziomu {choice}. Do rozwiązania: {len(test_set)} zadań.")

    for fc in test_set:
        result = ask_flashcard(fc, all_f)
        if result is None: break
        total += 1
        if result: correct += 1

    if total > 0: print_stats(start_time, correct, total)