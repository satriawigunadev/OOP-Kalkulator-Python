from kalkulator import Kalkulator

def main():
    while True:
        print(f"Selamat datang di aplikasi Kalkulator Python")
        print(f"============================================")

        try:
            angka_pertama = float(input("Masukkan angka pertama: "))
            angka_kedua = float(input("Masukkan angka kedua: "))
        except ValueError:
            print(f"Error: Masukkan angaka denga benar!")
            continue

        kalkulator_object = Kalkulator(angka_pertama, angka_kedua)

        print(f"Pilihan operasi: ")
        print(f"1. Tambah (+)")
        print(f"2. Kurang (-)")
        print(f"3. kali (*)")
        print(f"4. Bagi (/)")

        operasi = input("Masukkan pilihan (1/2/3/4/5): ")

        if operasi == '1':
            print(f"Hasil tambah : {kalkulator_object.tambah()}")
        elif operasi == '2':
            print(f"Hasil kurang: {kalkulator_object.kurang()}")
        elif operasi == '3':
            print(f"Hasil kali: {kalkulator_object.kali()}")
        elif operasi == '4':
            print(f"Hasil bagi: {kalkulator_object.bagi()}")
        else:
            print(f"Error: Masukkan pilihan dengan benar!")

        while True:
            print(f"Apakah anda ingin mengulangi Kalkulator Python?")
            print(f"1. Lanjutkan")
            print(f"2. Keluar")

            pilihan = input("Masukkan pilihan: ")

            if pilihan == '1':
                break
            elif pilihan == '2':
                return
            else:
                print(f"Error: Masukkan pilihan dengan benar!")
            
if __name__ == "__main__":
    main()