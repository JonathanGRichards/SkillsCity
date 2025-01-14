class Book:
  def __init__(self, title, author, availability):
    self.title = title
    self.author = author
    self.availability = availability

class Member:
  def __init__(self, name, id):
    self.name = name
    self.id = id
    self.books = []

  def __str__(self):
    return f"Name: {self.name}, ID: {self.id}, Books checked out: {', '.join(self.books)}"

class Library:
  def __init__(self):
    self.books = [];
    self.members = [];

  def add_book(self, book):
    self.books.append(book)

  def register(self, member):
    self.members.append(member)
    
  def lend_book(self, member_id, book_title):
    book_found = False
    for book in self.books:
      if (book.title == book_title) and (book.availability == True):
        for member in self.members:
          if member.id == member_id:
            member.books.append(book_title);
        book.availability = False
        book_found = True;
        print(f"{book_title} loaned to member id: {member_id}.")
    if book_found == False:
      print("Book unavailiable.")

  def return_book(self, member_id, book_title):
    found = False
    for member in self.members:
      if (member.id == member_id) and (book_title in member.books):
        member.books.remove(book_title)
        for book in self.books:
          if (book.title == book_title):
            book.availability = True
            found = True;
            print(f"{book_title} returned from member id: {member_id}.")

    if found == False:
      print("Error, book or member not found.")
    

book1 = Book('The Stand', 'Stephen King', True)
book2 = Book('To Kill a Mocking Bird', 'Harper Lee', True)

member1 = Member('John', 1)
member2 = Member('Sally', 2)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.register(member1)
library.register(member2)

# TESTS

# library.lend_book(1, 'The Stand')
# library.lend_book(1, 'To Kill a Mocking Bird')
# print(library.members[0].books)
# library.return_book(1, 'The Stand')
# print(library.members[0].books)
# print(library.books[0].availability)
# print(library.books[1].availability)




    