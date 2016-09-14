
from string import punctuation
ignore = """a, able, about, across, after, all, almost, also, am, among, an, and, any, are, as, at, be,
 because, been, but, by, can, cannot, could, dear, did, do, does, either, else, ever, every,
 for, from, get, got, had, has, have, he, her, hers, him, his, how, however, i, if, in, into, is,
 it, its, just, least, let, like, likely, may, me, might, most, must, my, neither, no, nor,
not, of, off, often, on, only, or, other, our, own, rather, said, say, says, she, should,
since, so, some, than, that, the, their, them, then, there, these, they, this, tis, to, too,
 twas, us, wants, was, we, were, what, when, where, which, while, who, whom, why, will, with,
 would, yet, you, your"""

with open("sample.txt") as open_file:
    book = open_file.read().lower()
    for item in punctuation:
        book = book.replace(item, "")
        book = book.replace(ignore, "")

    print(book)

#     book_list = book.split()
#     book_dict = {}
#     for word in book_list:
#         if word in book_dict:
#             book_dict[word] += 1
#         else:
#             book_dict[word] = 1
#     book_sort = sorted(book_dict.items(), key=lambda x: x[1])
#     book_sort = book_sort[:-21:-1]
#
# for item in book_sort:
#     print(item)
