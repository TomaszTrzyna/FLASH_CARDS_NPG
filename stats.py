import time

def print_stats(start_time,correct,total):
    elapsed_time = time.time() - start_time
    percent = (correct / total) * 100 if total > 0 else 0
    print("\n--- STATYSTYKI KOŃCOWE ---")
    print(f"Czas trwania: {elapsed_time:.2f} sekund")
    print(f"Liczba prób: {total}")
    print(f"Poprawne odpowiedzi: {correct}")
    print(f"Skuteczność: {percent:.2f}%")
    print("--------------------------\n")