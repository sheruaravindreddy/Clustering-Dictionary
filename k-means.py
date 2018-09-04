from loading_data import structure_data

from sklearn.cluster import KMeans

df = structure_data.df


def fit_kmeans(df, n):
    kmeans = KMeans(n_clusters = n, random_state = 0)
    kmeans.fit(df)
    return kmeans.inertia_/len(df)


# =============================================================================
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use('fivethirtyeight')
# MSD_list = {}
# for n in range(2,20):
#     MSD_list[n] = fit_kmeans(df,n)
#     print n
# print MSD_list
# 
# plt.plot(list(MSD_list.keys()), list(MSD_list.values()))
# plt.show()
# =============================================================================

fit_kmeans(df, 16)