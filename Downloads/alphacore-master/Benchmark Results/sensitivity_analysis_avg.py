import networkx as nx
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from alphacore import alphaCore 

def generate_small_graph(num_nodes=1000, edge_prob=0.05, num_features=6, seed=None):
    """
    Generates a small directed graph with random numeric node features.
    If a seed is provided, it sets the random seed for reproducibility.
    """
    if seed is not None:
        np.random.seed(seed)
    G = nx.gnp_random_graph(num_nodes, edge_prob, directed=True, seed=seed)
    for node in G.nodes():
        for i in range(1, num_features + 1):
            G.nodes[node][f"f{i}"] = np.random.rand()
    return G

# Sensitivity parameters
step_sizes = [0.01, 0.05, 0.1, 0.2]
expo_options = [True, False]
# Different random seeds to ensure variability
seeds = [42, 123, 2021, 7, 99]

results = []

for expo in expo_options:
    for step in step_sizes:
        runtime_list = []
        top_alpha_list = []
        for seed in seeds:
            # Generate a new graph for each seed
            G_small = generate_small_graph(num_nodes=1000, edge_prob=0.05, num_features=6, seed=seed)
            start_time = time.time()
            # Run alphaCore on a copy of the graph
            df_alpha = alphaCore(G_small.copy(), features=["all"], stepSize=step, startEpsi=1, expoDecay=expo)
            runtime_list.append(time.time() - start_time)
            if not df_alpha.empty:
                top_alpha_list.append(df_alpha['alpha'].iloc[0])
        avg_runtime = np.mean(runtime_list)
        avg_top_alpha = np.mean(top_alpha_list) if top_alpha_list else None
        results.append({
            "stepSize": step,
            "expoDecay": expo,
            "avg_runtime_sec": avg_runtime,
            "avg_top_alpha": avg_top_alpha
        })
        print(f"stepSize: {step}, expoDecay: {expo}, avg_runtime: {avg_runtime:.4f} sec, avg_top_alpha: {avg_top_alpha}")

# Convert the results to a DataFrame and display
results_df = pd.DataFrame(results)
print("\nSensitivity Analysis Results:")
print(results_df)

plt.figure(figsize=(8,6))
for expo in expo_options:
    subset = results_df[results_df["expoDecay"] == expo]
    plt.plot(subset["stepSize"], subset["avg_top_alpha"], marker='o', label=f"expoDecay = {expo}")
plt.xlabel("stepSize")
plt.ylabel("Average Top Node Alpha")
plt.title("Sensitivity of Top Node Alpha to stepSize and expoDecay")
plt.legend()
plt.grid(True)
plt.savefig("sensitivity_analysis_avg.png")
plt.show()
