"""Purpose: Study-design inspection and dominant analytical-processing classification.
Generated from the uploaded exploratory notebook. Final classifications must be validated against Supplementary Material S1.
"""
DATA_URL = "https://raw.githubusercontent.com/gelsonalexfg-hash/revisao-sistematica-/refs/heads/main/Replica.csv"


# ---- Original cell 17 ----
# ===============================
# 1. Importação de bibliotecas
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 2. Leitura do arquivo CSV
# ===============================
url = DATA_URL

df = pd.read_csv(url, sep=";")

# Visualização inicial
df.head()

# ---- Original cell 18 ----
# Dimensão do dataset
df.shape

# ---- Original cell 19 ----
# Contagem de valores por metodologia original
df['Methodology'].value_counts()

# ---- Original cell 20 ----
# Verificar valores ausentes
df['Methodology'].isna().sum()

# ---- Original cell 21 ----
# Função de reclassificação metodológica
def classify_processing(method):
    method = method.lower()

    # Narrative-based processing
    if any(k in method for k in [
        'qualitative', 'interview', 'case study',
        'document', 'historical', 'ethnographic',
        'content analysis', 'archival'
    ]):
        return 'Narrative-based processing'

    # Participatory–deliberative processing
    elif any(k in method for k in [
        'participatory', 'nominal group', 'workshop',
        'co-production', 'focus group', 'stakeholder'
    ]):
        return 'Participatory–deliberative processing'

    # Spatial-based processing
    elif any(k in method for k in [
        'gis', 'spatial', 'ppgis', 'marxan',
        'cluz', 'mapping', 'kernel density'
    ]):
        return 'Spatial-based processing'

    # Model-based processing
    elif any(k in method for k in [
        'model', 'simulation', 'ecosim', 'ecopath',
        'network', 'sen', 'mcda', 'risk matrix'
    ]):
        return 'Model-based processing'

    # Statistical-based processing
    elif any(k in method for k in [
        'survey', 'questionnaire', 'quantitative',
        'statistical', 'anova', 'pca', 'regression',
        'descriptive'
    ]):
        return 'Statistical-based processing'

    else:
        return 'Unclassified'

# ---- Original cell 22 ----
# Aplicar classificação
df['Data_Processing_Type'] = df['Methodology'].apply(classify_processing)

# Verificar distribuição
df['Data_Processing_Type'].value_counts()

# ---- Original cell 23 ----
# Agrupar metodologias dentro de cada tipo de processamento
examples_table = (
    df
    .groupby(['Data_Processing_Type', 'Methodology'])
    .size()
    .reset_index(name='n')
    .sort_values(['Data_Processing_Type', 'n'], ascending=[True, False])
)

examples_table.head(10)

# ---- Original cell 24 ----
# Agrupar metodologias dentro de cada categoria
grouped = (
    df.groupby('Data_Processing_Type')['Methodology']
    .apply(list)
    .reset_index()
)

grouped
