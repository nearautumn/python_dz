'''| Задание 44 |
| --- |
| В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?'''

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})

data.loc[data['whoAmI'] == 'robot', 'robot'] = True
data.loc[data['whoAmI'] != 'robot', 'robot'] = False

data.loc[data['whoAmI'] == 'human', 'human'] = True
data.loc[data['whoAmI'] != 'human', 'human'] = False

data = data.iloc[:, 1:]

print(data.head())