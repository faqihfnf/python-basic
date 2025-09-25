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
- Boolean (bool) -> true / false
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

## Manipulasi String

String adalah tipe data untuk menyimpan teks atau kumpulan karakter. String ditulis dengan menggunakan tanda kutip diawal dan diakhir:

- gunakan petik satu 'teks'
- gunakan petik dua "teks"
- gunakan petik tiga untuk multiple line """teks"""

```bash
nama = 'Budi' # contoh dengan petik satu
kota = "Jakarta" # contoh dengan petik dua
alamat = """
Jl Raya Cililitan No 50
Rt 001 Rw 002
Jakarta Timur
""" # contoh dengan petik tiga
```

### Menggabungkan String

- untuk menggabungkan string bisa dilakukan dengan menngunakan tanda +
- Tipe data string tidak bisa digabungkan dengan tipe data yang lain seperti integer, float dll
- Jika ingin digabungkan bisa dilakukan dengan dua cara :
  1.  Mengkonversi ketipe data string dengan function `str()`
  2.  Menggunakan `f-string` dan membungkus variabelnya didalam `{}`. ini disebut juga dengan <b>String Interpolation</b>
- f-string (formatted string literal) secara otomatis merubah nilai yang ada didalam `{}` menjadi string. Untuk itu tidak perlu menggunakan `str()` lagi untuk merubah variabel yang bukan string menjadi string
- f-string dapat mengeksekusi ekspresi langsung didalamnya

```bash
#contoh
nama = "Joe"
umur = 25

pesan = "Halo saya " + nama + " dan saya berusia " + str(umur) + " tahun" #variabel umur dikonversi ke str
msg = f"Halo saya {nama} dan saya berusia {umur} tahun" # menggunakan f-string

print(pesan)
print(msg)

#output keduanya -> Halo saya Joe dan saya berusia 25 tahun

#contoh ekspresi harga * jumlah bisa dieksekusi langsung didalam f-string
harga = 20000
jumlah = 5

total = f"Total harga adalah {harga * jumlah}"
print(total) # Total harga adalah 100000
```

### Menghitung Panjang String

- Gunakan function `len()` untuk menghitung panjang string / total karakter. Karakter disini termasuk spasi, jadi spasi juga akan dihitung sebagai karakter dalam string.
- Fungsi `len()` mengambalikan nilai dengan tipe data integer

### Mengakses karakter yang ada didalam string (Indexing)

- Setiap karakter dalam string memiliki posisi (index) yang dimulai dari angka 0
- Untuk mengakses data tersebut bisa menggunakan kurung siku[] dan masukan nomor indexnya.
- Untuk mengakses index bisa juga menggunakan index dengan angka negatif (-), jika menggunakan negatif, maka dihitung dari belakang

```bash
# Contoh
lang = "Python"

print(lang[0]) # P
print(lang[1]) # y
print(lang[2]) # t

print(lang[-3]) # h
print(lang[-2]) # o
print(lang[-1]) # n
```

### String Slicing

String slicing digunakan untuk mengambil sebagian karakter dari string. Yang membedakan dengan indexing, indexing hanya menagmbil satu karakter sementara slicing mengambil lebih dari satu karakter

- Sama dengan indexing, sliceing juga menggunakan kurung siku [] untuk mengakses karakter didalam string
- Yang membedakan adalah untuk slicing terdapat dua posisi index yang dipisahkan oleh titik dua (:).
- Angka sebelum titik dua menunjukan index awal, dan setelah titik dua menunjukan index akhir
- Contoh [1,4] berarti kita akan ambil karakter dari index 1 sampai dengan index 3 (index 1,2,3)
- Jika index pertama tidak disebutkan, secara default akan mengambil index pertama (0)
- Sementara jika index keduanya tidak diisi, maka secara default akan mengambil index terakhir
- Dan jika tidak menyebutkan index sama sekali, hanya titik dua saja, maka akan diambil semua karakter dalam stringnya.

