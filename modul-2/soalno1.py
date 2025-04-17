class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.cek_sks(sks):
            raise ValueError(f"SKS untuk mata kuliah '{nama}' tidak valid (hanya 2 atau 3).")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def cek_sks(sks):
        return sks in (2, 3)

    def __str__(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"


class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(f"NIM '{nim}' tidak valid. Harus diawali '24' dan 10 digit.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.mata_kuliah = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.mata_kuliah.append(matkul)

    def tampilkan_info(self):
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang diambil:")
        for mk in self.mata_kuliah:
            print(f" - {mk}")

    @classmethod
    def get_jumlah_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10

class Kampus:
    jumlah_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.cek_nama_kampus(nama):
            raise ValueError(f"Nama kampus '{nama}' tidak valid. Tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info_kampus(cls, nama):
        print(f"\nNama Kampus: {nama}")
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def cek_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

#bikin objek
matkul1 = MataKuliah("MK101", "DMJ", 3)
matkul2 = MataKuliah("MK102", "EBC", 3)
matkul3 = MataKuliah("MK103", "APB", 3)
matkul4 = MataKuliah("MK104", "PBD", 2)
matkul5 = MataKuliah("MK105", "PBO", 3)
matkul6 = MataKuliah("MK106", "PBW", 3)
matkul7 = MataKuliah("MK107", "b inggris", 2)
matkul8 = MataKuliah("MK108", "PAI", 3)

daftar_matkul = [matkul1, matkul2, matkul3, matkul4, matkul5, matkul6, matkul7, matkul8]

# 6 Mahasiswa
mahasiswa_list = [
    Mahasiswa("Andi", "2312345678", "Informatika"),
    Mahasiswa("Budi", "2312345679", "Informatika"),
    Mahasiswa("Citra", "2312345666", "Sistem Informasi"),
    Mahasiswa("Dewi", "2312345681", "Sistem Informasi"),
    Mahasiswa("Eka", "2312345682", "Informatika"),
    Mahasiswa("Fajar", "2312345683", "Informatika"),
]

# Tambahkan 4 mata kuliah untuk setiap mahasiswa
for index, mhs in enumerate(mahasiswa_list):
    mhs.tambah_matkul(daftar_matkul[index % 8])
    mhs.tambah_matkul(daftar_matkul[(index + 1) % 8])
    mhs.tambah_matkul(daftar_matkul[(index + 2) % 8])
    mhs.tambah_matkul(daftar_matkul[(index + 3) % 8])

# Update jumlah mahasiswa ke kampus
Kampus.jumlah_mahasiswa = Mahasiswa.get_jumlah_mahasiswa()

kampus1 = Kampus("Universitas Trunojoyo Madura1", "Jl. Raya Telang no 1")

print("\nDATA MAHASISWA DAN MATA KULIAH")
for mhs in mahasiswa_list:
    mhs.tampilkan_info()

print("\nDATA KAMPUS")
Kampus.tampilkan_info_kampus(kampus1.nama)
print("Validasi Nama Kampus:", "Valid" if Kampus.cek_nama_kampus(kampus1.nama) else "Tidak Valid")
