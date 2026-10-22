nilai = 82
kehadiran = 90

print("Nilai:", nilai)
print("Kehadiran:", str(kehadiran) + "%")
print("Nilai minimal 75:", nilai >= 75)
print("Kehadiran minimal 80%:", kehadiran >= 80)
print("Memenuhi kedua syarat (and):", nilai >= 75 and kehadiran >= 80)

nilai = 70
print("\nSetelah nilai diubah menjadi 70:")
print("Nilai minimal 75:", nilai >= 75)
print("Kehadiran minimal 80%:", kehadiran >= 80)
print("Memenuhi kedua syarat (and):", nilai >= 75 and kehadiran >= 80)
print("Memenuhi salah satu syarat (or):", nilai >= 75 or kehadiran >= 80)
