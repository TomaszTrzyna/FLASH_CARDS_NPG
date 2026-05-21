import random
import time
from ask import ask_flashcard
from stats import print_stats

def survival_mode(repo):
    all_f = repo.get_all()
    flashcards = list(all_f)
    random.shuffle(flashcards)
    correct, total, mistakes = 0, 0, 0
    start_time = time.time()


    print("\n--- TRYB PRZETRWANIA: 3 BŁĘDY I KONIEC ---")

    for fc in flashcards:
        result = ask_flashcard(fc, all_f)
        if result is None: break
        total += 1
        if result:
            correct += 1
        else:
            mistakes += 1
            print(f"Liczba błędów: {mistakes}/3")
            if mistakes >= 3:
                print("\nPRZEGRAŁEŚ! Wykorzystałeś wszystkie szanse.")
                break

    if total > 0: print_stats(start_time, correct, total)