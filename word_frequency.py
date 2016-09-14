
from string import punctuation

with open("sample.txt") as open_file:
    book = open_file.read().lower()
    for item in punctuation:
        book = book.replace(item, "")

    book_list = book.split()
    book_dict = {}
    for word in book_list:
        if word in book_dict:
            book_dict[word] += 1
        else:
            book_dict[word] = 1
    print(sorted(book_dict.items(), key=lambda x: x[1]))
