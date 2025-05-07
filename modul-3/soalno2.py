class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "truk":
            return 6
        elif self.jenis_kendaraan == "motor":
            return 4
        else:
            return super().estimasi_waktu()

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 2
        elif self.maskapai == "Lion Air":
            return 3
        else:
            return super().estimasi_waktu()

class PengirimanInternasional(PengirimanUdara, PengirimanDarat):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "truk":
            waktu_darat = 6
        elif self.jenis_kendaraan == "motor":
            waktu_darat = 4
        else:
            waktu_darat = 5

        if self.maskapai == "Garuda":
            waktu_udara = 2
        elif self.maskapai == "Lion Air":
            waktu_udara = 3
        else:
            waktu_udara = 5

        estimasi = waktu_darat + waktu_udara

        if self.tujuan.lower() != "indonesia":
            estimasi += 3

        return estimasi

    def info(self):
        print(f"Asal            : {self.asal}")
        print(f"Tujuan          : {self.tujuan}")
        print(f"Jenis Kendaraan : {self.jenis_kendaraan}")
        print(f"Maskapai        : {self.maskapai}")
        print("Metode          : Darat + Udara Internasional")
        print(f"Estimasi Waktu  : {self.estimasi_waktu()} hari")
        print("-" * 40)

peng1 = PengirimanInternasional("Jakarta", "Singapura", "truk", "Garuda")
peng2 = PengirimanInternasional("Bandung", "Indonesia", "motor", "Lion Air")
peng3 = PengirimanInternasional("Surabaya", "Malaysia", "motor", "Garuda")

peng1.info()
peng2.info()
peng3.info()
