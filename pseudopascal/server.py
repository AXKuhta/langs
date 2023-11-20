from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from interpreter import Interpreter
import json

def server(host, port):
	with socket(AF_INET, SOCK_STREAM) as sock:
		sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)	# Allow address reuse
		#sock.setblocking(False)							# Non blocking mode, suffers from high CPU usage
		sock.bind( (host, port) )
		sock.listen(10)

		print(f"Server is up on {host}:{port}")

		while True:
			try:
				client, addr = sock.accept()
				print("Client connected:", *addr)

				# Protocol:
				# - Client sends program length
				# - Client sends program code

				while True:
					msglen = int.from_bytes( client.recv(4) )

					if msglen == 0:
						break

					program = client.recv(msglen).decode()

					print("Program:", program)

					interp = Interpreter()

					try:
						state = interp.eval(program)
						response = json.dumps(state).encode()
					except Exception as e:
						response = json.dumps({"error": str(e)}).encode()

					client.send(len(response).to_bytes(4))
					client.send(response)

				print("Client", *addr, "disconnected")
				client.close()
			except BlockingIOError:
				pass

server("0.0.0.0", 8089)
