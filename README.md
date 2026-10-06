# LANGKAH-LANGKAH MENJALANKAN PROGRAM

## 1. Persiapan

Pastikan sudah tersedia:

- Python
- Flask
- Requests
- Visual Studio Code

Buka folder project di Visual Studio Code:

```text
C:\Users\hkltr\Downloads\SEMESTER 5\PAK REZA\tugas-pratikum-paradigma-sistem-untuk-it
```

Struktur file:

```text
tugas-pratikum-paradigma-sistem-untuk-it/
│
├── monolith_app.py
├── book_service.py
├── order_service.py
└── README.md
```

---

## 2. Membuka Terminal VS Code

Buka terminal di Visual Studio Code dengan:

```text
Ctrl + `
```

Cek versi Python:

```powershell
py --version
```

Install Flask dan Requests jika belum tersedia:

```powershell
py -m pip install Flask requests
```

---

## 3. Menjalankan Program Monolith

Monolith merupakan aplikasi yang menggabungkan fitur buku dan pesanan dalam satu aplikasi.

Buka terminal VS Code dan jalankan:

```powershell
py monolith_app.py
```

Jika berhasil, akan muncul:

```text
Running on http://127.0.0.1:5000
```

Artinya Monolith berjalan pada:

```text
http://localhost:5000
```

**Jangan tutup terminal tersebut.**

---

## 4. Mengecek Data Buku pada Monolith

Buka terminal VS Code baru.

Jalankan:

```powershell
curl.exe http://localhost:5000/books
```

Hasilnya akan menampilkan data buku, contohnya:

```json
[
    {
        "id": 1,
        "stock": 5,
        "title": "Belajar Flask"
    }
]
```

---

## 5. Membuat Pesanan pada Monolith

Pada terminal baru, buat data JSON:

```powershell
$body = '{"book_id":1}'
```

Kemudian jalankan:

```powershell
Invoke-RestMethod -Uri "http://localhost:5000/orders" -Method POST -ContentType "application/json" -Body $body
```

Jika berhasil, akan muncul:

```text
id       : 1
book_id  : 1
status   : berhasil
```

---

## 6. Mengecek Perubahan Stok

Jalankan kembali:

```powershell
curl.exe http://localhost:5000/books
```

Sebelum membuat pesanan:

```text
stock = 5
```

Setelah pesanan berhasil:

```text
stock = 4
```

Hal ini menunjukkan bahwa fitur buku dan pesanan bekerja dalam satu aplikasi Monolith.

---

## 7. Menjalankan Book Service

Setelah pengujian Monolith selesai, buka terminal VS Code baru.

Jalankan:

```powershell
py book_service.py
```

Jika berhasil:

```text
Running on http://127.0.0.1:5001
```

Book Service berjalan pada:

```text
http://localhost:5001
```

**Jangan tutup terminal Book Service.**

---

## 8. Mengecek Book Service

Buka terminal baru.

Jalankan:

```powershell
curl.exe http://localhost:5001/books
```

Untuk mengambil satu buku:

```powershell
curl.exe http://localhost:5001/books/1
```

Jika berhasil, data buku akan ditampilkan.

---

## 9. Menjalankan Order Service

Buka terminal VS Code baru.

Jalankan:

```powershell
py order_service.py
```

Jika berhasil:

```text
Running on http://127.0.0.1:5002
```

Order Service berjalan pada:

```text
http://localhost:5002
```

Sekarang terdapat tiga aplikasi/port:

```text
Monolith       : 5000
Book Service   : 5001
Order Service  : 5002
```

---

## 10. Menguji Komunikasi Microservices

Pastikan:

```text
Book Service  :5001 → aktif
Order Service :5002 → aktif
```

Buka terminal baru.

Buat data pesanan:

```powershell
$body = '{"book_id":1}'
```

Kemudian jalankan:

```powershell
Invoke-RestMethod -Uri "http://localhost:5002/orders" -Method POST -ContentType "application/json" -Body $body
```

Jika berhasil:

```text
id       : 1
book_id  : 1
status   : berhasil
```

Pada proses ini terjadi komunikasi:

```text
Client
   │
   │ POST /orders
   ▼
Order Service :5002
   │
   │ GET /books/1
   ▼
Book Service :5001
   │
   │ Data buku
   ▼
Order Service :5002
   │
   ▼
Pesanan berhasil
```

Order Service meminta data buku kepada Book Service menggunakan HTTP.

---

## 11. Pengujian Fault Isolation

Pengujian ini dilakukan untuk melihat apa yang terjadi ketika salah satu service mengalami gangguan.

Cari terminal yang menjalankan:

```text
py book_service.py
```

Tekan:

```text
Ctrl + C
```

Book Service sekarang berhenti:

```text
Book Service :5001 ❌
```

**Jangan hentikan Order Service.**

Order Service tetap berjalan:

```text
Order Service :5002 ✅
```

---

## 12. Menguji Order Service Saat Book Service Mati

Buka terminal baru.

Jalankan:

```powershell
$body = '{"book_id":1}'
```

Kemudian:

```powershell
Invoke-RestMethod -Uri "http://localhost:5002/orders" -Method POST -ContentType "application/json" -Body $body
```

Hasil yang diharapkan:

```text
error
-----
Book Service sedang down!
```

Hal ini membuktikan bahwa:

- Book Service mengalami gangguan.
- Order Service tetap berjalan.
- Order Service dapat mendeteksi bahwa Book Service tidak dapat dihubungi.

---

## 13. Menjalankan Kembali Book Service

Setelah pengujian Fault Isolation selesai, jalankan kembali:

```powershell
py book_service.py
```

Book Service kembali berjalan pada:

```text
http://localhost:5001
```

Kemudian Order Service dapat kembali berkomunikasi dengan Book Service.

---

## 14. Kesimpulan Pengujian

### Monolith

```text
Satu aplikasi
      │
      ├── Book
      │
      └── Order
```

Berjalan pada:

```text
Port 5000
```

### Microservices

```text
Book Service
    :5001
       ▲
       │ HTTP
       ▼
Order Service
    :5002
```

Microservices memisahkan fitur menjadi beberapa service yang dapat berjalan secara independen.

Pada pengujian Fault Isolation, ketika **Book Service dimatikan**, **Order Service tetap hidup** dan memberikan pesan:

```text
Book Service sedang down!
```

Dengan demikian, praktikum berhasil menunjukkan perbedaan cara kerja **Monolith dan Microservices** serta konsep **Fault Isolation**.
