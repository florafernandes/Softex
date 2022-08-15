import pandas as pd
import csv

notas = pd.read_csv('./notas_alunos.csv')
notas.head()
print(notas)
print()

notas['Media'] = (notas["nota_1:"] + notas["nota_2:"]) / 2
notas.loc[notas['faltas'] > 5, 'situacao'] =   'REPROVADO'
notas.loc[notas['Media'] >= 7, 'situacao'] = 'APROVADO'
notas.loc[notas['Media'] < 7, 'situacao'] = 'REPROVADO'
media_geral = notas['Media'].median()
maior_media = notas['Media'].max()
maior_falta = notas['faltas'].max()
print(f'A maior quantidade de faltas é {maior_falta}')
print(f'A media geral é {media_geral}')
print(f'A maior media foi {maior_media}')
print()
print(notas)

notas.to_csv('alunos_situacao.csv', index=False)
