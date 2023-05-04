import streamlit as st
import kmaps.folmaps as kmaps
import leafmap.foliumap as leafmap

st.set_page_config(layout = "wide")

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

# leafmap foliumap module에서 to_streamlit 기능 가져오기
# folmaps에 다른 기능들 (add_basemap, dropdown, ...) 추가
# finish it by today - and submit it
## 549도 오늘 digitizing 끝내기
