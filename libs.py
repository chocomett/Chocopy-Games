import socket
from time import sleep
from games import fishing,snake

PC_NAME = socket.gethostname()


def wellcome_message(message):
    style = "*" * (len(message) + 6)
    print(style)
    print(f"** {message} **")
    print(style)

def menu():
    user_option = int(input(f"Menu Program:\n\n1. Fishingpy\n2. Snakepy\n3. Keluar\n\nsilakan pilih: "))
    if user_option == 1:
        fishing.start() #from choco.py        
    elif user_option == 2:
        snake.start()
    elif user_option == 3:
        exit_program()        
    else:
        print("Pilihan tidak tersedia")
    

    
def exit_program():
    print("Program akan dihentikan ...")
    sleep(0.5) #program akan delay selama 1 detik
    print("3...")
    sleep(0.5) 
    print("2...")
    sleep(0.5) 
    print("1...")
    sleep(0.5) 
    print("Program di hentikan")
    exit()
       

if __name__ ==  "__main__":
    wellcome_message()
    menu()
    exit_program()
    