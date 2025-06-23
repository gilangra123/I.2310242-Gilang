
buku = []

def pilih():
    print("[1] Tambah Data")
    print("[2] Lihat Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")

    menu = input("Pilih aksi > ")

    if menu == '1':
        tambah()
    elif menu == '2':
        lihat()
    elif menu == '3':
        edit()
    elif menu == '4':
        hapus()
    else:
        print("Pilih sesuai menu")
        pilih()

# Menambah data
def tambah():
    x = input('Masukkan Nama buku = ')
    buku.append(x)

# Menampilkan data
def lihat():
    if len(buku) <= 0:
        print("Data masih kosong")
    else:
        for i, name in enumerate(buku):
            print(f"[{i}] {name}")

# Mengedit data
def edit():
    lihat()
    if len(buku) > 0:
        try:
            idx = int(input("Masukkan indeks data yang ingin diubah: "))
            if 0 <= idx < len(buku):
                baru = input("Masukkan nama baru: ")
                buku[idx] = baru
                print("Data berhasil diubah.")
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

# Menghapus data
def hapus():
    lihat()
    if len(buku) > 0:
        try:
            idx = int(input("Masukkan indeks data yang ingin dihapus: "))
            if 0 <= idx < len(buku):
                buku.pop(idx)
                print("Data berhasil dihapus.")
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

# Program utama
while True:
    pilih()
