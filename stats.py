import time

def print_stats(start_time,correct,total):
    elapsed_time = time.time() - start_time
    percent = (correct / total) * 100 if total > 0 else 0
    avg_time = elapsed_time / total if total > 0 else 0

    if percent >= 90:
        grade = "A"
    elif percent >= 75:
        grade = "B"
    elif percent >= 60:
        grade = "C"
    elif percent >= 40:
        grade = "D"
    else:
        grade = "F"



    print("\n--- STATYSTYKI KOŃCOWE ---")
    print(f"Czas trwania: {elapsed_time:.2f} sekund")
    print(f"Liczba prób: {total}")
    print(f"Poprawne odpowiedzi: {correct}")
    print(f"Skuteczność: {percent:.2f}%")
    print(f"Średni czas odpowiedzi: {avg_time:.2f} s")
    print(f"Ocena: {grade}")
    print("--------------------------\n")