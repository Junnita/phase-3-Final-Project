class Book:
    def __init__(self, title, copy_number, available=True):
        self.title = title
        self.copy_number = copy_number
        self.available = available
        self.author = None
        self.publisher = None

    def assign_author(self, author):
        self.author = author

    def assign_publisher(self, publisher):
        self.publisher = publisher

    def __str__(self):
        return f"Title: {self.title}, Copy Number: {self.copy_number}, Available: {self.available}, Author: {self.author.name if self.author else 'Unknown'} Publisher: {self.publisher.name if self.publisher else 'Unknown'}"