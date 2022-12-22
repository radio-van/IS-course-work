import csv
import json
import socket


"""
A demonstration program of multi-agent system.
This part is a client which sends data to the server and outputs reply from it.

In real world this could be an agent that gathers values from sensors on
a manufacturing and requests sever for estimating them.
"""


def read_data():
    with open('sensors.csv', mode='r') as data_file:
        csv_file = csv.reader(data_file)
        return {
            key: value for key, value in zip(
                *[line for line in csv_file]
            )}


def client():
    data = read_data()
    print(f'Data from sensors: {data}')
    data = json.dumps(data).encode()

    host = socket.gethostname()  # localhost, for demo purposes
    port = 5005

    client_socket = socket.socket()  # create socket
    client_socket.connect((host, port))  # connect to the server

    print(f'Connection to {host}:{port} established. Send data? (y/n)')

    if str(input('-> ')) == 'y':
        client_socket.send(data)  # send data
        response = client_socket.recv(1024).decode()  # receive response

        print('Failure estimation: ' + response)  # output estimation results

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client()
