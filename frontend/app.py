from flask import Flask, render_template, request, redirect, flash, send_file
import mysql.connector as sq
import time
import isbnlib 
from jinja2 import Markup
import bookGenerator

class book:
	def __init__(self,isbn,name):
		self.name = name
		self.cover = isbnlib.cover(isbn)['thumbnail']
		self.description = isbnlib.desc(isbn)
		self.description = self.description.replace('\n', '<br>')
		self.description = Markup(self.description)


bookGenerator.generateBooks()

app = Flask(__name__)
app.secret_key = 'secret_key'

LoggedIn = False
user = ''

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'users'
}

@app.route('/')
def index():
	if(not LoggedIn):
		books = ['CommunistManifesto','MeinKampf', 'StarshipTroopers', 'TheNightingale']
		Books=[]

		for b in books:
			f = open('static/isbns.txt','r')
			isbn = ""
			for line in f:
				if line[0:len(b)]==b:
					isbn = line[len(b)+1:]
			Book = book(isbn,b)
			Books.append(Book)
			f.close()
			
		return render_template('Free.html',LoggedIn = LoggedIn, books = Books)
	else:
		return redirect('/MyLibrary')

@app.route('/Ebooks')
def ebooks():
	if not LoggedIn:
		return redirect('/')
	
	books = []
	f = open('static/isbns.txt', 'r')
	for line in f:
		b = line[0:line.index(' ')]
		books.append(b)
	f.close()
	print(books)

	Books = []
	for b in books:
		f = open('static/isbns.txt','r')
		isbn = ""
		for line in f:
			print(line,end='\n')
			if line[0:len(b)]==b:
				isbn = line[len(b)+1:]
				print(isbn,end='\n\n')
				break
		if isbn != "":
			Book = book(isbn,b)
			Books.append(Book)
		f.close()	



	return render_template('Ebooks.html', LoggedIn = LoggedIn, books=Books)

@app.route('/book/<bookName>')
def bookpage(bookName):
	f = open('static/isbns.txt','r')
	isbn=''
	for line in f:
		if str(bookName) == line[0:len(bookName)]:
			isbn = line[len(bookName)+1:]
			#print(isbn)
			f.close()
			break
	#print("Name: " + bookName)
	#print("Isbn: " + isbn)
	books=[]
	if LoggedIn:
		connection = sq.connect(**config)
		cursor = connection.cursor(buffered=True)
		cursor.execute('SELECT * FROM liberdb WHERE username = %s',(user,))
		rows = cursor.fetchall()
		cursor.close()
		connection.close()
		
		books = rows[0][2]
		if books is not None:
			books = books.split()
		else:
			books = []
		print(books)

	Book = book(isbn,bookName)
	return render_template('bookpage.html', book = Book,LoggedIn = LoggedIn,books=books)

@app.route('/MyLibrary')
def mylibrary():
	Books = []

	if LoggedIn:
		connection = sq.connect(**config)
		cursor = connection.cursor(buffered=True)
		cursor.execute('SELECT * FROM liberdb WHERE username = %s',(user,))
		rows = cursor.fetchall()
		cursor.close()
		connection.close()
		print(rows)

		books = rows[0][2]
		print(type(books))
		if books is None:
			print("Books is empty and therefore a none-type object")
			books = []

		else:
			books = books.split()
			print(books)
			
		
		for b in books:
			f = open('static/isbns.txt','r')
			isbn = ""
			for line in f:
				if line[0:len(b)]==b:
					isbn = line[len(b)+1:]
			if isbn != '':
				Book = book(isbn,b)
				Books.append(Book)
			f.close()

	return render_template('MyLibrary.html', LoggedIn = LoggedIn, books=Books)

@app.route('/Featured')
def featured():
	books = ['MurderInTheMews', 'HarryPotter', 'HungerGame', 'MeinKampf']
	Books=[]
	for b in books:
		f = open('static/isbns.txt','r')
		isbn = ""
		for line in f:
			if line[0:len(b)]==b:
				isbn = line[len(b)+1:]
		if isbn != '':
			Book = book(isbn,b)
			Books.append(Book)
		f.close()

	return render_template('Featured.html', LoggedIn = LoggedIn, books=Books)

@app.route('/Login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		connection = sq.connect(**config)

		cursor = connection.cursor(buffered=True)
		global user
		user = request.form['email']
		password = request.form['pwd']

		cursor.execute('SELECT * FROM liberdb WHERE username = %s',(user,))
		rows = cursor.fetchone()
		cursor.close()
		connection.close()
		if rows is None:
			flash("Incorrect Credentials!")
		elif password == rows[1]:
			global LoggedIn
			LoggedIn = True
			return redirect('/')
		else:
			flash("Incorrect Credentials!")
	
	return render_template('Login.html', LoggedIn = False)

@app.route('/Logout')
def logout():
	global LoggedIn 
	LoggedIn = False
	return redirect('/')

@app.route('/Register', methods=['POST', 'GET'])
def register():
	if request.method == 'POST':
		connection = sq.connect(**config)
		cursor = connection.cursor(buffered=True)
		user = request.form['email']
		password = request.form['pwd']
		cpassword = request.form['cpwd']

		if user is None or (password) is None or (cpassword) is None:
			flash("All fields necessary!")
		
		elif password != cpassword:
			flash("Passwords do not Match!")

		else:
			cursor.execute("INSERT INTO liberdb VALUES(%s,%s,NULL)",(user,password,))
			connection.commit()
			cursor.close()
			connection.close()
			flash("Succesfully Registered!")
			time.sleep(2)
			return redirect('/Login')

	return render_template('Register.html', LoggedIn = False)

@app.route('/download/<bookname>')
def download(bookname):
	return send_file("static/Books/"+bookname+'.epub', as_attachment=True)

@app.route('/addtolib/<bookname>')
def addToLib(bookname):
	print("Book to be Added: " + str(bookname))
	connection = sq.connect(**config)
	cursor = connection.cursor(buffered=True)

	cursor.execute('SELECT * FROM liberdb WHERE username = %s',(user,))
	rows = cursor.fetchone()
	
	books = rows[2]
	
	print("Books: " + str(books))

	
	if books == '' or books is None:
		books = (bookname)
	else:
		print("Entered else conditon boi")
		books = books.split()
		books.append(' '+bookname)
		books = ' '.join(map(str,books))

	print("Updated books list: " + books)

	cursor.execute('UPDATE liberdb SET books_owned=%s WHERE username=%s',(books,user))
	connection.commit()
	cursor.close()
	connection.close()

	flash("Book Added!")

	return redirect('/book/'+bookname)
	


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)