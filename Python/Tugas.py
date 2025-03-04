height = int(input("Input your height of * pyramid : "))

for i in range(height):
    print(" " * (height - i - 1) + '*' * (2 * i + 1))

a = int(input("Sum of Students : "))
all = {}

for i in range(a):
    name = str(input(f"Name of Student {i+1} : "))
    score = int(input(f"Score of {name} : "))
    all[name] = score

print(all)

name = str(input("Masukkan Nama : "))
nim = int(input("Masukkan NIM : "))
resolusi = str(input("Resolusi Tahun Ini : "))

with open("readme.txt", "a") as x:
    x.write(f"Nama : {name}\n")
    x.write(f"NIM : {nim}\n")
    x.write(f"Resolusi : {resolusi}\n")
    x.write("\n")
