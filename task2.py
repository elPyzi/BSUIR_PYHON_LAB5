import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

dataset = pd.read_csv('test.csv')
values = dataset.sample(n=1000)
missing = values.isnull().sum()
print("Пропущенные значения:\n", missing)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))


values['Id'].plot.box(ax=axes[0])
axes[0].set_title('Boxplot for Id')


values['Id'].fillna(values['Id'].mean(), inplace=True)


lower_bound = values['Id'].quantile(0.05)
upper_bound = values['Id'].quantile(0.95)
values['Id'] = np.where(values['Id'] < lower_bound, lower_bound, values['Id'])
values['Id'] = np.where(values['Id'] > upper_bound, upper_bound, values['Id'])

room_counts = values['Rooms'].value_counts()
room_counts.plot(kind='bar', ax=axes[1])
axes[1].set_title('Count of Rooms')

plt.show()
