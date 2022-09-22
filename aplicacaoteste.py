import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#importando os dados
df = pd.read_csv('candidatos.csv')

#criando um menu
st.title('Gradiente ideológico dos presidenciáveis')

from PIL import Image
image = Image.open('gradiente.png')

st.image(image, caption='Da extrema Esquerda para a Estrema Direita')

st.write('     ')
st.write('     ')

candidato = st.select_slider(
        'Selecione um candidato',
        options=['Lula', 'Ciro', 'Simone Tebet', 'Bolsonaro'])


if candidato  == 'Lula':
    st.write('     ')
    st.write('     ')
    st.write('Luiz Inácio Lula da Silva, mais conhecido como Lula, é um ex-sindicalista, ex-metalúrgico e político brasileiro, filiado ao Partido dos Trabalhadores (PT). Foi o 35.º presidente do Brasil entre 1.º de janeiro de 2003 e 1.º de janeiro de 2011.')
    st.write('     ')
    st.write('     ')

    candidato = df[df.Candidato == candidato]

    plt.figure(figsize=(6,2))
    fig = sns.barplot(x='Rede social', y='Seguidores',data=candidato, palette="rocket_r")
    fig.set_title('Seguidores por Rede Social', loc='center',fontsize=6)
    fig.set_ylabel('Seguidores (milhões)',fontsize=4)


    st.pyplot(plt)
    plt.clf()


elif candidato == 'Ciro':

    st.write('     ')
    st.write('     ')
    st.write('Ciro Ferreira Gomes é um advogado, professor universitário e político brasileiro, filiado ao Partido Democrático Trabalhista (PDT), do qual é vice-presidente. Foi deputado estadual por duas legislaturas no Ceará, o 43.º prefeito de Fortaleza, o 52.º governador do Ceará, ministro da Fazenda do Governo Itamar Franco durante a implantação do Plano Real e ministro da Integração Nacional no governo de Luiz Inácio Lula da Silva')
    st.write('     ')
    st.write('     ')

    candidato = df[df.Candidato == candidato]

    plt.figure(figsize=(6,2))
    fig = sns.barplot(x='Rede social', y='Seguidores',data=candidato, palette="rocket_r")
    fig.set_title('Seguidores por Rede Social', loc='center',fontsize=6)
    fig.set_ylabel('Seguidores (milhões)',fontsize=4)


    st.pyplot(plt)
    plt.clf()



elif candidato == 'Simone Tebet':

    st.write('     ')
    st.write('     ')
    st.write('Simone Nassar Tebet é uma advogada, professora, escritora e política brasileira, filiada ao Movimento Democrático Brasileiro (MDB). Atualmente, ocupa o cargo de senadora da República pelo estado de Mato Grosso do Sul. Tebet é pré-candidata à presidência do Brasil nas eleições de 2022, com uma pré-campanha centrista e social liberal na chamada "terceira via".')
    st.write('     ')
    st.write('     ')

    candidato = df[df.Candidato == candidato]

    plt.figure(figsize=(6,2))
    fig = sns.barplot(x='Rede social', y='Seguidores',data=candidato, palette="rocket_r")
    fig.set_title('Seguidores por Rede Social', loc='center',fontsize=6)
    fig.set_ylabel('Seguidores (milhões)',fontsize=4)


    st.pyplot(plt)
    plt.clf()


elif candidato == 'Felipe':
    st.write('Felipeeeeeee')

elif candidato == 'Soraya':
    st.write('     ')
    st.write('     ')
    st.write('Descendente de alemães, Soraya Thronicke nasceu na cidade de Dourados em 1 de junho de 1973 e foi criada em Campo Grande. A então senadora é proprietária, junto com sua família, de uma rede de motéis no Mato Grosso do Sul. Entretanto, Soraya ficou conhecida por atuar em movimentos de rua desde 2013 e por ações que moveu contra políticos e empresas.')
    st.write('     ')
    st.write('     ')

    candidato = df[df.Candidato == candidato]

    plt.figure(figsize=(6,2))
    fig = sns.barplot(x='Rede social', y='Seguidores',data=candidato, palette="rocket_r")
    fig.set_title('Seguidores por Rede Social', loc='center',fontsize=6)
    fig.set_ylabel('Seguidores (milhões)',fontsize=4)


    st.pyplot(plt)
    plt.clf()

elif candidato == 'Bolsonaro':
    st.write('     ')
    st.write('     ')
    st.write('Jair Messias Bolsonaro GOMM (Glicério,[nota 3] 21 de março de 1955) é um militar reformado e político brasileiro, filiado ao Partido Liberal (PL). É o 38.º presidente do Brasil desde 1.º de janeiro de 2019, tendo sido eleito pelo Partido Social Liberal (PSL). Foi deputado federal pelo Rio de Janeiro entre 1991 e 2018. Nasceu no município de Glicério, no interior do estado de São Paulo, mas morou em várias outras cidades paulistas ao longo de sua infância. Em 1966, sua família se estabeleceu em Eldorado, no Vale do Ribeira, onde passou a adolescência com seus cinco irmãos.')
    st.write('     ')
    st.write('     ')

    candidato = df[df.Candidato == candidato]

    plt.figure(figsize=(6,2))
    fig = sns.barplot(x='Rede social', y='Seguidores',data=candidato, palette="rocket_r")
    fig.set_title('Seguidores por Rede Social', loc='center',fontsize=6)
    fig.set_ylabel('Seguidores (milhões)',fontsize=4)


    st.pyplot(plt)
    plt.clf()








