# Référentiel des matériaux et composants — Ébénisterie

> **Statut : V1 — taxonomie métier révisée**
> Ce document définit les produits et composants réellement achetés ou utilisés en atelier. Il ne constitue pas encore un mapping ecoinvent détaillé.

## Rôle de cet index

Ce document répond à la question : **« Quels matériaux et composants d'ébénisterie devons-nous couvrir ? »** Il constitue l'inventaire métier progressif des produits utilisés en ébénisterie et dans la fabrication de meubles au Québec.

La taxonomie part du produit ou du composant acheté : par exemple, une bande de chant ABS, une charnière invisible ou un panneau MDF mélaminé/TFL acheté fini. Une décomposition en matières et procédés ne sera envisagée que plus tard, si ecoinvent ne propose pas de produit ou de composant suffisamment représentatif.

Les candidats ecoinvent déjà identifiés sont conservés lorsqu'ils restent compatibles avec cette taxonomie, sans compléter les références par intuition. Les analyses dataset par dataset sont regroupées dans les [fiches d'inventaire détaillé](inventaire/README.md).

## Légende

### Priorités

| Priorité | Signification |
|---|---|
| **P1** | Incontournable ou très fréquent dans la fabrication de meubles et d'éléments d'ébénisterie |
| **P2** | Fréquent, mais dépend davantage du produit, du procédé ou de l'atelier |
| **P1/P2** | Usage réel dont la priorité précise reste à confirmer |

### Statuts

- **À rechercher** — aucun dataset candidat n'est encore retenu.
- **Dataset candidat identifié** — un ou plusieurs candidats ont été repérés, sans validation complète.
- **À analyser** — le candidat doit être étudié (technologie, géographie, intrants, etc.).
- **À confirmer** — l'usage, le produit exact ou sa composition doit encore être confirmé auprès de l'atelier.
- **À régionaliser** — un écart significatif avec le contexte québécois a été identifié.
- **Dataset Québec créé** — une adaptation ou reconstruction québécoise existe.
- **Validé** — le dataset et ses hypothèses ont été vérifiés et documentés.

---

## 1. Panneaux

| Priorité | Matériau / composant | Dataset ecoinvent candidat | Géographie | Statut | Notes |
|---|---|---|---|---|---|
| P1 | Panneau de particules brut | `particleboard production, uncoated, average glue mix` | RER / RoW | Dataset candidat identifié | Comparer ultérieurement avec la production québécoise |
| P1 | MDF brut | `medium density fibreboard production, uncoated` | RER / RoW | Dataset candidat identifié | |
| P1 | Contreplaqué de bouleau russe | — | — | À rechercher | Conserver comme produit métier distinct |
| P1 | Panneau de particules mélaminé / TFL | — | — | À rechercher | Produit acheté fini ; ne pas modéliser d'emblée comme panneau brut et papier décoratif appliqué en atelier |
| P1 | MDF mélaminé / TFL | — | — | À rechercher | Produit acheté fini ; la mélamine n'est pas appliquée en atelier |
| P1 | MDF plaqué bois acheté fini | — | — | À rechercher | Ne pas séparer d'emblée le support et le placage |
| P1 | Panneau de particules plaqué bois acheté fini | — | — | À rechercher | Ne pas séparer d'emblée le support et le placage |
| P2 | HDF brut | — | — | À rechercher | |
| P2 | OSB | — | — | À rechercher | |
| P2 | Autre contreplaqué | `plywood production, plywood` | CA-QC | À analyser | Candidat générique à vérifier selon le contreplaqué ; [fiche pilote CA-QC](inventaire/panneaux/plywood-ca-qc.md) |
| P2 | Panneau plaqué en atelier | — | — | À rechercher | Cas secondaire, seulement lorsque le panneau fini n'est pas disponible ; support, placage et adhésif seront alors comptabilisés séparément |

> **Règle métier :** les panneaux sont achetés déjà plaqués autant que possible. Le placage en atelier est secondaire. Un dataset localisé `CA-QC` n'est pas représentatif du Québec du seul fait de sa géographie : ses intrants, paramètres et hypothèses technologiques doivent être analysés.

## 2. Revêtements / surfaces

| Priorité | Matériau / composant | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Stratifié HPL | — | À rechercher | Revêtement utilisé notamment avec une colle contact |
| P1 | Placage de bois naturel | — | À rechercher | Matériau utilisé pour le cas secondaire du placage en atelier et pour les chants en bois, selon le produit acheté |

