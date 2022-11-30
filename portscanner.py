import socket 

ip = input("Digite o HOST alvo: ")

for X in range(1.65536):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = meusocket.connect_ex((ip,X))

    if res == 0:
        print(f"Porta {X} aberta")
        meusocket.close()
