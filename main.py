import random # import libary dari bawaan pythom

wellcome_message = "WELLCOME TO CHOCOMETT GAMES!"
hadiah_utama = random.randint(1, 4) # random integer dari angka 1 samapi dengan 4

print(wellcome_message)
nama_user = input("Masukan Nama Anda... ")
print(f"""Heyy, {nama_user}. Apakah kamu siap bermain tebak tebakan bersamaku ?
""")

jawaban_pembuka = input("Masukan Jawaban Anda, Y/N... ")

if jawaban_pembuka.upper() == "Y": # .upper() agar output dari input user di konversi menjadi uppercase
    print(f"Lesgowww mari kita bermain")
else:
    print(f"Sayang sekali, Mari kita berjumpa dilain waktu")
    exit()
    
print(f'''
Halo {nama_user}! Coba perhatikan 4 Kolom dibawah ini

|_| |_| |_| |_|
''')
print("""
Coba Tebak kolom nomer berapakah yang terdapat Hadiah Utama.
Mari Kita Coba Peruntunganmu!!!
""")

jawaban_user = int(input("Masukan Nomer Peruntunganmu 1/2/3/4... ")) # int() agar tipe data input menjadi Integer

print(f"Pilihanmu kolom nomer {jawaban_user}")

if jawaban_user == hadiah_utama:
    print(f"Wow Jawaban kamu benar, Hadiah Utama terdapat dikolom nomer {hadiah_utama}")
else:
    print(f"Sayang banget, Hadiah Utama terdapat pada nomer {hadiah_utama}")
