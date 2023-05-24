import networkx as nx
from cdlib import algorithms
from cdlib import evaluation
from cdlib import datasets
from cdlib.benchmark import LFR
import re

class BenchmarkGraph:
    def __init__(self, n, ad, mc, mu, nmi_demon, nmi_danmf, nmi_egosplit):
        self.n = n
        self.ad = ad
        self.mc = mc
        self.mu = mu
        self.nmi_demon = nmi_demon
        self.nmi_danmf = nmi_danmf
        self.nmi_egosplit = nmi_egosplit
    def __str__(self):
        x = "n: " + str(self.n) + " ad: " + str(self.ad) + " mc: " + str(self.mc) + " mu: " + str(self.mu) + " nmi_demon: " + str(self.nmi_demon) + " nmi_danmf: " + str(self.nmi_danmf) + " nmi_egosplit: " + str(self.nmi_egosplit)
        return x

list = datasets.available_networks()
results = []
for i in list:
    if (i[0:3] == "LFR"):
        G, coms = datasets.fetch_network_ground_truth(net_name=i, net_type="networkx")
        coms_demon = algorithms.demon(G, min_com_size=50, epsilon=0.25)
        coms_danmf = algorithms.danmf(G)
        coms_egosplit = algorithms.egonet_splitter(G)
        temp = i.split("_")
        n = int(re.findall(r"\d+", temp[1])[0])
        ad = int(re.findall(r"\d+", temp[2])[0])
        mc = int(re.findall(r"\d+", temp[3])[0])
        mu = float(re.findall(r"\d+\.\d+", temp[4])[0])
        nmi_demon = evaluation.overlapping_normalized_mutual_information_MGH(coms, coms_demon)
        nmi_danmf = evaluation.overlapping_normalized_mutual_information_MGH(coms, coms_danmf)
        nmi_egosplit = evaluation.overlapping_normalized_mutual_information_MGH(coms, coms_egosplit)
        results.append(BenchmarkGraph(n, ad, mc, mu, nmi_demon, nmi_danmf.score, nmi_egosplit.score))
        print("done with graph " + str(i))

for result in results:
    print(result)