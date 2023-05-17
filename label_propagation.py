from cdlib import algorithms
from cdlib import evaluation
import networkx as nx
import timeit

G_karate = nx.karate_club_graph()
G_florentine = nx.florentine_families_graph()
G_cities = nx.readwrite.gml.read_gml("cities_graph.gml")
G_amazon = nx.readwrite.gml.read_gml("amazon_graph.gml")

#KARATE
karate_mod_total = 0
karate_conductance_total = 0
karate_time = 0
for i in range(1000):
    karate_time_start = timeit.default_timer()
    coms_louvain_karate = algorithms.label_propagation(G_karate)
    karate_time += timeit.default_timer() - karate_time_start
    mod = evaluation.newman_girvan_modularity(G_karate, coms_louvain_karate)
    karate_mod_total += mod.score
    conductance = evaluation.conductance(G_karate, coms_louvain_karate)
    karate_conductance_total += conductance.score
karate_mod_avg = karate_mod_total / 1000
karate_conductance_avg = karate_conductance_total / 1000

print("Karate time: " + str(karate_time))
print("Karate modularity: " + str(karate_mod_avg))
print("Karate conductance: " + str(karate_conductance_avg))

#FLORENTINE
florentine_mod_total = 0
florentine_conductance_total = 0
florentine_time = 0
for i in range(1000):
    florentine_time_start = timeit.default_timer()
    coms_louvain_florentine = algorithms.label_propagation(G_florentine)
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
    coms_louvain_cities = algorithms.label_propagation(G_cities)
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
coms_amazon = algorithms.label_propagation(G_amazon)
amazon_time = timeit.default_timer() - amazon_start
mod = evaluation.newman_girvan_modularity(G_amazon, coms_amazon)
conductance = evaluation.conductance(G_amazon, coms_amazon)

print("Amazon time: " + str(amazon_time))
print("Amazon modularity: " + str(mod.score))
print("Amazon conductance: " + str(conductance.score))