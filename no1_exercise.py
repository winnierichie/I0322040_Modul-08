nama_baru="no1_exercise8.txt"
isi_baru="Email"
with open(nama_baru, "w") as file_baru:
    file_baru.write(isi_baru)

nama_lama="Biodata.txt"
gabungan="" 

with open(nama_lama, "r") as file_lama:
    biodata=file_lama.read()

gabungan=biodata+isi_baru
    
with open(nama_lama, "w") as file_lama:
    file_lama.write(gabungan)

print("File baru digabungkan dengan file Biodata.txt")