class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def tambah(self):
        return self.angka1 + self.angka2
    
    def kurang(self):
        return self.angka1 - self.angka2
    
    def kali(self):
        return self.angka1 * self.angka2
    
    def bagi(self):
        if self.angka2 != 0:
            return self.angka1 / self.angka2
        else:
            return ("Error: Tidak bisa dibagi dengan nol!")