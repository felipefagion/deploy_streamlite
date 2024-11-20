import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Definir o tema escuro fixo
st.set_page_config(
    page_title="Sobre Mim",  # Título da página
    layout="wide",  # Layout amplo
    initial_sidebar_state="expanded",  # Estado da barra lateral
)


# Definir o tema escuro através de CSS
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: #121212;
            color: white;
        }
        .css-18e3th9 {
            background-color: #121212;
        }
    </style>
""", unsafe_allow_html=True)


# Título centralizado e com fonte maior
st.markdown("""
    <h1 style="text-align: center; font-size: 2em;">
        Olá, Seja Bem-vindo(a) ao Meu Portfólio de Projetos de Ciência e Análise de Dados
    </h1>
""", unsafe_allow_html=True)



def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://www.esri.com/content/dam/esrisites/en-us/landing-pages/digital-transformation/2023-update/dt-banner.jpg");
             background-size: cover;
             background-position: center center;
             position: relative;
         }}
         .stApp::before {{
             content: '';
             position: absolute;
             top: 0;
             left: 0;
             right: 0;
             bottom: 0;
             background: rgba(255, 255, 255, 0.7);  /* Cor branca semitransparente com maior opacidade */
             z-index: -1;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()


# Função para exibir o fundo com partículas no meio da tela
def set_bg_particles_middle():
    st.markdown("""
    <style>
        .stApp {
            position: relative;
            height: 100vh;
            overflow: hidden;
            color: white;
            background-color: #000;
        }
        #particles-middle {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 40%;
            height: 40%;
            z-index: -1;
        }
    </style>
    """, unsafe_allow_html=True)

    components.html("""
        <html>
            <head>
                <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
            </head>
            <body>
                <div id="particles-middle"></div>
                <script>
                    particlesJS("particles-middle", {
                      "particles": {
                        "number": {"value": 400, "density": {"enable": true, "value_area": 600}},
                        "color": {"value": "#ffffff"},
                        "shape": {"type": "circle"},
                        "opacity": {"value": 0.5, "random": true},
                        "size": {"value": 4, "random": true},
                        "line_linked": {"enable": true, "distance": 100, "color": "#ffffff", "opacity": 0.4, "width": 1},
                        "move": {"enable": true, "speed": 0.5, "direction": "none", "random": false, "straight": false, "out_mode": "out", "bounce": false}
                      },
                      "interactivity": {
                        "events": {"onhover": {"enable": true, "mode": "grab"}, "onclick": {"enable": true, "mode": "push"}},
                        "modes": {"grab": {"distance": 150, "line_linked": {"opacity": 1.2}}}
                      },
                      "retina_detect": true
                    });
                </script>
            </body>
        </html>
    """, height=400)

set_bg_particles_middle()


    # Título "Sobre Mim" centralizado
st.markdown("""
    <h1 style="text-align: center; font-size: 3em; margin-top: 0px;">
        Sobre Mim
    </h1>
""", unsafe_allow_html=True)
st.write('')
st.write('')

# Configuração das colunas
col1, col2 = st.columns([0.7, 3])  # Ajuste proporcional para a imagem e o texto

# Exibir imagem redimensionada na primeira coluna
with col1:
    image = Image.open("foto_pessoal.jfif")  # Substitua pelo caminho da sua imagem
    st.image(image, use_column_width=True)  # Ajusta a largura à coluna

# Biografia na segunda coluna
with col2:
    st.write("""
Nascido em Americana, no coração do estado de São Paulo, aos 27 anos, construo minha trajetória com base em três pilares sólidos: a dedicação aos estudos, a entrega ao trabalho e os momentos de lazer. Cada um desses aspectos contribui para moldar quem sou e para onde desejo levar minha carreira e minha vida.

Minhas horas de descanso são preenchidas com atividades que me trazem alegria e relaxamento, como assistir a partidas de futebol e me perder nas páginas de um bom livro. No entanto, é no universo dos games que encontro minha maior diversão, especialmente por ser uma oportunidade incrível de compartilhar momentos de descontração e estratégia com os amigos.

Paralelamente, minha jornada acadêmica na Universidade Presbiteriana Mackenzie, cursando Ciência de Dados, é um caminho escolhido com propósito. Através dele, busco as ferramentas e o conhecimento necessário para interpretar o mundo através do universo dos dados.

