from stats import get_word_count
import sys

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
    path_to_file = sys.argv[1]
    file_contents = get_book_text(path_to_file)
    file_word_count = get_word_count(file_contents)
    char_counts = get_char_count(file_contents)
    print_report(path_to_file, file_word_count, char_counts)

def get_char_count(in_string: str) -> dict:
    chars = dict()
    for c in in_string:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def char_list_sort(in_dict:dict):
    return in_dict["count"]

def convert_char_dict_to_list(in_dict:dict)->list:
    out_list = []
    for key in in_dict:
        out_list.append({"char":key, "count":in_dict[key]})
    out_list.sort(reverse=True, key=char_list_sort)
    return out_list

def print_report(file_path:str, word_count:int, chars_dict:dict)->None:
    print(f"--- Begining report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()
    char_list = convert_char_dict_to_list(chars_dict)
    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["count"]} times")
    print("--- End report ---")
    return

def get_book_text(file_path : str) -> str:
    with open(file_path,"r") as fp:
        return fp.read()

if __name__ == "__main__":
    main()