Le papier décoratif imprégné de mélamine n'est pas un matériau direct d'atelier. Les panneaux mélaminés/TFL sont achetés finis. Le stratifié compact pourra être ajouté en P2 si son usage réel et sa pertinence sont documentés.

## 3. Bandes de chant

| Priorité | Matériau / composant | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Bande de chant en bois véritable préencollée | — | À rechercher | Produit acheté avec son adhésif |
| P1 | Bande de chant en bois véritable non encollée | — | À rechercher | Comptabiliser séparément l'adhésif appliqué en atelier |
| P1 | Bande de chant ABS | — | À rechercher | L'ABS est décrit selon son usage, et non comme famille de matière autonome |
| P1 | Bande de chant PVC | — | À rechercher | Le PVC est décrit selon son usage, et non comme famille de matière autonome |

Aucune bande de chant mélamine n'est retenue dans cette V1, faute d'usage atelier documenté.

## 4. Bois massif

Le bois massif est acheté brut et séché, principalement en épaisseur 4/4 ; les épaisseurs 6/4 et 8/4 sont plus occasionnelles. Les essences restent séparées dans la taxonomie métier.

| Priorité | Matériau / composant | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Érable massif, brut séché | — | À rechercher | Principalement 4/4 ; 6/4 ou 8/4 occasionnellement |
| P1 | Frêne massif, brut séché | — | À rechercher | Principalement 4/4 ; 6/4 ou 8/4 occasionnellement |
| P1 | Cerisier massif, brut séché | — | À rechercher | Principalement 4/4 ; 6/4 ou 8/4 occasionnellement |
| P1 | Chêne rouge massif, brut séché | — | À rechercher | Principalement 4/4 ; 6/4 ou 8/4 occasionnellement |
| P1/P2 | Tilleul massif, brut séché | — | À rechercher | Utilisé notamment pour le prototypage |
| P1/P2 | Bois feuillu exotique / bois africain exotique, brut séché | — | À rechercher | Catégorie d'usage réel, sans reproduire une liste exhaustive de catalogue fournisseur |

Le dataset déjà repéré `sawnwood production, hardwood, dried` (CH / Europe / RoW) reste un **candidat générique à analyser** pour un éventuel proxy. Il ne remplace pas les essences métier et n'est affecté automatiquement à aucune d'elles à ce stade.

## 5. Adhésifs

| Priorité | Matériau / composant | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Colle PVAc / PVA blanche | — | À rechercher | Collage et assemblage du bois ; exemple atelier possible : Richelieu 404, référence à confirmer |
| P1 | Adhésif thermofusible EVA / EVA hot-melt | — | À rechercher | Utilisé dans l'encolleuse de chants |
| P1 | Colle contact | — | À rechercher | Collage du stratifié HPL ; produit en pot type LePage, composition exacte à confirmer ultérieurement à partir de la FDS |
| P2 | Colle polyuréthane / PUR | — | À rechercher | Usage occasionnel pour le collage métal-bois ou plastique-bois |

Les adhésifs UF et MUF ne sont pas utilisés directement en atelier et ne figurent donc pas dans cette taxonomie. Ils pourront être traités ultérieurement comme intrants industriels de fabrication des panneaux. La colle PUR d'assemblage multimatériaux ne doit pas être confondue avec un PUR hot-melt : l'encolleuse considérée ici utilise un adhésif EVA hot-melt.

## 6. Produits de finition

| Priorité | Matériau / composant | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Vernis / laque à base d'eau | — | À rechercher | |
| P1 | Vernis / laque à base de solvant | — | À rechercher | |
| P1 | Scellant à base d'eau | — | À rechercher | |
| P1 | Scellant à base de solvant | — | À rechercher | |
| P2 | Teinture à base d'eau | — | À rechercher | |
| P2 | Teinture à base de solvant | — | À rechercher | |
| P2 | Acétone auxiliaire | — | À rechercher | Nettoyage et décrassage |
| P2 | Thinner auxiliaire | — | À rechercher | Dilution de produits à solvants ; composition à déterminer ultérieurement à partir du produit et de sa FDS |

L'eau n'est pas un produit de finition séparé. Le thinner n'est pas une substance unique et ne devra pas être mappé avant confirmation de sa composition.

## 7. Quincaillerie / composants fonctionnels

