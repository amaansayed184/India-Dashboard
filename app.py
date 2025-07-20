import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

final_df=pd.read_csv('india.csv')

list_of_states=list(final_df['State'].unique())
list_of_states.insert(0,'Overall India')


st.sidebar.title('India Census Data')
selected_state=st.sidebar.selectbox('Select a State',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(final_df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(final_df.columns[5:]))

plot= st.sidebar.button('Plot Graph')

if plot:
    if selected_state=='Overall India':
        #plot for india
        fig = px.scatter_mapbox(final_df, lat='Latitude', lon='Longitude',size=primary,color=secondary, zoom=4,width=1200,height=700,mapbox_style='carto-positron',hover_name='District')

        st.plotly_chart(fig,theme=None,use_container_width=True)

    else:
        #plot for states
        state_df = final_df[final_df['State']==selected_state]
        fig = px.scatter_mapbox(state_df,lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=6,width=1200,height=700,
                                mapbox_style='carto-positron', hover_name='District')
        st.plotly_chart(fig, theme=None, use_container_width=True)

