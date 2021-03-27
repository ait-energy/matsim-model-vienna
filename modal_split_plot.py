import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('modal_split.csv', index_col=0)

fig, axs = plt.subplots(figsize=(8, 4))
df.plot.bar(ax=axs, color=['#707f87', '#31b7bc', '#470f51'])
axs.set_ylabel('modal split [%]')
axs.set_title('Modal Split by Trip (within the City of Vienna)')
fig.savefig('modal_split.svg', dpi=100, bbox_inches='tight')
