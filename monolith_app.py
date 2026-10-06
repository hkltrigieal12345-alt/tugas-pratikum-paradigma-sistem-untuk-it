from flask import Flask, jsonify, request

app = Flask(__name__)

# Database bohongan (In-memory)
books = [
    {
        "id": 1,
        "title": "Belajar Flask",
        "stock": 5
    }
]

orders = []


# =========================
# FITUR BUKU
# =========================
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# =========================
# FITUR PESANAN
# =========================
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    book_id = data.get('book_id')

    # Cek stok buku langsung dari variabel global
    for book in books:
        if book['id'] == book_id and book['stock'] > 0:
            book['stock'] -= 1

            order = {
                "id": len(orders) + 1,
                "book_id": book_id,
                "status": "berhasil"
            }

            orders.append(order)

            return jsonify(order), 201

    return jsonify({
        "error": "Buku tidak ditemukan atau stok habis"
    }), 400


# =========================
# MENJALANKAN APLIKASI
# =========================
if __name__ == '__main__':
    # Monolith berjalan di port 5000
    app.run(port=5000, debug=True)