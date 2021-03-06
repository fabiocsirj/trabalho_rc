import networkx as nx
import pandas as pd
import itertools

def estatistica(G):
    # V = sorted(list(G.nodes))
    V = list(G.nodes)

    df_V = pd.DataFrame([0]*len(V), index=V, columns=['g'])
    vg   = dict((v,g) for v,g in G.degree())
    df_V['g'] = pd.Series(vg)
    # df_V['e'] = pd.Series(nx.eccentricity(G))
    df_V['c'] = pd.Series(nx.clustering(G))
    # df_V['b'] = pd.Series(nx.betweenness_centrality(G))
    # print(df_V)
    print()
    print("Componentes Conexas (CC)      :",nx.number_connected_components(G))
    print("Numero de Vértices nas CC     :",[len(i) for i in nx.connected_components(G)])
    print("Número de Arestas  nas CC     :",[int(sum([g for u,g in G.degree(i)])/2) for i in nx.connected_components(G)])
    print("Densidade do Grafo            : {:.2f}".format(nx.density(G)))
    # print("Vértice com maior betweenness :", df_V['b'].idxmax())
    print()
    for _ in range(97): print("-", end='')
    print("\n|Mética\t\t| Máximo\t| Mínimo\t| Média\t\t| Mediana\t| Desvio Padão\t|")
    for _ in range(97): print("-", end='')
    print("\n|Grau\t\t| {}\t\t| {}\t\t| {:.2f} *\t| {}\t\t| {:.2f}\t\t|".format(df_V['g'].max(), df_V['g'].min(), df_V['g'].mean(), df_V['g'].median(), df_V['g'].std(ddof=0)))
    for _ in range(97): print("-", end='')
    # print("\n|Excentricidade\t| {} **\t\t| {}\t\t| {:.2f}\t\t| {}\t\t| {:.2f}\t\t|".format(df_V['e'].max(), df_V['e'].min(), df_V['e'].mean(), df_V['e'].median(), df_V['e'].std(ddof=0)))
    # for _ in range(97): print("-", end='')
    print("\n|Clusterização\t| {:.2f}\t\t| {}\t\t| {:.2f} ***\t| {}\t\t| {:.2f}\t\t|".format(df_V['c'].max(), df_V['c'].min(), df_V['c'].mean(), df_V['c'].median(), df_V['c'].std(ddof=0)))

    # VV    = list(itertools.combinations(V, 2))
    # df_VV = pd.DataFrame(VV, columns=['u', 'v'])
    # df_VV['d'] = df_VV.apply(lambda x: (len(nx.shortest_path(G, x['u'], x['v']))-1), axis=1)
    # print(df_VV)
    # for _ in range(97): print("-", end='')
    # print("\n|Distância\t| {}\t\t| {}\t\t| {:.2f}\t\t| {}\t\t| {:.2f}\t\t|".format(df_VV['d'].max(), df_VV['d'].min(), df_VV['d'].mean(), df_VV['d'].median(), df_VV['d'].std(ddof=0)))
    for _ in range(97): print("-", end='')
    print()
    print("*   = Grau Médio    do Grafo")
    # print("**  = Diâmetro      do Grafo")
    print("*** = Clusterização do Grafo")
    print()
