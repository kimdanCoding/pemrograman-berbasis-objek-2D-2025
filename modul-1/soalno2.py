class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
    
    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan/Prodi:", self.jurusan)
        print("Alamat:", self.alamat)
        print("---------------------------")

# Input dan membuat objek mahasiswa
print("Hai, Selamat datang di daftar mahasiswa, Silahkan masukkan datamu untuk ditampilkan")
mahasiswa1 = Mahasiswa(input("Masukkan Nama: "), input("Masukkan NIM: "), input("Masukkan Jurusan/Prodi: "), input("Masukkan Alamat: "))
mahasiswa2 = Mahasiswa(input("Masukkan Nama: "), input("Masukkan NIM: "), input("Masukkan Jurusan/Prodi: "), input("Masukkan Alamat: "))
mahasiswa3 = Mahasiswa(input("Masukkan Nama: "), input("Masukkan NIM: "), input("Masukkan Jurusan/Prodi: "), input("Masukkan Alamat: "))

# Menampilkan data mahasiswa
print("")
print("Data Mahasiswa yang Telah Dimasukkan:")
print("")
mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()
mahasiswa3.tampilkan_info()
