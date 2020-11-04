import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from estatistica import estatistica

df = pd.read_csv('/Users/fabioguimaraes/Downloads/mexicanDrug/CosciaRios2012_DataBase.csv')
G  = nx.Graph()

mask = ((df['BL'] != 0) | (df['BLF'] != 0) | (df['F'] != 0) | (df['G'] != 0) | (df['J'] != 0) | (df['S'] != 0) | (df['SF'] != 0) | (df['T'] != 0) | (df['Z'] != 0) | (df['O'] != 0))
plot = {2002: 131, 2006: 132, 2010: 133}

for ano in plot:
    df_ano = df[(df['Year'] == ano) & mask].copy()
    df_ano.drop(['Year', 'Code'], axis=1, inplace=True)
    df_ano.drop_duplicates(inplace=True)

    arestas = []
    states  = []
    carteis = []
    for i in range(len(df_ano)):    
        for k,v in df_ano.iloc[i].items(): 
            if k != 'State' and v != 0: 
                arestas.append(tuple([df_ano['State'].iloc[i], k]))
                states.append(df_ano['State'].iloc[i])
                carteis.append(k)
    states  = list(set(states))
    carteis = list(set(carteis))
    # print(arestas)

    G.add_nodes_from(states)
    G.add_nodes_from(carteis)
    G.add_edges_from(arestas)

    axs = plt.subplot(plot[ano])
    axs.set_title(str(ano))

    pos1 = nx.circular_layout(states)
    pos2 = nx.circular_layout(carteis, scale=0.5)
    posAll = {}
    posAll.update(pos1)
    posAll.update(pos2)

    nx.draw_networkx_nodes(G, pos1, nodelist=states, node_shape='s', node_color="b")
    nx.draw_networkx_labels(states, pos1, {k:k for k in pos1})
    nx.draw_networkx_nodes(G, pos2, nodelist=carteis, node_shape='o', node_color="r")
    nx.draw_networkx_labels(carteis, pos2, {k:k for k in pos2}, font_size=8)
    nx.draw_networkx_edges(G, posAll)

    estatistica(G)

    G.clear_edges()
    G.remove_nodes_from(states)
    G.remove_nodes_from(carteis)

plt.subplots_adjust(left=0.02, right=0.98, wspace=0.05)
plt.show()
