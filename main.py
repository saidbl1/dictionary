from PyDictionary import PyDictionary
import os

dictionary = PyDictionary()

term_size = os.get_terminal_size()

# translation
# Synonym
# Antonyms
# translation

arrow_unicode = chr(129138)
red_dot = chr(128308)
while True:

    print("\nWhat do you want?\n")
    print("1. Meaning")
    print("2. Synonym")
    print("3. Antonyms")
    print("4. translation")
    print("5. Exit the program")
    choice = input("\n\033[93m>\033[0m Enter your choice: ")

    if choice == "1":
        word = input('\nEnter your word: ')
        print(f"\n\033[95m {arrow_unicode} \033[0m {dictionary.meaning(word)}")
        # print("\033[92m\u2500\033[0m" * term_size.columns)
        while True:

            print("\n1. Find the Meaning of another word?")
            print("2. Go back to previous menu")
            again = input("\n\033[93m>\033[0m Enter your choice: ")
            if again == "1":
                word = input("\nEnter a word: ")
                print(
                    f"\n\033[95m {arrow_unicode} \033[0m {dictionary.meaning(word)}")
            elif again == "2":
                break
            else:
                print("\n" + red_dot + "\033[91m Enter a valid choice.\033[0m")
    elif choice == "2":
        word = input('\nEnter your word: ')
        print(f"\n\033[95m {arrow_unicode} \033[0m {dictionary.synonym(word)}")
        while True:

            print("\n1. Find the Synonym of another word?")
            print("2. Go back to previous menu")
            again = input("\n\033[93m>\033[0m Enter your choice: ")
            if again == "1":
                word = input("\nEnter a word: ")
                print(
                    f"\n\033[95m {arrow_unicode} \033[0m {dictionary.synonym(word)}")
            elif again == "2":
                break
            else:
                print("\n" + red_dot + "\033[91m Enter a valid choice.\033[0m")
    elif choice == "3":
        word = input('\nEnter your word: ')
        print(f"\n\033[95m {arrow_unicode} \033[0m {dictionary.antonym(word)}")
        while True:

            print("\n1. Find the antonym of another word?")
            print("2. Go back to previous menu")
            again = input("\n\033[93m>\033[0m Enter your choice: ")
            if again == "1":
                word = input("\nEnter a word: ")
                print(
                    f"\n\033[95m {arrow_unicode} \033[0m {dictionary.antonym(word)}")
            elif again == "2":
                break
            else:
                print("\n" + red_dot + "\033[91m Enter a valid choice.\033[0m")
    elif choice == "4":
        word = input('\nEnter your word: ')
        language = input(
            "\nWhat language you want to translate to. ex(fr, hi, ge, ar): ")
        print(
            f"\n\033[95m {arrow_unicode} \033[0m {dictionary.translate(word, language)}")
        while True:

            print("\n1. Translate another word:")
            print("2. Go back to previous menu")
            again = input("\n\033[93m>\033[0m Enter your choice: ")
            if again == "1":
                word = input("\nEnter a word: ")
                print(
                    f"\n\033[95m {arrow_unicode} \033[0m {dictionary.translate(word, language)}")
            elif again == "2":
                break
            else:
                print("\n" + red_dot + "\033[91m Enter a valid choice.\033[0m")
    elif choice == "5":
        print("Program Ended")
        quit()
    else:
        print("\n" + red_dot + "\033[91m Enter a valid choice.\033[0m")
