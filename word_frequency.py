
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
    book_sort = sorted(book_dict.items(), key=lambda x: x[1])
    book_sort = book_sort[:-21:-1]

for a, b in book_sort:
    print("{} {}".format(a, b))
