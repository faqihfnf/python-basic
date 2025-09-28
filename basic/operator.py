a = 10
b = 3

print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333333333333335
print(a % b) # 1
print(a ** b) # 1000
print(a // b) # 3

print("===============================")

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

print("===============================")

d = 10
e = 3

print(d == b) # False
print(d != b) # True
print(d < b) # False
print(d > b) # True
print(d <= b) # False
print(d >= b) # True

nama_satu = "Joe"
nama_dua = "John"

print(nama_satu == nama_dua) # False
print(nama_satu != nama_dua) # True

print("===============================")

age = 25

print(age > 25 and age < 30) # False
print(age > 25 or age < 30) # True
print(not age > 20) # False

print("===============================")

nama_depan = "John"
nama_belakang = "Doe"

print(nama_depan + " " + nama_belakang)

garis = "-"

print(garis * 10)

kata = "Python adalah bahasa pemrograman yang populer"

print("Python" in kata) # True
print("python" in kata) # False
print("Javascript" in kata) # False
print("python" not in kata) # True
print("Python" not in kata) # False