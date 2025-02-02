class Library:

    # 140-225pm) nordic box
    # (240-245pm)(2/2/25)(Sun) this chapter done

    books_available = 100    # Total books in library

    # TODO: Implement class methods to manage book lending
    # TODO: Implement return_books method to increase the number of books available        

    def lend_books(num1: int) -> None:
        Library.books_available -= num1

    def return_books(num1: int) -> None:
        Library.books_available += num1


# Don't change the code below
print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
