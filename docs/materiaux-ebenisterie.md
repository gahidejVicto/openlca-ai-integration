# Référentiel des matériaux — Ébénisterie

> **Statut : V0 — inventaire métier initial**  
> Ce document est volontairement évolutif. Il sert d'abord à définir les matériaux à couvrir, avant de sélectionner, analyser puis éventuellement régionaliser les datasets ACV.

## Objectif

Ce document constitue l'inventaire progressif des matériaux utilisés en ébénisterie et dans la fabrication de meubles au Québec.

Il sert de point de départ pour :

- identifier les matériaux prioritaires ;
- associer chaque matériau à un ou plusieurs datasets ecoinvent 3.11 candidats ;
- évaluer la représentativité des datasets existants ;
- identifier les données devant être régionalisées pour le Québec ;
- documenter progressivement les futurs datasets québécois.

La démarche est volontairement itérative : **inventaire métier → mapping ecoinvent → analyse des écarts Québec → régionalisation**.

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
| P1 | Contreplaqué | `plywood production, plywood` | CA-QC | À rechercher | Dataset QC identifié — à valider |
| P2 | OSB | — | — | À rechercher | |



### 1.1 Exemple du contreplaqué :

Pour notre tableau, je noterais donc pour le contreplaqué :

Élément	ecoinvent 3.11	Évaluation
Production du contreplaqué	CA-QC	✓ Québec
Électricité	CA-QC	✓ Québec
Bois feuillu	RoW	⚠ À régionaliser/vérifier
Quantité de bois	2,206 m³/m³ plywood	⚠ Valeur à valider pour le Québec
Source de cette quantité	échantillon/littérature Allemagne	⚠ Faible représentativité géographique
Résine UF	à vérifier	?
Chaleur	à vérifier	?
Statut	Très bon candidat — validation en cours


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

Pour chaque matériau, suivre progressivement les étapes suivantes :

1. **Définir le produit métier** réellement utilisé par l'industrie québécoise.
2. **Identifier les datasets ecoinvent 3.11 candidats**, sans les modifier à ce stade.
3. **Examiner les Inputs/Outputs** du procédé candidat.
4. **Évaluer la représentativité technologique** : matière première, densité, colle, taux de matière recyclée, procédé, rendement, etc.
5. **Évaluer la représentativité géographique** du dataset.
6. **Identifier les paramètres sensibles** pour les résultats ACV.
7. **Identifier les données québécoises disponibles** : énergie, transport, approvisionnement, déchets, technologies de production, etc.
8. **Décider de la stratégie** : conserver le dataset, l'adapter ou le reconstruire.
9. **Documenter les sources et hypothèses** utilisées.
10. **Valider le dataset québécois** avant de le considérer comme référence.

## Itérations prévues

| Version | Étape | Résultat attendu |
|---|---|---|
| **V0** | Inventaire métier | Liste initiale des matériaux réellement utilisés en ébénisterie |
| **V1** | Mapping ecoinvent | Un ou plusieurs datasets candidats pour chaque matériau |
| **V2** | Analyse des écarts Québec | Écarts technologiques, géographiques et énergétiques documentés |
| **V3** | Régionalisation | Datasets québécois adaptés ou reconstruits lorsque nécessaire |

---

## Principe de prudence

La présence d'un nom de dataset dans ce document **ne signifie pas qu'il est validé**. À ce stade, les datasets indiqués sont des candidats de travail. Leur adéquation doit être vérifiée dans openLCA avant toute utilisation comme référence québécoise.
