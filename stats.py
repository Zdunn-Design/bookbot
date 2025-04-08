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
    #print(characters)
    return characters


def sort_on(d):
    return d["num"]


def dict_to_sorted_list(count_dict):
    sorted_list = []
    for ch in count_dict:
        sorted_list.append({"char": ch, "num": count_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list