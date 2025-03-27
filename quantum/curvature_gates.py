from qiskit.circuit import Gate

class CurvatureGate(Gate):
    def __init__(self, kappa):
        super().__init__(name=f"Curv({kappa})", num_qubits=1, params=[kappa])

    def _define(self):
        qc = QuantumCircuit(1)
        qc.rz(self.params[0], 0)
        self.definition = qc
