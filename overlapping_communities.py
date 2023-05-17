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

#demon
demon_start = timeit.default_timer()
coms_demon_karate = algorithms.demon(G_karate, min_com_size=3, epsilon=0.25)
coms_demon_florentine = algorithms.demon(G_florentine, min_com_size=3, epsilon=0.25)
coms_demon_lesmis = algorithms.demon(G_lesmis, min_com_size=3, epsilon=0.25)
coms_demon_synthetic = algorithms.demon(G_synthetic, min_com_size=3, epsilon=0.25)
demon_time = timeit.default_timer() - demon_start


#egonet_splitter
egonet_start = timeit.default_timer()
coms_egonet_karate = algorithms.egonet_splitter(G_karate)
coms_egonet_florentine = algorithms.egonet_splitter(G_florentine)
coms_egonet_lesmis = algorithms.egonet_splitter(G_lesmis)
coms_egonet_synthetic = algorithms.egonet_splitter(G_synthetic)
egonet_time = timeit.default_timer() - egonet_start

#danmf
danmf_start = timeit.default_timer()
coms_danmf_karate = algorithms.danmf(G_karate)
coms_danmf_florentine = algorithms.danmf(G_florentine)
coms_danmf_lesmis = algorithms.danmf(G_lesmis)
coms_danmf_synthetic = algorithms.danmf(G_synthetic)
danmf_time = timeit.default_timer() - danmf_start

#METRICS - TIME
print("Time:")
print("Demon: " + str(demon_time))
print("Egonet: " + str(egonet_time))
print("Danmf: " + str(danmf_time))

#METRICS - MODULARITY
print("Modularity:")
print("Demon karate: " + str(evaluation.modularity_overlap(G_karate, coms_demon_karate)))
print("Egonet karate: " + str(evaluation.modularity_overlap(G_karate, coms_egonet_karate)))
print("Danmf karate: " + str(evaluation.modularity_overlap(G_karate, coms_danmf_karate)))
print("Demon florentine: " + str(evaluation.modularity_overlap(G_florentine, coms_demon_florentine)))
print("Egonet florentine: " + str(evaluation.modularity_overlap(G_florentine, coms_egonet_florentine)))
print("Danmf florentine: " + str(evaluation.modularity_overlap(G_florentine, coms_danmf_florentine)))
print("Demon lesmis: " + str(evaluation.modularity_overlap(G_lesmis, coms_demon_lesmis)))
print("Egonet lesmis: " + str(evaluation.modularity_overlap(G_lesmis, coms_egonet_lesmis)))
print("Danmf lesmis: " + str(evaluation.modularity_overlap(G_lesmis, coms_danmf_lesmis)))
print("Demon synthetic: " + str(evaluation.modularity_overlap(G_synthetic, coms_demon_synthetic)))
print("Egonet synthetic: " + str(evaluation.modularity_overlap(G_synthetic, coms_egonet_synthetic)))
print("Danmf synthetic: " + str(evaluation.modularity_overlap(G_synthetic, coms_danmf_synthetic)))

#METRICS - Conductance
print("Conductance:")
print("Demon karate: " + str(evaluation.conductance(G_karate, coms_demon_karate)))
print("Egonet karate: " + str(evaluation.conductance(G_karate, coms_egonet_karate)))
print("Danmf karate: " + str(evaluation.conductance(G_karate, coms_danmf_karate)))
print("Demon florentine: " + str(evaluation.conductance(G_florentine, coms_demon_florentine)))
print("Egonet florentine: " + str(evaluation.conductance(G_florentine, coms_egonet_florentine)))
print("Danmf florentine: " + str(evaluation.conductance(G_florentine, coms_danmf_florentine)))
print("Demon lesmis: " + str(evaluation.conductance(G_lesmis, coms_demon_lesmis)))
print("Egonet lesmis: " + str(evaluation.conductance(G_lesmis, coms_egonet_lesmis)))
print("Danmf lesmis: " + str(evaluation.conductance(G_lesmis, coms_danmf_lesmis)))
print("Demon synthetic: " + str(evaluation.conductance(G_synthetic, coms_demon_synthetic)))
print("Egonet synthetic: " + str(evaluation.conductance(G_synthetic, coms_egonet_synthetic)))
print("Danmf synthetic: " + str(evaluation.conductance(G_synthetic, coms_danmf_synthetic)))


