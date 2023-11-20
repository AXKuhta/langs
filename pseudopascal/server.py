from interpreter import Interpreter
import json
import zmq

def handle_client(client):
	# Protocol:
	# - Client sends program length
	# - Client sends program code

	while True:
		program = client.recv().decode()

		print("Program:", program)

		interp = Interpreter()

		try:
			state = interp.eval(program)
			response = json.dumps(state)
		except Exception as e:
			response = json.dumps({"error": str(e)})

		client.send(response.encode())

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
