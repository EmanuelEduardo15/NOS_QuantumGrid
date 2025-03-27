from qiskit import QuantumCircuit, Aer, execute

class QuantumTSP:
    def __init__(self, cities):
        self.n = len(cities)
        self.backend = Aer.get_backend('qasm_simulator')

    def _create_circuit(self):
        qc = QuantumCircuit(self.n)
        for qubit in range(self.n):
            qc.h(qubit)
        qc.measure_all()
        return qc

    def solve(self, shots=1024):
        qc = self._create_circuit()
        result = execute(qc, self.backend, shots=shots).result()
        return max(result.get_counts(), key=lambda k: result.get_counts()[k])

# Uso:
tsp = QuantumTSP(["Lisboa", "Porto", "Faro"])
print(tsp.solve())
