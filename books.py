books = []

#Add 3 books to shelf
for i in range(3):
    book = dict()
    book["author"] = input("Enter an author: ")
    book["title"] = input("Enter a title: ")
    books.append(book)

#Print list of books
for book in books:
    print(book)
