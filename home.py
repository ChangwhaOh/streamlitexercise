import streamlit as st
import kmaps


st.set_page_config(layout = "wide")

# Customize page title
st.title('Introduction')

st.write('Changwha Oh, Ph.D. student at the University of Tennessee, Knoxville')

#st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.
"""

st.markdown(markdown)

m = kmaps.Map(center = [37, 127], zoom = 7)
m.add_base_dropdown()
m.add_states_dropdown()
m
#m.to_streamlit(height = 500)