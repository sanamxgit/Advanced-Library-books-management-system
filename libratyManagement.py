def addBook(books):
  name = input("Enter the book name:")
  author = input("Enter the author name:")
  year = input("year of publication")

 
  book = {
      'Title': name,
      'Author': author,
      'Year': year
  }

  books.append(book)
  print("\n New book added succefully")

def removeBook(books):
    name = input("Enter the name of the book to remove: ")
    for book in books:
        if book['Title'].lower() == name.lower():
            books.remove(book)
            print("\nBook removed successfully!\n")
            return
    print("\nBook not found!\n")

def searchBook (books):
    name = input("Search book name: ")

    for book in books:
      if book['Title'].lower() == name.lower():
            print("\nBook found:")
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Year: {book['Year']}\n")
            return
      print("\nBook not found!\n")

def bookList(books):
    if not books:
      print("\n no books available")
    else:
      print("\nList of books")
      for book in books:
          print(f"Title: {book['Title']}")
          print(f"Author: {book['Author']}")
          print(f"Year: {book['Year']}")
          print("---------------")
    
def main():
    books= []
    while True:
      print("1. Add a new book")
      print("2. Remove Book")
      print("3. Search for Book")
      print("4. List all the books")
      print("5. Exit")
      choice = input("Enter your choice:")
      if choice == '1':
        addBook(books)
      elif choice =='2':
        removeBook(books)
      elif choice == '3':
        searchBook(books)
      elif choice == '4':
        bookList(books)
      elif choice == '5':
        print("Closing!")
        break
      else:
        print("Invalid option")

if __name__ == "__main__":
     main()
        








