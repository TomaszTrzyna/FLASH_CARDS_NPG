import random
import time


def learning_mode(repo):
    all_f = repo.get_all()
    flashcards = list(all_f)
    random.shuffle(flashcards)
    correct, total = 0, 0
    start_time = time.time()
