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