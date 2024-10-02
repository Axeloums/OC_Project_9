import pandas as pd

### Analyse PESTEL

### P - Politique :
### data/raw/political_stability.csv

df_politique = pd.read_csv(
    r"C:\Users\Axel\Desktop\Data_Project\OC_Project_9\data\raw\political_stability.csv"
)
df_politique

country_to_region = {
    "Afghanistan": "South Asia",
    "Albania": "Europe and Central Asia",
    "Algeria": "Middle East and North Africa",
    "American Samoa": "East Asia and Pacific",
    "Andorra": "Europe and Central Asia",
    "Angola": "Sub-Saharan Africa",
    "Antigua and Barbuda": "Latin America & the Caribbean",
    "Argentina": "Latin America & the Caribbean",
    "Armenia": "Europe and Central Asia",
    "Australia": "East Asia and Pacific",
    "Austria": "Europe and Central Asia",
    "Azerbaijan": "Europe and Central Asia",
    "Bahamas": "Latin America & the Caribbean",
    "Bahrain": "Middle East and North Africa",
    "Bangladesh": "South Asia",
    "Barbados": "Latin America & the Caribbean",
    "Belarus": "Europe and Central Asia",
    "Belgium": "Europe and Central Asia",
    "Belize": "Latin America & the Caribbean",
    "Benin": "Sub-Saharan Africa",
    "Bermuda": "Latin America & the Caribbean",
    "Bhutan": "South Asia",
    "Bolivia (Plurinational State of)": "Latin America & the Caribbean",
    "Bosnia and Herzegovina": "Europe and Central Asia",
    "Botswana": "Sub-Saharan Africa",
    "Brazil": "Latin America & the Caribbean",
    "Brunei Darussalam": "East Asia and Pacific",
    "Bulgaria": "Europe and Central Asia",
    "Burkina Faso": "Sub-Saharan Africa",
    "Burundi": "Sub-Saharan Africa",
    "Cabo Verde": "Sub-Saharan Africa",
    "Cambodia": "East Asia and Pacific",
    "Cameroon": "Sub-Saharan Africa",
    "Canada": "North America",
    "Central African Republic": "Sub-Saharan Africa",
    "Chad": "Sub-Saharan Africa",
    "Chile": "Latin America & the Caribbean",
    "China": "East Asia and Pacific",
    "China, mainland": "East Asia and Pacific",
    "China, Hong Kong SAR": "East Asia and Pacific",
    "China, Macao SAR": "East Asia and Pacific",
    "China, Taiwan Province of": "East Asia and Pacific",
    "Colombia": "Latin America & the Caribbean",
    "Comoros": "Sub-Saharan Africa",
    "Congo": "Sub-Saharan Africa",
    "Costa Rica": "Latin America & the Caribbean",
    "Côte d'Ivoire": "Sub-Saharan Africa",
    "Croatia": "Europe and Central Asia",
    "Cuba": "Latin America & the Caribbean",
    "Cyprus": "Europe and Central Asia",
    "Czechia": "Europe and Central Asia",
    "Democratic People's Republic of Korea": "East Asia and Pacific",
    "Democratic Republic of the Congo": "Sub-Saharan Africa",
    "Denmark": "Europe and Central Asia",
    "Djibouti": "Sub-Saharan Africa",
    "Dominica": "Latin America & the Caribbean",
    "Dominican Republic": "Latin America & the Caribbean",
    "Ecuador": "Latin America & the Caribbean",
    "Egypt": "Middle East and North Africa",
    "El Salvador": "Latin America & the Caribbean",
    "Equatorial Guinea": "Sub-Saharan Africa",
    "Eritrea": "Sub-Saharan Africa",
    "Estonia": "Europe and Central Asia",
    "Eswatini": "Sub-Saharan Africa",
    "Ethiopia": "Sub-Saharan Africa",
    "Fiji": "East Asia and Pacific",
    "Finland": "Europe and Central Asia",
    "France": "Europe and Central Asia",
    "Gabon": "Sub-Saharan Africa",
    "Gambia": "Sub-Saharan Africa",
    "Georgia": "Europe and Central Asia",
    "Germany": "Europe and Central Asia",
    "Ghana": "Sub-Saharan Africa",
    "Greece": "Europe and Central Asia",
    "Greenland": "Europe and Central Asia",
    "Grenada": "Latin America & the Caribbean",
    "Guatemala": "Latin America & the Caribbean",
    "Guinea": "Sub-Saharan Africa",
    "Guinea-Bissau": "Sub-Saharan Africa",
    "Guyana": "Latin America & the Caribbean",
    "Haiti": "Latin America & the Caribbean",
    "Honduras": "Latin America & the Caribbean",
    "Hungary": "Europe and Central Asia",
    "Iceland": "Europe and Central Asia",
    "India": "South Asia",
    "Indonesia": "East Asia and Pacific",
    "Iran (Islamic Republic of)": "Middle East and North Africa",
    "Iraq": "Middle East and North Africa",
    "Ireland": "Europe and Central Asia",
    "Israel": "Middle East and North Africa",
    "Italy": "Europe and Central Asia",
    "Jamaica": "Latin America & the Caribbean",
    "Japan": "East Asia and Pacific",
    "Jordan": "Middle East and North Africa",
    "Kazakhstan": "Europe and Central Asia",
    "Kenya": "Sub-Saharan Africa",
    "Kiribati": "East Asia and Pacific",
    "Kuwait": "Middle East and North Africa",
    "Kyrgyzstan": "Europe and Central Asia",
    "Lao People's Democratic Republic": "East Asia and Pacific",
    "Latvia": "Europe and Central Asia",
    "Lebanon": "Middle East and North Africa",
    "Lesotho": "Sub-Saharan Africa",
    "Liberia": "Sub-Saharan Africa",
    "Libya": "Middle East and North Africa",
    "Lithuania": "Europe and Central Asia",
    "Luxembourg": "Europe and Central Asia",
    "Madagascar": "Sub-Saharan Africa",
    "Malawi": "Sub-Saharan Africa",
    "Malaysia": "East Asia and Pacific",
    "Maldives": "South Asia",
    "Mali": "Sub-Saharan Africa",
    "Malta": "Europe and Central Asia",
    "Marshall Islands": "East Asia and Pacific",
    "Mauritania": "Sub-Saharan Africa",
    "Mauritius": "Sub-Saharan Africa",
    "Mexico": "Latin America & the Caribbean",
    "Micronesia (Federated States of)": "East Asia and Pacific",
    "Mongolia": "East Asia and Pacific",
    "Montenegro": "Europe and Central Asia",
    "Morocco": "Middle East and North Africa",
    "Mozambique": "Sub-Saharan Africa",
    "Myanmar": "East Asia and Pacific",
    "Namibia": "Sub-Saharan Africa",
    "Nauru": "East Asia and Pacific",
    "Nepal": "South Asia",
    "Netherlands (Kingdom of the)": "Europe and Central Asia",
    "New Zealand": "East Asia and Pacific",
    "Nicaragua": "Latin America & the Caribbean",
    "Niger": "Sub-Saharan Africa",
    "Nigeria": "Sub-Saharan Africa",
    "North Macedonia": "Europe and Central Asia",
    "Norway": "Europe and Central Asia",
    "Oman": "Middle East and North Africa",
    "Pakistan": "South Asia",
    "Palau": "East Asia and Pacific",
    "Palestine": "Middle East and North Africa",
    "Panama": "Latin America & the Caribbean",
    "Papua New Guinea": "East Asia and Pacific",
    "Paraguay": "Latin America & the Caribbean",
    "Peru": "Latin America & the Caribbean",
    "Philippines": "East Asia and Pacific",
    "Poland": "Europe and Central Asia",
    "Portugal": "Europe and Central Asia",
    "Puerto Rico": "Latin America & the Caribbean",
    "Qatar": "Middle East and North Africa",
    "Republic of Korea": "East Asia and Pacific",
    "Republic of Moldova": "Europe and Central Asia",
    "Romania": "Europe and Central Asia",
    "Russian Federation": "Europe and Central Asia",
    "Rwanda": "Sub-Saharan Africa",
    "Saint Kitts and Nevis": "Latin America & the Caribbean",
    "Saint Lucia": "Latin America & the Caribbean",
    "Saint Vincent and the Grenadines": "Latin America & the Caribbean",
    "Samoa": "East Asia and Pacific",
    "Sao Tome and Principe": "Sub-Saharan Africa",
    "Saudi Arabia": "Middle East and North Africa",
    "Senegal": "Sub-Saharan Africa",
    "Serbia": "Europe and Central Asia",
    "Seychelles": "Sub-Saharan Africa",
    "Sierra Leone": "Sub-Saharan Africa",
    "Singapore": "East Asia and Pacific",
    "Slovakia": "Europe and Central Asia",
    "Slovenia": "Europe and Central Asia",
    "Solomon Islands": "East Asia and Pacific",
    "Somalia": "Sub-Saharan Africa",
    "South Africa": "Sub-Saharan Africa",
    "South Sudan": "Sub-Saharan Africa",
    "Spain": "Europe and Central Asia",
    "Sri Lanka": "South Asia",
    "Sudan": "Sub-Saharan Africa",
    "Suriname": "Latin America & the Caribbean",
    "Sweden": "Europe and Central Asia",
    "Switzerland": "Europe and Central Asia",
    "Syrian Arab Republic": "Middle East and North Africa",
    "Tajikistan": "Europe and Central Asia",
    "Thailand": "East Asia and Pacific",
    "Timor-Leste": "East Asia and Pacific",
    "Togo": "Sub-Saharan Africa",
    "Tonga": "East Asia and Pacific",
    "Trinidad and Tobago": "Latin America & the Caribbean",
    "Tunisia": "Middle East and North Africa",
    "Türkiye": "Europe and Central Asia",
    "Turkmenistan": "Europe and Central Asia",
    "Tuvalu": "East Asia and Pacific",
    "Uganda": "Sub-Saharan Africa",
    "Ukraine": "Europe and Central Asia",
    "United Arab Emirates": "Middle East and North Africa",
    "United Kingdom of Great Britain and Northern Ireland": "Europe and Central Asia",
    "United Republic of Tanzania": "Sub-Saharan Africa",
    "United States of America": "North America",
    "Uruguay": "Latin America & the Caribbean",
    "Uzbekistan": "Europe and Central Asia",
    "Vanuatu": "East Asia and Pacific",
    "Venezuela (Bolivarian Republic of)": "Latin America & the Caribbean",
    "Viet Nam": "East Asia and Pacific",
    "Yemen": "Middle East and North Africa",
    "Zambia": "Sub-Saharan Africa",
    "Zimbabwe": "Sub-Saharan Africa",
    "Vietnam": "Viet Nam",
    "St. Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "United States": "United States of America",
    "Tanzania": "United Republic of Tanzania",
    "Turkey": "Türkiye",
    "Slovak Republic": "Slovakia",
    "West Bank and Gaza": "Palestine",
    "Netherlands": "Netherlands (Kingdom of the)",
    "Macedonia, FYR": "North Macedonia",
    "Moldova": "Republic of Moldova",
    "St. Lucia": "Saint Lucia",
    "Lao PDR": "Lao People's Democratic Republic",
    "Korea, Rep.": "Republic of Korea",  # Peut aussi être "South Korea"
    "St. Kitts and Nevis": "Saint Kitts and Nevis",
    "Kyrgyz Republic": "Kyrgyzstan",
    "Iran, Islamic Rep.": "Iran (Islamic Republic of)",
    "Hong Kong SAR, China": "China, Hong Kong SAR",
    "Gambia, The": "Gambia",
    "United Kingdom": "United Kingdom of Great Britain and Northern Ireland",
    "Micronesia, Fed. Sts.": "Micronesia (Federated States of)",
    "Egypt, Arab Rep.": "Egypt",
    "Czech Republic": "Czechia",
    "Congo, Rep.": "Congo",
    "Congo, Dem. Rep.": "Democratic Republic of the Congo",
    "Cote d'Ivoire": "Côte d'Ivoire",  # Assure que l'accent est inclus
    "Bolivia": "Bolivia (Plurinational State of)",
    "Bahamas, The": "Bahamas",
}

