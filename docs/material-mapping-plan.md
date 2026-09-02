# Plan d’implémentation — Mapping matériaux d’ébénisterie → ecoinvent

> **Statut : plan de travail de la branche `feat/material-mapping`**  
> Ce document sert de contrat de périmètre pour éviter de dériver vers des travaux de régionalisation, de reconstruction de datasets ou d’implémentation openLCA prématurés.

## Objectif de la branche

Automatiser la phase **V1 — Mapping ecoinvent** de la roadmap : à partir d’un matériau métier issu d’une nomenclature d’ébénisterie, identifier plusieurs datasets ecoinvent candidats, les inspecter, les filtrer, les classer et produire une recommandation explicable à valider par un humain.

Cette branche ne vise pas à régionaliser, modifier ou reconstruire des datasets ecoinvent. Elle prépare seulement la sélection documentée des meilleurs candidats.

## Entrée cible

Une entrée minimale doit pouvoir représenter :

- le nom métier du matériau ;
- la quantité ;
- l’unité d’origine ;
- le contexte géographique d’utilisation ;
- éventuellement des précisions utiles comme l’épaisseur, le revêtement, l’essence ou la formulation.

Exemple de référence :

```text
MDF non revêtu | 18 mm | 24,6 kg | Québec
```

## Pipeline cible

```text
Nomenclature meuble
    ↓
Matériau métier
    ↓
1. Normalisation / synonymes
    ↓
2. Recherche ecoinvent via openLCA
    ↓
3. Inspection des candidats
    ↓
4. Filtrage des faux positifs
    ↓
5. Classement
    ↓
6. Recommandation explicable
    ↓
7. Validation humaine
```

## 1. Normalisation du matériau

Transformer un terme métier en un ensemble de termes de recherche pertinents sans perdre le libellé original.

Exemples :

- `MDF` → `medium density fibreboard` ;
- `panneau de particules` → `particleboard` ;
- `contreplaqué` → `plywood`.

La normalisation doit rester traçable : le programme doit conserver le terme d’origine et les synonymes utilisés.

## 2. Recherche ecoinvent

Interroger la base active via `olca-ipc` et récupérer plusieurs processus candidats.

Le moteur ne doit pas s’arrêter au premier résultat lexical. Il doit accepter plusieurs termes de recherche et conserver assez de candidats pour permettre une comparaison raisonnable.

## 3. Inspection des candidats

Pour chaque candidat, récupérer au minimum :

- nom exact du processus ;
- UUID ;
- produit ou flux de référence (`qref`) ;
- unité de référence ;
- géographie / location ;
- type ou rôle du processus lorsque cela peut être déterminé (`market for`, production, traitement de déchet, etc.) ;
- description utile si elle aide à distinguer les candidats.

Le `qref` est une vérification centrale : un nom de processus proche du matériau recherché ne suffit pas si le produit de référence ne correspond pas au matériau à modéliser.

## 4. Filtrage des faux positifs

Écarter ou pénaliser les candidats manifestement incompatibles avec le besoin métier.

Exemple observé :

```text
medium density fibre board production, uncoated | residual wood, dry
```

Le nom évoque le MDF, mais si le produit de référence est `residual wood, dry`, ce processus ne doit pas être retenu comme représentation directe d’un achat de MDF.

Les règles de filtrage doivent être explicites et testables.

## 5. Classement des candidats

Le score ou classement doit considérer séparément plusieurs dimensions plutôt que d’utiliser uniquement la similarité textuelle.

Critères initiaux :

1. adéquation entre le matériau métier et le produit de référence ;
2. adéquation du type de processus au contexte d’utilisation ;
3. pertinence géographique ;
4. compatibilité de l’unité de référence avec la quantité disponible ;
5. qualité de la correspondance lexicale / sémantique ;
6. présence d’éléments ambigus ou de limites connues.

Le classement doit rester explicable. Chaque note importante doit pouvoir être reliée à une règle compréhensible.

## 6. Résultat attendu

Le programme doit produire une structure contenant au minimum :

