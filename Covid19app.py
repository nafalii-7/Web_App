import streamlit as st 
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

st.title('Suivi du covid 19 au maroc')

st.cache(persist=True) 

df = pd.read_csv(r'https://raw.githubusercontent.com/nafalii-7/Web_App/main/covid19data.csv', encoding='ISO-8859-1',thousands='.', decimal=',', engine='python')
df.head()  
df = df.set_index('date')



st.sidebar.title("Choisir entre les données du jour, le suivi des cas de Covid-19 ou le suivi de la campagne de vaccination")
votre_choix = st.sidebar.radio(label="", options=["Données du jour", "Suivi épidémiologique", "Vaccination"])

    
    
if  votre_choix == "Suivi épidémiologique":
      st.image("https://aujourdhui.ma/wp-content/uploads/2020/07/coronavirus-30.jpg")
    
      st.markdown('__Voici un tableau regroupant les donnés sur la situation épidémiologique au Maroc__')
      df = df.drop(df.columns[[8,9,10]], axis=1)
      st.write(df)
      with st.beta_expander("Source"):
        st.markdown('Données quotidiennes tirées [du Portail Officiel du Coronavirus au Maroc](http://www.covidmaroc.ma/pages/Accueilfr.aspx)')
    #
    
    ################
      st.write("\n")
    
      colors = px.colors.qualitative.D3
      fig6 = go.Figure()
      fig6.add_trace(go.Bar(y=df[["Nouveaux décès", "Cas confirmés", "Nouveaux tests"]].columns.tolist(),
                             x=df[["Nouveaux décès", "Cas confirmés", "Nouveaux tests"]].sum().values,
                             text=df[["Nouveaux décès", "Cas confirmés", "Nouveaux tests"]].sum().values,
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
            title="Nombre Total",
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
           st.header("Tests effectués")
           st.warning(df['Tests effectués'][df.index[-1]])
 
      with col2:
           st.header("Cas confirmés")
           st.success(df['Cas confirmés'][df.index[-1]])
      with col3:
           st.header("Décès")
        
           st.info( df['Décès'][df.index[-1]])
    
      st.write("\n")
      st.write("\n") 
      st.title("Visualisation des données quotidiennes" )
    
      all_columns_names= df.columns.tolist()
      selected_column_names = st.multiselect("Choisir la(les) colonne(s) à dessiner dans le graphe",all_columns_names, default = ["Cas confirmés", "Décès"])



      fig = px.line(df,
                  y=selected_column_names,
                  title=f'Èvolution de {selected_column_names}')

      st.plotly_chart(fig)
    
    
      fig2 = px.area(df, x=df.index, y=selected_column_names)
    
      st.plotly_chart(fig2)
 
elif  votre_choix == "Données du jour": 
    st.title("Données du jour")
    
    st.image("https://boursenews.ma/uploads/actualites/5f4f7ebeee78f.jpg")
    
    st.write("\n")
    
    col1, col2, col3 = st.beta_columns(3)

    with col1:
           st.header("Nouveaux tests")
           st.warning(df['Nouveaux tests'][df.index[-1]])
 
    with col2:
           st.header("Nouveaux cas ")
           st.success(df['Nouveaux cas'][df.index[-1]])
    with col3:
           st.header("Nouveaux déces")
        
           st.info( df['Nouveaux décès'][df.index[-1]]) 
      
else:
    st.image("https://www.sante.gov.ma/PublishingImages/2021/vaccin%202021/vaccinfr-d.jpg?csf=1&e=ygzHDz")
    st.write("\n")
    st.info("Depuis son lancement fin janvier, la campagne de vaccination avance à un rythme impressionnant au Maroc, qui a fait appel au laboratoire chinois Sinopharm et au britannique AstraZeneca. Plus de 4 millions de Marocains sur 36 millions d’habitants ont déjà reçu au moins une dose de vaccin")
    with st.beta_expander("Pour plus d'informations concernant les vaxins utilisés, l'opération de vaccination, ou l'enregistrement"):
        st.markdown('Veuillez visiter [le portail de la campagne de vaccination contre le Coronavirus](https://www.liqahcorona.ma/fr)')
    st.markdown('__Voici un tableau regroupant les donnés sur la campagne de vaccination au maroc__')
    df = df.drop(df.columns[[0,1,2,3,4,5,6,7]], axis=1)
    df = df.drop(df.index[[1,337]], axis=0)
    st.write(df)
    
    y_options = [
    "Nouveaux vaccinations","Personnes entièrement vaccinées","Bénéficiaires de la vaccination"
    ]

    y_axis = st.selectbox('Quel graphe voulez vous?', y_options)


    fig = px.line(df,
                y=y_axis,
                title=f'Èvolution de {y_axis}')

    st.plotly_chart(fig)
