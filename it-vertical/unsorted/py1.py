import pandas as pd

base = pd.read_csv('files\customers.csv', delimiter=';')
count = 0

print('Ответ 1')
print(base[(base['Age'] > 19) & (base['Income'] < 30000)])
print('Ответ 2')
print(base[(base['Profession'] > 'Lawyer') & (base['Work Experience'] > 5)])