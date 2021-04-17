import streamlit as st 
import pandas as pd 
import plotly.express as px


st.title('suivi du covid 19 au maroc')

st.cache(persist=True) 

df = pd.read_csv(r'/Users/nafalismac/desktop/temp.py', encoding='ISO-8859-1',thousands='.', decimal=',', engine='python')
df.head()  
df = df.set_index('date')



st.sidebar.title("choisir entre le suivi des cas de covid19 ou le suivi de la vaccination")
votre_choix = st.sidebar.radio(label="", options=["suivi epideomologique", "vaccination"])

if votre_choix == "suivi epideomologique":
    st.image("https://aujourdhui.ma/wp-content/uploads/2020/07/coronavirus-30.jpg")
    
    st.markdown('__voici un tableau regroupant les donnés sur la situation épidémiologique au maroc__')
    df = df.drop(df.columns[[13,14,15]], axis=1)
    st.write(df)
    with st.beta_expander("Source"):
        st.markdown('données quotidiennes tirées [du Portail Officiel du Coronavirus au Maroc](http://www.covidmaroc.ma/pages/Accueilfr.aspx)')
    #
    
    col1, col2, col3 = st.beta_columns(3)

    with col1:
         st.header("total cases")
         st.warning(df['total_cases'][df.index[-1]])
 
    with col2:
        st.header("total cases")
        st.success(df['total_cases'][df.index[-1]])
    with col3:
         st.header("total deaths")
        
         st.info( df['total_deaths'][df.index[-1]])
      

    all_columns_names= df.columns.tolist()
    selected_column_names = st.multiselect("select column to plot",all_columns_names, default = ["total_cases", "total_deaths"])



    fig = px.line(df,
                y=selected_column_names,
                title=f'graph of {selected_column_names}')

    st.plotly_chart(fig)
    
    
    fig2 = px.area(df, x=df.index, y=selected_column_names)
    
    st.plotly_chart(fig2)
else:
    st.image("https://www.sante.gov.ma/PublishingImages/2021/vaccin%202021/vaccinfr-d.jpg?csf=1&e=ygzHDz")
    st.markdown('__voici un tableau regroupant les donnés sur la campagne de vaccination au maroc__')
    df = df.drop(df.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12]], axis=1)
    st.write(df)
    
    y_options = [
    "new_vaccinations","people_fully_vaccinated","people_vaccinated"
    ]

    y_axis = st.selectbox('quel graphe voulez vous?', y_options)


    fig = px.line(df,
                y=y_axis,
                title=f'graph of {y_axis}')

    st.plotly_chart(fig)