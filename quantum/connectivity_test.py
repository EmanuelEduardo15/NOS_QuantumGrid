# connectivity_test.py
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def test_quantum_connection():
    # Criação do circuito quântico
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0,1], [0,1])
    
    # Execução no simulador
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts(qc)
    
    # Verificação do estado de Bell (conectividade quântica)
    assert '00' in counts and '11' in counts, "Falha na conectividade quântica!"
    return "Conexão quântica validada com sucesso!"

if __name__ == "__main__":
    print(test_quantum_connection())
