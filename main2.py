import pandas as pd

data = pd.read_csv('C:/PyCh/new_matplotlib/divanpars/divanpars/spiders/light.csv')
print(data['Цена'].mean())
