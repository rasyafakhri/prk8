## __init__(self): Metode inisialisasi yang membuat objek DaftarNilaiMahasiswa dengan satu atribut data yang awalnya kosong, digunakan untuk menyimpan data nilai mahasiswa.

## tambah(self, nama, nilai): Metode untuk menambahkan data nilai mahasiswa ke dalam data dengan key sebagai nama dan value sebagai nilai yang diinput.

## tampilkan(self): Metode untuk menampilkan daftar nilai mahasiswa. Jika data kosong, akan mencetak pesan bahwa daftar nilai mahasiswa kosong. Jika tidak, metode ini akan mencetak judul tabel dengan nama dan nilai sebagai kolom, kemudian mencetak setiap nama dan nilai mahasiswa dalam bentuk tabel.

## hapus(self, nama): Metode untuk menghapus data nilai mahasiswa berdasarkan nama yang diberikan.

## ubah(self, nama, nilai_baru): Metode untuk mengubah nilai mahasiswa berdasarkan nama yang diberikan dengan nilai baru yang ditentukan.

## Fungsi main(): Membuat objek daftar_nilai dari class DaftarNilaiMahasiswa.

## Menggunakan loop while untuk menampilkan menu dan menerima input dari pengguna.

## Jika pengguna memilih opsi:

## '1': Meminta nama dan nilai mahasiswa untuk menambahkannya ke daftar nilai menggunakan metode tambah() dari objek daftar_nilai.
## '2': Menampilkan daftar nilai mahasiswa menggunakan metode tampilkan() dari objek daftar_nilai.
## '3': Meminta nama mahasiswa yang ingin dihapus dan menghapusnya menggunakan metode hapus() dari objek daftar_nilai.
## '4': Meminta nama dan nilai baru untuk mengubah nilai mahasiswa menggunakan metode ubah() dari objek daftar_nilai.
## '5': Mengakhiri program.