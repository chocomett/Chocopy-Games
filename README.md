# Chocopy-Games

Simple Clean Code

# if __name__ == '__main__': 
# Berfungsi sebagai Protect code agar code dapat tereksekusi secara rapi
# Karena Program akan selalu mengeksekusi isi file tersebut saat pertama kali program dijalankan

# Alur Code:
1. if __name__ == '__main__': memanggil def main
2. def main() berisi wellcome message dan def dari file choco.py
3. file choco.py berisi def start yang berisi logic game
4. lalu terdapat if __name__ == '__main__': di file choco.py yang berisi mengeksekusi def start()