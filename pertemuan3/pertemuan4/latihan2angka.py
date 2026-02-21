try:
    aku = int(input("Masukkan angka pertama: "))
    kamu = int(input("Masukkan angka kedua: "))
    hasil = aku / kamu
    print("Hasilnya adalah:", hasil)
except ValueError:
    print("Harus angka yang dimasukkan!!!")
except ZeroDivisionError:
    print("Tidak bisa dibagi sama noll!!")
finally:
    print("SIAP DAHH")