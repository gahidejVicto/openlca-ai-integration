# Référentiel des matériaux — Ébénisterie

> **Statut : V0 — inventaire métier initial**  
> Ce document est volontairement évolutif. Il sert d'abord à définir les matériaux à couvrir, avant de sélectionner, analyser puis éventuellement régionaliser les datasets ACV.

## Rôle de cet index

Ce document répond à la question : **« Quels matériaux d'ébénisterie devons-nous couvrir ? »** Il constitue l'inventaire métier progressif des matériaux utilisés en ébénisterie et dans la fabrication de meubles au Québec.

Il conserve les familles, priorités, statuts et datasets candidats déjà identifiés, sans détailler tous leurs Inputs/Outputs. Les analyses dataset par dataset sont regroupées dans les [fiches d'inventaire détaillé](inventaire/README.md). Elles distinguent le lieu du procédé, la géographie des intrants, les paramètres quantitatifs, l'origine des valeurs et les données québécoises restant à valider.

Il sert de point de départ pour :

- identifier les matériaux prioritaires ;
- associer chaque matériau à un ou plusieurs datasets ecoinvent 3.11 candidats ;
- orienter les analyses détaillées et la recherche de données québécoises ;
- suivre les décisions sans anticiper l'implémentation dans openLCA.

La démarche est volontairement itérative : **inventaire métier → identification des datasets ecoinvent candidats → inventaire détaillé du dataset → identification des maillons faibles → recherche et validation de données québécoises → décision de conserver, adapter ou reconstruire → future implémentation dans openLCA**.

## Légende

### Priorités

| Priorité | Signification |
|---|---|
| **P1** | Incontournable ou très fréquent dans la fabrication de meubles et d'éléments d'ébénisterie |
| **P2** | Fréquent, mais dépend davantage du produit ou du procédé |
| **P3** | Spécialisé ou à traiter dans une itération ultérieure |

### Statuts

- **À rechercher** — aucun dataset candidat n'est encore retenu.
- **Dataset candidat identifié** — un ou plusieurs candidats ont été repérés, sans validation complète.
- **À analyser** — le candidat doit être étudié (technologie, géographie, intrants, etc.).
- **À régionaliser** — un écart significatif avec le contexte québécois a été identifié.
- **Dataset Québec créé** — une adaptation ou reconstruction québécoise existe.
- **Validé** — le dataset et ses hypothèses ont été vérifiés et documentés.

---

## 1. Panneaux

| Priorité | Matériau | Dataset ecoinvent candidat | Géographie | Statut | Notes |
|---|---|---|---|---|---|
| P1 | Panneau de particules brut | `particleboard production, uncoated, average glue mix` | RER / RoW | Dataset candidat identifié | Comparer avec la production québécoise |
| P1 | MDF | `medium density fibreboard production, uncoated` | RER / RoW | Dataset candidat identifié | |
| P2 | HDF | — | — | À rechercher - premiere passe pas trouvé | |
| P1 | Contreplaqué | `plywood production, plywood` | CA-QC | À analyser | [Fiche pilote CA-QC](inventaire/panneaux/plywood-ca-qc.md) ; la géographie du procédé ne valide pas tous les intrants et paramètres |
| P2 | OSB | — | — | À rechercher | |



## 2. Panneaux revêtus et surfaces

| Priorité | Matériau | Dataset ecoinvent candidat | Géographie | Statut | Notes |
|---|---|---|---|---|---|
| P1 | Panneau de particules mélaminé (TFL) | À construire | — | À analyser | Probablement panneau + papier imprégné + pressage |
| P1 | MDF mélaminé | À construire | — | À analyser | |
| P1 | Stratifié HPL | — | — | À rechercher | |
| P1 | Placage de bois | — | — | À rechercher | |
| P2 | Papier imprégné mélamine | `melamine impregnated paper production` | RER / RoW | Dataset candidat identifié | |

> **Point méthodologique :** un terme métier comme « panneau mélaminé » ne correspond pas nécessairement à un dataset unique. Il peut devoir être construit à partir d'un panneau support, d'un papier décoratif imprégné de résine mélamine et d'une étape de pressage.

## 3. Bois massif

| Priorité | Matériau | Dataset ecoinvent candidat | Géographie | Statut | Notes |
|---|---|---|---|---|---|
| P1 | Bois feuillu séché | `sawnwood production, hardwood, dried` | CH / Europe / RoW | À analyser | Humidité et rabotage à préciser |
| P1 | Bois résineux séché | — | — | À rechercher | |
| P2 | Bois feuillu raboté | — | — | À rechercher | |
| P2 | Bois résineux raboté | — | — | À rechercher | |

## 4. Adhésifs

| Priorité | Matériau | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Urée-formaldéhyde (UF) | — | À rechercher | Très pertinent pour les panneaux |
| P1 | PVAc | — | À rechercher | |
| P1 | Polyuréthane (PUR) | — | À rechercher | |
| P2 | EVA / Hot-melt | — | À rechercher | |
| P2 | Mélamine-urée-formaldéhyde (MUF) | `melamine urea formaldehyde adhesive production` | Dataset candidat identifié | |

## 5. Produits de finition

| Priorité | Matériau | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Vernis / laque | — | À rechercher | Distinguer les technologies et formulations |
| P1 | Peinture | — | À rechercher | |
| P2 | Teinture | — | À rechercher | |
| P2 | Solvants | — | À rechercher | |

## 6. Métaux et quincaillerie

| Priorité | Matériau | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Acier | — | À rechercher | |
| P1 | Aluminium | — | À rechercher | |
| P2 | Zinc / acier galvanisé | — | À rechercher | |
| P2 | Quincaillerie | — | À analyser | Modélisation possiblement par composition massique |

## 7. Plastiques

| Priorité | Matériau | Dataset ecoinvent candidat | Statut |
|---|---|---|---|
| P1 | ABS | — | À rechercher |
| P2 | Polypropylène (PP) | — | À rechercher |
| P2 | Polyéthylène (PE) | — | À rechercher |
| P2 | PVC | — | À rechercher |

## 8. Emballages

| Priorité | Matériau | Dataset ecoinvent candidat | Statut |
|---|---|---|---|
| P1 | Carton ondulé | — | À rechercher |
| P1 | Film PE | — | À rechercher |
| P2 | Palette de bois | — | À rechercher |

---

# Données transversales à régionaliser pour le Québec

Ces éléments sont volontairement séparés de la liste des matériaux. Ils représentent des données de contexte ou d'arrière-plan nécessaires aux ACV, plutôt que des matériaux achetés directement par l'ébéniste.

| Élément | Priorité | Dataset actuel | Action envisagée |
|---|---|---|---|
| Électricité | P1 | À identifier | Représenter le mix québécois |
| Gaz naturel | P1 | À identifier | Vérifier l'approvisionnement Québec |
| Chaleur industrielle | P1 | À identifier | Définir des scénarios québécois |
| Transport routier | P1 | À identifier | Définir distances et véhicules représentatifs |
| Eau potable | P2 | À identifier | Vérifier l'importance de la régionalisation |
| Traitement des eaux usées | P2 | À identifier | Vérifier la représentativité |
| Déchets de bois | P1 | À identifier | Définir des scénarios québécois de fin de vie |
| Déchets industriels | P2 | À identifier | Définir des scénarios québécois |
| Fin de vie | P1 | À construire | Enfouissement, recyclage, valorisation énergétique |

---

# Méthode de travail

Pour chaque matériau :

1. définir le produit métier utilisé par l'industrie québécoise ;
2. identifier les datasets ecoinvent candidats, sans les modifier ;
3. créer une fiche d'inventaire détaillé des Inputs/Outputs, paramètres, providers et hypothèses importants ;
4. identifier précisément les maillons faibles, sans reconstruire automatiquement un dataset imparfait ;
5. rechercher et valider les données québécoises nécessaires ;
6. décider de conserver, adapter ou reconstruire ;
7. implémenter ultérieurement dans openLCA, seulement lorsque l'analyse est suffisamment documentée.

La [roadmap](roadmap.md) décrit les jalons V0 à V5 et le [template d'analyse](../research/templates/dataset-analysis.md) structure les futures fiches.

## Itérations prévues

| Version | Étape | Résultat attendu |
|---|---|---|
| **V0** | Inventaire métier | Liste initiale des matériaux réellement utilisés en ébénisterie |
| **V1** | Mapping ecoinvent | Un ou plusieurs datasets candidats pour chaque matériau |
| **V2** | Inventaire détaillé | Inputs/Outputs, paramètres, providers et hypothèses documentés |
| **V3** | Analyse Québec | Éléments représentatifs et besoins de données ou de régionalisation identifiés |
| **V4** | Implémentation | Datasets adaptés dans openLCA lorsque l'analyse le justifie |
| **V5** | Validation | Dataset québécois comparé, vérifié et documenté |

---

## Principe de prudence

La présence d'un nom ou d'une géographie `CA-QC` dans ce document **ne signifie pas que le dataset est validé**. Un procédé québécois peut encore dépendre d'intrants RoW, de valeurs européennes ou d'hypothèses technologiques non représentatives. Les datasets indiqués restent des candidats jusqu'à l'analyse et à la validation documentées.
