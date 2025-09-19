import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

# Read data from file
    df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
    
    # Extraindo as colunas necessárias do df e armazenado-as nas variáveis
    years = df['Year']
    seaLevel = df['CSIRO Adjusted Sea Level']

    # Plotando o gráfico de dispersão com as variáveis
    plt.scatter(years, seaLevel)

# Create first line of best fit

    # Definição do INTERVALO de anos (nosso X)
    x_1st =  pd.Series(range(1880, 2051)) # o range gera a sequência de num. inteiros, e o series transforma os dados em objeto pandas que pode ser usado para operações matemáticas

    # Cálculo dos PARÂMETROS que serão utilizados na regressão linear
    slope, intercept, *_ = linregress(years, seaLevel) # atribuição de multiplos valores de uma só vez com tupla, ignorando os ultimos 3 valores que são retornados com a função linregress (r_value, p_value e std_err)

    # Regressão linear que vai gerar as PREVISÕES: utilizei a equação matemática da reta y = m*x + b; onde m -> slope (coeficiente angular); e b -> intercept (cruzamento no Y).
    y_pred = (slope * x_1st) + intercept

    # Plotando a linha vermelha no scatterplot já existente
    plt.plot(x_1st, y_pred, color='red')

# Create second line of best fit

    # Criar um novo dataframe filtrando apenas os dados de 2000 em diante
    df_recent = df[df['Year'] >= 2000]

    # Extraindo as colunas necessárias do df e armazenado-as nas variáveis
    years_recent = df_recent["Year"]
    seaLevel_recent = df_recent['CSIRO Adjusted Sea Level']

    # Definição do novo INTERVALO de anos
    x_2nd =  pd.Series(range(2000, 2051))

    # Novos parâmetros
    slope_recent, intercept_recent, *_ = linregress(years_recent, seaLevel_recent)

    # Regressão linear
    y_pred2 = (slope_recent * x_2nd) + intercept_recent

    # Plotando a linha amarela no scatterplot
    plt.plot(x_2nd, y_pred2, color='yellow')

# Add labels and title

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

# Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
