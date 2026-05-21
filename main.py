from repository import FlashcardRepository
from learning import learning_mode
from progress import progress_check_mode
from survival_mode import survival_mode
from add_flashcard import add_flashcard_mode


def main():
    repo = FlashcardRepository()
    while True:
        print("\n============================")
        print("      PROGRAM: FISZKI       ")
        print("============================")
        print("1. Tryb Nauki (losowy)")
        print("2. Sprawdź postępy (poziomy)")
        print("3. Tryb Przetrwania")
        print("4. Dodaj własną fiszkę")
        print("5. Zamknij program")
        print("============================")

        c = input("Wybierz opcję: ").strip()

        if c == '1':
            learning_mode(repo)
        elif c == '2':
            progress_check_mode(repo)
        elif c == '3':
            survival_mode(repo)
        elif c == '4':
            add_flashcard_mode(repo)
        elif c == '5':
            print("Zamykanie... Do zobaczenia!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()