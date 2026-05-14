def progress_check_mode(repo):
    print("\nWybierz poziom trudności testu:")
    print("1. Łatwy (Podstawy)")
    print("2. Średni (Komunikacja)")
    print("3. Trudny (Zaawansowany)")

    choice = input("Wybór: ").strip()

    if choice not in ['1', '2', '3']:
        print("Nieprawidłowy poziom.")
        return

    level_f = ....get_by_level(int(choice)) #do uzupełnienia po zrobieniu bazy
    all_f = ....get_all() #do uzupelnienia