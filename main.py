def main():
    book_path = "books/frankenstein.txt"
    text = get_text_book(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text)
    print(f"--- Iniciando relatório de {book_path}--- \n")
    print(f"{num_words} palavras encontradas nesse livro\n")
    print_char_count(convert_to_list(chars_dict))
    print("\n---Fim do relatório---")

def get_text_book(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def get_num_characters(text):
    lowered_text = text.lower()
    char_cont = dict()
    for char in lowered_text:
        if not char.isalpha():
            pass
        elif char not in char_cont:
            char_cont[char] = 1
        elif char in char_cont:
            char_cont[char] +=  1
    return char_cont

def sort_on(dict):
    return dict["count"]

def convert_to_list(data):
    char_list = []
    for key in data:
        char_list.append({ 'name': key, 'count': data[key]})
    return char_list

def print_char_count(list_chars):
    list_chars.sort(reverse=True, key=sort_on)
    for count in list_chars:
        print(f"O caractér '{count['name']}' foi encontrado {count['count']} vezes")
main()
