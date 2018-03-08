import socket as sock
serverName = '192.168.1.110'
serverPort = 12000
clientSocket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("To exchange currency enter: <amount> <cur1> cur2>\n")
while 1:
    message = input()
    if (message == '?'):
        print("USD \t United States Dollar \nEUR \t Euro\nCAD \t Canadian dollar \nGBP \t United Kingdom pound")
        print("To exchange currency enter: <amount> <cur1> cur2>\n")
    elif (message.upper() == 'Q'):
        break
    elif (message.upper() == ''):
        continue
    else:
        res = clientSocket.send(message.encode())
        modifiedMessage= clientSocket.recv(1024)
        print(modifiedMessage.decode() + "\n")
clientSocket.close()
