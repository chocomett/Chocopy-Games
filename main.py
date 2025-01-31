from libs import wellcome_message
import random # import libary dari bawaan python

wellcome_message("WELLCOME TO CHOCOMETT GAMES!")

nama_user = input("Masukan Nama Anda... ")
while nama_user == "":
    nama_user = input("isi dulu nama lu egeee... ")

while True:
    bentuk_goa = "|_|"
    goa = [bentuk_goa] * 4 #jadikan array agar dapet diambil data didalamnya dan dapat dirubah
    goa_hadiah = goa.copy() #membuat agar goa pada hasil akhir dapat mengikuti desain yang sama seperti goa awal namun isi goa hadia tidak diketahui dari awal
    hadiah_utama = random.randint(1, 4) # random integer dari angka 1 samapi dengan 4
    goa_hadiah[hadiah_utama - 1] = "|🏆|" #memunculkan hadiah dengan mereplace sesuai dengan random randint lalu - 1 agar hasil sesuai dengan bahasa manusia
    new_goa = " ".join(goa) #menghilangkan tanda koma dan bukatutup kurung di awal
    goa_hadiah = " ".join(goa_hadiah) #menghilangkan tanda koma dan bukatutup kurung di hasil akhir

    print(f"\nHalo {nama_user}! Coba perhatikan 4 Kolom dibawah ini\n\n{new_goa}")
    print("\nCoba Tebak kolom nomer berapakah yang terdapat Hadiah Utama.\nMari Kita Coba Peruntunganmu!!!\n")
    jawaban_user = int(input("Masukan Nomer Peruntunganmu [ 1 / 2 / 3 / 4 ]... ")) # int() agar tipe data input menjadi Integer
    while jawaban_user != 1 and jawaban_user != 2 and jawaban_user != 3 and jawaban_user != 4: #!= tidak sama dengan | and : dan
        jawaban_user = int(input("CUMAN BISA 4 ANGKA INI KOCAK [ 1 / 2 / 3 / 4 ]... "))
    if jawaban_user == hadiah_utama:
        print(f"\n{goa_hadiah}")
        print(f"\nWow Jawaban kamu benar, Hadiah Utama terdapat dikolom nomer {hadiah_utama}\n")
        print("SELAMAT KAMU MENANG 🏆🏆 \n")
    else:
        print(f"\n{goa_hadiah}")
        print(f"\nSayang banget, Hadiah Utama terdapat pada nomer {hadiah_utama}\n")
        print("UBUR UBUR IKAN LELE COBA LAGI LEEE 😁😁 \n")
    
    main_lagi = input("apakah ingin bermain lagi [Y / N]... ")
    if main_lagi.upper() == "N":
        print("\nProgram Berhernti, Terimakasih Sudah Bermain Chocomett Games 🤩🤩\n")
        break