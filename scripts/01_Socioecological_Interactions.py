"""Purpose: Primary and secondary socio-ecological interaction classification and Figure 5.
Generated from the uploaded exploratory notebook. Final classifications must be validated against Supplementary Material S1.
"""
DATA_URL = "https://raw.githubusercontent.com/gelsonalexfg-hash/revisao-sistematica-/refs/heads/main/Replica.csv"


# ---- Original cell 0 ----
# --- 1. Importar bibliotecas ---
import pandas as pd
import matplotlib.pyplot as plt

# --- 2. Carregar o arquivo atualizado ---
url = DATA_URL
df = pd.read_csv(url, sep=';')

# --- 3. Limpeza e verificação ---
df = df.dropna(subset=['Type of social-ecological interaction'])
df['Type of social-ecological interaction'] = df['Type of social-ecological interaction'].astype(str).str.strip()
df = df[df['Type of social-ecological interaction'] != '']
df = df.drop_duplicates(subset=['Type of social-ecological interaction'])

print(f"✅ Total de artigos após limpeza: {len(df)} (esperado: 105)\n")

# --- 4. Função de categorização (contextos insulares) ---
def categorize_interaction(text):
    text = text.lower()
    if any(x in text for x in ['tourism', 'visitor', 'ecotourism', 'recreation', 'diving', 'snorkel']):
        return "Coastal and Marine Tourism"
    elif any(x in text for x in ['fishing', 'fishery', 'artisanal', 'marine resource', 'harvest', 'catch']):
        return "Artisanal Fisheries and Marine Resource Use"
    elif any(x in text for x in ['agriculture', 'farming', 'crop', 'livestock', 'pastoral']):
        return "Subsistence Agriculture and Livelihood Systems"
    elif any(x in text for x in ['governance', 'policy', 'management', 'planning', 'institution', 'decision']):
        return "Governance, Institutions and Policy Processes"
    elif any(x in text for x in ['conservation', 'biodiversity', 'protected area', 'reserve', 'habitat', 'species']):
        return "Biodiversity Conservation and Protected Area Management"
    elif any(x in text for x in ['climate', 'adaptation', 'resilience', 'vulnerability', 'hazard', 'sea level']):
        return "Climate Change Adaptation and Resilience"
    elif any(x in text for x in ['education', 'awareness', 'capacity', 'training', 'knowledge']):
        return "Environmental Education and Awareness"
    elif any(x in text for x in ['cultural', 'traditional', 'heritage', 'belief', 'custom']):
        return "Cultural and Traditional Ecological Knowledge"
    elif any(x in text for x in ['community', 'participation', 'engagement', 'co-management', 'stakeholder']):
        return "Community Participation and Co-management"
    elif any(x in text for x in ['urban', 'infrastructure', 'housing', 'development', 'construction']):
        return "Infrastructure Development and Urban Expansion"
    elif any(x in text for x in ['energy', 'waste', 'pollution', 'plastic', 'contamination']):
        return "Pollution, Waste and Energy Systems"
    elif any(x in text for x in ['migration', 'demographic', 'population', 'mobility']):
        return "Migration and Demographic Pressure"
    else:
        return "Other Island-Specific Interventions"

# --- 5. Aplicar categorização ---
df['Intervention Category'] = df['Type of social-ecological interaction'].apply(categorize_interaction)

# --- 6. Criar tabela de frequência ---
freq_table = df['Intervention Category'].value_counts().reset_index()
freq_table.columns = ['Intervention Category', 'count']  # 'count' = número de artigos
freq_table['Percentage'] = (freq_table['count'] / len(df) * 100).round(1)

print("=== Frequência de Artigos por Categoria (105 artigos) ===\n")
print(freq_table)

# --- 7. Gráfico de barras ---
plt.figure(figsize=(10,6))
plt.barh(freq_table['Intervention Category'], freq_table['count'], color='skyblue')
plt.xlabel('Number of Articles')
plt.ylabel('Intervention Category')
plt.title('Frequency of Articles by Socio-ecological Intervention Category (Island Regions))')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# --- 8. Exportar resultado ---
df.to_csv("SES_intervention_categorized_islands_final.csv", index=False, sep=';')
print("\n💾 Arquivo 'SES_intervention_categorized_islands_final.csv' salvo com sucesso.")


# ---- Original cell 1 ----
import pandas as pd

# Carregar dados
url = DATA_URL
df = pd.read_csv(url, sep=';')

# Limpeza (igual ao teu script)
df = df.dropna(subset=['Type of social-ecological interaction'])
df['Type of social-ecological interaction'] = df['Type of social-ecological interaction'].astype(str).str.strip()
df = df[df['Type of social-ecological interaction'] != '']
df = df.drop_duplicates(subset=['Type of social-ecological interaction'])

