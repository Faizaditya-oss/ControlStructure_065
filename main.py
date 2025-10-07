percentage = float(input(" Masukkan presentase nilai siswa : "))

if percentage >= 90 :
    print (" Excellent performance")
elif percentage >= 80 :
    print ("Very good performance")
elif percentage >= 70 :
    print ("Good performance")
elif percentage >= 60 :
    print ("Average performance")
else :
    print("Needs improvement")


a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))


if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c
else:
    largest = print("Tidak ada angka terbesar")


print("Angka terbesar adalah:", largest)