df_politique["Region"] = df_politique["Area"].map(country_to_region)

df_politique = df_politique[["Area", "Value", "Region"]]
df_politique.Value.median()  # -> 0.025
df_politique.Value.mean()  # -0.068

## Premier tri
df_politique_new = df_politique[df_politique["Value"] >= 0]
df_politique_new.to_csv(
    r"C:\Users\Axel\Desktop\Data_Project\OC_Project_9\data\processed\df_politique_new.csv",
    index=False,
)
df_politique_new

### E - Economique
### Calcul du GNI par hab
df_gni = pd.read_csv(
    r"C:\Users\Axel\Desktop\Data_Project\OC_Project_9\data\raw\GNI Per Capita & Income Thresholds_data.csv",
    sep=";",
)

df_gni = df_gni[df_gni["Year"] == 2017]


### appliquer les Threshold
def classify_gni(value):
    if value >= 12055:
        return "Upper Middle / High"
    elif value >= 3895:
        return "Lower Middle / Upper Middle"
    else:
        return "Low / Lower Middle"


df_gni["Class"] = df_gni["Max. Ny Gnp Pcap Cd"].apply(classify_gni)
df_gni = df_gni.dropna(subset=["Countryname", "Max. Ny Gnp Pcap Cd"])
df_gni = df_gni[["Countryname", "Max. Ny Gnp Pcap Cd", "Class"]]

