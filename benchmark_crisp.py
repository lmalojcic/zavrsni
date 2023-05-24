import networkx as nx
from cdlib import algorithms
from cdlib import evaluation
from cdlib import datasets
import re

class BenchmarkGraph:
    def __init__(self, n, ad, mc, mu, nmi_louvain, nmi_leiden, nmi_lprop):
        self.n = n
        self.ad = ad
        self.mc = mc
        self.mu = mu
        self.nmi_louvain = nmi_louvain
        self.nmi_leiden = nmi_leiden
        self.nmi_lprop = nmi_lprop
    def __str__(self):
        x = "n: " + str(self.n) + " ad: " + str(self.ad) + " mc: " + str(self.mc) + " mu: " + str(self.mu) + " nmi_louvain: " + str(self.nmi_louvain) + " nmi_leiden: " + str(self.nmi_leiden) + " nmi_lprop: " + str(self.nmi_lprop)
        return x

list = datasets.available_networks()
results = []
for i in list:
    if (i[0:3] == "LFR"):
        G, coms = datasets.fetch_network_ground_truth(net_name=i, net_type="networkx")
        coms_louvain = algorithms.louvain(G)
        coms_leiden = algorithms.leiden(G)
        coms_lprop = algorithms.label_propagation(G)
        temp = i.split("_")
        n = int(re.findall(r"\d+", temp[1])[0])
        ad = int(re.findall(r"\d+", temp[2])[0])
        mc = int(re.findall(r"\d+", temp[3])[0])
        mu = float(re.findall(r"\d+\.\d+", temp[4])[0])
        nmi_louvain = evaluation.normalized_mutual_information(coms, coms_louvain)
        nmi_leiden = evaluation.normalized_mutual_information(coms, coms_leiden)
        nmi_lprop = evaluation.normalized_mutual_information(coms, coms_lprop)
        results.append(BenchmarkGraph(n, ad, mc, mu, nmi_louvain, nmi_leiden, nmi_lprop))
        print("done with graph " + str(i))

for result in results:
    print(result)