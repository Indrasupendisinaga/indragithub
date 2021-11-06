#Tugas
#Buatlah program untuk menghitung luas dan keliling lingkaran menggunakan phyton
#Simpan project praktikum hari ini ke repository server
#buat penjelasan setiap Lab/latihannya pada file READMI.md
#sertakan flowchart dan penjelasan program dan screenshot hasil eksekusi program

#_____Keterangan_____
#Rumus luas dan keliling lingkaran
#Luas pi x r2
#keliling 2 x pi x r
#(nilai yang kita gunakan adalah 3.14)
#(r adalah jari jari lingkaran)
#____________________

import math
r = float(input("masukkan jari-jari :"))

luas = math.pi*(r*r)
keliling = 2*math.pi*r

print ("luas lingkaran \t\t = ",luas)
print ("keliling lingkaran \t =", keliling)

#Penjelasan
#program diatas menginput modul math yang sudah disediakan oleh pyhton
#fungsinya supaya dapat menyertakan nilai phi yang sudah tersedia dalam modul tersebut
#dengan perintah math.pi.