| Priorité | Matériau / composant | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Vis d'assemblage #6 | — | À rechercher | Composant fonctionnel, plutôt que métal générique |
| P1 | Vis d'assemblage #8 | — | À rechercher | Composant fonctionnel, plutôt que métal générique |
| P1 | Charnière invisible de meuble | — | À rechercher | Blum est un exemple atelier, pas le nom principal du composant |
| P1 | Coulisse de tiroir | — | À rechercher | Exemple atelier : Blum ; profondeurs typiques de 10 à 22 pouces |
| P1 | Poignée de meuble métallique | — | À rechercher | |
| P1 | Pied niveleur / niveleur | — | À rechercher | Composant actuellement en plastique |
| P1/P2 | Ferrure métallique de suspension pour meuble mural | — | À rechercher | Type clé française / French cleat |

Lors du futur mapping ecoinvent, rechercher d'abord le composant fonctionnel, puis un produit proche. Une reconstruction à partir de matières et de procédés ne viendra qu'en dernier recours. L'acier, l'aluminium, le zinc et le plastique ne constituent pas des familles principales autonomes.

## 8. Emballages

Les emballages sont suivis séparément des matériaux constitutifs du meuble.

| Priorité | Matériau / composant | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Carton d'emballage / carton ondulé | — | À rechercher | |
| P1 | Film à bulles / papier bulle | — | À rechercher | Composition exacte à confirmer avant le mapping |

Une palette de bois, un film étirable ou un feuillard ne seront ajoutés que si leur usage réel est documenté.

---

# 9. Flux et processus transversaux de fabrication

Ces flux et processus sont volontairement séparés des matériaux et composants achetés.

| Priorité | Flux / processus | Dataset ecoinvent candidat | Statut | Notes |
|---|---|---|---|---|
| P1 | Électricité d'atelier | — | À rechercher | Représenter le contexte d'approvisionnement réel de l'atelier |
| P1 | Transport entrant des matériaux et composants | — | À rechercher | Définir les distances, charges et véhicules représentatifs |
| P1 | Transport sortant du meuble fini | — | À rechercher | Définir les distances, charges et véhicules représentatifs |
| P1 | Chutes de bois massif | — | À rechercher | Associer ultérieurement la quantité produite à la pratique réelle du fabricant |
| P1 | Chutes de panneaux | — | À rechercher | Distinguer ce flux des chutes de bois massif |
| P1 | Sciures / poussières d'usinage | — | À rechercher | Caractériser la collecte et la pratique réelle du fabricant |
| P2 | Gaz naturel / chaleur | — | À confirmer | Inclure uniquement si réellement utilisé dans le périmètre |
| P2 | Eau de procédé / nettoyage | — | À confirmer | Vérifier les usages et quantités réels |
| P2 | Eaux usées | — | À confirmer | Relier au traitement réellement appliqué |
| P2 | Résidus contaminés par colles, finitions, solvants ou chiffons | — | À confirmer | Caractériser séparément les flux et pratiques réels |

Pour chaque résidu, appliquer la logique : **résidu produit → pratique réelle du fabricant → scénario ou dataset ecoinvent correspondant**. Ne pas imposer une filière unique : les pratiques observées peuvent relever de la déchèterie ou de l'élimination, de l'incinération, ou du recyclage et de la valorisation en développement.

La fin de vie du meuble est un scénario ACV séparé ; elle ne constitue ni un matériau ni un flux de fabrication de l'atelier.

---

# Méthode de travail

Pour chaque produit, composant ou flux :

1. confirmer l'usage réel, la forme achetée et la priorité métier ;
2. identifier les datasets ecoinvent candidats, sans les inventer ni les modifier ;
3. privilégier le produit ou composant fonctionnel, puis un produit proche ;
4. n'envisager une décomposition matière + procédé qu'en dernier recours ;
5. analyser la technologie, les intrants, les paramètres et la géographie du candidat ;
6. rechercher et valider les données québécoises nécessaires ;
7. décider de conserver, adapter ou reconstruire avant toute implémentation dans openLCA.

La [roadmap](roadmap.md) décrit les jalons du projet et le [template d'analyse](../research/templates/dataset-analysis.md) structure les futures fiches.

## Principe de prudence

La présence d'un nom ou d'une géographie `CA-QC` dans ce document **ne signifie pas que le dataset est validé ni représentatif du Québec**. Un procédé québécois peut dépendre d'intrants RoW, de valeurs européennes ou d'hypothèses technologiques non représentatives. Les datasets indiqués restent des candidats jusqu'à l'analyse et à la validation documentées.
