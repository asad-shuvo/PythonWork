class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("The Book Object Has Been Deleted")


book=Book('Python Rock','Jose',500)
print(str(book))
print(len(book))
del book
print(book)