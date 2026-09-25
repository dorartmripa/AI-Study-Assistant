from ai import ask_ai, summarise
from menu import display_menu

def main():
    while True:
        choice = display_menu()

        if choice == 1:
            note = input('Enter file name (must be .txt): ')
            question = input('Ask a question: ')

            answer = ask_ai(question, note)
        elif choice == 2:
            note = input('Enter file name (must be .txt): ')

            answer = summarise(note)
        elif choice == 7:
            print('\nGoodbye!')
            break
        else:
            print('\nThat feature isn\'t implemented yet.')

if __name__ == '__main__':
    main()