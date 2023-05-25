from cdlib import algorithms
from cdlib import evaluation
from cdlib import datasets
import networkx as nx
import timeit

G_karate, karate_g_truth = datasets.fetch_network_ground_truth(net_name="karate_club", net_type="networkx")
G_florentine = nx.florentine_families_graph()
G_cities = nx.readwrite.gml.read_gml("cities_graph.gml")
G_amazon, amazon_g_truth = datasets.fetch_network_ground_truth(net_name="amazon", net_type="networkx")

n = 10000

#KARATE
karate_mod_total = 0
karate_conductance_total = 0
karate_time = 0
karate_mod_results = []
karate_conductance_results = []
karate_nmi_total = 0
karate_nmi_results = []
karate_nf1_total = 0
karate_nf1_results = []

for i in range(n):
    karate_time_start = timeit.default_timer()
    coms_louvain_karate = algorithms.infomap(G_karate)
    karate_time += timeit.default_timer() - karate_time_start
    mod = evaluation.newman_girvan_modularity(G_karate, coms_louvain_karate)
    karate_mod_total += mod.score
    karate_mod_results.append(mod.score)
    conductance = evaluation.conductance(G_karate, coms_louvain_karate)
    karate_conductance_total += conductance.score
    karate_conductance_results.append(conductance.score)
    karate_nmi = evaluation.normalized_mutual_information(karate_g_truth, coms_louvain_karate)
    karate_nmi_total += karate_nmi.score
    karate_nmi_results.append(karate_nmi.score)
    karate_nf1 = evaluation.nf1(karate_g_truth, coms_louvain_karate)
    karate_nf1_total += karate_nf1.score
    karate_nf1_results.append(karate_nf1.score)

karate_mod_avg = karate_mod_total / n
karate_conductance_avg = karate_conductance_total / n
karate_mod_stdev = (sum((x-(sum(karate_mod_results) / len(karate_mod_results)))**2 for x in karate_mod_results) / (len(karate_mod_results)-1))**0.5
karate_conductance_stdev = (sum((x-(sum(karate_conductance_results) / len(karate_conductance_results)))**2 for x in karate_conductance_results) / (len(karate_conductance_results)-1))**0.5
karate_nmi_avg = karate_nmi_total / n
karate_nmi_stdev = (sum((x-(sum(karate_nmi_results) / len(karate_nmi_results)))**2 for x in karate_nmi_results) / (len(karate_nmi_results)-1))**0.5
karate_nf1_avg = karate_nf1_total / n
karate_nf1_stdev = (sum((x-(sum(karate_nf1_results) / len(karate_nf1_results)))**2 for x in karate_nf1_results) / (len(karate_nf1_results)-1))**0.5

print("Karate time: " + str(karate_time))
print("Karate modularity: " + str(karate_mod_avg))
print("Karate modularity stdev: " + str(karate_mod_stdev))
print("Karate conductance: " + str(karate_conductance_avg))
print("Karate conductance stdev: " + str(karate_conductance_stdev))
print("Karate NMI: " + str(karate_nmi_avg))
print("Karate NMI stdev: " + str(karate_nmi_stdev))
print("Karate NF1: " + str(karate_nf1_avg))
print("Karate NF1 stdev: " + str(karate_nf1_stdev))

#FLORENTINE
florentine_mod_total = 0
florentine_conductance_total = 0
florentine_time = 0
florentine_mod_results = []
florentine_condcutance_results = []
for i in range(n):
    florentine_time_start = timeit.default_timer()
    coms_louvain_florentine = algorithms.infomap(G_florentine)
    florentine_time += timeit.default_timer() - florentine_time_start
    mod = evaluation.newman_girvan_modularity(G_florentine, coms_louvain_florentine)
    florentine_mod_total += mod.score
    florentine_mod_results.append(mod.score)
    conductance = evaluation.conductance(G_florentine, coms_louvain_florentine)
    florentine_conductance_total += conductance.score
    florentine_condcutance_results.append(conductance.score)
florentine_mod_avg = florentine_mod_total / n
florentine_conductance_avg = florentine_conductance_total / n
florentine_mod_stdev = (sum((x-(sum(florentine_mod_results) / len(florentine_mod_results)))**2 for x in florentine_mod_results) / (len(florentine_mod_results)-1))**0.5
florentine_conductance_stdev = (sum((x-(sum(florentine_condcutance_results) / len(florentine_condcutance_results)))**2 for x in florentine_condcutance_results) / (len(florentine_condcutance_results)-1))**0.5

print("Florentine time: " + str(florentine_time))
print("Florentine modularity: " + str(florentine_mod_avg))
print("Florentine modularity stdev: " + str(florentine_mod_stdev))
print("Florentine conductance: " + str(florentine_conductance_avg))
print("Florentine conductance stdev: " + str(florentine_conductance_stdev))

#CITIES
cities_mod_total = 0
cities_conductance_total = 0
cities_time = 0
cities_mod_results = []
cities_conductance_results = []
for i in range(n):
    cities_time_start = timeit.default_timer()
    coms_louvain_cities = algorithms.infomap(G_cities)
    cities_time += timeit.default_timer() - cities_time_start
    mod = evaluation.newman_girvan_modularity(G_cities, coms_louvain_cities)
    cities_mod_total += mod.score
    cities_mod_results.append(mod.score)
    conductance = evaluation.conductance(G_cities, coms_louvain_cities)
    cities_conductance_total += conductance.score
    cities_conductance_results.append(conductance.score)
cities_mod_avg = cities_mod_total / n
cities_conductance_avg = cities_conductance_total / n
cities_mod_stdev = (sum((x-(sum(cities_mod_results) / len(cities_mod_results)))**2 for x in cities_mod_results) / (len(cities_mod_results)-1))**0.5
cities_conductance_stdev = (sum((x-(sum(cities_conductance_results) / len(cities_conductance_results)))**2 for x in cities_conductance_results) / (len(cities_conductance_results)-1))**0.5

print("Cities time: " + str(cities_time))
print("Cities modularity: " + str(cities_mod_avg))
print("Cities modularity stdev: " + str(cities_mod_stdev))
print("Cities conductance: " + str(cities_conductance_avg))
print("Cities conductance stdev: " + str(cities_conductance_stdev))

#AMAZON
amazon_start = timeit.default_timer()
coms_amazon = algorithms.infomap(G_amazon)
amazon_time = timeit.default_timer() - amazon_start
mod = evaluation.newman_girvan_modularity(G_amazon, coms_amazon)
conductance = evaluation.conductance(G_amazon, coms_amazon)

print("Amazon time: " + str(amazon_time))
print("Amazon modularity: " + str(mod.score))
print("Amazon conductance: " + str(conductance.score))