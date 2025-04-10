class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print(self.nama, "sedang berjalan")
    
    def berlari(self):
        print(self.nama, "sedang berlari")

# Membuat objek dari class Manusia
manusia1 = Manusia("Arif", 19, "Blega")
manusia2 = Manusia("Galih", 30, "Jombang")
manusia3 = Manusia("Citra", 22, "Gresik")
manusia4 = Manusia("gwen", 28, "Malaysia")
manusia5 = Manusia("fifi", 35, "Sumenep")

# Memanggil method berjalan dan berlari
manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()
