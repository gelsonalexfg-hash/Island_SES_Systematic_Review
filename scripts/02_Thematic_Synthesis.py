"""Purpose: Thematic aggregation of findings, gaps, and future research.
Generated from the uploaded exploratory notebook. Final classifications must be validated against Supplementary Material S1.
"""
DATA_URL = "https://raw.githubusercontent.com/gelsonalexfg-hash/revisao-sistematica-/refs/heads/main/Replica.csv"


# ---- Original cell 7 ----
# =========================================
# Análise de revisão sistemática SES - Ilhas
# =========================================

# 1️⃣ Importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

# Configurações de visualização
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10,6)

# 2️⃣ Carregar o CSV
url = DATA_URL
df = pd.read_csv(url, sep=';')

# Visualizar dados
print("Primeiras linhas do dataset:")
display(df.head())
print("\nInformações gerais do dataset:")
df.info()
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# 3️⃣ Função para contar palavras em uma coluna
def count_words(text_series):
    all_text = ' '.join(text_series.dropna().astype(str)).lower()
    all_text = re.sub(r'[^\w\s]', '', all_text)  # Remove pontuação
    words = all_text.split()
    word_count = Counter(words)
    return word_count

# Contagem de palavras em Main findings
mf_count = count_words(df['Main findings'])
print("\n20 palavras mais frequentes em 'Main findings':")
print(mf_count.most_common(20))

# 4️⃣ Função de categorização baseada em palavras-chave
def categorize(text):
    text = str(text).lower()
    if any(x in text for x in ['governance', 'policy', 'management']):
        return 'Governance & Policy'
    elif any(x in text for x in ['education', 'awareness', 'training']):
        return 'Education & Awareness'
    elif any(x in text for x in ['biodiversity', 'species', 'ecosystem']):
        return 'Biodiversity Conservation'
    elif any(x in text for x in ['community', 'participation', 'local people']):
        return 'Community Engagement'
    else:
        return 'Other'

# Aplicar categorização
df['Theme_MainFindings'] = df['Main findings'].apply(categorize)
df['Theme_Conclusion'] = df['Conclusion summary'].apply(categorize)
df['Theme_Gaps'] = df['Research gaps'].apply(categorize)
df['Theme_Future'] = df['Future research'].apply(categorize)

# 5️⃣ Frequência de artigos por tema
theme_counts = df['Theme_MainFindings'].value_counts()
print("\nFrequência de temas em Main findings:")
print(theme_counts)

# Gráfico de barras - Main Findings
plt.figure(figsize=(10,6))
sns.barplot(x=theme_counts.values, y=theme_counts.index, palette='viridis')
plt.title('Frequency of Main SES Findings Themes in Island Regions (2015-2025)')
plt.xlabel('Number of Articles')
plt.ylabel('Themes')
plt.show()

# Gráfico de barras - Research Gaps
gap_counts = df['Theme_Gaps'].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=gap_counts.values, y=gap_counts.index, palette='magma')
plt.title('Frequency of Research Gaps in SES for Island Regions')
plt.xlabel('Number of Mentions')
plt.ylabel('Research Gaps')
plt.show()

# 6️⃣ Cruzamento de temas e lacunas (heatmap)
cross_tab = pd.crosstab(df['Theme_MainFindings'], df['Theme_Gaps'])
plt.figure(figsize=(12,8))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap of Main Findings vs Research Gaps')
plt.show()

# 7️⃣ Exportar resultados para Excel
df.to_excel("SES_Review_Analysis.xlsx", index=False)
print("Resultados exportados para 'SES_Review_Analysis.xlsx'")


# ---- Original cell 8 ----
# =========================================
# SES in Island Regions - Combined Thematic Analysis
# =========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações estéticas
sns.set(style="whitegrid", font_scale=1.2)
plt.rcParams['figure.figsize'] = (12,8)

# 1️⃣ Carregar o dataset
url = DATA_URL
df = pd.read_csv(url, sep=';')

# 2️⃣ Função de categorização refinada
def categorize_island_context(text):
    text = str(text).lower()
    if any(x in text for x in ['governance', 'policy', 'management', 'planning', 'decision']):
        return 'Governance & Policy'
    elif any(x in text for x in ['community', 'livelihood', 'local people', 'stakeholder', 'participation']):
        return 'Community & Livelihoods'
    elif any(x in text for x in ['biodiversity', 'ecosystem', 'species', 'habitat', 'conservation']):
        return 'Biodiversity & Ecosystem Conservation'
    elif any(x in text for x in ['education', 'awareness', 'training', 'capacity building']):
        return 'Education & Awareness'
    elif any(x in text for x in ['climate', 'resilience', 'vulnerability', 'adaptation', 'mitigation']):
        return 'Climate Change & Resilience'
    elif any(x in text for x in ['science', 'policy interface', 'evidence', 'knowledge integration']):
        return 'Science-Policy Integration'
    else:
        return None  # elimina "Other"

