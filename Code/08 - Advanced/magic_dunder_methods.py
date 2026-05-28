# Magic Methods in Python
# They are also known as 'dunder' methods (double underscore methods) because they are surrounded by double underscores.
# They are automatically called by Python's built-in functions such as print and len, or by operators such as + and ==.
# They allow us to define or customize the behavior of our objects.


class Book:
    def __init__(self, title, author):  # This is the constructor method that initializes the attributes of the Book class.
        self.title = title
        self.author = author

    def __str__(self):  # This method is called when we print an object of the Book class. It returns a string representation of the object.
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):  # This method is called when we compare two objects of the Book class using the == operator.
        return self.title == other.title and self.author == other.author
    
    def __contains__(self, keyword):  # This method is called when we use the 'in' operator to check if a keyword is present in the title or author of the book.
        return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()
    
    def __getitem__(self, index):  # This method allows us to use the indexing operator [] to access the title or author of the book.
        if index == 0 or index == -2:
            return self.title
        elif index == 1 or index == -1:
            return self.author
        else:
            return "Index out of range, use 0 for title and 1 for author. Negative indices also work: -2 for title and -1 for author."


# Create some book objects to test the magic methods
book1 = Book("Ramayana", "Maharishi Valmiki")
book2 = Book("Mahabharata", "Maharishi Ved Vyas")
book3 = Book("Asthadhyayi", "Maharishi Panini")
book4 = Book("Ramayana", "Maharishi Valmiki")

# Test the magic methods
print(book1)  # Output: Ramayana by Maharishi Valmiki
print(book2)  # Output: Mahabharata by Maharishi Ved Vyas
print(book3)  # Output: Asthadhyayi by Maharishi Panini

print("maha" in book1)  # Output: True
print("Maharishi" in book2)  # Output: True

print(book1[0])  # Output: Ramayana
print(book2[1])  # Output: Maharishi Ved Vyas
print(book3[2])  # Output: Index out of range, use 0 for title and 1 for author. Negative indices also work: -2 for title and -1 for author.

print(book1 == book2)  # Output: False
print(book1 == book4)  # Output: True
