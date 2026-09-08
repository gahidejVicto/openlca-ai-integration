# Inventaire ACV — Contreplaqué

Ce répertoire constitue le **cas pilote** de l'inventaire RECQ36 pour le contreplaqué.

Il sert à comparer une référence Ecoinvent avec les données de fabricants québécois afin d'identifier les écarts entre une donnée ACV générique/internationale et la réalité industrielle locale.

## 📁 Fichiers

| Fichier | Rôle |
|---|---|
| [`ecoinvent.md`](ecoinvent.md) | Documente le dataset Ecoinvent utilisé comme référence et ses limites de représentativité. |
| [`husky-plywood.md`](husky-plywood.md) | Fiche de collecte et de comparaison pour le fabricant québécois Husky Plywood. |
| [`columbia-forest-products-saint-casimir.md`](columbia-forest-products-saint-casimir.md) | Lot 1 — fiche Columbia Forest Products, contreplaqué, usine de Saint-Casimir. |
| [`tafisa-lac-megantic.md`](tafisa-lac-megantic.md) | Lot 1 — fiche Tafisa, panneau de particules, usine de Lac-Mégantic. |
| [`uniboard-val-dor.md`](uniboard-val-dor.md) | Lot 1 — fiche Uniboard, panneau de particules, usine de Val-d'Or. |
| [`uniboard-mont-laurier.md`](uniboard-mont-laurier.md) | Lot 2 — MDF/HDF, Uniboard, usine de Mont-Laurier. |
| [`arbec-osb-quebec.md`](arbec-osb-quebec.md) | Lot 2 — OSB, Arbec, usines de Shawinigan et Amos. |
| [`west-fraser-osb-chambord.md`](west-fraser-osb-chambord.md) | Lot 2 — OSB, West Fraser, usine de Chambord. |
| [`formica-saint-jean-sur-richelieu.md`](formica-saint-jean-sur-richelieu.md) | Lot 2 — HPL, Formica, installation de Saint-Jean-sur-Richelieu. |

## 🔄 Logique de travail

```text
Ecoinvent / openLCA
        ↓
ecoinvent.md
        ↓
Variables importantes à vérifier
        ↓
husky-plywood.md
        ↓
Recherche documentaire publique
        ↓
Données encore manquantes
        ↓
Questions ciblées au fabricant
        ↓
Comparaison Québec ↔ Ecoinvent
```

> [!IMPORTANT]
> L'objectif n'est pas de remplir immédiatement toutes les cases. Une valeur explicitement marquée `non trouvée`, `à demander` ou `non accessible` est une information utile au diagnostic.

## Règle de correspondance avec Ecoinvent

Une fiche fabricant documente uniquement les informations publiques
disponibles sur un fabricant, une usine et un produit. Elle doit distinguer
clairement les données propres au **produit**, à l'**usine**, à
l'**entreprise** et au **groupe**.

> [!IMPORTANT]
> **Une fiche fabricant n'est pas une preuve de correspondance avec
> Ecoinvent.** Elle ne doit entraîner ni la sélection automatique d'un proxy,
> ni celle d'un dataset Ecoinvent.

La fiche sert à préparer la comparaison et à identifier les données
manquantes. La correspondance finale ne peut être établie qu'après :

1. la caractérisation du dataset Ecoinvent ;
2. la définition du produit physique qu'il représente ;
3. la sélection d'un produit fabricant comparable ;
4. la comparaison des paramètres significatifs ;
5. la validation humaine.

En cas d'incertitude, inscrire explicitement :

> **Correspondance Ecoinvent non établie à ce stade.**

## 👀 Lire confortablement les fichiers Markdown dans Visual Studio Code

Visual Studio Code possède un lecteur Markdown intégré. Il n'est pas nécessaire d'installer un logiciel supplémentaire.

### Afficher l'aperçu rendu

Ouvrir un fichier `.md`, puis utiliser :

- **Windows/Linux : `Ctrl+Shift+V`** — ouvre l'aperçu Markdown ;
- **macOS : `Cmd+Shift+V`**.

Les titres, tableaux, listes, liens et blocs d'information sont alors affichés comme un document plutôt que comme du texte Markdown brut.

