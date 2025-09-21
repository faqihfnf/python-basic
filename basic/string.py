nama = "Joe"
umur = 25

pesan = "Halo saya " + nama + " dan saya berusia " + str(umur) + " tahun"
msg = f"Halo saya {nama} dan saya berusia {umur} tahun"

print(pesan)
print(msg)

print(len(nama))

lang = "Python"
print(lang[0])
print(lang[1])
print(lang[2])

print(lang[-3])
print(lang[-2])
print(lang[-1])

nation = "Indonesia"

print(nation[0:3]) # Ind (index 0,1,2)
print(nation[3:6]) # one (index 3,4,5)

print(nation[:3]) # Ind (index awal  sampai 2)
print(nation[3:]) # onesia (index 3 sampai akhir)
print(nation[:]) # Indonesia (index awal sampai akhir)

name = "John doe"

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.strip())
print(name.replace("John", "Budi"))
print(name.count("o"))
print(name.find("o"))