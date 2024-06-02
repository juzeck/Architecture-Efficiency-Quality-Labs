class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False


class ExtendedLibraryBook:
    def __init__(self, library_book):
        self.library_book = library_book
        self.condition = "Good"  # Default condition
        self.additional_info = "No additional info available"

    def check_out(self):
        return self.library_book.check_out()

    def return_book(self):
        return self.library_book.return_book()

    def get_book_info(self):
        return {
            "title": self.library_book.title,
            "author": self.library_book.author,
            "publication_year": self.library_book.publication_year,
            "condition": self.condition,
            "additional_info": self.additional_info,
            "is_checked_out": self.library_book.is_checked_out
        }

    def set_condition(self, condition):
        self.condition = condition

    def set_additional_info(self, info):
        self.additional_info = info


book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
extended_book = ExtendedLibraryBook(book)
print(extended_book.check_out())
print(extended_book.check_out())
print(extended_book.get_book_info())
extended_book.set_condition("Worn")
extended_book.set_additional_info("First edition")
print(extended_book.get_book_info())