Na Tenda Construtora, uma das gigantes do setor de construção civil no país, aplico esse conhecimento em um ambiente dinâmico e repleto de oportunidades. Lá, minhas responsabilidades vão desde a validação e manutenção de grandes volumes de dados até a criação de relatórios que apoiam decisões estratégicas fundamentais para o negócio. Utilizo uma combinação de linguagens de programação como Python e Excel para códigos e fórmulas de validação de dados, além de SQL para extrair informações de bancos de dados e construir novos indicadores.

Essa rotina é equilibrada com um espírito de aprendizado contínuo e uma busca por inovação. Cada projeto, cada linha de código e cada análise é uma oportunidade de crescer não apenas como profissional, mas também como indivíduo. Acredito firmemente no poder dos dados de transformar indústrias e impulsionar mudanças significativas, e é com essa convicção que me dedico a cada tarefa que assumo.

Minha biografia é, portanto, uma mistura de ambição profissional e paixões pessoais, tecendo uma história que é tão única quanto a jornada que escolhi trilhar. É com esse espírito que enfrento cada novo dia, sempre pronto para o próximo desafio.
""")


# Estilo para os ícones das redes sociais
st.markdown("""
    <style>
        .icon {
            width: 40px;  /* Tamanho do ícone */
            margin: 0 10px;  /* Espaçamento lateral */
        }
        .social-icons {
            display: flex;
            justify-content: right; 
            margin-top: 20px;  /* Espaçamento superior */
        }
    </style>
    
    <div class="social-icons">
        <a href="https://www.linkedin.com/in/felipefagion/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/480px-LinkedIn_logo_initials.png" class="icon" alt="LinkedIn">
        </a>
        <a href="https://www.instagram.com/felipefagion/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" class="icon" alt="Instagram">
        </a>
    </div>
