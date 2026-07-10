"""Purpose: Classification and synthesis of social and ecological variables.
Generated from the uploaded exploratory notebook. Final classifications must be validated against Supplementary Material S1.
"""
DATA_URL = "https://raw.githubusercontent.com/gelsonalexfg-hash/revisao-sistematica-/refs/heads/main/Replica.csv"


# ---- Original cell 10 ----
# ===========================================
# Análise Exploratória de Dados Qualitativos
# Autor: Gelson Alex Monteiro
# Objetivo: Categorização e análise de 106 artigos sobre SES em ilhas
# ===========================================

# --- 1. Importação das bibliotecas ---
import pandas as pd

# --- 2. Leitura do arquivo ---
url = DATA_URL

# O separador é ";"
df = pd.read_csv(url, sep=';', encoding='utf-8')

# Visualizar as primeiras linhas
print("Pré-visualização do dataset:")
display(df.head())

# --- 3. Padronizar textos para facilitar categorização ---
for col in ['Methodology', 'Framework used', 'Social variable', 'Ecological variable']:
    df[col] = df[col].astype(str).str.lower().str.strip()

# --- 4. Criar funções de categorização específicas ---

def categorize_methodology(x):
    if any(word in x for word in ['qualitative', 'interview', 'focus group', 'case study']):
        return 'Qualitative / Case Study'
    elif any(word in x for word in ['quantitative', 'survey', 'statistical', 'regression']):
        return 'Quantitative / Statistical'
    elif any(word in x for word in ['mixed', 'triangulation', 'combined']):
        return 'Mixed Methods'
    elif any(word in x for word in ['model', 'simulation', 'scenario']):
        return 'Model-Based / Simulation'
    else:
        return 'Empirical Field / Observational'

def categorize_framework(x):
    if 'ses' in x or 'socio-ecological' in x:
        return 'Socio-Ecological Systems (SES) Framework'
    elif 'dpsir' in x:
        return 'DPSIR (Drivers–Pressures–State–Impact–Response)'
    elif 'resilience' in x:
        return 'Resilience or Adaptive Cycle'
    elif 'ecosystem services' in x or 'es' in x:
        return 'Ecosystem Services Approach'
    elif 'co-management' in x or 'governance' in x:
        return 'Co-management / Governance Framework'
    elif 'sustainability' in x:
        return 'Sustainability Assessment Model'
    else:
        return 'Integrated Island System Approach'

def categorize_social_variable(x):
    if any(word in x for word in ['livelihood', 'income', 'employment']):
        return 'Livelihoods & Economic Activities'
    elif any(word in x for word in ['governance', 'policy', 'institution']):
        return 'Governance & Policy'
    elif any(word in x for word in ['education', 'awareness', 'knowledge']):
        return 'Education & Environmental Awareness'
    elif any(word in x for word in ['participation', 'community', 'stakeholder']):
        return 'Community Participation & Social Engagement'
    elif any(word in x for word in ['culture', 'heritage', 'traditional']):
        return 'Cultural Values & Traditional Knowledge'
    else:
        return 'Social Well-being & Perception'

def categorize_ecological_variable(x):
    if any(word in x for word in ['biodiversity', 'species', 'habitat']):
        return 'Biodiversity & Habitat Conservation'
    elif any(word in x for word in ['climate', 'temperature', 'rainfall']):
        return 'Climate & Environmental Change'
    elif any(word in x for word in ['marine', 'coastal', 'fish', 'coral']):
        return 'Marine & Coastal Ecosystems'
    elif any(word in x for word in ['forest', 'land use', 'soil']):
        return 'Terrestrial & Land Use Dynamics'
    elif any(word in x for word in ['ecosystem service', 'provisioning', 'regulating']):
        return 'Ecosystem Function & Services'
    else:
        return 'Ecological Integrity & Natural Resources'

# --- 5. Aplicar as funções de categorização ---
df['Methodology_Category'] = df['Methodology'].apply(categorize_methodology)
df['Framework_Category'] = df['Framework used'].apply(categorize_framework)
df['Social_Category'] = df['Social variable'].apply(categorize_social_variable)
df['Ecological_Category'] = df['Ecological variable'].apply(categorize_ecological_variable)

# --- 6. Tabela resumo de frequências ---
summary = {
    'Methodology': df['Methodology_Category'].value_counts(),
    'Framework used': df['Framework_Category'].value_counts(),
    'Social variable': df['Social_Category'].value_counts(),
    'Ecological variable': df['Ecological_Category'].value_counts()
}

# Converter em DataFrame
summary_df = pd.DataFrame(summary).fillna(0).astype(int)
display(summary_df)

# --- 7. Exportar tabela final ---
df.to_csv("SES_islands_categorized.csv", sep=';', index=False, encoding='utf-8')
summary_df.to_csv("SES_summary_table.csv", sep=';', encoding='utf-8')

print("\nArquivos exportados:")
print("1. SES_islands_categorized.csv -> base com categorias aplicadas")
print("2. SES_summary_table.csv -> tabela resumo de frequências por categoria")


# ---- Original cell 11 ----
# ===========================================
# Análise cruzada e gráficos de barra agrupada
# ===========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Ler o arquivo categorizado (ou usar df do passo anterior) ---
df = pd.read_csv("SES_islands_categorized.csv", sep=';')

# --- 2. Social variable vs Ecological variable ---

# Tabela de frequência cruzada
social_ecological_ct = pd.crosstab(df['Social_Category'], df['Ecological_Category'])
display(social_ecological_ct)

