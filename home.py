import streamlit as st
import kmaps.folmaps as kmaps
#import leafmap.foliumap as leafmap
#import leafmap

st.set_page_config(layout = "wide")

# Customize page title
st.title('Introduction')

st.write('Changwha Oh, Ph.D. student at the University of Tennessee, Knoxville')

#st.header("Instructions")
st.sidebar.info('Contact')
st.sidebar.markdown('[Twitter](https://twitter.com)')

col1, col2 = st.columns([4, 1])

#options = list(leafmap.basemaps.keys())

with col2:
    dropdown = st.selectbox('Basemap', ['roadmap', 'satellite']) # options
    #default_url = leafmap.basemaps[dropdown].tiles
    url = st.text_input('Enter URL')


m = kmaps.Map()
m.add_basemap(dropdown)

if url:
    m.add_tile_layer(url, name = 'User URL', attr = 'Tile')


with col1:
    m.to_streamlit()