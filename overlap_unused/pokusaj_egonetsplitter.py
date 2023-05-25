from cdlib import algorithms
from cdlib import evaluation
import networkx as nx
import timeit

G_karate = nx.karate_club_graph()
G_cities = nx.readwrite.gml.read_gml("cities_graph.gml")
G_amazon = nx.readwrite.gml.read_gml("amazon_graph.gml")

#KARATE
karate_mod_total = 0
karate_conductance_total = 0
karate_time = 0
for i in range(100):
    karate_time_start = timeit.default_timer()
    coms_louvain_karate = algorithms.egonet_splitter(G_karate)
    karate_time += timeit.default_timer() - karate_time_start
    mod = evaluation.modularity_overlap(G_karate, coms_louvain_karate)
    karate_mod_total += mod.score
    conductance = evaluation.conductance(G_karate, coms_louvain_karate)
    karate_conductance_total += conductance.score
karate_mod_avg = karate_mod_total / 100
karate_conductance_avg = karate_conductance_total / 100

print("Karate time: " + str(karate_time))
print("Karate modularity: " + str(karate_mod_avg))
print("Karate conductance: " + str(karate_conductance_avg))

#CITIES
cities_mod_total = 0
cities_conductance_total = 0
cities_time = 0
for i in range(100):
    cities_time_start = timeit.default_timer()
    coms_louvain_cities = algorithms.egonet_splitter(G_cities)
    cities_time += timeit.default_timer() - cities_time_start
    mod = evaluation.modularity_overlap(G_cities, coms_louvain_cities)
    cities_mod_total += mod.score
    conductance = evaluation.conductance(G_cities, coms_louvain_cities)
    cities_conductance_total += conductance.score
cities_mod_avg = cities_mod_total / 100
cities_conductance_avg = cities_conductance_total / 100

print("Cities time: " + str(cities_time))
print("Cities modularity: " + str(cities_mod_avg))
print("Cities conductance: " + str(cities_conductance_avg))

#AMAZON
# IZVRSAVA SE, NEMA SE S CIM USPOREDITI - OSTALI OVERLAPPING NE RADE    
amazon_start = timeit.default_timer()
coms_amazon = algorithms.egonet_splitter(G_amazon)
amazon_time = timeit.default_timer() - amazon_start
mod = evaluation.modularity_overlap(G_amazon, coms_amazon)
conductance = evaluation.conductance(G_amazon, coms_amazon)

print("Amazon time: " + str(amazon_time))
print("Amazon modularity: " + str(mod.score))
print("Amazon conductance: " + str(conductance.score))