# 3️⃣ Aplicar categorias às quatro colunas
df['MainFindings_Theme'] = df['Main findings'].apply(categorize_island_context)
df['ResearchGaps_Theme'] = df['Research gaps'].apply(categorize_island_context)
df['FutureResearch_Theme'] = df['Future research'].apply(categorize_island_context)
df['Conclusion_Theme'] = df['Conclusion summary'].apply(categorize_island_context)

# 4️⃣ Lista de categorias ordenadas
themes = [
    'Governance & Policy',
    'Community & Livelihoods',
    'Biodiversity & Ecosystem Conservation',
    'Education & Awareness',
    'Climate Change & Resilience',
    'Science-Policy Integration'
]

# 5️⃣ Calcular frequências
data = {
    'Main Findings': [df['MainFindings_Theme'].value_counts().get(t,0) for t in themes],
    'Research Gaps': [df['ResearchGaps_Theme'].value_counts().get(t,0) for t in themes],
    'Future Research': [df['FutureResearch_Theme'].value_counts().get(t,0) for t in themes],
    'Conclusion Summary': [df['Conclusion_Theme'].value_counts().get(t,0) for t in themes]
}

df_plot = pd.DataFrame(data, index=themes)

# 6️⃣ Gráfico de barras agrupadas aprimorado
colors = sns.color_palette("Set2", n_colors=4)

ax = df_plot.plot(kind='bar', width=0.8, color=colors, edgecolor='black')
plt.title('Thematic Distribution Across SES Study Components in Island Regions (2015–2025, n=105)', fontsize=16)
plt.ylabel('Number of Articles')
plt.xlabel('Socioecological Themes')
plt.xticks(rotation=35, ha='right')

# Adicionar valores acima das barras
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=10, padding=3)

plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 7️⃣ Exportar tabela consolidada
df_plot.to_excel("SES_Themes_Combined_Analysis.xlsx")
print("✅ Gráfico gerado e tabela exportada como 'SES_Themes_Combined_Analysis.xlsx'")


# ---- Original cell 9 ----
# =========================================
# Tabela consolidada de temas (SES - Ilhas)
# =========================================

import pandas as pd

# Reutiliza o mesmo dataset e categorias do gráfico
url = DATA_URL
df = pd.read_csv(url, sep=';')

# Função de categorização refinada (igual à usada no gráfico)
def categorize_island_context(text):
    text = str(text).lower()
    if any(x in text for x in ['governance', 'policy', 'management', 'planning', 'decision']):
        return 'Governance & Policy'
    elif any(x in text for x in ['community', 'livelihood', 'local people', 'stakeholder', 'participation']):
        return 'Community & Livelihoods'
    elif any(x in text for x in ['biodiversity', 'ecosystem', 'species', 'habitat', 'conservation']):
        return 'Biodiversity & Ecosystem Conservation'
    elif any(x in text for x in ['education', 'awareness', 'training', 'capacity building']):
        return 'Education & Awareness'
    elif any(x in text for x in ['climate', 'resilience', 'vulnerability', 'adaptation', 'mitigation']):
        return 'Climate Change & Resilience'
    elif any(x in text for x in ['science', 'policy interface', 'evidence', 'knowledge integration']):
        return 'Science-Policy Integration'
    else:
        return None

# Aplicar categorização
df['MainFindings_Theme'] = df['Main findings'].apply(categorize_island_context)
df['ResearchGaps_Theme'] = df['Research gaps'].apply(categorize_island_context)
df['FutureResearch_Theme'] = df['Future research'].apply(categorize_island_context)
df['Conclusion_Theme'] = df['Conclusion summary'].apply(categorize_island_context)

# Lista ordenada de temas
themes = [
    'Governance & Policy',
    'Community & Livelihoods',
    'Biodiversity & Ecosystem Conservation',
    'Education & Awareness',
    'Climate Change & Resilience',
    'Science-Policy Integration'
]

# Criar dataframe consolidado com contagens
table_data = {
    'Main Findings': [df['MainFindings_Theme'].value_counts().get(t, 0) for t in themes],
    'Research Gaps': [df['ResearchGaps_Theme'].value_counts().get(t, 0) for t in themes],
    'Future Research': [df['FutureResearch_Theme'].value_counts().get(t, 0) for t in themes],
    'Conclusion Summary': [df['Conclusion_Theme'].value_counts().get(t, 0) for t in themes]
}

table = pd.DataFrame(table_data, index=themes)
table['Total (per Theme)'] = table.sum(axis=1)
table.loc['Total (All Categories)'] = table.sum(axis=0)

# Exibir tabela no Colab
display(table)

# Exportar para Excel
table.to_excel("SES_Combined_Thematic_Table.xlsx", index=True)
print("✅ Tabela consolidada salva como 'SES_Combined_Thematic_Table.xlsx'")

