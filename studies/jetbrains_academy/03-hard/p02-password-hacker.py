import socket
from sys import argv

# python hack.py 127.0.0.1 9090 qwerty <- These are the "sys.argvs",
# according to the exercise:
# [0] = file name
# [1] = hostname
# [2] = port
# [3] = data to be sent

with socket.socket() as client_socket:
    # Host and port definitions:
    hostname = argv[1]
    port = int(argv[2])
    address = (hostname, port)

    # Connection between socket and address:
    client_socket.connect(address)

    # Data input, encoding and sending:
    data = argv[3]
    data = data.encode()
    client_socket.send(data)

    # Response:
    response = client_socket.recv(1024)
    response = response.decode()
    print(response)
