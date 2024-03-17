from cirq import GridQubit, Circuit, X, I, H, CNOT, measure, Simulator, plot_state_histogram
import matplotlib.pyplot as plt
import sys


def getCircuit1(qA, qB):
	circuit = Circuit(
		X(qA), CNOT(qA, qB), H(qB), # Apply the quantum gates
		measure(qA, qB)  # Measurement
	)
	return circuit


def getCircuit2(qA, qB):
	circuit = Circuit(
		H(qA), CNOT(qA, qB), H(qA), X(qA), # Apply the quantum gates
		measure(qA, qB)  # Measurement
	)
	return circuit


def getCircuit3(qA, qB):
	circuit = Circuit(
		X(qB), H(qA), CNOT(qA, qB), # Apply the quantum gates
		measure(qA, qB)  # Measurement
	)
	return circuit


def main():
	# Initialize two qubits in state 0 
	# (must be different coords since a quantum processor/device has qubits at different locations)
	qubit_A = GridQubit(0, 0)
	qubit_B = GridQubit(0, 1)

	# Create a circuit
	circuit_number = int(sys.argv[1])
	if circuit_number == 1:
		circuit = getCircuit1(qubit_A, qubit_B)

	elif circuit_number == 2:
		circuit = getCircuit2(qubit_A, qubit_B)

	elif circuit_number == 3:
		circuit = getCircuit3(qubit_A, qubit_B)

	print("Circuit:")
	print(circuit)

	# Simulate the circuit several times.
	simulator = Simulator()
	result = simulator.run(circuit, repetitions=100)

	print("Results:")
	plot_state_histogram(result, plt.subplot(), tick_label=['00', '01', '10', '11'])
	plt.show()


if __name__ == '__main__':
	# Check for correct number of arguments
	num_args = len(sys.argv)
	if num_args < 2:
		raise Exception("Not enough arguments. Usage: \'python3 main.py <circuit_number>\'")
	elif num_args > 3:
		raise Exception("Too many arguments. Usage: \'python3 main.py <circuit_number>\'")
	
	# Check for valid circuit number choice
	if int(sys.argv[1]) not in [1, 2, 3]:
		raise Exception("Invalid circuit number. Must be either 1, 2, or 3.")

	# Create and run the circuit
	main()
