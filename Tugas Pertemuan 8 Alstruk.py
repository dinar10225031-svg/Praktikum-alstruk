import array

# 1. ARRAY (Daftar Harga)
harga = array.array('i', [15000, 18000, 20000, 12000])

# 2. LINKED LIST (Daftar Pesanan)
class Node:
    def __init__(self, nama, pesanan, total):
        self.nama = nama
        self.pesanan = pesanan
        self.total = total
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, nama, pesanan, total):
        node_baru = Node(nama, pesanan, total)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampilkan(self):
        current = self.head

        while current:
            print("Nama Pelanggan :", current.nama)
            print("Pesanan        :", current.pesanan)
            print("Total Harga    : Rp", current.total)
            print("--------------------------")
            current = current.next
# 3. TUPLE (Data Menu Tetap)
menu = (
    ("K01", "Kopi Hitam"),
    ("K02", "Kopi Susu"),
    ("K03", "Cappuccino"),
    ("K04", "Teh Manis")
)

# PROGRAM UTAMA
pesanan = LinkedList()

print("=== KEDAI KOPI MAUNGHEUAY ===")

# Menampilkan menu
print("\nDaftar Menu:")
for i in range(len(menu)):
    print(menu[i][0], "-", menu[i][1],
          ": Rp", harga[i])

# Input pesanan
jumlah = int(input("\nJumlah pelanggan: "))

for i in range(jumlah):
    print("\nPelanggan ke-", i + 1)
    nama = input("Nama pelanggan: ")

    kode = input("Masukkan kode menu: ").upper()

    ditemukan = False

    for j in range(len(menu)):
        if kode == menu[j][0]:
            total = harga[j]
            nama_menu = menu[j][1]
            ditemukan = True
            break

    if ditemukan:
        pesanan.tambah(nama, nama_menu, total)
        print("Pesanan berhasil ditambahkan!")
    else:
        print("Kode menu tidak ditemukan!")

# Menampilkan semua pesanan
print("\n=== DAFTAR PESANAN PELANGGAN ===")
pesanan.tampilkan()
