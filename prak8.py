class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah(self, nama, nilai):
        self.data[nama] = nilai
        print(f"Data nilai untuk {nama} berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data:
            print("Daftar nilai mahasiswa kosong.")
        else:
            print("Daftar Nilai Mahasiswa:")
            print("=" * 27)
            print("| {:<15} | {:<10} |".format("Nama", "Nilai"))
            print("=" * 27)
            for nama, nilai in self.data.items():
                print("| {:<15} | {:<10} |".format(nama, nilai))
            print("=" * 27)

    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            print(f"Data nilai untuk {nama} berhasil dihapus.")
        else:
            print(f"Data untuk {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        if nama in self.data:
            self.data[nama] = nilai_baru
            print(f"Data nilai untuk {nama} berhasil diubah.")
        else:
            print(f"Data untuk {nama} tidak ditemukan.")

# Fungsi untuk menjalankan program
def main():
    daftar_nilai = DaftarNilaiMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah data nilai mahasiswa")
        print("2. Tampilkan data nilai mahasiswa")
        print("3. Hapus data nilai mahasiswa")
        print("4. Ubah data nilai mahasiswa")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nilai = input("Masukkan nilai mahasiswa: ")
            daftar_nilai.tambah(nama, nilai)
        elif pilihan == '2':
            print()
            daftar_nilai.tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            daftar_nilai.hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_baru = input("Masukkan nilai baru: ")
            daftar_nilai.ubah(nama, nilai_baru)
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka yang sesuai.")

if __name__ == "__main__":
    main()
