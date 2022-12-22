import json
import socket

# import preparation from external script (agent)
from data_prepare_agent import prepare_data
from failure_estimation_agent import estimate_failure


"""
A demonstration program of multi-agent system.
This part is a server which receives data from client and
uses external agents to prepare data and estimate failure.

In real world this could be a main server that listens to
multiple clients from various manufacturing sections.
"""


FAILURE_TYPES = [
    'Heat Dissipation Failure',
    'No Failure',
    'Overstrain Failure',
    'Power Failure',
    'Random Failures',
    'Tool Wear Failure',
]


def server():
    host = socket.gethostname()  # localhost, for demo purposes
    port = 5005

    server_socket = socket.socket()  # create socket
    server_socket.bind((host, port))  # bind to host and port

    print("Server is listening on: " + f'{host}:{port}')

    server_socket.listen(1)  # listen to one client
    conn, address = server_socket.accept()  # accept new connection

    print("Received connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()  # read 1024 bytes of incoming data
        if not data:
            break

        data = json.loads(data)
        print(f'Received data from client: {data}')

        prepared_data = prepare_data(data)
        estimated_failure_type = estimate_failure(prepared_data)

        # estimator returns an index of failure type
        result = FAILURE_TYPES[estimated_failure_type]

        conn.send(result.encode())  # send estimation back to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server()
