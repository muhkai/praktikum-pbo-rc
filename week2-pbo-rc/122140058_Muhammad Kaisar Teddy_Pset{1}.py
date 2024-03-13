import random

class Ayah:
    def __init__(self):
        self.goldar_ayah = input("Masukkan golongan darah ayah (A, B, AB, O): ")
        self.allele = self.get_allele()

    def get_allele(self):
        if self.goldar_ayah == 'A':
            return ['A', 'O']
        elif self.goldar_ayah == 'B':
            return ['B', 'O']
        elif self.goldar_ayah == 'AB':
            return ['A', 'B']
        elif self.goldar_ayah == 'O':
            return ['O']
        else:
            raise ValueError('Golongan darah tidak sesuai')

class Ibu:
    def __init__(self):
        self.goldar_ibu = input("Masukkan golongan darah ibu (A, B, AB, O): ")
        self.allele = self.get_allele()

    def get_allele(self):
        if self.goldar_ibu == 'A':
            return ['A', 'O']
        elif self.goldar_ibu == 'B':
            return ['B', 'O']
        elif self.goldar_ibu == 'AB':
            return ['A', 'B']
        elif self.goldar_ibu == 'O':
            return ['O']
        else:
            raise ValueError('Golongan darah tidak sesuai')

class Anak:
    def __init__(self, ayah, ibu):
        self.allele_ayah = ayah.allele
        self.allele_ibu = ibu.allele
        self.goldar_anak = self.generate_goldar()

    def generate_goldar(self):
        alel_ayah = random.choice(self.allele_ayah)
        alel_ibu = random.choice(self.allele_ibu)
        
        if alel_ayah == 'A' and alel_ibu == 'O':
            return ['A']
        if alel_ayah == 'O' and alel_ibu == 'A':
            return ['A']
        elif alel_ayah == 'B' and alel_ibu == 'O':
            return ['B']
        elif alel_ayah == 'O' and alel_ibu == 'B':
            return ['B']
        elif alel_ayah == 'A' and alel_ibu == 'B':
            return ['AB']
        elif alel_ayah == 'O' and alel_ibu == 'O':
            return ['O']
        else:
            raise ValueError('Golongan darah tidak sesuai')

# Main program
ayah = Ayah()
ibu = Ibu()
child = Anak(ayah, ibu)
print("Golongan darah anak adalah:", child.goldar_anak[0])
