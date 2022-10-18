nama = ("Ardina")
gaji_pokok = 150000
gaji_lembur_per_jam = 15000
lama_lembur = 30
gaji_lembur = gaji_lembur_per_jam * lama_lembur

gaji_kotor = gaji_pokok + gaji_lembur
pajak = 9/100
potongan = int(gaji_pokok * 9/100)
gaji_bersih = gaji_kotor - potongan

print("Nama :", nama)
print ("gaji pokok :Rp.", gaji_pokok)
print ("gaji lembur :Rp.", gaji_lembur)
print ("gaji kotor :Rp.", gaji_kotor)
print ("pajak :",pajak)
print ("potongan :RP.", potongan)
print ("gaji Bersih :RP.",gaji_bersih)
