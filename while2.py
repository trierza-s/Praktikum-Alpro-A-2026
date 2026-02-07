#Dengan perulangan while kita dapat mengeksekusi serangkaian pernyataan selama suatu kondisi benar.

i = 1
while i < 6:
  print(i)
  i += 1

#Perulangan while mengharuskan variabel yang relevan untuk siap, dalam contoh ini kita perlu mendefinisikan variabel pengindeksan, i, yang kita atur ke 1.
#Dengan pernyataan break kita dapat menghentikan loop bahkan jika kondisi while adalah true:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Dengan pernyataan else kita dapat menjalankan blok kode sekali ketika kondisi tidak lagi benar:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
