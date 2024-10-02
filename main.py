def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    word_count = get_word_count(book_content)
    char_counts = get_unique_char_count(book_content)
    sorted_char_counts = get_char_count_sorted_list(char_counts)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n\n")

    for k in sorted_char_counts:
        print(f"The '{k["char"]}' character was found {k["count"]} times")
    print("--- End Report ---")


def get_book_text(file_path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def sort_on(dict):
    return dict["count"]

def get_unique_char_count(text):
    normalized_text = text.lower()
    char_dict = {}
    for t in normalized_text:
        if(t.isalpha()):
            if t in char_dict:
                char_dict[t] += 1
            else:
                char_dict[t] = 1
    
    return char_dict

def get_char_count_sorted_list(char_dict):
    dict_list = []
    for item in char_dict:
        dict_list.append({"char": item, "count": char_dict[item]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

main()