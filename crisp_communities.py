from cdlib import algorithms
from cdlib import evaluation
import networkx as nx
import timeit

#GRAPHS
comms = [10] * 100
G_karate = nx.karate_club_graph()
G_florentine = nx.florentine_families_graph()
G_lesmis = nx.les_miserables_graph()
G_synthetic = nx.random_partition_graph(comms, 0.3, 0.1)

#ALGORITHMS

#louvain
louvain_start = timeit.default_timer()
coms_louvain_karate = algorithms.louvain(G_karate)
coms_louvain_florentine = algorithms.louvain(G_florentine)
coms_louvain_lesmis = algorithms.louvain(G_lesmis)
coms_louvain_synthetic = algorithms.louvain(G_synthetic)
louvain_time = timeit.default_timer() - louvain_start

#leiden
leiden_start = timeit.default_timer()
coms_leiden_karate = algorithms.leiden(G_karate)
coms_leiden_florentine = algorithms.leiden(G_florentine)
coms_leiden_lesmis = algorithms.leiden(G_lesmis)
coms_leiden_synthetic = algorithms.leiden(G_synthetic)
leiden_time = timeit.default_timer() - leiden_start

#label propagation
lprop_start = timeit.default_timer()
coms_lprop_karate = algorithms.label_propagation(G_karate) 
coms_lprop_florentine = algorithms.label_propagation(G_florentine)
coms_lprop_lesmis = algorithms.label_propagation(G_lesmis)
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
mod_louvain_lesmis = evaluation.newman_girvan_modularity(G_lesmis, coms_louvain_lesmis)
mod_louvain_synthetic = evaluation.newman_girvan_modularity(G_synthetic, coms_louvain_synthetic)

#leiden
mod_leiden_karate = evaluation.newman_girvan_modularity(G_karate, coms_leiden_karate)
mod_leiden_florentine = evaluation.newman_girvan_modularity(G_florentine, coms_leiden_florentine)
mod_leiden_lesmis = evaluation.newman_girvan_modularity(G_lesmis, coms_leiden_lesmis)
mod_leiden_synthetic = evaluation.newman_girvan_modularity(G_synthetic, coms_leiden_synthetic)
#label propagation
mod_lprop_karate = evaluation.newman_girvan_modularity(G_karate, coms_lprop_karate)
mod_lprop_florentine = evaluation.newman_girvan_modularity(G_florentine, coms_lprop_florentine)
mod_lprop_lesmis = evaluation.newman_girvan_modularity(G_lesmis, coms_lprop_lesmis)
mod_lprop_synthetic = evaluation.newman_girvan_modularity(G_synthetic, coms_lprop_synthetic)

print("Louvain karate modularity:\t", mod_louvain_karate)
print("Leiden karate modularity:\t", mod_leiden_karate)
print("Label Prop karate modularity:\t", mod_lprop_karate)

print("Louvain florentine modularity:\t", mod_louvain_florentine)
print("Leiden florentine modularity:\t", mod_leiden_florentine)
print("Label Prop florentine modularity:\t", mod_lprop_florentine)

print("Louvain lesmis modularity:\t", mod_louvain_lesmis)
print("Leiden lesmis modularity:\t", mod_leiden_lesmis)
print("Label Prop lesmis modularity:\t", mod_lprop_lesmis)

print("Louvain synthetic modularity:\t", mod_louvain_synthetic)
print("Leiden synthetic modularity:\t", mod_leiden_synthetic)
print("Label Prop synthetic modularity:\t", mod_lprop_synthetic)


#METRICS - CONDUCTANCE
#louvain
cond_louvain_karate = evaluation.conductance(G_karate, coms_louvain_karate)
cond_louvain_florentine = evaluation.conductance(G_florentine, coms_louvain_florentine)
cond_louvain_lesmis = evaluation.conductance(G_lesmis, coms_louvain_lesmis)
cond_louvain_synthetic = evaluation.conductance(G_synthetic, coms_louvain_synthetic)

#leiden
cond_leiden_karate = evaluation.conductance(G_karate, coms_leiden_karate)
cond_leiden_florentine = evaluation.conductance(G_florentine, coms_leiden_florentine)
cond_leiden_lesmis = evaluation.conductance(G_lesmis, coms_leiden_lesmis)
cond_leiden_synthetic = evaluation.conductance(G_synthetic, coms_leiden_synthetic)

#label propagation
cond_lprop_karate = evaluation.conductance(G_karate, coms_lprop_karate)
cond_lprop_florentine = evaluation.conductance(G_florentine, coms_lprop_florentine)
cond_lprop_lesmis = evaluation.conductance(G_lesmis, coms_lprop_lesmis)
cond_lprop_synthetic = evaluation.conductance(G_synthetic, coms_lprop_synthetic)

print("Louvain karate conductance:\t", cond_louvain_karate)
print("Leiden karate conductance:\t", cond_leiden_karate)
print("Label Prop karate conductance:\t", cond_lprop_karate)

print("Louvain florentine conductance:\t", cond_louvain_florentine)
print("Leiden florentine conductance:\t", cond_leiden_florentine)
print("Label Prop florentine conductance:\t", cond_lprop_florentine)

print("Louvain lesmis conductance:\t", cond_louvain_lesmis)
print("Leiden lesmis conductance:\t", cond_leiden_lesmis)
print("Label Prop lesmis conductance:\t", cond_lprop_lesmis)

print("Louvain synthetic conductance:\t", cond_louvain_synthetic)
print("Leiden synthetic conductance:\t", cond_leiden_synthetic)
print("Label Prop synthetic conductance:\t", cond_lprop_synthetic)