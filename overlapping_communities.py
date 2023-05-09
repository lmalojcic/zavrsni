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

#bigclam
# bigclam_start = timeit.default_timer()
# coms_bigclam_karate = algorithms.big_clam(G_karate)
# coms_bigclam_florentine = algorithms.big_clam(G_florentine)
# coms_bigclam_lesmis = algorithms.big_clam(G_lesmis)
# coms_bigclam_synthetic = algorithms.big_clam(G_synthetic)
# bigclam_time = timeit.default_timer() - bigclam_start

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
# print("BigClam: " + str(bigclam_time))
print("Egonet: " + str(egonet_time))
print("Danmf: " + str(danmf_time))

#METRICS - MODULARITY
print("Modularity:")
# print("BigClam karate: " + str(evaluation.modularity_overlap(G_karate, coms_bigclam_karate)))
print("Egonet karate: " + str(evaluation.modularity_overlap(G_karate, coms_egonet_karate)))
print("Danmf karate: " + str(evaluation.modularity_overlap(G_karate, coms_danmf_karate)))
# print("BigClam florentine: " + str(evaluation.modularity_overlap(G_florentine, coms_bigclam_florentine)))
print("Egonet florentine: " + str(evaluation.modularity_overlap(G_florentine, coms_egonet_florentine)))
print("Danmf florentine: " + str(evaluation.modularity_overlap(G_florentine, coms_danmf_florentine)))
# print("BigClam lesmis: " + str(evaluation.modularity_overlap(G_lesmis, coms_bigclam_lesmis)))
print("Egonet lesmis: " + str(evaluation.modularity_overlap(G_lesmis, coms_egonet_lesmis)))
print("Danmf lesmis: " + str(evaluation.modularity_overlap(G_lesmis, coms_danmf_lesmis)))
# print("BigClam synthetic: " + str(evaluation.modularity_overlap(G_synthetic, coms_bigclam_synthetic)))
print("Egonet synthetic: " + str(evaluation.modularity_overlap(G_synthetic, coms_egonet_synthetic)))
print("Danmf synthetic: " + str(evaluation.modularity_overlap(G_synthetic, coms_danmf_synthetic)))

#METRICS - Conductance
print("Conductance:")
# print("BigClam karate: " + str(evaluation.conductance(G_karate, coms_bigclam_karate)))
print("Egonet karate: " + str(evaluation.conductance(G_karate, coms_egonet_karate)))
print("Danmf karate: " + str(evaluation.conductance(G_karate, coms_danmf_karate)))
# print("BigClam florentine: " + str(evaluation.conductance(G_florentine, coms_bigclam_florentine)))
print("Egonet florentine: " + str(evaluation.conductance(G_florentine, coms_egonet_florentine)))
print("Danmf florentine: " + str(evaluation.conductance(G_florentine, coms_danmf_florentine)))
# print("BigClam lesmis: " + str(evaluation.conductance(G_lesmis, coms_bigclam_lesmis)))
print("Egonet lesmis: " + str(evaluation.conductance(G_lesmis, coms_egonet_lesmis)))
print("Danmf lesmis: " + str(evaluation.conductance(G_lesmis, coms_danmf_lesmis)))
# print("BigClam synthetic: " + str(evaluation.conductance(G_synthetic, coms_bigclam_synthetic)))
print("Egonet synthetic: " + str(evaluation.conductance(G_synthetic, coms_egonet_synthetic)))
print("Danmf synthetic: " + str(evaluation.conductance(G_synthetic, coms_danmf_synthetic)))

#METRICS - NMI
print("NMI:")
print("Karate: " + str(evaluation.overlapping_normalized_mutual_information_LFK(coms_egonet_karate, coms_danmf_karate)))
print("Florentine: " + str(evaluation.overlapping_normalized_mutual_information_LFK(coms_egonet_florentine, coms_danmf_florentine)))
print("Lesmis: " + str(evaluation.overlapping_normalized_mutual_information_LFK(coms_egonet_lesmis, coms_danmf_lesmis)))
print("Synthetic: " + str(evaluation.overlapping_normalized_mutual_information_LFK(coms_egonet_synthetic, coms_danmf_synthetic)))
