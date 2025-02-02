import random # import libary dari bawaan python
import libs 

def user():
    nama_user = input("Masukan Nama Anda... ")
    while nama_user == "":
        nama_user = input("isi dulu nama lu egeee... ")
    return nama_user #fungsi return untuk mengambil nilai variabel yang terdapat didalam def tersebut dan dapat digunakan di def yang lain

def start(): #eksekusi keempat
    nama_user = user()
    while True: #looping secara terus menerus
        bentuk_kolam = "|_|"
        kolam = [bentuk_kolam] * 4 #jadikan array agar dapet diambil data didalamnya dan dapat dirubah
        kolam_kepiting = kolam.copy() #membuat agar kolam pada hasil akhir dapat mengikuti desain yang sama seperti kolam awal namun isi kolam hadia tidak diketahui dari awal
        kepiting_alaska = random.randint(1, 4) # random integer dari angka 1 samapi dengan 4
        kolam_kepiting[kepiting_alaska - 1] = "|🦀|" #memunculkan hadiah dengan mereplace sesuai dengan random randint lalu - 1 agar hasil sesuai dengan bahasa manusia
        new_kolam = " ".join(kolam) #menghilangkan tanda koma dan bukatutup kurung di awal
        kolam_kepiting = "".join(kolam_kepiting) #menghilangkan tanda koma dan bukatutup kurung di hasil akhir

        print(f"\nHalo! {nama_user} Coba perhatikan 4 kolam dibawah ini\n\n{new_kolam}")
        print("\nCoba Tebak kolam nomer berapakah yang terdapat KEPITING ALASKA 🦀🦀.\nMari Kita Coba Peruntunganmu!!!\n")
        jawaban_user = int(input("Masukan Nomer Peruntunganmu [ 1 / 2 / 3 / 4 ]... ")) # int() agar tipe data input menjadi Integer
        while jawaban_user != 1 and jawaban_user != 2 and jawaban_user != 3 and jawaban_user != 4: #!= tidak sama dengan | and : dan
            jawaban_user = int(input("CUMAN BISA 4 ANGKA INI KOCAK [ 1 / 2 / 3 / 4 ]... "))
        if jawaban_user == kepiting_alaska:
            print(f"\n{kolam_kepiting}")
            print(f"\nWow Jawaban kamu benar, KEPITING ALASKA terdapat dikolom nomer {kepiting_alaska}\n")
            print("SELAMATTT PANEN KEPITING ALASKAAA 🦀🦀 \n")
        else:
            print(f"\n{kolam_kepiting}")
            print(f"\nSayang banget, KEPITING ALASKA terdapat pada nomer {kepiting_alaska}\n")
            print("UBUR UBUR IKAN LELE COBA LAGI LEEE 😁😁 \n")
        
        main_lagi = input("apakah ingin bermain lagi [Y / N]... ")
        if main_lagi.upper() == "N":
            print("\nProgram Berhernti, Terimakasih Sudah Bermain Fishing Games 🤩🤩\n")
            libs.menu()
    
if __name__ == '__main__': #eksekusi ketiga
    user()
    start()        