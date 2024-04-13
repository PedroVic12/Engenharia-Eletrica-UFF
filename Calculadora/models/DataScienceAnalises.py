import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sweetviz as sv


class DataScienceAnalises:
    def __init__(self):
        pass

    def analise_inicial(self, df_dsa):
        print(f"Tamanho: {df_dsa.shape}")
        print(f"Colunas: {df_dsa.columns}")
        df_dsa.head()
        try:
            print(f"Info: {df_dsa.info()}")
            print(f"Valores ausentes?: {df_dsa.isnull().sum()}")
            print(f"Correlação entre colunas: {df_dsa.corr()}")
            print(f"Analise descritiva simples : {df_dsa.describe()}")
        except Exception as e:
            print("Erro na análise inicial", e)

    def dashboard_inicial(self, df):
        my_report = sv.analyze(df)
        my_report.show_html()

    def _compararTabelas(self, df1, df2, nomes):
        print(df1.shape)
        print(df2.shape)
        report = sv.compare([df1, nomes[0], df2, nomes[1]])
        report.show_html()

    def analise_exploratoria(self, df):
        pass

    #!Storytelling com dados cap 2 - 35
    def plot_barras(self, df, coluna, type="vertical"):

        if type == "vertical":
            plt.bar(x=df[coluna].value_counts().index, height=df[coluna].value_counts())
            sns.countplot(data=df, x=coluna)
            plt.show()
        elif type == "horizontal":
            print("Gratico horizontal")

        elif type == "vertical-empilhado":
            print("Gratico vertical empilhado")

        elif type == "horizontal-empilhado":
            print("Gratico horizontal empilhado")

    def cascata(self, df):
        pass

    def area(self, df):
        pass

    def texto_simples(self, txt):
        print("===========================================")
        print(txt)
        print("===========================================")

    def tabela(self, array, colunas):
        df = pd.DataFrame(array)
        return df

    def grafico_dispersao(
        self,
        df,
        coluna_alvo,
        col,
    ):
        plt.scatter(df[coluna_alvo], df[col])

    def histograma(self, df, coluna_alvo):
        sns.histplot(data=df, x=coluna_alvo, kde=True)

    def grafico_linhas(self, df, col):

        plt.plot(col)

    def mapa_inclinacao(self, df):
        pass

    def plots(self, df, coluna_alvo, col, tipo=None):

        # barras
        self.plot_barras(df, col)
        # mean, sum, count  como tipo da plotagem
        plt.bar(
            x=df.groupby(coluna_alvo)[col].mean().index,
            height=df.groupby(coluna_alvo)[col].mean(),
        )

        self.grafico_linhas(df, coluna_alvo)

        # var categorias
        sns.catplot(x=coluna_alvo, kind="count", data=df)

        # dispersao com reg linear
        # sns.reqplot()

        self.grafico_dispersao(
            df,
            coluna_alvo,
            col,
        )

        # box_plot

        # histograma
        self.histograma(df, coluna_alvo)
