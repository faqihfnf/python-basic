# Dokumentasi Belajar Python

## Variable

### Apa itu variabel ?

- Variabel adalah "wadah" yang digunakan untuk menyimpan data didalam memori.
- Dalam Python, variabel bersifat dinamis yaitu tipe datanya bisa berubah-rubah selama program berjalan.
- Analogi sederhana nya, variable itu seperti kotak yang ada labelnya. Label tersebut adalah nama variabelnya dan isi yang dimasukan kedalam kotak adalah datanya.

```bash
# contoh variable
nama  = "Budi"
umur = 25
tinggi = 170.5
```

### Aturan Penulisan / penamaan variabel

- Tidak boleh dimulai dengan angka
- Tidak boleh menggunakan tanda minus "-"
- Tidak boleh menggunakan spasi
- Tidak boleh menggunakan keyword yang sudah ada secara default di python (contoh : if, def dll)

### Membuat Variabel

- Untuk membuat variabel, langsung buat nama variable nya kemudian tanda sama dengan "=" dan setelahnya value/nilai dari variabelnya.
- Begitupun untuk merubah variable. Tulis nama variabelnya kemudian tanda sama dengan dan value/nilai perubahannya.

```bash
#Assignment Dasar
nama = "Budi"
umur = 30
tinggi = 165.5
is_Active = True

# Multiple assignment
x = y = z = 0 #artinya variable x,y dan z valuenya adalah 0

a, b, c = 1,2,3, #artinya variabel a nilainya 1, b nilainya 2, c nilainya 3

name, age = "joe", 25 #artinya variabel name valuenya adalah joe dan variable age valuenya adalah 25

# Merubah nilai variabel
skor = 80 # initial variable
skor = 90 #nilai variable dirubah

print(skor) #output = 90
```

### Menggunakan variabel

- untuk menggunakan variable, bisa langsung dengan menyebutkan nama variabelnya
- Jika ingin menggunakanlebih dari satu variabel, gunakan tanda koma (,) sebagai pemisah antar nama variabel yang dimasukan.

```bash
# Contoh
panjang = 10
lebar = 5
luas = panjang * lebar

print("Luas : " ,luas ) #Output -> Luas : 50
```

### Input Variabel dari User

- Untuk meminta dan mengisi value sebuah variabel dari user, bisa menggunakan function `input()`
- function `input()` akan selalu me-return value dengan tipe data string

```bash
# Contoh
nama = input("Masukan Nama : ")
usia = input("Masukan Usia : ")

print("Halo saya " + nama + " dan saya berusia " + usia + " tahun")

```

## Tipe Data

### Tipe data dasar yang ada di python

- Integer (int) -> bilangan bulat
- Float -> Bilangan desimal
- String -> teks
  -> Boolean (bool) -> true / false
- Python bisa handle tipe data yang sangat besar
- Untuk memeriksa tipe data bisa gunakan function `type()`

```bash
# contoh tipe data
nama  = "Budi" #string
umur = 25 #integer
tinggi = 170.5 #float
isAdmin = True #boolean

print(type(umur)) # <class 'int'>
print(type(tinggi)) # <class 'float'>
```

### Tipe Data String

untuk membuat string, bisa dilakukan dengan tiga cara;

- gunakan petik satu 'teks'
- gunakan petik dua "teks"
- gunakan petik tiga untuk multiple line """teks"""

```bash
nama = 'Budi'
kota = "Jakarta"
alamat = """
Jl Raya Cililitan No 50
Rt 001 Rw 002
Jakarta Timur
"""
```

## Konversi Type Data

Konversi tipe data adalah mengubah data dari satu tipe ke tipe lainnya. Hal ini dahal dilakukan dengan menggunakan function yang sudah ada dari python, diantaranya:

- `int()` untuk merubah data menjadi integer
- `str()` untuk merubah data menjadi string
- `float()` untuk merubah data menjadi float
- `bool()` untuk merubah data menjadi boolean

```bash
#contoh
usia = input("Masukan Usia : ")
umur = int(usia)

print(type(usia)) # output -> <class 'str'>
print(type(umur)) # output -> <class 'int
```