### Éditer et lire côte à côte

Pour travailler sur une fiche tout en voyant son rendu :

- **Windows/Linux : `Ctrl+K`, puis `V`** ;
- **macOS : `Cmd+K`, puis `V`**.

Le fichier source reste à gauche et l'aperçu apparaît à droite. C'est le mode recommandé pour ce projet.

> [!TIP]
> On peut aussi ouvrir la palette de commandes (`Ctrl+Shift+P`) et chercher **Markdown: Open Preview** ou **Markdown: Open Preview to the Side**.

## 🧭 Conventions de lecture

Les fiches utilisent les statuts suivants :

| Symbole | Signification |
|---|---|
| ✅ | Information confirmée et sourcée |
| 🔎 | Information à rechercher dans les sources publiques |
| ❓ | Information à demander au fabricant |
| 🧮 | Information à calculer à partir de données collectées |
| ⚠️ | Limite, incertitude ou information à vérifier |
| — | Non renseigné ou non applicable |

Les blocs visuels ont également un sens :

```markdown
> [!IMPORTANT]
> Information méthodologique importante.

> [!WARNING]
> Limitation ou risque d'interprétation.

> [!NOTE]
> Information complémentaire utile.
```

Visual Studio Code les affiche comme des encadrés dans l'aperçu Markdown.

## ✍️ Règles pour modifier une fiche

### 1. Toujours conserver la source

Une donnée fabricant ne doit pas devenir `✅ Confirmé` sans source identifiable.

Au minimum, conserver :

- le document ou la page utilisée ;
- l'organisme ou fabricant ;
- la date du document si disponible ;
- l'URL ou la référence ;
- la date de consultation.

### 2. Ne pas transformer une hypothèse en donnée

Une interprétation doit rester explicitement identifiée comme telle.

Par exemple :

```text
⚠️ À vérifier : la chaleur industrielle pourrait être produite à partir
 de biomasse.
```

ne doit pas devenir :

```text
✅ Source de chaleur : biomasse
```

sans source fabricant ou documentaire.

### 3. Ne pas déduire une géographie à partir d'un nom de processus

Si openLCA/MCP ne permet pas de désambiguïser un fournisseur Ecoinvent, conserver :

```text
⚠️ Géographie fournisseur : non résolue
```

plutôt que de choisir un processus homonyme.

### 4. Normaliser les valeurs pour la comparaison

Lorsque possible, les données fabricant doivent finalement être ramenées à la même unité que la référence Ecoinvent :

**1 m³ de contreplaqué en sortie d'usine.**

Une donnée annuelle peut être conservée telle quelle dans la source puis convertie si la production annuelle correspondante est connue.

### 5. Chercher avant de demander

Pour la fiche fabricant :

1. rechercher d'abord les informations publiques ;
2. documenter les sources trouvées ;
3. identifier les trous réellement importants ;
4. générer ensuite une courte liste de questions au fabricant.

Le questionnaire fabricant est donc **dérivé des données manquantes**, et non maintenu comme un document parallèle indépendant.

## 🧑‍🎓 Utilisation pour une recherche étudiante

Un étudiant peut travailler principalement dans la fiche fabricant.

Son travail documentaire consiste à rechercher notamment :

- site et fiches techniques du fabricant ;
- DEP/EPD ;
- ACV/LCA ;
- déclarations environnementales ;
- rapports de développement durable ;
- autorisations et informations environnementales publiques pertinentes ;
- certifications et documentation technique.

Il doit renseigner la **valeur**, le **statut** et la **source**, sans inventer les informations absentes.

## 🧪 Statut pilote

Cette structure est une **V1 expérimentale**.

Elle doit d'abord être testée sur le contreplaqué et Husky Plywood. Après la première collecte réelle, on évaluera :

- les champs réellement utiles ;
- les champs impossibles à obtenir ;
- les informations manquantes ;
- le niveau de détail approprié ;
- ce qui peut devenir un template réutilisable pour les autres matériaux.

> [!NOTE]
> Ne pas généraliser prématurément cette structure à tous les matériaux. Le cas pilote doit d'abord permettre de stabiliser la méthode RECQ36.
