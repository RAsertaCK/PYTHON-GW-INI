class Kendaraan:
    def __init__ (self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print(f"Jenis kendaraan = {self.jenis}\n")
        print(f"Kecepatan max = {self.kecepatan_maksimum}\n")

    def bergerak(self):
        print(f"Mobil sedang bergerak\n")

class Mobil(Kendaraan):
    def __init__ (self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil (self):
        self.info_kendaraan()
        print(f"Merk Mobil = {self.merk}\n")
        print(f"Jumlah pintu = {self.jumlah_pintu}\n")
        
    def bunyikan_klakson(self):
        print(f"BEEEP BEEEP\n")
        
class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga

    def get_tenaga_kuda(self):
        return self.__tenaga_kuda

    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda += value

    def get_harga(self):
        return self.__harga

    def set_harga(self, value):
        self.__harga += value

    def info_mobil_sport(self):
        self.info_mobil()
        print(f"Tenaga Kuda: {self.__tenaga_kuda} HP")
        print(f"Harga: Rp {self.__harga} juta")

    def mode_balap(self):
        print(f"{self.merk} sedang masuk ke mode balap!\n")

mobil_sport = MobilSport("Darat", 350, "Ferrari", 2, 700, 10000)
mobil_sport.info_mobil_sport()
mobil_sport.bergerak()
mobil_sport.bunyikan_klakson()
mobil_sport.mode_balap()
mobil_sport.set_tenaga_kuda(50)
mobil_sport.set_harga(2000)
print(f"Tenaga Kuda Baru: {mobil_sport.get_tenaga_kuda()} HP")
print(f"Harga Baru: Rp {mobil_sport.get_harga()} juta")