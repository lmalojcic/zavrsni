from cdlib import algorithms
from cdlib import evaluation
import networkx as nx
import timeit

#GRAPHS
G_karate = nx.karate_club_graph()
G_florentine = nx.florentine_families_graph()
G_cities = nx.readwrite.gml.read_gml("cities_graph.gml")
G_synthetic = nx.generators.LFR_benchmark_graph(n = 250, tau1 = 3, tau2 = 1.5, mu = 0.1, average_degree=5, min_community=20, seed=10)

#ALGORITHMS

#louvain
louvain_start = timeit.default_timer()
coms_louvain_karate = algorithms.louvain(G_karate)
coms_louvain_florentine = algorithms.louvain(G_florentine)
coms_louvain_cities = algorithms.louvain(G_cities)
coms_louvain_synthetic = algorithms.louvain(G_synthetic)
louvain_time = timeit.default_timer() - louvain_start

#leiden
leiden_start = timeit.default_timer()
coms_leiden_karate = algorithms.leiden(G_karate)
coms_leiden_florentine = algorithms.leiden(G_florentine)
coms_leiden_cities = algorithms.leiden(G_cities)
coms_leiden_synthetic = algorithms.leiden(G_synthetic)
leiden_time = timeit.default_timer() - leiden_start

#label propagation
lprop_start = timeit.default_timer()
coms_lprop_karate = algorithms.label_propagation(G_karate) 
coms_lprop_florentine = algorithms.label_propagation(G_florentine)
coms_lprop_cities = algorithms.label_propagation(G_cities)
coms_lprop_synthetic = algorithms.label_propagation(G_synthetic)
lprop_time = timeit.default_timer() - lprop_start


#METRICS - TIME
print("Time:")
print("Louvain:\t", louvain_time)
print("Leiden:\t\t", leiden_time)
print("Label Prop:\t", lprop_time)

#METRICS - MODULARITY
#louvain
mod_louvain_karate = evaluation.newman_girvan_modularity(G_karate, coms_louvain_karate)
mod_louvain_florentine = evaluation.newman_girvan_modularity(G_florentine, coms_louvain_florentine)
mod_louvain_cities = evaluation.newman_girvan_modularity(G_cities, coms_louvain_cities)
mod_louvain_synthetic = evaluation.newman_girvan_modularity(G_synthetic, coms_louvain_synthetic)

#leiden
mod_leiden_karate = evaluation.newman_girvan_modularity(G_karate, coms_leiden_karate)
mod_leiden_florentine = evaluation.newman_girvan_modularity(G_florentine, coms_leiden_florentine)
mod_leiden_cities = evaluation.newman_girvan_modularity(G_cities, coms_leiden_cities)
mod_leiden_synthetic = evaluation.newman_girvan_modularity(G_synthetic, coms_leiden_synthetic)
#label propagation
mod_lprop_karate = evaluation.newman_girvan_modularity(G_karate, coms_lprop_karate)
mod_lprop_florentine = evaluation.newman_girvan_modularity(G_florentine, coms_lprop_florentine)
mod_lprop_cities = evaluation.newman_girvan_modularity(G_cities, coms_lprop_cities)
mod_lprop_synthetic = evaluation.newman_girvan_modularity(G_synthetic, coms_lprop_synthetic)

print("Louvain karate modularity:\t", mod_louvain_karate)
print("Leiden karate modularity:\t", mod_leiden_karate)
print("Label Prop karate modularity:\t", mod_lprop_karate)

print("Louvain florentine modularity:\t", mod_louvain_florentine)
print("Leiden florentine modularity:\t", mod_leiden_florentine)
print("Label Prop florentine modularity:\t", mod_lprop_florentine)

print("Louvain cities modularity:\t", mod_louvain_cities)
print("Leiden cities modularity:\t", mod_leiden_cities)
print("Label Prop cities modularity:\t", mod_lprop_cities)

print("Louvain synthetic modularity:\t", mod_louvain_synthetic)
print("Leiden synthetic modularity:\t", mod_leiden_synthetic)
print("Label Prop synthetic modularity:\t", mod_lprop_synthetic)


#METRICS - CONDUCTANCE
#louvain
cond_louvain_karate = evaluation.conductance(G_karate, coms_louvain_karate)
cond_louvain_florentine = evaluation.conductance(G_florentine, coms_louvain_florentine)
cond_louvain_cities = evaluation.conductance(G_cities, coms_louvain_cities)
cond_louvain_synthetic = evaluation.conductance(G_synthetic, coms_louvain_synthetic)

#leiden
cond_leiden_karate = evaluation.conductance(G_karate, coms_leiden_karate)
cond_leiden_florentine = evaluation.conductance(G_florentine, coms_leiden_florentine)
cond_leiden_cities = evaluation.conductance(G_cities, coms_leiden_cities)
cond_leiden_synthetic = evaluation.conductance(G_synthetic, coms_leiden_synthetic)

#label propagation
cond_lprop_karate = evaluation.conductance(G_karate, coms_lprop_karate)
cond_lprop_florentine = evaluation.conductance(G_florentine, coms_lprop_florentine)
cond_lprop_cities = evaluation.conductance(G_cities, coms_lprop_cities)
cond_lprop_synthetic = evaluation.conductance(G_synthetic, coms_lprop_synthetic)

print("Louvain karate conductance:\t", cond_louvain_karate)
print("Leiden karate conductance:\t", cond_leiden_karate)
print("Label Prop karate conductance:\t", cond_lprop_karate)

print("Louvain florentine conductance:\t", cond_louvain_florentine)
print("Leiden florentine conductance:\t", cond_leiden_florentine)
print("Label Prop florentine conductance:\t", cond_lprop_florentine)

print("Louvain cities conductance:\t", cond_louvain_cities)
print("Leiden cities conductance:\t", cond_leiden_cities)
print("Label Prop cities conductance:\t", cond_lprop_cities)

print("Louvain synthetic conductance:\t", cond_louvain_synthetic)
print("Leiden synthetic conductance:\t", cond_leiden_synthetic)
print("Label Prop synthetic conductance:\t", cond_lprop_synthetic)