sen = input("Masukan deret angka : ")
isn = sen . split(",")
ist = 0
bilangan = ''

for x in isn : 
    if int(x) % 2 == 0 : 
        angka = 0 + int(x)
    else :
        angka = 0 - int (x)
    ist = ist + angka 
print ("Total : ", end = '')

for y in isn : 
    if int (y) % 2 == 0 :
        angka = ("+" + str(y) + " ")
    else :
        angka = ("-" +  str(y) + " ")
    bilangan += angka 
if bilangan [0] == "+" : 
    print (bilangan[2 : len(bilangan)]) 
else :
    print(bilangan) 
print ("Hasil Perhitungan di atas adalah", ist ) 
