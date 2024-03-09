def main():
    book_path ='books/frankenstein.txt'
    texts = get_book_text(book_path)
    word_count = word_counter(texts)
    letter_dict = letter_counter(texts)
    letter_list_sorted = dict_to_sorted_list(letter_dict)

    print(f"--- Start Report of {book_path} ---")
    print()
    print(f"Word count comes to {word_count}")
    print()
    
    for item in letter_list_sorted:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print()
    print(f"--- END OF REPORT ---")    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def dict_to_sorted_list(count_dict):
    sorted_list = []
    for ch in count_dict:
        sorted_list.append({"char": ch, "num": count_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def letter_counter(text):
    characters = {}
    for x in text:
        low = x.lower()
        if low in characters:
            characters[low] += 1
        else:
            characters[low] = 1
    #print(characters)
    return characters

if __name__ == '__main__':
    main()
