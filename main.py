def main():
    book_path ='books/frankenstein.txt'
    texts = get_book_text(book_path)
    word_count = word_counter(texts)
    print(f"word count comes to {word_count}")
    letter_dict = letter_counter(texts)
    print(letter_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def letter_counter(text):
    characters = {}
    for x in text:
        low = x.lower()
        if low in characters:
            characters[low] += 1
        else:
            characters[low] = 1
    return characters

if __name__ == '__main__':
    main()
