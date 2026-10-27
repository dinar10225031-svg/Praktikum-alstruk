print("=== PROGRAM MENENTUKAN KELULUSAN ===")

nama = input("Masukkan nama mahasiswa: ")
nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    print("\nNama mahasiswa:", nama)
    print("Nilai:", nilai)
    print("Keterangan: LULUS")
else:
    print("\nNama mahasiswa:", nama)
    print("Nilai:", nilai)
    print("Keterangan: TIDAK LULUS")
    