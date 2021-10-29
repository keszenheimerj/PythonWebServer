#~/Desktop/PythonWebServer.py
# Project 2 - TCP Web Server Lab
 
# import socket module
from socket import *
import sys  # In order to terminate the program
import argparse  # In order to help command-line-environment

# Fill in comment
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 1111  # sererSocket.getsockname()[1]
serverSocket.bind(('', serverPort))  # bind the socket to the address and port 74 .83.223.8
serverSocket.listen(1)  # listen for one connection

#  hostname = serverSocket.gethostname()
#  local_ip = serverSocket.gethostbyname(hostname)
#  print(local_ip)

while True:

    # Establish the connection
    print('Ready to serve CSCI340 Students...')

    # listen for requests that are coming in from the client connection
    connectionSocket, addr = serverSocket.accept()
    
    try:

        # receive requests that are coming in up to 4096 bytes of data
        message = connectionSocket.recv(4096)
        print(message.decode())  # print out the request
        filename = message.split()[1]  # parse the message for the file name
        f = open(filename[1:])  # open the body of the file

        outputdata = f.read()  # view the body of the file

        # Send one HTTP header line into socket for a 200 OK message
        connectionSocket.send('\nHTTP/1.1 200 OK\nContent-Type: html\n\n'.encode(encoding="utf-8", errors="strict"))

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # close the connection now that we're done, so we don't use all resources
        connectionSocket.close()

    except IOError:

        # Send HTTP response message for file not found encoding is same standard is utf8 and strict
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode(encoding="utf-8", errors="strict"))
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        # Close the client connection socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
