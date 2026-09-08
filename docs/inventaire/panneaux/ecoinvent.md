# Contreplaqué — Référence Ecoinvent Canada, Quebec

> [!IMPORTANT]
> **Statut du dataset : à auditer pour sa représentativité québécoise.**  
> Le processus est localisé `Canada, Quebec`, mais sa documentation indique qu'il a été créé comme copie du dataset européen et que les données industrielles sont basées sur un échantillon de production allemande.

## 📌 Résumé

| Élément | Valeur |
|---|---|
| Matériau | Contreplaqué (*plywood*) |
| Famille | Panneaux à base de bois |
| Type de fiche | Référence Ecoinvent |
| Unité de comparaison | **1 m³ de contreplaqué en sortie d'usine** |
| Localisation déclarée | **Canada, Quebec** |
| Représentativité industrielle québécoise | ⚠️ **À vérifier** |

## 1. Dataset étudié

| Champ | Valeur |
|---|---|
| Processus | `plywood production \| plywood \| Cutoff, U` |
| UUID | `5538194d-92b2-3020-bb3e-fbc59cb71248` |
| Produit de référence | `plywood` |
| Quantité de référence | 1 |
| Unité | m³ |
| Catégorie | `C:Manufacturing/16/162/1621` — Manufacture de panneaux à base de bois |
| Modèle système | Non accessible comme champ structuré ; suffixe `Cutoff, U` |
| Version Ecoinvent | Probablement **3.11** d'après l'URL de documentation — à confirmer |
| Période temporelle | Non accessible avec l'outil actuel |
| Infrastructure | Incluse ; décrite comme une estimation grossière |

## 2. Provenance et représentativité

### ✅ Faits établis dans la documentation Ecoinvent

- Le dataset représente nominalement une production de contreplaqué au Québec.
- Il a été créé comme **copie du dataset local correspondant pour l'Europe**.
- Les données sont basées sur **un échantillon de production allemande**.
- Le procédé est générique : il ne distingue pas les contreplaqués selon le nombre ou l'épaisseur des plis.
- L'infrastructure est décrite comme une **estimation grossière**.

> [!IMPORTANT]
> **Règle méthodologique pour RECQ36**  
> Une localisation Ecoinvent `Canada, Quebec` ne suffit pas à démontrer que les coefficients technologiques du procédé représentent une usine québécoise réelle.

### 🔎 Question du diagnostic

Déterminer quels paramètres de ce procédé générique diffèrent des pratiques des fabricants québécois et lesquels devraient être documentés, adaptés ou régionalisés.

## 3. Matières premières et énergie

Valeurs rapportées à **1 m³ de contreplaqué**.

### 🌲 Bois

| Paramètre | Valeur Ecoinvent |
|---|---:|
| Intrant | Grumes feuillues pour sciage/déroulage |
| Quantité | **2,2057 m³/m³** |
| Fournisseur nominal | `market for sawlog and veneer log, hardwood...` |
| Géographie du fournisseur | ⚠️ Non résolue avec l'interface MCP actuelle |

**À confronter au Québec :** essences, provenance du bois, forme de matière entrante et rendement grumes → produit fini.

### 🧪 Résine / adhésif

| Paramètre | Valeur Ecoinvent |
|---|---:|
| Type | Résine urée-formaldéhyde |
| Quantité | **87,073 kg/m³** |
| Fournisseur nominal | `market for urea formaldehyde resin` |
| Géographie | Non vérifiée |

### ⚡ Électricité

| Paramètre | Valeur Ecoinvent |
|---|---:|
| Niveau | Moyenne tension |
| Consommation | **519,338 kWh/m³** |
| Fournisseur nominal | `market for electricity, medium voltage` |
| Géographie | ⚠️ Non résolue avec l'interface MCP actuelle |

### 🔥 Chaleur et combustibles

| Intrant | Quantité | Unité |
|---|---:|---|
| Chaleur industrielle — fioul léger | **53,260** | MJ/m³ |
| Diesel — engin de chantier | **3,497** | MJ/m³ |

> [!NOTE]
> La pertinence du fioul léger comme source de chaleur doit être confrontée aux pratiques des fabricants québécois. Il ne faut pas supposer une autre source énergétique sans données fabricant.

### 💧 Eau et autres intrants