# Gráfico de barras agrupadas
social_ecological_ct.plot(kind='bar', figsize=(12,7), width=0.8)
plt.title('Distribuição de Artigos por Social vs Ecological Variable')
plt.xlabel('Social Variable')
plt.ylabel('Número de Artigos')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Ecological Variable', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()

# --- 3. Methodology vs Framework used ---

# Tabela de frequência cruzada
method_framework_ct = pd.crosstab(df['Methodology_Category'], df['Framework_Category'])
display(method_framework_ct)

# Gráfico de barras agrupadas
method_framework_ct.plot(kind='bar', figsize=(12,7), width=0.8)
plt.title('Distribuição de Artigos por Methodology vs Framework Used')
plt.xlabel('Methodology')
plt.ylabel('Número de Artigos')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Framework', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()

# --- 4. Exportar tabelas cruzadas para CSV ---
social_ecological_ct.to_csv("Social_vs_Ecological.csv", sep=';', encoding='utf-8')
method_framework_ct.to_csv("Methodology_vs_Framework.csv", sep=';', encoding='utf-8')

print("Tabelas cruzadas exportadas com sucesso!")


# ---- Original cell 12 ----
# ===========================================
# Categorização e tabelas de frequência (Base: 105 artigos)
# ===========================================

import pandas as pd

# --- 1. Ler o arquivo ---
url = DATA_URL
df = pd.read_csv(url, sep=';', encoding='utf-8')

# Confirmar total de artigos
print(f"✅ Total de artigos carregados: {len(df)} (esperado: 105)\n")

# Padronizar textos
for col in ['Methodology', 'Framework used', 'Social variable', 'Ecological variable']:
    df[col] = df[col].astype(str).str.lower().str.strip()

# --- 2. Funções de categorização ---

# Categorias Methodology
def categorize_methodology(x):
    if any(word in x for word in ['qualitative', 'interview', 'focus group', 'case study']):
        return 'Qualitative / Case Study'
    elif any(word in x for word in ['quantitative', 'survey', 'statistical', 'regression']):
        return 'Quantitative / Statistical'
    elif any(word in x for word in ['mixed', 'triangulation', 'combined']):
        return 'Mixed Methods'
    elif any(word in x for word in ['model', 'simulation', 'scenario']):
        return 'Model-Based / Simulation'
    else:
        return 'Empirical Field / Observational'

# Categorias Framework used
def categorize_framework(x):
    if 'ses' in x or 'socio-ecological' in x:
        return 'Socio-Ecological Systems (SES) Framework'
    elif 'dpsir' in x:
        return 'DPSIR (Drivers–Pressures–State–Impact–Response)'
    elif 'resilience' in x:
        return 'Resilience or Adaptive Cycle'
    elif 'ecosystem services' in x or 'es' in x:
        return 'Ecosystem Services Approach'
    elif 'co-management' in x or 'governance' in x:
        return 'Co-management / Governance Framework'
    elif 'sustainability' in x:
        return 'Sustainability Assessment Model'
    else:
        return 'Integrated Island System Approach'

# Categorias Social variable
def categorize_social_variable(x):
    if any(word in x for word in ['livelihood', 'income', 'employment']):
        return 'Livelihoods & Economic Activities'
    elif any(word in x for word in ['governance', 'policy', 'institution']):
        return 'Governance & Policy'
    elif any(word in x for word in ['education', 'awareness', 'knowledge']):
        return 'Education & Environmental Awareness'
    elif any(word in x for word in ['participation', 'community', 'stakeholder']):
        return 'Community Participation & Social Engagement'
    elif any(word in x for word in ['culture', 'heritage', 'traditional']):
        return 'Cultural Values & Traditional Knowledge'
    else:
        return 'Social Well-being & Perception'

# Categorias Ecological variable
def categorize_ecological_variable(x):
    if any(word in x for word in ['biodiversity', 'species', 'habitat']):
        return 'Biodiversity & Habitat Conservation'
    elif any(word in x for word in ['climate', 'temperature', 'rainfall']):
        return 'Climate & Environmental Change'
    elif any(word in x for word in ['marine', 'coastal', 'fish', 'coral']):
        return 'Marine & Coastal Ecosystems'
    elif any(word in x for word in ['forest', 'land use', 'soil']):
        return 'Terrestrial & Land Use Dynamics'
    elif any(word in x for word in ['ecosystem service', 'provisioning', 'regulating']):
        return 'Ecosystem Function & Services'
    else:
        return 'Ecological Integrity & Natural Resources'

# --- 3. Aplicar categorias ---
df['Methodology_Category'] = df['Methodology'].apply(categorize_methodology)
df['Framework_Category'] = df['Framework used'].apply(categorize_framework)
df['Social_Category'] = df['Social variable'].apply(categorize_social_variable)
df['Ecological_Category'] = df['Ecological variable'].apply(categorize_ecological_variable)

# --- 4. Tabelas de frequência separadas ---
method_freq = df['Methodology_Category'].value_counts()
framework_freq = df['Framework_Category'].value_counts()
social_freq = df['Social_Category'].value_counts()
ecological_freq = df['Ecological_Category'].value_counts()

print("\n=== Frequência: Methodology ===")
display(method_freq)

print("\n=== Frequência: Framework Used ===")
display(framework_freq)

print("\n=== Frequência: Social Variable ===")
display(social_freq)

print("\n=== Frequência: Ecological Variable ===")
display(ecological_freq)

# --- 5. Exportar CSV com categorias ---
df.to_csv("SES_islands_categorized_separately.csv", sep=';', index=False, encoding='utf-8')
print("\nArquivo SES_islands_categorized_separately.csv exportado com sucesso!")

