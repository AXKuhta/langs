from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
import json

pretty = lambda x: json.dumps(x, indent=4)

def eval(sock, program):
	bstr = program.encode()
	sock.send(len(bstr).to_bytes(4))
	sock.send(bstr)

	response_len = int.from_bytes( sock.recv(4) )
	response = sock.recv(response_len).decode()

	results = json.loads(response)

	print(pretty(results))

with socket(AF_INET, SOCK_STREAM) as sock:
	sock.connect( ("127.0.0.1", 8089) )

	program = """
	BEGIN
		a := 2 + 2
	END.
	"""

	eval(sock, program)

	sleep(10)

	program = """
	BEGIN
		a := 2 * 9999
	END.
	"""

	eval(sock, program)

