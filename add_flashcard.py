#!/usr/bin/python
# -*- coding: utf-8 -*-
def add_flashcard_mode(repo):
    print("\n--- KREATOR NOWEJ FISZKI ---")
    pl = input("Słowo po polsku: ").strip()
    en = input("Słowo po angielsku: ").strip()
    print("Poziom trudności: 1 (łatwy), 2 (średni), 3 (trudny)")
    lvl = input("Wybierz poziom: ").strip()

    if pl and en and lvl in ['1', '2', '3']:

        if repo.add(pl, en, int(lvl)):