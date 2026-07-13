#%%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

# %%
'''abrindo o dataframe'''
df = pd.read_excel('vendas_bar.xlsx')
df.head(5)
# %%
'''verificando tipos de dados das colunas'''
df.dtypes
#%%
'''excluindo colunas desnecessarias'''
df= df.drop(['Unnamed: 3','Unnamed: 7'], axis=1)
# %%
''' ajustando tipo de dados da coluna data'''
df['data da operacao'] = pd.to_datetime(
    df['data da operacao'],
    dayfirst=True,
    format= 'mixed')

df['data da liberacao'] = pd.to_datetime(
    df['data da liberacao'],
    dayfirst=True,
    format= 'mixed')
# %%
'''tranformando em numeros decimais'''
#%%
df['valor bruto'] = (
    df['valor bruto']
    .astype(str)
    .str.replace(',', '.', regex=False)
    .astype(float)
)
#%%
df['descontos dobre as vendas'] = (
    df['descontos dobre as vendas']
    .astype(str)
    .str.replace(',', '.', regex=False)
    .astype(float)
)
#%%
df['valor liquido'] = (
    df['valor liquido']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)
# %%
'''remvendo valores nulos'''
df.isnull().sum()
df = df.dropna()
# %%
'''renomeando colunas'''
df = df.rename(columns={'descontos dobre as vendas': 'descontos sobre as vendas'})
#%%
'''Analise exploratória de dados'''
'''verificando tipos de dados do dataframe'''
df.info()
'''exploração das estatisticas descritivas do dataframe'''
df.describe()
'''contagem do dataframe'''
len(df)
'''linhas e colunas do dataframe'''
df.shape
#%%
'''tirando uma amotragem aleatória dos dados para verificação'''
df.sample(5)

#%%
'''Qual foi o faturamento bruto do período?'''
df['valor bruto'].sum()
#%%
'''valor maximo de venda'''
df['valor bruto'].max()
#%%
'''valor minimo de venda'''
df['valor bruto'].min()
#%%
'''Qual foi o faturamento líquido?'''
df['valor liquido'].sum().round(2)

#%%
'''Quanto foi pago em taxas?'''
df['descontos sobre as vendas'].sum().round(2)
#%%
'''Qual o ticket médio?'''
df['valor bruto'].mean().round(2)
#%%
'''Quantas vendas ocorreram por dia?'''
df.groupby(df['data da operacao'].dt.date)['valor bruto'].sum()
#%%
'''Existe sazonalidade?'''
vendas_dia = df.groupby(df['data da operacao'].dt.date)['valor bruto'].sum()
#%%
vendas_dia.plot(kind='line',
                figsize=(10,5),
                marker='o'
                )
plt.title('vendas de maio')
plt.xlabel('Data')
plt.ylabel('Valor Bruto')
plt.show()
#%%
'''Quais formas de pagamento predominam?'''
df['meio de pagamento'].value_counts()
#%%
'''Em quais horários ocorrem mais vendas?'''
vendas_hora = df.groupby(df['data da operacao'].dt.hour)['valor bruto'].sum()
# %%
vendas_hora.plot(kind='bar',
                 figsize=(13,6)
                 )
plt.title('vendas por hora')
plt.xlabel('Hora')
plt.ylabel('Valor bruto')
plt.xticks(rotation=35)
plt.show()
# %%
'''baixar dados tratato para o power bi '''
#%%
df.to_csv('df_tratado_bar.csv', index=False, sep=';')