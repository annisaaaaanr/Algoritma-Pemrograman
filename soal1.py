# data diri
print("Nama\t: Annisa Nur Rachmawati\n")
print("NIM\t: 21081000004\n")
print("Kelas\t: 1D\n")

# judul program
print("menampilkan modus bilangan")

# variabel angka
a = int(input("Masukkan angka : "))

# variabel list angka
listAngka = [4, 7, 3, 2, 1, 6, 7, 8, 1, 10, 10, 3, 3, 3]

jumlahMunculnya = 0

# perulangan untuk menghitung jumlah angka
for i in range(len(listAngka)):
    if a == listAngka[i]:
        jumlahMunculnya = jumlahMunculnya + 1

print("jumlah bilangan " + str(a) + " ada " + str(jumlahMunculnya) + " jumlah")