df_gni["Region"] = df_gni["Countryname"].map(country_to_region)
nan_regions = df_gni[df_gni["Region"].isna()]
nan_regions

# Liste des pays à remplacer
country_name_mapping = {
    "Vietnam": "Viet Nam",
    "St. Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "United States": "United States of America",
    "Tanzania": "United Republic of Tanzania",
    "Turkey": "Türkiye",
    "Slovak Republic": "Slovakia",
    "West Bank and Gaza": "Palestine",
    "Netherlands": "Netherlands (Kingdom of the)",
    "Macedonia, FYR": "North Macedonia",
    "Moldova": "Republic of Moldova",
    "St. Lucia": "Saint Lucia",
    "Lao PDR": "Lao People's Democratic Republic",
    "Korea, Rep.": "Republic of Korea",  # Peut aussi être "South Korea"
    "St. Kitts and Nevis": "Saint Kitts and Nevis",
    "Kyrgyz Republic": "Kyrgyzstan",
    "Iran, Islamic Rep.": "Iran (Islamic Republic of)",
    "Hong Kong SAR, China": "China, Hong Kong SAR",
    "Gambia, The": "Gambia",
    "United Kingdom": "United Kingdom of Great Britain and Northern Ireland",
    "Micronesia, Fed. Sts.": "Micronesia (Federated States of)",
    "Egypt, Arab Rep.": "Egypt",
    "Czech Republic": "Czechia",
    "Congo, Rep.": "Congo",
    "Congo, Dem. Rep.": "Democratic Republic of the Congo",
    "Cote d'Ivoire": "Côte d'Ivoire",  # Assure que l'accent est inclus
    "Bolivia": "Bolivia (Plurinational State of)",
    "Bahamas, The": "Bahamas",
}

