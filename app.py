import streamlit as st
import numpy as np
import folium
import geopandas as gpd
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_folium import st_folium
from utils import popupTable
import branca

dataframe = gpd.read_file("./static/pescanovaGeoJsonWithProperties.geojson")

# Specify the title and logo for the web page.
st.set_page_config(page_title='Pond Health Analysis for Neuva Pescanova', page_icon='./static/galaxeye.png', layout="wide")

# Add a sidebar to the web page. 
with st.sidebar:
    choose = option_menu("Pond Health Analysis for Neuva Pescanova", ["Dashboard","Chlorophyll","Dissolved Oxygen","pH","Salinity","Turbidity","Custom Filter"],
                         icons=['graph-up', 'brightness-high', 'cloud-haze2', 'speedometer2', 'snow', 'moisture', 'funnel'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#26272F"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#0F1116"},
        "nav-link-selected": {"background-color": "#000000"},
    }
    )

logo = Image.open("./static/galaxeye.png")
if choose == "Dashboard":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #ffffff;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Detailed Analysis</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=130 )
    
    map = folium.Map(location=[-2.4474679490380993, -79.98500168575568], zoom_start=16, scrollWheelZoom=True)
    # img = folium.raster_layers.ImageOverlay(
    #     name="RGB Image",
    #     image="./static/rgbimage.png",
    #     bounds=[[-2.460891311086019, -79.99976724386217], [-2.4354694248845985, -79.96761258691551]],
    #     opacity=1.0,
    #     interactive=True,
    #     cross_origin=False,
    #     zindex=1,
    # )

    # img.add_to(map)
    # for l, row in enumerate(dataframe.iterrows()):
    #         html = popupTable(dataframe, l)
    #         iframe = branca.element.IFrame(html=html,width=700,height=600)
    #         popup = folium.Popup(folium.Html(html, script=True), max_width=500)
    #         folium.GeoJson(data=row[1][5], popup=popup).add_to(map)
    st_map = st_folium(map, width=1000, height=650)