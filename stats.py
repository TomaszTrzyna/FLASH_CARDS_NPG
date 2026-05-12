import time

def print_stats(start_time,total):
    elapsed_time = time.time() - start_time
    print("\n--- STATYSTYKI KOŃCOWE ---")
    print(f"Czas trwania: {elapsed_time:.2f} sekund")
    print(f"Liczba prób: {total}")