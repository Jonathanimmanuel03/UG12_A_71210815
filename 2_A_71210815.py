
tempatduduk = []
namal = []
ulang = "ya"

while (ulang == "ya") :
    nama = str(input("Silahkan Masukan Nama Anda : "))
    nok = int(input("Masukan Nomor Kursi : "))
    namal.append(nama)
    tempatduduk.append(nok)
    ulang = input("Apakah Anda Ingin Melanjutkan ? : ")

print ("List Kursi yang Telah terisi : ")
print ("Kursi Nomor ",tempatduduk,"telah diisi oleh ",namal)

