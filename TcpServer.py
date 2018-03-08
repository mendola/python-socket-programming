import socket as sock

def procMsg(msg):
        lst = msg.split(" ")
        try:
                amount = float(lst[0])
        except NameError:
                return "Error!"
        except IndexError:
                return "Error!"
        except ValueError:
                return "Error!"

        cur1 = lst[1]
        cur2 = lst[2]

        try:
                val = exchange[cur1][cur2]
                return str(str(amount) + " " + cur1 + str(" = ") + str(amount * val) + " " + cur2)
        except KeyError:
                return "Error!"


exchange = {"USD" : {"USD":1.00, "EUR":0.81, "CAD":1.25, "GBP":0.72}, \
            "EUR" : {"USD":1.24, "EUR":1.00, "CAD":1.55, "GBP":0.89}, \
            "CAD" : {"USD":0.80, "EUR":0.64, "CAD":1.00, "GBP":0.57}, \
            "GBP" : {"USD":1.40, "EUR":1.13, "CAD":1.75, "GBP":1.00}}

serverPort = 12000
serverSocket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
connectionSocket, addr = serverSocket.accept()
print("The server is ready to receive")
while 1:
        try:
                request = connectionSocket.recv(1024)
        except ConnectionResetError:
                break
        reply = procMsg(request.decode().upper())
        try:
                connectionSocket.send(reply.encode())
        except BrokenPipeError:
                break
        except ConnectionResetError:
                break
print("Closed Connection.")
connectionSocket.close()