```bash
#contoh

nation = "Indonesia"

print(nation[0:3]) # Ind (index 0,1,2)
print(nation[3:6]) # one (index 3,4,5)

print(nation[:3]) # Ind (index awal  sampai 2)
print(nation[3:]) # onesia (index 3 sampai akhir)
print(nation[:]) # Indonesia (index awal sampai akhir)
```

### String Method

Tipe data string memiliki method (fungsi) bawaan dari python yang bisa digunakan untuk melakukan manipulasi pada string.

- `upper()` : mengubah semua karkter string menjadi huruf besar.
- `lower()` : mengubah semua karkter string menjadi huruf kecil.
- `title()` : mengubah setiap awal karakter pada kata menjadi huruf besar.
- `capitalize()` : mengubah hanya awal karakter pada kata menjadi huruf besar.
- `strip()` : menghilangkan karakter kosong (whitespace).
- `replace(sebelum,sesudah)` : mengganti bagian tertentu dari string.
- `count()` : menghitung berapa kali sebuah text muncul.
- `find()` : mencari posisi (index) keberapa text muncul.

```bash
#contoh
name = "John doe"

print(name.upper()) # JOHN DOE
print(name.lower()) # john doe
print(name.title()) # John Doe
print(name.capitalize()) # John doe
print(name.strip()) # John doe
print(name.replace("John", "Budi")) # Budi doe
print(name.count("o")) # 2
print(name.find("o")) # 1

```

### Escape Characters

Excape Characters merupakan karakter-karakter khusus dalam string yang untuk menggunakannya harus mengikuti aturan khusus dari python.

- `\n` : New Line
- `\t` : Tab
- `\` : Backslash

```bash
#contoh
data = "Name: Joe \nAge: 25\nCountry: Indonesia"
path = "C:\\Users\\Documents\\main.py"
words = "I\'m learning python \t now"

print(data)
#Name: Joe
#Age: 25
#Country: Indonesia
print(path) # C:\Users\Documents\main.py
print(words) # I'm learning python      now
```

## Operator

### Apa itu operator ?

Operator adalah simbol yang digunakan untuk melakukan operasi pada variabel atau value. Dan didalam python ada beberapa jenis operator yang bisa digunakan untuk melakukan operasi.

### Operator Aritmatika

Operator aritmatika digunakan untuk melakukan operasi matematika pada variabel atau value. Diantaranya:

- `+` : Penjumlahan
- `-` : Pengurangan
- `*` : Perkalian
- `/` : Pembagian
- `%` : Modulus
- `**` : Pangkat
- `//` : Floor Division ( pembagian dengan pembulatan kebawah)

```bash
#contoh
a = 10
b = 3

print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333333333333335
print(a % b) # 1
print(a ** b) # 1000
print(a // b) # 3
```

### Operator Penugasan (Assignment)

Operator assignment digunakan untuk memberikan nilai pada sebuah variabel. Operarot assignment sendiri ada dua jenis;

1. Assignment
2. Compound Assignment, yaitu operator yang menggabungkan antara operasi artimatika dengan operator penugasan

Contoh operator assignment:

- `=` : Penugasan

Contoh operator compound assignment:

- `+=` : Penjumlahan dan penugasan
- `-=` : Pengurangan dan penugasan
- `*=` : Perkalian dan penugasan
- `/=` : Pembagian dan penugasan
- `%=` : Modulus dan penugasan
- `**=` : Pangkat dan penugasan
- `//=` : Floor Division ( pembagian dengan pembulatan kebawah) dan penugasan

```bash
#contoh
c = 5

c += 2 # c = c + 2 = 7
print(c)
c -= 3 # c = c - 3 = 4
print(c)
c *= 2 # c = c * 2 = 8
print(c)
c /= 2 # c = c / 2 = 4
print(c)
c %= 2 # c = c % 2 = 0
print(c)
c **= 2 # c = c ** 2 = 0
print(c)
c //= 2 # c = c // 2 = 0
print(c)
```
