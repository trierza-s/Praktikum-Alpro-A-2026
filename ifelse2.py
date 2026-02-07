#Kata kunci else menangkap apa pun yang tidak tertangkap oleh kondisi sebelumnya.
#Pernyataan else dijalankan ketika kondisi if (dan kondisi elif apa pun) dievaluasi ke False.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Dalam contoh ini a lebih besar dari b, jadi kondisi pertama tidak benar, juga kondisi elif tidak benar, jadi kita pergi ke kondisi else dan mencetak ke layar bahwa "a lebih besar dari b".

#kita juga bisa buat tanpa :elseelif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Pernyataan else menyediakan tindakan default ketika tidak ada kondisi sebelumnya yang benar. Anggap saja sebagai "catch-all" untuk skenario apa pun yang tidak tercakup dalam pernyataan if dan elif Anda.

