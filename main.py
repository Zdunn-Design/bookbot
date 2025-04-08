import sys

from stats import (word_counter, letter_counter, dict_to_sorted_list)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    texts = get_book_text(book_path)
    word_count = word_counter(texts)
    letter_dict = letter_counter(texts)
    letter_list_sorted = dict_to_sorted_list(letter_dict)

    print(f"--- Start Report of {book_path} ---")
    print()
    print(f"{word_count} words found in the document")
    print()
    
    for item in letter_list_sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print()
    print(f"--- END OF REPORT ---")    


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    main()
