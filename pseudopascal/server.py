from interpreter import Interpreter
from time import sleep
import json
import zmq

def handle_client(client):
	while True:
		try:
			program = client.recv(zmq.NOBLOCK).decode() # Nothing available -> an exception is raised

			print("Program:", program)

			interp = Interpreter()

			try:
				state = interp.eval(program)
				response = json.dumps(state)
			except Exception as e:
				response = json.dumps({"error": str(e)})

			client.send(response.encode())
		except zmq.Again:
			sleep(.05)

def server(host, port):
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind(f"tcp://{host}:{port}")

	print(f"Server is up on {host}:{port}")

	handle_client(socket)

	"""
	try:
		client, addr = sock.accept()
		print("Client connected:", *addr)
		handle_client(client)
		print("Client", *addr, "disconnected")
		client.close()
	except BlockingIOError:
		pass
	"""

server("0.0.0.0", 8089)
