#%%

import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram


simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(6, 6)

for i in range(1,5):
  circuit.h(i)

for n in range(1,5):
  circuit.cx(0, n)

circuit.measure([0,1,2,3,4,5], [0,1,2,3,4,5])


job = execute(circuit, simulator, shots=1000)

result = job.result()

counts = result.get_counts(circuit)
print(counts)


circuit.draw()
# %%
