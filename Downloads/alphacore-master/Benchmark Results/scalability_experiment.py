import networkx as nx
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from alphacore import alphaCore 

def generate_graph(num_nodes, edge_prob, num_features):
    """
    Generates a random directed graph with specified parameters.
    Each node gets num_features random numeric attributes.
    """
    G = nx.gnp_random_graph(num_nodes, edge_prob, directed=True)
    for node in G.nodes():
        for i in range(1, num_features+1):
            G.nodes[node][f"f{i}"] = np.random.rand()
    return G

# Define parameter ranges
node_counts = [1000, 5000, 10000]            
feature_counts = [6, 20, 40, 60, 80, 100]      
edge_probs = np.arange(0.01, 0.305, 0.005)      # from 0.01 to 0.3 (inclusive) by increments of 0.005

# To store results
results = []

# Loop over parameter combinations
for n in node_counts:
    for f_count in feature_counts:
        for p in edge_probs:
            G = generate_graph(n, p, f_count)
            start_time = time.time()
            # Run alphaCore (using default parameters for stepSize, startEpsi, expoDecay)
            _ = alphaCore(G, features=["all"], stepSize=0.1, startEpsi=1, expoDecay=False)
            runtime = time.time() - start_time
            results.append({"nodes": n, "features": f_count, "edge_prob": p, "runtime_sec": runtime})
            print(f"Nodes: {n}, Features: {f_count}, Edge_Prob: {p:.3f}, Runtime: {runtime:.4f} sec")

df_results = pd.DataFrame(results)

# Plot runtime vs. node count for a fixed feature count and edge probability
fixed_features = 20
fixed_edge_prob = 0.05
subset = df_results[(df_results["features"] == fixed_features) & (np.isclose(df_results["edge_prob"], fixed_edge_prob, atol=0.001))]

plt.figure(figsize=(8,6))
plt.plot(subset["nodes"], subset["runtime_sec"], marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("Runtime (seconds)")
plt.title(f"Runtime vs. Number of Nodes (Features={fixed_features}, Edge_Prob={fixed_edge_prob})")
plt.grid(True)
plt.show()