""", unsafe_allow_html=True)

st.write('')

    
def mostrar_projeto(imagem_url, titulo, descricao, linguagem, link):
    col1, col2 = st.columns([1, 2])  
    
    with col1:
        st.image(imagem_url, use_column_width=True)  
    
    with col2:
        st.markdown(f"### {titulo}")  # Título em destaque.
        st.write(descricao)  # Descrição do projeto.
        st.write(linguagem)  # Linguagem utilizada.
        st.write(f"[Veja no GitHub]({link})", unsafe_allow_html=True) 
# Criar duas colunas para os botões
col1, col2 = st.columns(2)

# Definir o estado dos botões
projetos_button = col1.button("📂 Projetos")
curriculo_button = col2.button("📄 Currículo")
# Se o botão "Projetos" for pressionado
if projetos_button:
    st.subheader("Projetos")
    st.write('')

    # Projeto 1
    mostrar_projeto(
        imagem_url="https://github.com/felipefagion/bank_machine_learning/blob/main/arvore_decisao.png?raw=true",
        titulo='Análise Bancária',
        descricao="Este projeto visa analisar dados relacionados a campanhas de marketing bancário, focando na compreensão das características dos clientes que influenciam suas decisões de depósito. O modelo é projetado para aprender com os dados existentes, permitindo prever o público-alvo e identificar fatores que impactam a adesão a depósitos a prazo.",
        linguagem='Liguagem Utilizada: Python',
        link="https://github.com/felipefagion/bank_machine_learning/blob/main/Projeto.ipynb"
    )
    st.write('')
    # Projeto 2
    mostrar_projeto(
        imagem_url="https://github.com/felipefagion/imoveis_regressao_linear/blob/main/pairplot_mobiliado.png?raw=true",
        titulo="Análise Imóveis",
        descricao="O projeto tem como objetivo analisar dados de imóveis para aluguel no Brasil, com foco em variáveis como cidade, área, número de quartos, banheiros, vagas de garagem, e mais. A análise busca entender quais fatores influenciam no preço total do aluguel e aplicar um modelo de machine learning para prever esse valor..",
        linguagem='Liguagem Utilizada: Python',        
        link="https://github.com/felipefagion/imoveis_regressao_linear/blob/main/imoveis.ipynb"
    )
    st.write('')
    # Projeto 3
    mostrar_projeto(
        imagem_url="https://github.com/felipefagion/mackenzie_projeto_aplicado/blob/main/Imagens/image_resized.png?raw=true",
        titulo="Análise Exploratória de Imóveis ",
        descricao="O presente estudo tem como objetivo realizar uma análise exploratória aprofundada sobre as variáveis presentes em uma base de dados de imóveis na cidade de São Paulo. Tratou-se de um projeto colaborativo no qual desempenhei um papel significativo, concentrando-me especialmente na elaboração de gráficos, bem como na exploração e descrição detalhada das variáveis analisadas".,
        linguagem='Liguagem Utilizada: Python',
        link="https://github.com/felipefagion/mackenzie_projeto_aplicado/blob/main/scripts/analise_exploratoria.ipynb"
    )
    st.write('')
    # Projeto 4
    mostrar_projeto(
        imagem_url="https://github.com/felipefagion/varejo_analise_exploratoria/blob/main/vendas.png?raw=true",
        titulo="Análise Varejo",
        descricao="O objetivo deste dataset é analisar e monitorar as vendas de produtos em diferentes categorias e segmentos, facilitando a identificação de tendências de mercado, performance de vendas, e eficiência dos vendedores.",
        linguagem='Liguagem Utilizada: Python', 
        link="https://github.com/felipefagion/varejo_analise_exploratoria/blob/main/projeto.ipynb"
    )
# Se o botão "Currículo" for pressionado
elif curriculo_button:
    # Mostrando as principais informações do currículo
    st.write("""
    **Felipe Fagion Longarini**  
    **Local:** Americana - São Paulo/SP  
    **Telefone:** (19) 99230-9687  
    **Email:** [lipe.fagion@hotmail.com](mailto:lipe.fagion@hotmail.com)  
    **LinkedIn:** [linkedin.com/in/felipefagion](https://www.linkedin.com/in/felipefagion)  
    """)

    # Síntese de conhecimentos
    st.write("### Síntese de Conhecimentos")
    st.write("""
    - **Desenvolvimento e Integração de Modelos de Dados:** Experiência na criação e implementação de modelos de dados escaláveis e dinâmicos.
    - **Automatização de Processos:** Competências em automação de fluxos de trabalho utilizando Python e Excel.
    - **Visualização de Dados:** Proficiente em Power BI e bibliotecas Python para dashboards interativos.
    - **Interpretação de Resultados e Insights Estratégicos:** Habilidade para transformar grandes volumes de dados em insights.
    """)

    # Formação Acadêmica
    st.write("### Formação Acadêmica")
    st.write("- Tecnólogo em Ciência de Dados | Universidade Presbiteriana Mackenzie (Previsão de Término: 06/2026)")

    # Experiência Profissional
    st.write("### Trajetória Profissional")
    st.write("""
    - **Tenda Construtora**  
    Estágio – Cientista de Dados | 06/2024 – 11/2024  
    Preparação de dados, elaboração de relatórios, e desenvolvimento de modelos de dados para apoiar a tomada de decisões.

    - **Móveis Planejados**  
    Freelancer - Assistente Administrativo e Mídias Sociais | 02/2024 – 05/2024  
    Atendimento a clientes, promoção de marcas em mídias sociais e gestão de campanhas publicitárias.

    - **A.A de Melo & CIA LTDA**  
    Balconista | 06/2013 – 08/2023  
    Gestão de relacionamento com clientes e organização do estoque.
    """)

    # Cursos e Certificações
    st.write("### Cursos e Certificações")
    st.write("""
    - Pacote Office | Prime Cursos (2024)
    - Fundamentos do Aprendizado de Máquina | Dio (2024)
    - Excel para Análise de Dados | Preditiva (2024)
    - Tableau de A a Z Business Analytics | Udemy (2024)
    - SQL Avançado para Análise de Dados com Bigquery | Udemy (2024)
    - Introdução a Inteligência Artificial | Science Academy (2024)
    - Microsoft Power BI para Business Intelligence e Data Science | Data Science Academy (2024)
    - Linguagem Python para Análise de Dados e Ciência de Dados | Data Science Academy (2023)
    """)

    # Idiomas
    st.write("### Idiomas")
    st.write("- Inglês Básico")

    st.subheader("Currículo")
    with open("Currículo - Felipe Fagion Longarini.docx", "rb") as file:
        st.download_button(
            label="Baixar Currículo",
            data=file,
            file_name="Curriculo - Felipe Fagion Longarini.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )