from cdlib import algorithms
from cdlib import evaluation
from cdlib import datasets
import networkx as nx
import timeit

G_karate, karate_g_truth = datasets.fetch_network_ground_truth(net_name="karate_club", net_type="networkx")
G_florentine = nx.florentine_families_graph()
G_cities = nx.readwrite.gml.read_gml("cities_graph.gml")
G_amazon, amazon_g_truth = datasets.fetch_network_ground_truth(net_name="amazon", net_type="networkx")
print(amazon_g_truth.overlap)

#KARATE
karate_mod_total = 0
karate_conductance_total = 0
karate_nmi_total = 0
karate_time = 0
for i in range(1000):
    karate_time_start = timeit.default_timer()
    coms_louvain_karate = algorithms.leiden(G_karate)
    karate_time += timeit.default_timer() - karate_time_start
    mod = evaluation.newman_girvan_modularity(G_karate, coms_louvain_karate)
    karate_nmi = evaluation.normalized_mutual_information(karate_g_truth, coms_louvain_karate)
    karate_nmi_total += karate_nmi.score
    karate_mod_total += mod.score
    conductance = evaluation.conductance(G_karate, coms_louvain_karate)
    karate_conductance_total += conductance.score
karate_mod_avg = karate_mod_total / 1000
karate_conductance_avg = karate_conductance_total / 1000
karate_nmi_avg = karate_nmi_total / 1000


print("Karate time: " + str(karate_time))
print("Karate modularity: " + str(karate_mod_avg))
print("Karate conductance: " + str(karate_conductance_avg))
print("Karate NMI: " + str(karate_nmi_avg))


#FLORENTINE
florentine_mod_total = 0
florentine_conductance_total = 0
florentine_time = 0
for i in range(1000):
    florentine_time_start = timeit.default_timer()
    coms_louvain_florentine = algorithms.leiden(G_florentine)
    florentine_time += timeit.default_timer() - florentine_time_start
    mod = evaluation.newman_girvan_modularity(G_florentine, coms_louvain_florentine)
    florentine_mod_total += mod.score
    conductance = evaluation.conductance(G_florentine, coms_louvain_florentine)
    florentine_conductance_total += conductance.score
florentine_mod_avg = florentine_mod_total / 1000
florentine_conductance_avg = florentine_conductance_total / 1000

print("Florentine time: " + str(florentine_time))
print("Florentine modularity: " + str(florentine_mod_avg))
print("Florentine conductance: " + str(florentine_conductance_avg))

#CITIES
cities_mod_total = 0
cities_conductance_total = 0
cities_time = 0
for i in range(1000):
    cities_time_start = timeit.default_timer()
    coms_louvain_cities = algorithms.leiden(G_cities)
    cities_time += timeit.default_timer() - cities_time_start
    mod = evaluation.newman_girvan_modularity(G_cities, coms_louvain_cities)
    cities_mod_total += mod.score
    conductance = evaluation.conductance(G_cities, coms_louvain_cities)
    cities_conductance_total += conductance.score
cities_mod_avg = cities_mod_total / 1000
cities_conductance_avg = cities_conductance_total / 1000

print("Cities time: " + str(cities_time))
print("Cities modularity: " + str(cities_mod_avg))
print("Cities conductance: " + str(cities_conductance_avg))

#AMAZON
amazon_start = timeit.default_timer()
coms_amazon = algorithms.leiden(G_amazon)
amazon_time = timeit.default_timer() - amazon_start
mod = evaluation.newman_girvan_modularity(G_amazon, coms_amazon)
conductance = evaluation.conductance(G_amazon, coms_amazon)
amazon_nmi = evaluation.normalized_mutual_information(amazon_g_truth, coms_amazon)

print("Amazon time: " + str(amazon_time))
print("Amazon modularity: " + str(mod.score))
print("Amazon conductance: " + str(conductance.score))
print("Amazon NMI: " + str(amazon_nmi.score))