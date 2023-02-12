from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(180))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)

    return {"books": "output"}

@app.route('/books/<id>')
def get_drink(id):
    book = Book.query.get_or_404(id)
    return jsonify(){"book_name": book.book_name, "author": book.author, "publisher": book.publisher}
@app.route('/books', methods=['POST'])
def add_book():
    drink = Book(name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': drink.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if drink is None:
        return["error": "not found"]
    db.session.delete(book)
    db.session.commit()
    return{"message": "great!@"}
