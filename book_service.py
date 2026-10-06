from flask import Flask, jsonify

app = Flask(__name__)

# Database khusus Book Service
books = [
    {
        "id": 1,
        "title": "Belajar Flask",
        "stock": 5
    }
]


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)

    return jsonify({
        "error": "Not found"
    }), 404


if __name__ == '__main__':
    # Book Service berjalan di port 5001
    app.run(port=5001, debug=True)