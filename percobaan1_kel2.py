# non return function
def non_return_function(nama, nim):
    print("Selamat datang di praktikum Pemrograman Dasar 2025 {} dengan NIM {}".format(nama, nim))

# return function
def return_func(angka):
    print(f"Angka kalian adalah {angka}")
    if angka % 2 == 0:
        return "Mengembalikan nilai genap dengan angka {}".format(angka)
    else:
        return "Mengembalikan nilai ganjil dengan angka {}".format(angka)

# arbitrary function
def arbitrary_func(*penutup):
    for nama in penutup:
        print(f"Terima kasih {nama}")

# anonymous function
add = lambda x, y: x + y
result = add(5, 8)

# Menjalankan fungsi
non_return_function("Clara", 21120125120005)
print(return_func(13))   # perlu print agar nilai return terlihat
arbitrary_func("- Coba 1", "- Coba 2", "- Coba 3")
print(add(4, 9))
