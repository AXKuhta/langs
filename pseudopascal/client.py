from time import sleep
import json
import zmq

pretty = lambda x: json.dumps(x, indent=4)

def eval(sock, program):
	sock.send(program.encode())

	response = sock.recv()

	results = json.loads(response)

	print(pretty(results))

context = zmq.Context()
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:8089")

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

