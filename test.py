import networkx as nx
import matplotlib.pyplot as plt
from cdlib import datasets

G = datasets.fetch_network_data(net_name="amazon", net_type="networkx")

print(nx.get_node_attributes(G, 'community'))   

nx.readwrite.gml.write_gml(G, "amazon_graph.gml")