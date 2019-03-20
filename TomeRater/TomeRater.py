class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        print("{name} email updated.".format(name=self.name))

    def get_average_rating(self):
        sum_ratings = 0
        count = 0
        try:
            for rate in self.books.values():
                if rate == None:
                    continue
                count += 1
                sum_ratings += rate
            return sum_ratings / count
        except ZeroDivisionError:
            return "No ratings"

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def __repr__(self):
        return "User {name}\nEmail: {email}\nBooks read: {read}".format(name=self.name, email=self.email, read=len(self.books))

""" THIS DOESN'T WORK, I DON'T KNOW WHY.
    def __eq__(self, other_user):
        if (self.name == other_user.name) and (self.email == other_user.email):
            return True
        else:
            return False
"""
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{title} ISBN changed.".format(title=self.title))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        sum_ratings = 0
        count = 0
        try:
            for rate in self.ratings:
                if rate == None:
                    continue
                count += 1
                sum_ratings += rate
            return sum_ratings / count
        except ZeroDivisionError:
            return "No ratings for {title}".format(title=self.title)

    def __eq__(self, other_book):
        if (self.title == other_book.title) and (self.isbn == other_book.isbn):
            return True
        else:
            return False

    def __repr__(self):
        return self.title

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if self.users.get(email) == None:
            print("No user with email {email}!".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        if email in self.users:
            print("User with email {email} already exists. Try another user.".format(email=email))
        else:
            new_user = User(name, email)
            if self.users.get(email) == None:
                self.users[email] = new_user
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_reads_book = None
        most_reads = 0
        for book, reads in self.books.items():
            if reads > most_reads:
                most_reads_book = book
        return most_reads_book

    def highest_rated_book(self):
        highest_rate_book = None
        highest_rate = 0
        for book in self.books:
            if book.get_average_rating() > highest_rate:
                highest_rate = book.get_average_rating()
                highest_rate_book = book
        return highest_rate_book

    def most_positive_user(self):
        most_pos_user = None
        most_pos_rate = 0
        for user in self.users.values():
            if user.get_average_rating() > most_pos_rate:
                most_pos_rate = user.get_average_rating()
                most_pos_user = user
        return most_pos_user