- matériau métier d’origine ;
- termes de recherche utilisés ;
- candidat recommandé ;
- candidats alternatifs ;
- UUID ;
- `qref` ;
- unité ;
- géographie ;
- type de processus ;
- niveau de confiance ;
- justification ;
- limites ;
- statut de validation humaine.

Exemple conceptuel :

```text
Matériau : MDF non revêtu
Candidat recommandé : market for medium density fibreboard | RoW
Confiance : moyenne
Pourquoi : produit de référence correct, logique d’achat cohérente
Limites : géographie RoW, technologie sous-jacente à vérifier pour le Québec
Validation humaine : requise
```

## 7. Validation humaine obligatoire

La sortie du moteur est une recommandation, pas une validation ACV définitive.

L’utilisateur doit pouvoir :

- accepter le candidat ;
- choisir une alternative ;
- rejeter tous les candidats ;
- demander une analyse V2 plus détaillée.

La décision humaine doit être conservée afin d’éviter de refaire inutilement le même arbitrage.

## Hors périmètre de cette branche

Ne pas implémenter ici :

- modification ou suppression de datasets ecoinvent ;
- création automatique de datasets québécois ;
- remplacement automatique de providers ;
- régionalisation des paramètres ;
- création automatique de Product Systems ;
- calcul LCIA automatique à partir d’une nomenclature complète ;
- reconstruction d’un dataset jugé imparfait.

Ces travaux appartiennent aux phases V2 à V5 de la roadmap et ne doivent être engagés qu’après validation du mapping.

## Architecture technique visée

La logique métier de mapping doit vivre dans le dépôt `openlca-ai-integration`, principalement dans la couche Python.

Principe :

```text
Utilisateur / Claude
        ↓
logique de mapping Python
        ↓
olca-ipc
        ↓
openLCA
        ↓
ecoinvent local
```

Le MCP peut ensuite exposer cette logique à Claude, mais il ne doit pas contenir la logique métier principale ni devenir un moteur ACV parallèle.

## Ordre d’implémentation proposé

### Étape A — Contrats de données

Créer les structures représentant :

- un matériau d’entrée ;
- un candidat ecoinvent ;
- une recommandation de mapping.

### Étape B — Recherche brute

Créer une fonction Python simple qui interroge openLCA et retourne des processus candidats pour un terme donné.

### Étape C — Inspection

Enrichir chaque candidat avec `qref`, unité, géographie et métadonnées nécessaires.

### Étape D — Filtrage

Implémenter les premières règles déterministes d’exclusion ou de pénalisation.

### Étape E — Classement

Introduire un score explicable fondé sur les critères définis plus haut.

### Étape F — Cas de référence MDF

Valider le pipeline sur :

```text
MDF non revêtu | 18 mm | 24,6 kg | Québec
```

Le pipeline doit retrouver les candidats ecoinvent pertinents, rejeter les faux positifs liés au `qref` et fournir une recommandation argumentée.

### Étape G — Généralisation

Tester ensuite au minimum :

- panneau de particules ;
- contreplaqué ;
- bois massif séché ;
- un matériau hors panneaux afin de vérifier que le moteur ne soit pas sur-spécialisé.

## Critères de fin de branche

La branche peut être considérée comme terminée lorsque :

- les contrats de données sont stables ;
- la recherche et l’inspection fonctionnent sur ecoinvent via openLCA ;
- les faux positifs évidents peuvent être détectés ;
- le classement est explicable ;
- le cas MDF est couvert par des tests ou un script reproductible ;
- la validation humaine est prévue dans le modèle de sortie ;
- la documentation décrit les limites connues ;
- aucune donnée ecoinvent propriétaire n’est committée dans Git.

## Rappel de méthode

Cette branche réalise **V1 — Mapping ecoinvent**.

La séquence à respecter reste :

```text
V0 Inventaire métier
    ↓
V1 Mapping ecoinvent          ← branche actuelle
    ↓
V2 Inventaire détaillé
    ↓
V3 Analyse Québec
    ↓
V4 Implémentation
    ↓
V5 Validation
```

Si le développement commence à dériver vers la modification de datasets, la régionalisation ou la construction d’un modèle ACV complet, revenir à ce document avant de poursuivre.
