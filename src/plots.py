import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


### Plot pour Politique
df_politique_new = pd.read_csv(
    r"C:\Users\Axel\Desktop\Data_Project\OC_Project_9\data\processed\df_politique_new.csv"
)
region_counts = df_politique_new["Region"].value_counts()
sns.set(style="whitegrid")
ax = sns.countplot(
    data=df_politique_new,
    y="Region",
    order=region_counts.index,
    hue="Region",
    edgecolor="black",
    palette="pastel",
)
# Enlever les labels des axes x et y
ax.set_xlabel("")
ax.set_ylabel("")

plt.tight_layout()
plt.title("Nombre pays stable par région")
plt.show()


### Plot pour Economique
mean_gni_by_region

# Création du barplot horizontal
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    data=mean_gni_by_region,
    x="Max. Ny Gnp Pcap Cd",  # GNI sur l'axe x
    y="Region",  # Region sur l'axe y
    edgecolor="black",
    palette="pastel",
)

# Ajouter des lignes verticales pour les seuils
thresholds = {
    "Upper Middle / High": (12055, "green"),
    "Lower Middle / Upper Middle": (3895, "blue"),
    "Low / Lower Middle": (995, "orange"),
}

# Tracer les lignes de seuils avec différentes couleurs
for label, (threshold, color) in thresholds.items():
    ax.axvline(x=threshold, color=color, linestyle="--", label=f"Threshold: {label}")

# Ajouter des labels et une légende
ax.set_xlabel("Mean GNI per Capita")
ax.set_ylabel("")
ax.legend(title="Thresholds")

# Afficher le titre et le graphique
plt.title("Mean GNI per Capita by Region with Thresholds")
plt.show()

### Plot pour Économique n°2

# Trier df_merged par 'Valeur' et sélectionner les 20 premiers pays dans le barplot
plt.figure(figsize=(10, 6))
sns.barplot(
    x="Valeur",
    y="Country",
    data=df_merged.sort_values("Valeur", ascending=False).head(20),
    palette="pastel",
)

# Ajouter un titre et des labels
plt.title("Top 20 des pays par Valeur", fontsize=14)
plt.xlabel("Valeur")
plt.ylabel("Pays")

# Afficher le graphique
plt.tight_layout()
plt.show()
