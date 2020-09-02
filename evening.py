import graphistry
import pandas as pd

graphistry.register(api=3, protocol="https", server="hub.graphistry.com", username="Aashiq.R", password="Amma@2805")
hg = graphistry.hypergraph(pd.read_csv('aurora.csv'), ['Time', 'Source', 'Destination','Protocol','Length','Info'], direct=True)
hg['graph'].plot()
