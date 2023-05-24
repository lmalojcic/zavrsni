import networkx as nx
from cdlib import algorithms
from cdlib import evaluation
from cdlib import NodeClustering
from cdlib import datasets


# G = nx.generators.LFR_benchmark_graph(n = 250, tau1 = 3, tau2 = 1.5, mu = 0.1, average_degree=5, min_community=20, seed=10)
# communities = [(G.nodes[v]['community']) for v in G.nodes]

# test = NodeClustering(communities, G, "benchmark")

# communities_egonet = algorithms.egonet_splitter(G)
# communities_louvain = algorithms.louvain(G)

# print("NMI egonet: " + str(evaluation.overlapping_normalized_mutual_information_LFK(test, communities_egonet)))
# print("NMI louvain: " + str(evaluation.normalized_mutual_information(test, communities_louvain)))

g_list = datasets.available_ground_truths()

for g in g_list:
    coms = datasets.fetch_ground_truth_data(net_name=g)
    print(str(g) + " " + str(coms.overlap))