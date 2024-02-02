import matplotlib.pyplot as plt
import networkx as nx

def create_letter_mapping_graph(key_mappings):
    G = nx.DiGraph()

    for mapping in key_mappings:
        G.add_edge(mapping[0], mapping[1])

    plt.figure(figsize=(14, 14))
    pos = nx.spring_layout(G, k=0.15, iterations=20)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, edge_color='gray', linewidths=1, font_size=10, arrowsize=15)
    plt.title("Bokstavkoblinger", fontsize=20)
    plt.show()

key_mappings = [('ø', 'd'), ('q', 'e'), ('w', 't'), ('x', 'v'), ('l', 'a'), ('i', 'r'), ('t', 'e'), ('x', 'n'), 
                ('f', 'g'), ('g', 'a'), ('z', 'n'), ('l', 'g'), ('u', 'e'), ('v', 'n'), ('æ', 'f'), ('y', 'r'), 
                ('a', 's'), ('a', 'k'), ('x', 'm'), ('l', 's'), ('q', 'o'), ('d', 'h'), ('q', 'i'), ('p', 'i'), 
                ('y', 'e'), ('u', 'o'), ('g', 'l'), ('h', 'l'), ('å', 'e'), ('g', 'h'), ('h', 's'), ('k', 'a'), 
                ('æ', 'd'), ('w', 'r'), ('s', 'd'), ('o', 't'), ('k', 'f'), ('s', 'l'), ('ø', 's'), ('f', 'k'), 
                ('o', 'u'), ('i', 't'), ('c', 'm'), ('å', 'i'), ('å', 'o'), ('n', 'v'), ('k', 'l'), ('o', 'å'), 
                ('q', 'r'), ('t', 'i'), ('æ', 'a'), ('j', 'd'), ('a', 'g'), ('u', 't'), ('g', 'k'), ('u', 'r'), 
                ('e', 't'), ('e', 'p'), ('m', 'b'), ('å', 'u'), ('k', 'æ'), ('i', 'y'), ('b', 'm'), ('c', 'b'), 
                ('a', 'f'), ('m', 'v'), ('s', 'g'), ('h', 'j'), ('z', 'b'), ('æ', 'j'), ('p', 'u'), ('i', 'p'), 
                ('u', 'p'), ('w', 'o'), ('d', 'ø'), ('d', 'f'), ('q', 'p'), ('w', 'p'), ('t', 'u'), ('y', 'o'), 
                ('b', 'c'), ('n', 'c'), ('r', 'u'), ('e', 'q'), ('z', 'c'), ('y', 'i'), ('t', 'q'), ('v', 'x')]

create_letter_mapping_graph(key_mappings)
