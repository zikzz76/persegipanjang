#main.py


#fungsi untuk memeriksa apakah input adalah bilangan positif:
def input_positif(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai > 0:
                return nilai 
            else:
                print("nilai harus lebih dari 0. coba lagi.")
        except ValueError:
            print("input tidak valid. masukkan angka.")
                

#meminta input panjang dan lebar dari pengguna
panjang = float(input("Masukkan panjang persegi panjang:  "))
lebar = float(input("Masukkan lebar persegi panjang:  "))
 
#menghitung luas
luas = panjang * lebar

#menghitung keliling
keliling = 2 * (panjang + lebar)

#menampilkan hasil luas dan keliling
print(f"luas persegi panjang adalah: {luas}")
print(f"keliling persegi panjang adalah: {keliling}")