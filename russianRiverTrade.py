import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from estatistica import estatistica

df   = pd.read_csv('/Users/fabioguimaraes/Downloads/russiantrade/russiantrade_edges.txt', delimiter='\t', header=None)
rec  = list(df.to_records(index=False))
G    = nx.Graph(rec)
estatistica(G)

nx.draw(G, with_labels=True)
plt.show()
