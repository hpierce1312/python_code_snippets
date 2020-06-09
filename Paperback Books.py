book = {
        'Rowling':{'name':'Harry Potter', 'type':'ebook', 'price':16.87},
        'Brown':{'name':'Da Vinci Code', 'type':'Paperback', 'price':17.35},
        'Grisham':{'name':'The Client', 'type':'Paperback', 'price':12.39},
        'Child':{'name':'Jack Reacher', 'type':'Hardcover', 'price':18.19},
        'Christie':{'name':'Curtain', 'type':'Paperback', 'price':13.48}
        }

def newList(book):
    price = 0
    bookList = []

    for key, value in book.items():
        if value["type"] == "Paperback":
            bookList.append(value["name"])
            price += value["price"]

    bookList.append(price)
    print(bookList)

newList(book)