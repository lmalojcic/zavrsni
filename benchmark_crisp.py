import networkx as nx
from cdlib import algorithms
from cdlib import evaluation
from cdlib import datasets
import re

class BenchmarkGraph:
    def __init__(self, n, ad, mc, mu, nmi_louvain, nmi_leiden, nmi_lprop, nmi_infomap, nmi_cpm, nf1_louvain, nf1_leiden, nf1_lprop, nf1_infomap, nf1_cpm):
        self.n = n
        self.ad = ad
        self.mc = mc
        self.mu = mu
        self.nmi_louvain = nmi_louvain
        self.nmi_leiden = nmi_leiden
        self.nmi_lprop = nmi_lprop
        self.nmi_infomap = nmi_infomap
        self.nmi_cpm = nmi_cpm
        self.nf1_louvain = nf1_louvain
        self.nf1_leiden = nf1_leiden
        self.nf1_lprop = nf1_lprop
        self.nf1_infomap = nf1_infomap
        self.nf1_cpm = nf1_cpm
    def __str__(self):
        x = str(self.n) + "," + str(self.ad) + "," + str(self.mc) + "," + str(self.mu) + "," + str(self.nmi_louvain) + "," + str(self.nmi_leiden) + "," + str(self.nmi_lprop) + "," + str(self.nmi_infomap) + "," + str(self.nmi_cpm) + "," + str(self.nf1_louvain) + "," + str(self.nf1_leiden) + "," + str(self.nf1_lprop) + "," + str(self.nf1_infomap) + "," + str(self.nf1_cpm)
        return x

list = datasets.available_networks()
results = []
for i in list:
    if (i[0:3] == "LFR"):
        G, coms = datasets.fetch_network_ground_truth(net_name=i, net_type="networkx")
        coms_louvain = algorithms.louvain(G)
        coms_leiden = algorithms.leiden(G)
        coms_lprop = algorithms.label_propagation(G)
        coms_infomap = algorithms.infomap(G)
        coms_cpm = algorithms.cpm(G)
        temp = i.split("_")
        n = int(re.findall(r"\d+", temp[1])[0])
        ad = int(re.findall(r"\d+", temp[2])[0])
        mc = int(re.findall(r"\d+", temp[3])[0])
        mu = float(re.findall(r"\d+\.\d+", temp[4])[0])
        nmi_louvain = evaluation.normalized_mutual_information(coms, coms_louvain)
        nmi_leiden = evaluation.normalized_mutual_information(coms, coms_leiden)
        nmi_lprop = evaluation.normalized_mutual_information(coms, coms_lprop)
        nmi_infomap = evaluation.normalized_mutual_information(coms, coms_infomap)
        nmi_cpm = evaluation.normalized_mutual_information(coms, coms_cpm)
        nf1_louvain = evaluation.nf1(coms, coms_louvain)
        nf1_leiden = evaluation.nf1(coms, coms_leiden)
        nf1_lprop = evaluation.nf1(coms, coms_lprop)
        nf1_infomap = evaluation.nf1(coms, coms_infomap)
        nf1_cpm = evaluation.nf1(coms, coms_cpm)
        results.append(BenchmarkGraph(n, ad, mc, mu, nmi_louvain.score, nmi_leiden.score, nmi_lprop.score, nmi_infomap.score, nmi_cpm.score, nf1_louvain.score, nf1_leiden.score, nf1_lprop.score, nf1_infomap.score, nf1_cpm.score))
        print("done with graph " + str(i))

header = "n,ad,mc,mu,nmi_louvain,nmi_leiden,nmi_lprop,nmi_infomap,nmi_cpm,nf1_louvain,nf1_leiden,nf1_lprop,nf1_infomap,nf1_cpm"
f = open("benchmark_crisp.csv", "w")
f.write(header + "\n")
f.writelines(str(x) + "\n" for x in results)
f.close()
for result in results:
    print(result)