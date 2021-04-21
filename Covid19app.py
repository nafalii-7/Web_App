import streamlit as st 
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

st.title('suivi du covid 19 au maroc')

st.cache(persist=True) 

df = pd.read_csv(r'C:\Users\Lenovo\Downloads\streamlit\covid19_data.csv', encoding='ISO-8859-1',thousands='.', decimal=',', engine='python')
df.head()  
df = df.set_index('date')



st.sidebar.title("choisir entre les données du jour, le suivi des cas de covid19 ou le suivi de la compaghne de vaccination")
votre_choix = st.sidebar.radio(label="", options=["données du jour", "suivi epideomologique", "vaccination"])

    
    
if  votre_choix == "suivi epideomologique":
      st.image("https://aujourdhui.ma/wp-content/uploads/2020/07/coronavirus-30.jpg")
    
      st.markdown('__voici un tableau regroupant les donnés sur la situation épidémiologique au maroc__')
      df = df.drop(df.columns[[8,9,10]], axis=1)
      st.write(df)
      with st.beta_expander("Source"):
        st.markdown('données quotidiennes tirées [du Portail Officiel du Coronavirus au Maroc](http://www.covidmaroc.ma/pages/Accueilfr.aspx)')
    #
    
    ################
      st.write("\n")
    
      colors = px.colors.qualitative.D3
      fig6 = go.Figure()
      fig6.add_trace(go.Bar(y=df[["new_deaths", "new_cases", "new_tests"]].columns.tolist(),
                             x=df[["new_deaths", "new_cases", "new_tests"]].sum().values,
                             text=df[["new_deaths", "new_cases", "new_tests"]].sum().values,
                             orientation='h',
                             marker=dict(color=[colors[1], colors[3], colors[2]]),
                             ),
                      )
        
      fig6.update_traces(opacity=0.7,
                          textposition=["inside", "outside", "inside"],
                          texttemplate='%{text:.3s}',
                          hovertemplate='Status: %{y} <br>Count: %{x:,.2f}',
                          marker_line_color='rgb(255, 255, 255)',
                          marker_line_width=2.5
                          )
      fig6.update_layout(
            title="Total count",
            width=800,
            legend_title_text="Status",
            xaxis=dict(title="Count"),
            yaxis=dict(showgrid=False, showticklabels=True),
        )

    
      st.plotly_chart(fig6)
    
      st.write("\n")
      st.write("\n")
    
      col1, col2, col3 = st.beta_columns(3)

      with col1:
           st.header("tests effectués")
           st.warning(df['total_tests'][df.index[-1]])
 
      with col2:
           st.header("cas confirmés ")
           st.success(df['total_cases'][df.index[-1]])
      with col3:
           st.header("décès")
        
           st.info( df['total_deaths'][df.index[-1]])
    
      st.write("\n")
      st.write("\n") 
      st.title("visualisation des données quotidiennes" )
    
      all_columns_names= df.columns.tolist()
      selected_column_names = st.multiselect("choisir la(les) colonne(s) à dessiner",all_columns_names, default = ["total_cases", "total_deaths"])



      fig = px.line(df,
                  y=selected_column_names,
                  title=f'graph of {selected_column_names}')

      st.plotly_chart(fig)
    
    
      fig2 = px.area(df, x=df.index, y=selected_column_names)
    
      st.plotly_chart(fig2)
 
elif  votre_choix == "données du jour": 
    st.title("données du jour")
    
    st.image("https://boursenews.ma/uploads/actualites/5f4f7ebeee78f.jpg")
    
    st.write("\n")
    
    col1, col2, col3 = st.beta_columns(3)

    with col1:
           st.header("nouveaux tests")
           st.warning(df['new_tests'][df.index[-1]])
 
    with col2:
           st.header("nouveaux cas ")
           st.success(df['new_cases'][df.index[-1]])
    with col3:
           st.header("nouveaux deces")
        
           st.info( df['new_deaths'][df.index[-1]]) 
      
else:
    st.image("https://www.sante.gov.ma/PublishingImages/2021/vaccin%202021/vaccinfr-d.jpg?csf=1&e=ygzHDz")
    st.write("\n")
    st.info("Depuis son lancement fin janvier, la campagne de vaccination avance à un rythme impressionnant au Maroc, qui a fait appel au laboratoire chinois Sinopharm et au britannique AstraZeneca. Plus de 4 millions de Marocains sur 36 millions d’habitants ont déjà reçu au moins une dose de vaccin")
    with st.beta_expander("pour plus d'informations concernant les vaxins utilisés, l'opération de vaxination, ou l'enregistrement"):
        st.markdown('veuillez visiter [le portail de la campagne de vaccination contre le coronavirus](https://www.liqahcorona.ma/fr)')
    st.markdown('__voici un tableau regroupant les donnés sur la campagne de vaccination au maroc__')
    df = df.drop(df.columns[[0,1,2,3,4,5,6,7]], axis=1)
    df = df.drop(df.index[[1,337]], axis=0)
    st.write(df)
    
    y_options = [
    "new_vaccinations","people_fully_vaccinated","people_vaccinated"
    ]

    y_axis = st.selectbox('quel graphe voulez vous?', y_options)


    fig = px.line(df,
                y=y_axis,
                title=f'graph of {y_axis}')

    st.plotly_chart(fig)
