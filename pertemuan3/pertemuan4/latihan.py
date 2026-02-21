angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

# Kalau kita memasukkan angka nol, seperti yang disuruh. maka dia bakal mengeluarkan output 10 dan Selesai
# Kalau kita memasukkan huruf, maka yang jalan itu except ValueError dan Selesai
# Kalau kita memasukkan angka negatif, dia akan tetap jalan mulus dan output bakal keluar, tetapi negatif dihitung dari sebelah kanan.