class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur
    
    def bersuara(self):
        print(self.nama, "mengeluarkan suara: Meow!")

class Anjing:
    def __init__(self, nama, ras, umur):
        self.nama = nama
        self.ras = ras
        self.umur = umur
    
    def bersuara(self):
        print(self.nama, "mengeluarkan suara: Guk guk!")

class Burung:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
    
    def bersuara(self):
        print(self.nama, "mengeluarkan suara: Cuit cuit!")

# Membuat beberapa objek menggunakan looping
hewan_list = []
for i in range(2): 
    nama = input("Nama Kucing: ")
    warna = input("Warna: ")
    umur = input("Umur: ")
    hewan_list.append(Kucing(nama, warna, umur))
    
    nama = input("Nama Anjing: ")
    ras = input("Ras: ")
    umur = input("Umur: ")
    hewan_list.append(Anjing(nama, ras, umur))
    
    nama = input("Nama Burung: ")
    jenis = input("Jenis: ")
    umur = input("Umur: ")
    hewan_list.append(Burung(nama, jenis, umur))

# Menampilkan suara hewan
print("Suara Hewan:")
for hewan in hewan_list:
    hewan.bersuara()
