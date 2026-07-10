"""Purpose: Classification of formal SES frameworks and management-oriented approaches.
Generated from the uploaded exploratory notebook. Final classifications must be validated against Supplementary Material S1.
"""
DATA_URL = "https://raw.githubusercontent.com/gelsonalexfg-hash/revisao-sistematica-/refs/heads/main/Replica.csv"


# ---- Original cell 13 ----
# Importar bibliotecas
import pandas as pd

# URL do arquivo CSV
url = DATA_URL

# Ler o CSV com separador ";"
df = pd.read_csv(url, sep=';')

# -----------------------------
# 1. Categorizar a coluna 'Framework used' para contextos de ilhas
# -----------------------------
def categorize_framework_islands(x):
    x = str(x).lower()
    if "social-ecological systems" in x or "ses" in x:
        return "SES Island Framework"
    elif "ecosystem services" in x:
        return "Ecosystem Services Assessment"
    elif "resilience" in x:
        return "Resilience Assessment"
    elif "conservation planning" in x:
        return "Conservation Planning Island"
    elif "biodiversity management" in x:
        return "Biodiversity Management Island"
    elif "marine spatial planning" in x or "msp" in x:
        return "Marine Spatial Planning Island"
    elif "participatory" in x or "co-management" in x:
        return "Participatory/Co-management Island"
    elif "adaptive management" in x:
        return "Adaptive Management Island"
    elif "integrated coastal management" in x or "icm" in x:
        return "Integrated Coastal Management Island"
    elif "fisheries management" in x:
        return "Fisheries Management Island"
    elif "tourism management" in x:
        return "Tourism Management Island"
    elif "agroecology" in x or "sustainable agriculture" in x:
        return "Sustainable Agriculture Island"
    else:
        # Se não se encaixa em nenhum acima, tentar mapear pelo conteúdo mais específico
        return "Island Socio-Ecological Management"

df['Framework_Category'] = df['Framework used'].apply(categorize_framework_islands)

# -----------------------------
# 2. Categorizar a coluna 'Methodology' para contextos de ilhas
# -----------------------------
def categorize_methodology_islands(x):
    x = str(x).lower()
    if "qualitative" in x:
        return "Qualitative Analysis"
    elif "quantitative" in x:
        return "Quantitative Analysis"
    elif "mixed" in x:
        return "Mixed Methods"
    elif "survey" in x or "questionnaire" in x:
        return "Survey/Questionnaire"
    elif "interview" in x:
        return "Interviews"
    elif "model" in x or "modelling" in x:
        return "Modeling/Simulation"
    elif "case study" in x:
        return "Case Study"
    elif "spatial analysis" in x or "gis" in x:
        return "Spatial/GIS Analysis"
    elif "participatory" in x or "workshop" in x:
        return "Participatory Methods"
    elif "ecosystem assessment" in x:
        return "Ecosystem Assessment"
    elif "fisheries survey" in x or "catch data" in x:
        return "Fisheries Data Analysis"
    elif "tourism survey" in x:
        return "Tourism Data Analysis"
    elif "land use analysis" in x:
        return "Land Use/Resource Analysis"
    else:
        return "Island-specific Method"

df['Methodology_Category'] = df['Methodology'].apply(categorize_methodology_islands)

# -----------------------------
# 3. Tabela de frequência Framework
# -----------------------------
framework_freq = df['Framework_Category'].value_counts().reset_index()
framework_freq.columns = ['Framework_Category', 'Frequency']
framework_freq['Percentage'] = round((framework_freq['Frequency'] / framework_freq['Frequency'].sum())*100, 1)

# -----------------------------
# 4. Tabela de frequência Methodology
# -----------------------------
method_freq = df['Methodology_Category'].value_counts().reset_index()
method_freq.columns = ['Methodology_Category', 'Frequency']
method_freq['Percentage'] = round((method_freq['Frequency'] / method_freq['Frequency'].sum())*100, 1)

# -----------------------------
# 5. Salvar CSV com as categorias
# -----------------------------
df.to_csv("Replica_Categorized_Islands.csv", index=False, sep=';')

# -----------------------------
# 6. Mostrar resultados
# -----------------------------
print("Tabela de frequência - Framework used (Ilhas):")
print(framework_freq)

print("\nTabela de frequência - Methodology (Ilhas):")
print(method_freq)


# ---- Original cell 14 ----
import pandas as pd

url = DATA_URL
df = pd.read_csv(url, sep=';')

# ---- Original cell 15 ----
df['Framework_Category'] = df['Framework used'].apply(categorize_framework_islands)

# ---- Original cell 16 ----
# Agrupar todos os valores originais por categoria
framework_grouped = (
    df.groupby('Framework_Category')['Framework used']
    .apply(list)
    .reset_index()
)

# Mostrar tudo sem cortar texto
pd.set_option('display.max_colwidth', None)

framework_grouped