df_gni["Countryname"] = df_gni["Countryname"].replace(country_name_mapping)
df_gni["Region"] = df_gni["Countryname"].map(country_to_region)

mean_gni_by_region = (
    df_gni.groupby("Region")["Max. Ny Gnp Pcap Cd"]
    .mean()
    .sort_values(ascending=False)
    .round()
    .reset_index()
)
mean_gni_by_region

### DisponibiliteAlimentaire_2017.csv

### Focus sur les exportations

df_main = pd.read_csv(
    r"C:\Users\Axel\Desktop\Data_Project\OC_Project_9\data\raw\DisponibiliteAlimentaire_2017.csv"
)
df_main.Élément.unique

df_main_export = df_main[df_main["Élément"] == "Exportations - Quantité"]
df_main_export = df_main_export[
    (df_main_export["Produit"] == "Viande de Volailles")
    & (df_main_export["Valeur"] > 0)
]
df_main_export = df_main_export[["Code zone", "Valeur", "Unité"]]
df_main_export

df_table_correspondance = pd.read_csv(
    r"C:\Users\Axel\Desktop\Data_Project\OC_Project_9\data\raw\table_correspondance_pays.csv"
)
df_table_correspondance = df_table_correspondance[["Country Code", "Country"]]
df_table_correspondance = df_table_correspondance.drop_duplicates(
    subset=["Country Code"]
)
df_table_correspondance

df_merged = pd.merge(
    df_main_export,
    df_table_correspondance,
    left_on="Code zone",
    right_on="Country Code",
    how="left",
)
df_merged["Region"] = df_merged["Country"].map(country_to_region)
df_merged.sort_values(by="Valeur", ascending=False)

df_export_region = (
    df_merged.groupby("Region")["Valeur"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
df_export_region

### Socio Culturel

### Faire avec la colonne Disponibilité alimentaire en quantité (kg/personne/an)
