
import pandas as pd
import plotly.express as px

tabelas = pd.read_csv("cancelamentos.csv aula2.csv") 

tabelas = tabelas.drop(columns="CustomerID")    #tabela sem interesse

tabelas = tabelas.dropna()  #Tabelas com valores vazios

print(tabelas.info())

# Analisar cancelamentos dos clientes
print(tabelas["cancelou"].value_counts())
print(tabelas["cancelou"].value_counts(normalize=True).map("{:.1%}".format)) #Calcula o percentual


coluna = "duracao_contrato"

for coluna in tabelas.columns:
    grafico = px.histogram(tabelas, x = coluna, color="cancelou",text_auto=True)
    grafico.show() #Exibir grafico














 


