import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

# Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df.head(3))

# Create scatter plot
    
    years = df['Year']
    seaLevel = df['CSIRO Adjusted Sea Level']

    plt.scatter(years, seaLevel)

# Create first line of best fit

    # Definição do INTERVALO de anos.
    x_1st =  pd.Series(range(1880, 2051)) # o range gera a sequência de anos, e o series transforma os dados em objeto pandas que pode ser usado para operações matemáticas

    # Cálculo dos PARÂMETROS que serão utilizados na regressão linear
    slope, intercept, *_ = linregress(years, seaLevel) # atribuição de multiplos valores de uma só vez com tupla, ignorando os ultimos 3 valores que são retornados com a função

    # Escrevendo a regressão linear que vai gerar as PREVISÕES, com a equação matemática da reta: y = m*x + b (m -> slope (coeficiente angular); b -> intercept (cruzamento no Y))
    y_pred = (slope * x_1st) + intercept

    # Plotando a linha vermelha no scatterplot já existente
    plt.plot(x_1st, y_pred, color='red')

# Create second line of best fit

    # Novo intervalo de dados
    df_recent = df[df['Year'] >= 2000]

    years_recent = df_recent["Year"]
    seaLevel_recent = df_recent['CSIRO Adjusted Sea Level']

    # Definição do novo INTERVALO de anos.
    x_2nd =  pd.Series(range(2000, 2051))

    # Novos parâmetros
    slope_recent, intercept_recent, *_ = linregress(years_recent, seaLevel_recent)

    # Regressão linear
    y_pred2 = (slope_recent * x_2nd) + intercept_recent

    # Plotando a linha roxa no scatterplot
    plt.plot(x_2nd, y_pred2, color='purple')


# Add labels and title

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

# Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()