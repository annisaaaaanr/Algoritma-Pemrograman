def pengurutan(bilangan):
    # perulangan
    for i in range(len(bilangan)-1):
        for j in range(len(bilangan)-1):
            if(bilangan[j] > bilangan[j+1]):
                # menukar variabel
                bilangan[j], bilangan[j+1] = bilangan[j+1], bilangan[j]
    # mengembalikan variabel bilangan
    return bilangan


# variabel ulang untuk menjalankan ulang program
ulang = "Y"

# perulangan while berjalan ketika variabel ulang berisi Y/y
while ulang == "Y" or ulang == "y":

    # data diri
    print("Nama \t : Annisa Nur Rachmawati")
    print("NIM \t : 21081000004")
    print("Kelas \t : 1D")

    # membuat variabel untuk menyimpan inputan dari user
    a = int(input("\nMasukkan bilangan pertama : "))
    b = int(input("Masukkan bilangan kedua : "))
    c = int(input("Masukkan bilangan ketiga : "))

    # variabel bilangan untuk menyimpan inputan dari user
    bilangan = [a, b, c]

    # mencetak variabel bilangan
    print("Bilangan yang tidak berurutan : ", bilangan)

    print("bilangan yang berurutan adalah : ", pengurutan(bilangan))

    ulang = input("Apakah anda ingin mengulangi program kembali? (Y/T) : ")

    if ulang == "T" or ulang == "t":
        break