# Função de categorização
def categorize_interaction(text):
    text = text.lower()
    if any(x in text for x in ['tourism', 'visitor', 'ecotourism', 'recreation', 'diving', 'snorkel']):
        return "Coastal and Marine Tourism"
    elif any(x in text for x in ['fishing', 'fishery', 'artisanal', 'marine resource', 'harvest', 'catch']):
        return "Artisanal Fisheries and Marine Resource Use"
    elif any(x in text for x in ['agriculture', 'farming', 'crop', 'livestock', 'pastoral']):
        return "Subsistence Agriculture and Livelihood Systems"
    elif any(x in text for x in ['governance', 'policy', 'management', 'planning', 'institution', 'decision']):
        return "Governance, Institutions and Policy Processes"
    elif any(x in text for x in ['conservation', 'biodiversity', 'protected area', 'reserve', 'habitat', 'species']):
        return "Biodiversity Conservation and Protected Area Management"
    elif any(x in text for x in ['climate', 'adaptation', 'resilience', 'vulnerability', 'hazard', 'sea level']):
        return "Climate Change Adaptation and Resilience"
    elif any(x in text for x in ['education', 'awareness', 'capacity', 'training', 'knowledge']):
        return "Environmental Education and Awareness"
    elif any(x in text for x in ['cultural', 'traditional', 'heritage', 'belief', 'custom']):
        return "Cultural and Traditional Ecological Knowledge"
    elif any(x in text for x in ['community', 'participation', 'engagement', 'co-management', 'stakeholder']):
        return "Community Participation and Co-management"
    elif any(x in text for x in ['urban', 'infrastructure', 'housing', 'development', 'construction']):
        return "Infrastructure Development and Urban Expansion"
    elif any(x in text for x in ['energy', 'waste', 'pollution', 'plastic', 'contamination']):
        return "Pollution, Waste and Energy Systems"
    elif any(x in text for x in ['migration', 'demographic', 'population', 'mobility']):
        return "Migration and Demographic Pressure"
    else:
        return "Other Island-Specific Interventions"

# Aplicar categorização
df['Intervention Category'] = df['Type of social-ecological interaction'].apply(categorize_interaction)

# ---- Original cell 2 ----
# Agrupar conteúdo por categoria
grouped = (
    df.groupby('Intervention Category')['Type of social-ecological interaction']
    .apply(lambda x: sorted(set(x)))
    .reset_index()
)

pd.set_option('display.max_colwidth', None)

grouped

# ---- Original cell 3 ----
def categorize_interaction(text):
    text = str(text).lower()

    # 1. MARINE RESOURCE USE (pesca primeiro - alta prioridade)
    if any(x in text for x in ['fishing', 'fishery', 'artisanal', 'catch', 'harvest']):
        return "Marine Resource Use and Fisheries Systems"

    # 2. TOURISM SYSTEMS
    elif any(x in text for x in ['tourism', 'ecotourism', 'visitor', 'recreation', 'diving', 'snorkel']):
        return "Tourism-Based Socio-Ecological Systems"

    # 3. AGRICULTURE / LAND USE
    elif any(x in text for x in ['agriculture', 'farming', 'crop', 'livestock', 'pastoral', 'land use']):
        return "Agricultural and Land-Based Livelihood Systems"

    # 4. CONSERVATION / BIODIVERSITY
    elif any(x in text for x in ['conservation', 'biodiversity', 'protected area', 'reserve', 'habitat', 'species']):
        return "Conservation and Biodiversity Management Systems"

    # 5. CLIMATE / ENVIRONMENTAL CHANGE
    elif any(x in text for x in ['climate', 'adaptation', 'resilience', 'vulnerability', 'hazard', 'sea level']):
        return "Climate and Environmental Change Interactions"

    # 6. POLLUTION / DEGRADATION
    elif any(x in text for x in ['pollution', 'waste', 'plastic', 'contamination', 'energy']):
        return "Pollution and Environmental Degradation Systems"

    # 7. SOCIO-CULTURAL SYSTEMS
    elif any(x in text for x in ['cultural', 'traditional', 'heritage', 'belief', 'custom', 'indigenous', 'knowledge']):
        return "Socio-Cultural and Knowledge-Based Interactions"

    # 8. COMMUNITY / PARTICIPATORY SYSTEMS
    elif any(x in text for x in ['community', 'participation', 'co-management', 'stakeholder', 'engagement']):
        return "Community-Based and Participatory Systems"

    # 9. GOVERNANCE (AGORA COM PRIORIDADE MAIS BAIXA ⚠️)
    elif any(x in text for x in ['governance', 'policy', 'institution', 'decision', 'management']):
        return "Governance and Institutional Dynamics"

    # 10. CONCEPTUAL (SES, POWER, NARRATIVES)
    elif any(x in text for x in ['ses', 'social-ecological', 'power', 'narrative']):
        return "Conceptual and Theoretical Interactions"

    # 11. NÃO ESPECIFICADO
    elif any(x in text for x in ['not mentioned', 'not explicit']):
        return "Unspecified Socio-Ecological Interactions"

    # 12. SISTEMAS COMPLEXOS / MULTI-SETORIAIS
    else:
        return "Integrated and Multi-Sector Socio-Ecological Systems"

# ---- Original cell 4 ----
df['Intervention Category'] = df['Type of social-ecological interaction'].apply(categorize_interaction)

# ---- Original cell 5 ----
import matplotlib.pyplot as plt

# Ordenar do menor para o maior (fica mais bonito)
freq_table = df['Intervention Category'].value_counts().reset_index()
freq_table.columns = ['Category', 'Count']
freq_table = freq_table.sort_values('Count')

# Criar gráfico
plt.figure(figsize=(10,7))
plt.barh(freq_table['Category'], freq_table['Count'])

# Labels
for i, v in enumerate(freq_table['Count']):
    plt.text(v, i, f' {v}', va='center')

plt.xlabel('Number of Articles')
plt.title('Socio-Ecological Interaction Types Across Island Studies')
plt.tight_layout()
plt.show()

# ---- Original cell 6 ----
# Mostrar conteúdo de cada categoria
grouped = (
    df.groupby('Intervention Category')['Type of social-ecological interaction']
    .apply(lambda x: sorted(set(x)))
    .reset_index()
)

# Mostrar sem cortar texto
pd.set_option('display.max_colwidth', None)

grouped
