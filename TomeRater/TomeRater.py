class TomeRater(object):
	def __init__(self):
		self.users = {}
		self.books = {}
	def __repr__(self):
		string = "Tome Rater with Books: \n"
		for book in self.books.keys():
			string += (book.title + "\n")
		string += "and Users: "
		for user in self.users.values():
			string += (user.name + "\n")
		return string
	def create_book(self, title, isbn):
		return Book(title, isbn)
	def create_novel(self, title, author, isbn):
		return Fiction(title, author, isbn)
	def create_non_fiction(self, title, subject, level, isbn):
		return NonFiction(title, subject, level, isbn)
	def add_book_to_user(self, book, email, rating = None):
		if email in self.users.keys():
			self.users[email].read_book(book, rating)
			if rating:
				book.add_rating(rating)
			if book in self.books.keys():
				if self.books[book]:
					self.books[book] += 1
				else:
					self.books[book] = 1
			else:
				self.books[book] = 1
		else:
			print("No user with this email!")
	def add_user(self, name, email, user_books = None):
		new_user = User(name, email)
		self.users[email] = new_user
		if user_books:
			for book in user_books:
				self.add_book_to_user(book, email)
	def print_catalog(self):
		for key in self.books.keys():
			print(key)
	def print_users(self):
		for value in self.users.values():
			print(value)
	def get_most_read_book(self):
		maxNum = 0
		maxBook = ""
		for key in self.books.keys():
			if self.books[key] > maxNum:
				maxNum = self.books[key]
				maxBook = key
		return maxBook
	def highest_rated_book(self):
		maxNum = 0
		maxBook = ""
		for book in self.books.keys():
			if book.get_average_rating() > maxNum:
				maxNum = book.get_average_rating()
				maxBook = book
		return maxBook
	def most_positive_user(self):
		maxNum = 0
		maxUser = ""
		for user in self.users.values():
			if user.get_average_rating() > maxNum:
				maxNum = user.get_average_rating()
				maxUser = user
		return maxUser
	def __eq__(self, other):
		return self.users = other.users and self.books = other.books
class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}
	
	def get_email(self):
		return self.email

	def change_email(self, address):
		self.email = address

	def __repr__(self):
		return "User {x}, email: {y}, books read: {z}".format(x=self.name,y=self.email,z=len(self.books))
	def read_book(self, book, rating = None):
		self.books[book] = rating
	def get_average_rating(self):
		avg_rating = 0
		for value in self.books.values():
			if value:
				avg_rating += value
		avg_rating = avg_rating / len(self.books)
		return avg_rating

	def __eq__(self, other_user):
		return self.name == other_user.name and self.email == other_user.email
class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
	def get_title(self):
		return self.title
	def get_isbn(self):
		return self.isbn
	def __repr__(self):
		return self.title
	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
	def add_rating(self, rating):
		if (rating >= 0 and rating <= 4):
			self.ratings.append(rating)
		else:
			print("Invalid Rating")
	def get_average_rating(self):
		avg_rating = 0
		for rating in self.ratings:
			avg_rating += rating
		avg_rating = avg_rating / len(self.ratings)
		return avg_rating
	def	__hash__(self):		
		return hash((self.title, self.isbn))
		
	def __eq__(self, other_book):
		return self.title == other_book.title and self.isbn == other_book.isbn
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
	def __repr__(self):
		return "{x} by {y}".format(x=self.title,y=self.author)
	def get_author(self):
		return self.author
class NonFiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level
	def __repr__(self):
		return ("{x}, a {y} manual on {z}".format(x=self.title,y=self.level,z=self.subject))
	def get_level(self):
		return self.level
	def get_subject(self):
		return self.subject
		
		
