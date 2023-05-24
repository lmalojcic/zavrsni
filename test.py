import networkx as nx
import matplotlib.pyplot as plt
from cdlib import datasets
from cdlib import algorithms
from cdlib.benchmark import LFR
from cdlib import evaluation
from cdlib import viz
from networkx.generators.community import LFR_benchmark_graph
from cdlib import NodeClustering

# n = 250
# tau1 = 3
# tau2 = 1.5
# mu = 0.1
# G, coms = LFR(n, tau1, tau2, mu, average_degree=5, min_community=20)
# G_test, test_coms = datasets.fetch_network_ground_truth(net_name="LFR_N5000_ad5_mc50_mu0.7", net_type="networkx")
# dict = {}
# for com in coms.communities:
#     for i in com:
#         dict[i] = dict.get(i, 0) + 1
# print(dict)
# leiden_coms = algorithms.leiden(G)
# louvain_coms = algorithms.louvain(G)
# leiden_amazon_coms = algorithms.leiden(G_test)
# aaaaaa = algorithms.danmf(G_test)

# print(evaluation.normalized_mutual_information(coms, leiden_coms))
# print(evaluation.normalized_mutual_information(coms, louvain_coms))

# print(evaluation.normalized_mutual_information(test_coms, leiden_amazon_coms))
# print(evaluation.overlapping_normalized_mutual_information_LFK(test_coms, aaaaaa))

# G, coms = datasets.fetch_network_ground_truth(net_name="karate_club", net_type="networkx")
# print(coms.communities)