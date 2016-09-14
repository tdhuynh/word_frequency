
exclude = ",'.\"[]()!?/:$-@*"

with open("sample.txt") as open_file:
    book = open_file.read().lower()
    for item in exclude:
        book = book.replace(item, "")


print(book)
