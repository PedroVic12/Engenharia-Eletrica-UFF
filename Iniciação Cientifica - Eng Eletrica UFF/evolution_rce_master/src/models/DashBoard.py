import pandas as pd
import plotly.express as px
import streamlit as st
import json
from abc import ABC, abstractmethod


class FileReader(ABC):
    @abstractmethod
    def read(self, file_path: str):
        pass


class ExcelFileReader(FileReader):
    def read(self, file_path: str):
        return pd.read_excel(file_path)


class JsonFileReader(FileReader):
    def read(self, file_path: str):
        with open(file_path, "r") as file:
            data = json.load(file)
        return pd.DataFrame(data)


class DataHandler:
    def __init__(self, file_reader: FileReader):
        self.file_reader = file_reader

    def load_data(self, file_path: str):
        return self.file_reader.read(file_path)


class dashPY:
    def __init__(self, df):
        self.df = df

    def gerar_graficos_interativos(self, colunas):
        """
        Gera gráficos interativos para colunas selecionadas do DataFrame.

        Args:
            colunas: Lista de colunas a serem usadas para os gráficos.
        """
        if len(colunas) < 3:
            st.write("Por favor, selecione ao menos três colunas.")
            return

        st.plotly_chart(px.histogram(self.df, x=colunas[0]))
        st.plotly_chart(px.line(self.df, x=colunas[1], y=colunas[2]))
        st.plotly_chart(px.bar(self.df, x=colunas[1], y=colunas[2]))

    def exibir_dataset(self):
        st.dataframe(self.df)

    def plot_interativo(self, df):

        st.title("Visualização de dados Alg Evolutivo")

        mes_selecionado = st.sidebar.multiselect(
            "Escolha a coluna", df.columns, placeholder="Selecione"
        )

        if mes_selecionado:
            fig = px.line(df, x="dias", y=mes_selecionado)
            st.plotly_chart(fig)

            st.write(df[mes_selecionado])

            col1, col2, col3 = st.columns(3)

            col1.bar_chart(df[mes_selecionado])
            col2.line_chart(df[mes_selecionado])
            col2.area_chart(df[mes_selecionado])

            col3.line_chart(df[mes_selecionado])


def load_params(file_path):
    with open(file_path, "r") as file:
        params = json.load(file)
    return params


def main():
    st.title("Visualização de Dados Interativos")

    def select_file():

        file_type = st.radio("Selecione o tipo de arquivo", ("Excel", "JSON"))
        file_path = st.text_input("Insira o caminho do arquivo:")

        if not file_path:
            st.write("Por favor, insira o caminho do arquivo.")
            return

        if file_type == "Excel":
            file_reader = ExcelFileReader()
        elif file_type == "JSON":
            file_reader = JsonFileReader()

        data_handler = DataHandler(file_reader)
        df = data_handler.load_data(file_path)

    # columns = st.multiselect("Selecione as colunas para os gráficos", df.columns)
    excel = "/home/pedrov/Documentos/GitHub/Engenharia-Eletrica-UFF/Iniciação Cientifica - Eng Eletrica UFF/evolution_rce_master/src/db/consumo_eletrico_agua.xlsx"
    dash = dashPY(excel)
    params = load_params(
        r"/home/pedrov/Documentos/GitHub/Engenharia-Eletrica-UFF/Iniciação Cientifica - Eng Eletrica UFF/evolution_rce_master/src/db/parameters.json"
    )
    print(params)
    st.title("Visualização de Dados Interativos")
    df = pd.read_excel(
        "/home/pedrov/Documentos/GitHub/Engenharia-Eletrica-UFF/Iniciação Cientifica - Eng Eletrica UFF/evolution_rce_master/src/db/consumo_eletrico_agua.xlsx",
    )
    colunas = df.columns
    print(colunas)

    df.dropna()
    print(df)

    consumo = df["consumo"]
    dias = df["dias"]
    estacao = df["estacao do ano"]

    # checa coluna temporal
    y = dias.dt.strftime("%d-%m-%y")

    #!CASO DE USO
    dash = dashPY(df)
    dash.exibir_dataset()
    dash.plot_interativo(df)

    # if st.button("Exibir Gráficos"):
    # dash.plot_interativo(df)


if __name__ == "__main__":
    main()
