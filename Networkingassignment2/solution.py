#import socket module
from socket import *
import sys # In order to terminate the program

HOST = '127.0.0.1'

PORT = 13331

def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)

   #Prepare a server socket
   serverSocket.bind((HOST,PORT))
   serverSocket.listen(1)

   while True:
       #Establish the connection
       connectionSocket, addr = serverSocket.accept()

       try:
           message = connectionSocket.recv(1024)
           #print(message)
           filename = message.split()[1]
           #print (message.split()[1])
           f = open(filename[1:])
           outputdata = f.read()

           #Send one HTTP header line into socket
           connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n")

           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())

           connectionSocket.send("\r\n".encode())
           connectionSocket.close()
       except IOError:
           connectionSocket.send("HTTP/1.0 404 Not Found \r\n\r\n")

           connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

           #Close client socket
           connectionSocket.close()


   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)

