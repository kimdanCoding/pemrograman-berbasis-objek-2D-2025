class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("Status: Karyawan Tetap")
        print("-" * 40)

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji_per_jam, departemen, jam_kerja):
        super().__init__(nama, gaji_per_jam, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        total_gaji_per_hari = self.gaji * self.jam_kerja
        super().info()
        print(f"Jam Kerja per Hari: {self.jam_kerja} jam")
        print(f"Gaji per Hari: {total_gaji_per_hari}")
        print("Status: Karyawan Harian")
        print("-" * 40)

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("=== Daftar Semua Karyawan ===")
        for karyawan in self.daftar_karyawan:
            karyawan.info()

manajemen = ManajemenKaryawan()

manajemen.tambah_karyawan(KaryawanTetap("Andi", 5000000, "IT", 1000000))
manajemen.tambah_karyawan(KaryawanTetap("Siti", 6000000, "HRD", 1500000))

manajemen.tambah_karyawan(KaryawanHarian("Budi", 100000, "Produksi", 8))
manajemen.tambah_karyawan(KaryawanHarian("Rina", 120000, "Gudang", 7))

manajemen.tampilkan_semua_karyawan()
