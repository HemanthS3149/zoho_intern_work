from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(20), nullable=False, unique=True)
    genre = db.Column(db.String(50))
    published_year = db.Column(db.Integer)

    def __repr__(self):
        return f'<Book {self.title}>'

# Routes
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        genre = request.form['genre']
        published_year = request.form['published_year']

        new_book = Book(title=title, author=author, isbn=isbn, genre=genre, published_year=published_year)

        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            print(e)  # Print the exception for debugging
            return render_template('add_book.html')

    return render_template('add_book.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.isbn = request.form['isbn']
        book.genre = request.form['genre']
        book.published_year = request.form['published_year']

        try:
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            print(e)  # Print the exception for debugging
            return 'Error updating book'

    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        try:
            db.session.delete(book)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            print(e)  # Print the exception for debugging
            return 'Error deleting book'

    return render_template('delete_book.html', book=book)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
