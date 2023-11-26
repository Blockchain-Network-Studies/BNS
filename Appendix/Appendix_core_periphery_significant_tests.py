#!/usr/bin/env python
# coding: utf-8
# The code requires the Aave transaction data (after preprocessing)
# as the input, and will output the significant test results on the
# core-periphery structure for each day's transaction network
# either True or False

import pandas as pd
import cpnet
import networkx as nx

df = pd.read_csv('/Users/aoziqiao/Desktop/AAVE transaction data_after preprocessing.csv')
df_time_partition= df.groupby(['timestamp'])['to_address'].agg(['nunique']).reset_index()
df_time_partition = df_time_partition.drop(['nunique'], axis=1)


significant_test = []
date = 0
for i in range(0,len(df_time_partition)):
    df_1 = df.loc[df['timestamp']==df_time_partition['timestamp'][i]]
    
    #Build the daily transaction network
    G = nx.from_pandas_edgelist(df_1, 'from_address', 'to_address', 'value', nx.Graph())
    
    #Extract the core-periphery structure by BE algorithm
    alg = cpnet.BE()
    alg.detect(G)
    c = alg.get_pair_id()
    x = alg.get_coreness()

    #Significant test
    sig_c, sig_x, significant, p_values = cpnet.qstest(
        c, x, G, alg, significance_level=0.05, num_of_rand_net=100, num_of_thread=16)
    significant_test.append(significant)
    date+=1
    print(date)
    print(significant)


significant_test = pd.DataFrame(significant_test)
significant_test['date'] = significant_test['timestamp']

significant_test.to_csv('/Users/bonnieao/Desktop/Undergraduate/BlockChain Network Study/2023-08 Revised/Data/core_periphery_significant_test.csv')

