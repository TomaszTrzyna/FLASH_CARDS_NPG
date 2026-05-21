import random
import time
from ask import ask_flashcard
from stats import print_stats

def learning_mode(repo):
    all_f = repo.get_all()
    flashcards = list(all_f)
    random.shuffle(flashcards)
    correct, total = 0, 0
    start_time = time.time()
    for fc in flashcards:
        result = ask_flashcard(fc, all_f)
        if result is None: break
        total += 1
        if result: correct += 1

    if total > 0:
        print_stats(start_time, correct, total)