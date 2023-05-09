import networkx as nx
import matplotlib.pyplot as plt
# from networkx.generators.community import LFR_benchmark_graph

# n = 20

# tau1 = 3

# tau2 = 1.5

# mu = 0.1

# G = LFR_benchmark_graph(

#     n, tau1, tau2, mu, average_degree=5, min_community=20, seed=10

# )

#G = nx.relaxed_caveman_graph(5, 5, 0.5, seed=42)

G = nx.random_partition_graph([10, 10, 10, 10, 10, 10, 10, 10], 0.3, 0.1)

pos = nx.spring_layout(G)

plt.figure(1)
nx.draw_networkx(G, with_labels = True, pos=pos)
plt.show()