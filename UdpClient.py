import socket as sock
serverName = '192.168.1.110'
serverPort = 12000
clientSocket = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
while 1:
    message = input("To exchange currency enter: <amount> <cur1> cur2>")
    if (message == '?'):
        print("USD \t United States Dollar \nEUR \t Euro\nCAD \t Canadian dollar \nGBP \t United Kingdom pound")
    elif (message.upper() == 'Q'):
        break
    else:
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
clientSocket.close()

