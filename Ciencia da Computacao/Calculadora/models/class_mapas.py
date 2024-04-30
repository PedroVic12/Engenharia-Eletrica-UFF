import geopandas as gpd
import rtree
import pygeos
import mapclassify
import geobr


class Mapas:
    def __init__(self) -> None:
        self.sistema_referencia = "espg:4674"

    def mapas_interativos(self, geo_df, item):
        print("Mapas interativos")

        print(geo_df.columns)

        porto_alegre_df = geo_df[geo_df.name_muni == item]
        porto_alegre_df.crs = "espg:4674"

        display(geo_df.head())
        mapa = porto_alegre_df.explore(
            color="gray",
            tooltip="name_muni",
            name=item,  # tiles="CartoDB positron"
        )
        geo_df.explore(
            m=mapa,
            column="government_level",
            color="red",
            tooltip=False,
            name="Escolas",
            legend=True,
            popup=["name_school", "address", "government_level", "phone_number"],
            marker_icon="school",
            scheme="naturalbreaks",
            # style_kwds = dict(            color: "black",        weight: 1,      opacity: 0.5,    ),
            cmap="Spectral",
            marker_type="circle_marker",
            marker_kwds=dict(
                fill_color="red",
                radius=5,
            ),
            height=500,
            width=500,
        )

        display(mapa)

    def juntar_mapas(self, df_base, porto_alegre_df):
        # juntar Rs e as escolas
        geo_df = gpd.sjoin(df_base, porto_alegre_df)
        print(geo_df.columns)
        display(geo_df.head())

    def exportar_html(self, mapa):
        mapa.save(outfile="./escolas.html")
        display(mapa)