| Intrant | Quantité | Unité |
|---|---:|---|
| Eau du robinet | 120,688 | kg/m³ |
| Eau de refroidissement | 10,340 | m³/m³ |
| Huile lubrifiante | 0,2354 | kg/m³ |
| Acier faiblement allié | 0,1128 | kg/m³ |
| Caoutchouc synthétique | 0,0214 | kg/m³ |

## 4. Sorties et résidus

| Sortie | Quantité | Unité |
|---|---:|---|
| **Contreplaqué — produit de référence** | **1** | **m³** |
| Eaux usées de production | 0,08592 | m³ |
| Cendres de bois | 5,6277 | kg |
| Déchets municipaux | 0,4814 | kg |
| Déchets d'acier | 0,11282 | kg |
| Huile minérale usée | 0,23536 | kg |
| Caoutchouc usagé | 0,02140 | kg |

Aucun coproduit n'a été identifié dans le processus interrogé.

## 5. Émissions directes structurantes

> [!NOTE]
> Ces valeurs sont des **émissions directes du procédé**. Elles ne doivent pas être confondues avec les impacts indirects de la production d'électricité, de résine ou des autres fournisseurs technosphère.

| Émission directe | Quantité | Unité |
|---|---:|---|
| CO₂ non fossile | 1204,325 | kg/m³ |
| NOx | 2,53246 | kg/m³ |
| CO non fossile | 2,25108 | kg/m³ |
| Particules < 2,5 µm | 0,28138 | kg/m³ |
| Formaldéhyde | 0,13179 | kg/m³ |
| COVNM | 0,03939 | kg/m³ |
| SO₂ | 0,02814 | kg/m³ |

Des flux traces supplémentaires existent (métaux lourds, composés organiques, etc.). Ils pourront être documentés si leur analyse devient nécessaire.

## 6. Paramètres prioritaires à confronter aux fabricants québécois

| Priorité | Paramètre | Référence Ecoinvent | Question principale |
|---|---|---|---|
| 🔴 | Définition du produit | Contreplaqué générique | Quel produit réel compare-t-on ? |
| 🔴 | Essence / provenance du bois | Feuillus ; fournisseur non résolu | Quelles essences et quelles provenances ? |
| 🔴 | Rendement matière | 2,2057 m³ de grumes / m³ produit | Quel est le rendement industriel réel ? |
| 🔴 | Résine | UF — 87,073 kg/m³ | Quel liant et quelle quantité ? |
| 🔴 | Électricité | 519,338 kWh/m³ | Quelle consommation réelle ? |
| 🔴 | Chaleur | 53,26 MJ/m³ au fioul léger | Quelle quantité et quelle source réelle ? |
| 🟠 | Eau | 120,688 kg + 10,34 m³ | Quelle consommation réelle ? |
| 🟠 | Émissions | Voir section 5 | Quelles mesures industrielles sont disponibles ? |
| 🟠 | Déchets / résidus | Voir section 4 | Quels volumes et quelles valorisations ? |
| 🟠 | Transport amont | Non explicite au niveau du procédé | Comment le bois et la résine sont-ils approvisionnés ? |

## 7. Limites et points ouverts

> [!WARNING]
> **Fournisseurs non désambiguïsés**  
> Pour certains échanges, MCP retourne le nom textuel du fournisseur mais pas son UUID ni sa géographie. Plusieurs processus homonymes peuvent exister. Aucune géographie ne doit donc être déduite d'une recherche par nom.

- ⚠️ Fournisseur/géographie exacts du marché de grumes : **non accessibles avec l'interface MCP actuelle**.
- ⚠️ Fournisseur/géographie exacts de l'électricité : **non accessibles avec l'interface MCP actuelle**.
- 🔎 Version exacte Ecoinvent : à confirmer.
- 🔎 Période temporelle : non accessible actuellement.
- 🔎 Représentativité des coefficients technologiques pour le Québec : à tester.
- 🔎 Pertinence de l'UF et du fioul léger : à confronter aux fabricants.

## 8. Traçabilité

| Élément | Information |
|---|---|
| Source principale | Ecoinvent via openLCA |
| Mode d'accès | Claude → MCP → openLCA |
| Mode d'interrogation | Lecture seule |
| UUID | `5538194d-92b2-3020-bb3e-fbc59cb71248` |
| Date d'interrogation | 2026-09-08 |
| Outils utilisés | `process_details`, `search_processes` |
| Modification openLCA | **Aucune** |

---

## Journal des mises à jour

| Date | Modification |
|---|---|
| 2026-09-08 | Création de la fiche pilote à partir de l'interrogation openLCA/Ecoinvent. |
