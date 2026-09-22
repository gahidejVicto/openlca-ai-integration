# Tableau transversal des lacunes Ecoinvent — RECQ36

Livrable demandé par Nicolas en réunion de validation métier du **2026-09-15**. Ce tableau rassemble, en une vue unique, l'état du diagnostic de représentativité Ecoinvent pour **tous les produits métier déjà couverts par les Lots 2A à 2G**, les objets ajoutés le 2026-09-15, et leur réconciliation avec l'interrogation OpenLCA vérifiée sur Ecoinvent 3.11 du **2026-09-16** ([rapport source](RECQ36_diagnostic_ecoinvent_openLCA.md)). Une ligne = un produit métier.

**Correction (2026-09-16, passe corrective) :** une première réconciliation avait été intégrée par erreur (commit `aaabecd`) alors que la mauvaise base OpenLCA (`cups`) était ouverte après un changement de poste de travail — tous ses résultats sont invalidés. Ce tableau est désormais aligné sur une nouvelle interrogation complète, réalisée depuis zéro sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` (`database_family` forcé et confirmé à `ecoinvent`, 25 412 processus / 14 051 flux / 0 méthode). L'anomalie `database_family: "flcac"` est **résolue** (cause : mauvaise base ouverte, pas une anomalie Ecoinvent) — voir le [référentiel](../materiaux-ebenisterie.md#anomalie-résolue--database_family-flcac). Les objets non encore diagnostiqués restent marqués `NON RÉALISÉE` ; les objets reconfirmés indépendamment (Lot antérieur + Ecoinvent 3.11) portent la mention `RÉALISÉE (2× )` en note.

**Stade du projet — rappel méthodologique important :** nous sommes au stade **diagnostic**. Ce tableau identifie et qualifie des écarts ; il ne les convertit **ni** en score carbone, **ni** en métrique quantitative agrégée. Un écart identifié (`ÉCART`) est déjà, en soi, une information valide à ce stade — il n'appelle pas nécessairement une correction immédiate.

Le [référentiel métier](../materiaux-ebenisterie.md) reste la source détaillée par produit (fiches complètes, citations, UUID). Ce tableau en est la vue transversale condensée.

---

## Légende

### Colonnes de correspondance (dimension physique/technique)

| Code | Signification |
|---|---|
| **OK** | La dimension est jugée satisfaisante par le diagnostic sourcé (correspondance bonne à forte, documentée). |
| **ÉCART** | Un écart est identifié et documenté par le diagnostic sourcé pour cette dimension (absence, non-représentativité, donnée manquante confirmée). |
| **À VÉRIFIER** | L'analyse existante est insuffisante pour trancher cette dimension précise ; ni `OK` ni `ÉCART` ne peuvent être affirmés avec le sourçage actuel. |
| **N/A** | Dimension sans objet pour ce produit (ex. produit entièrement absent d'Ecoinvent → la composition/technologie/géographie du dataset absent est sans objet). |

Colonnes concernées : `Produit_fonction`, `Composition_matiere`, `Technologie_procede`, `Geographie`, `Donnees_primaires_QC`.

### Colonnes de besoin d'action

| Code | Signification |
|---|---|
| **OUI** | Cette action est nécessaire d'après le diagnostic sourcé. |
| **NON** | Cette action n'est pas nécessaire d'après le diagnostic sourcé (correspondance déjà suffisante sur ce plan). |
| **À VÉRIFIER** | Le besoin n'a pas pu être établi avec certitude par le diagnostic disponible. |
| **N/A** | Sans objet (ex. aucune information fournisseur ne peut aider tant que le matériau lui-même n'est pas identifié). |

Colonnes concernées : `Adaptation_geo_necessaire`, `Proxy_necessaire`, `Reconstruction_necessaire`, `Info_fournisseur_necessaire`.

### Colonne `Analyse_Ecoinvent`

| Valeur | Signification |
|---|---|
| **RÉALISÉE** | Un lot de diagnostic dédié a recherché ce produit dans Ecoinvent (process + flow) et conclu. |
| **PARTIELLE** | Une recherche a eu lieu mais reste incomplète, limitée par l'outil, ou hérite de conclusions d'un produit voisin sans recherche dédiée. |
| **NON RÉALISÉE** | Aucune recherche Ecoinvent n'a encore été menée pour ce produit précis. |

### Colonne `Statut_referentiel`

Reprend la légende du [référentiel métier](../materiaux-ebenisterie.md#légende-des-statuts) : 🟢 Utilisable, 🟡 À valider, 🟠 À adapter, 🟣 À reconstruire, 🔴 Lacune majeure.

---

## 1. Panneaux

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Panneau de particules brut | P1 | OK | ÉCART | À VÉRIFIER | ÉCART | ÉCART | OUI | NON | NON | OUI | RÉALISÉE (2B) | 🟠 |
| MDF brut | P1 | OK | ÉCART | À VÉRIFIER | ÉCART | ÉCART | OUI | NON | NON | OUI | RÉALISÉE (2B) | 🟠 |
| Contreplaqué merisier / yellow birch / Baltic plywood *(ex-« bouleau russe »)* | P1 | OK *(proxy `plywood production`, Canada-Quebec, `5538194d-…`, reconfirmé)* | ÉCART *(hardwood générique ≠ bouleau)* | ÉCART *(colle urée-formaldéhyde générique)* | ÉCART *(copie administrative de l'échantillon allemand)* | ÉCART | NON *(copie administrative)* | OUI | NON | OUI *(si précision requise)* | RÉALISÉE 2× (Lot 2A + Ecoinvent 3.11, 2026-09-16) | 🟠 |
| Panneau de particules mélaminé / TFL | P1 | ÉCART | OK *(service)* | À VÉRIFIER | ÉCART | ÉCART | OUI | NON | OUI | OUI | RÉALISÉE (2B) | 🟣 |
| MDF mélaminé / TFL | P1 | ÉCART | À VÉRIFIER | À VÉRIFIER | ÉCART | ÉCART | OUI | NON | OUI | OUI | RÉALISÉE (2B) | 🟣 |
| MDF plaqué bois acheté fini | P1 | ÉCART | ÉCART *(substrat seul)* | ÉCART | ÉCART | ÉCART | À VÉRIFIER | À VÉRIFIER | OUI | OUI | RÉALISÉE (2E) | 🔴 |
| Panneau de particules plaqué bois acheté fini | P1 | ÉCART | ÉCART *(substrat seul)* | ÉCART | ÉCART | ÉCART | À VÉRIFIER | À VÉRIFIER | OUI | OUI | RÉALISÉE (2E) | 🔴 |
| HDF brut | P2 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |
| OSB *(déprioritisé, Nicolas 2026-09-15)* | P2 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 *(hors priorité)* |
| Autre contreplaqué *(déprioritisé, Nicolas 2026-09-15)* | P2 | OK | ÉCART | ÉCART | ÉCART | ÉCART | OUI | NON | NON | OUI | RÉALISÉE (2A) | 🟠 *(hors priorité)* |
| Panneau plaqué en atelier | P2 | ÉCART | ÉCART | ÉCART | ÉCART | ÉCART | À VÉRIFIER | À VÉRIFIER | OUI | OUI | PARTIELLE — hérite 2B/2E/2F | 🟡 |

## 2. Surfaces

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stratifié HPL | P1 | ÉCART | ÉCART | ÉCART | N/A | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2E) | 🔴 |
| Placage de bois naturel | P1 | ÉCART | ÉCART | ÉCART | ÉCART | ÉCART | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2E) | 🔴 |
| Papier mélaminé appliqué en atelier *(nouvel objet, Nicolas 2026-09-15)* | P1/P2 | OK *(papier + marché + service reconfirmés sur Ecoinvent 3.11)* | OK *(302 g/m² documenté)* | À VÉRIFIER *(simple vs double face ; échelle atelier vs industriel)* | ÉCART *(RoW/Europe/Global)* | ÉCART | NON | NON | NON | À VÉRIFIER *(grammage réel atelier)* | RÉALISÉE 2× (Lot 2B + Ecoinvent 3.11, 2026-09-16) | 🟡 |

## 3. Bandes de chant

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bande de chant bois véritable préencollée | P1 | ÉCART | N/A | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2D) | 🔴 |
| Bande de chant bois véritable non encollée | P1 | ÉCART | N/A | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2D) | 🔴 |
| Bande de chant ABS | P1 | ÉCART | OK *(matière)* | ÉCART | À VÉRIFIER | ÉCART | À VÉRIFIER | OUI | OUI | OUI | RÉALISÉE (2D) | 🟣 |
| Bande de chant PVC *(place relative à revalider, Nicolas 2026-09-15)* | P1 | ÉCART | OK *(matière, suspension polymerised reconfirmée)* | À VÉRIFIER *(indice partiel)* | À VÉRIFIER | ÉCART | À VÉRIFIER | OUI | OUI | OUI | RÉALISÉE 2× (Lot 2D + Ecoinvent 3.11, 2026-09-16) | 🟣 |
| Bande de chant PE / polyéthylène *(nouvel objet, Nicolas 2026-09-15)* | P1 | ÉCART *(0 résultat confirmé sur Ecoinvent 3.11)* | OK *(matière PE générique)* | ÉCART *(aucun procédé de profilé plat)* | N/A *(Global)* | ÉCART | À VÉRIFIER | OUI | OUI | OUI | RÉALISÉE (Ecoinvent 3.11, 2026-09-16) | 🟣 |

## 4. Bois massif

*(Aucun changement demandé par Nicolas — table reproduite pour la vue transversale uniquement.)*

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Érable massif, brut séché | P1 | OK | ÉCART *(essence absente)* | À VÉRIFIER | ÉCART | ÉCART | OUI | NON | NON | OUI | RÉALISÉE (2C) | 🔴 |
| Frêne massif, brut séché | P1 | OK | ÉCART *(essence absente)* | À VÉRIFIER | ÉCART | ÉCART | OUI | NON | NON | OUI | RÉALISÉE (2C) | 🔴 |
| Merisier / bouleau jaune massif, brut séché | P1 | À VÉRIFIER *(nom vernaculaire `birch`)* | À VÉRIFIER | À VÉRIFIER | ÉCART *(Suède)* | ÉCART | OUI | NON | NON | OUI | RÉALISÉE (2C) | 🟠 |
| Chêne rouge massif, brut séché | P1 | À VÉRIFIER *(nom vernaculaire `oak`)* | À VÉRIFIER | À VÉRIFIER | ÉCART *(Allemagne)* | ÉCART | OUI | NON | NON | OUI | RÉALISÉE (2C) | 🟠 |
| Tilleul massif, brut séché | P1/P2 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |
| Bois feuillu exotique, brut séché | P1/P2 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |

## 5. Adhésifs

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colle PVAc / PVA blanche | P1 | ÉCART *(monomère seul, reconfirmé sur Ecoinvent 3.11)* | ÉCART | ÉCART | À VÉRIFIER | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE 2× (Lot 2F + Ecoinvent 3.11, 2026-09-16) | 🔴 |
| Adhésif thermofusible EVA hot-melt | P1 | ÉCART *(résine seule, reconfirmé)* | ÉCART | À VÉRIFIER | À VÉRIFIER | ÉCART | N/A | À VÉRIFIER | OUI | OUI | RÉALISÉE 2× (Lot 2F + Ecoinvent 3.11, 2026-09-16) | 🟣 |
| Colle contact *(formulations à base d'eau pertinentes aujourd'hui, Nicolas 2026-09-15)* | P1 | ÉCART *(aucune brique, reconfirmé même pour base eau)* | ÉCART | ÉCART | N/A | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE 2× (Lot 2F + Ecoinvent 3.11, 2026-09-16) | 🔴 |
| Colle polyuréthane / PUR | P2 | ÉCART *(précurseurs seuls ; produit formulé trouvé pour CLT, non équivalent)* | ÉCART | ÉCART | OK *(Global, pour le produit CLT)* | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE 2× (Lot 2F + Ecoinvent 3.11, 2026-09-16) | 🔴 |

## 6. Finitions

*(Aucun changement demandé par Nicolas — aucun diagnostic Ecoinvent encore mené.)*

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vernis / laque | P1 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |
| Scellant | P1 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |
| Teinture | P2 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |
| Solvants / diluants auxiliaires | P2 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |

## 7. Quincaillerie

> **Priorisation métier (Nicolas, 2026-09-15) :** charnières, coulisses de tiroir, poignées, pieds/niveleurs et ferrures de suspension sont désormais prioritaires. Les vis ne le sont pas — un modèle simplifié masse + matière est jugé probablement suffisant.

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vis d'assemblage #6 *(modèle simplifié probablement suffisant, Nicolas)* | P1 | ÉCART | À VÉRIFIER | ÉCART | N/A | ÉCART | N/A | À VÉRIFIER | OUI | OUI | RÉALISÉE (2D) | 🟣 |
| Vis d'assemblage #8 *(idem)* | P1 | ÉCART | À VÉRIFIER | ÉCART | N/A | ÉCART | N/A | À VÉRIFIER | OUI | OUI | RÉALISÉE (2D) | 🟣 |
| Charnière invisible de meuble *(priorisé, Nicolas)* | P1 | ÉCART (reconfirmé 2 fois, dont Ecoinvent 3.11) | ÉCART (nomenclature absente ; services génériques identifiés sans UUID) | À VÉRIFIER (mise en forme/revêtement disponibles, sans UUID) | N/A | ÉCART | N/A | OUI (bottom-up) | À VÉRIFIER | OUI (bloquant) | RÉALISÉE 2 fois (Lot 2D + Ecoinvent 3.11, 2026-09-16) | 🔴 |
| Coulisse de tiroir *(priorisé + modèle fournisseur de référence à choisir, Nicolas)* | P1 | ÉCART *(reconfirmé 2×, dont Ecoinvent 3.11)* | ÉCART *(nomenclature absente ; mêmes services génériques)* | À VÉRIFIER | N/A | ÉCART | N/A | OUI *(bottom-up)* | À VÉRIFIER | OUI *(bloquant)* | RÉALISÉE 2× (Lot 2D + Ecoinvent 3.11, 2026-09-16) | 🔴 |
| Poignée de meuble métallique *(priorisé, Nicolas)* | P1 | ÉCART *(absence reconfirmée sans ambiguïté sur Ecoinvent 3.11 ; incohérence de la passe `cups` sans objet)* | À VÉRIFIER *(alu conditionnel)* | À VÉRIFIER | N/A | ÉCART | N/A | À VÉRIFIER | OUI | OUI | RÉALISÉE 2× (Lot 2D + Ecoinvent 3.11, 2026-09-16) | 🟣 |
| Pied niveleur / niveleur *(priorisé, Nicolas)* | P1 | ÉCART *(reconfirmé sur Ecoinvent 3.11)* | À VÉRIFIER *(PP conditionnel)* | À VÉRIFIER | N/A | ÉCART | N/A | À VÉRIFIER | OUI | OUI | RÉALISÉE 2× (Lot 2D + Ecoinvent 3.11, 2026-09-16) | 🟣 |
| Ferrure métallique de suspension (French cleat) *(priorisé, Nicolas)* | P1/P2 | ÉCART *(désormais couvert et confirmé absent, Ecoinvent 3.11)* | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | OUI | OUI | RÉALISÉE (Ecoinvent 3.11, 2026-09-16) | 🟣 |

## 8. Emballage

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carton d'emballage / carton ondulé | P1 | OK *(Lot 2A, reconfirmé indépendamment sur Ecoinvent 3.11, même UUID)* | À VÉRIFIER *(linerboard)* | OK | OK *(marché explicitement régional, documenté par Ecoinvent lui-même)* | À VÉRIFIER *(données de fabrication datées de 2008)* | NON | NON | NON | À VÉRIFIER *(linerboard, électricité)* | RÉALISÉE 2× (Lot 2A + Ecoinvent 3.11, 2026-09-16) | 🟢 |
| Film à bulles / papier bulle | P1 | ÉCART *(0 résultat confirmé sur plusieurs synonymes, Ecoinvent 3.11)* | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (Ecoinvent 3.11, synonymes usuels testés) | 🔴 |
| Matériau d'emballage blanc fin en rouleau *(film/mousse PE — identification confirmée par validation métier Nicolas, 2026-09-22)* | P1/P2 | ÉCART *(aucune mousse PE dans la base, confirmé par recherche exhaustive sur `foam` + 14 variantes lexicales, 2026-09-22)* | OK *(matière PE-LD vierge)* / ÉCART *(mousse elle-même)* | ÉCART *(seul procédé de moussage trouvé est documenté calibré polystyrène, pas PE)* | N/A | ÉCART | À VÉRIFIER | OUI *(sous réserve du calibrage polystyrène)* | OUI | OUI *(bloquant — caractéristiques physiques et fournisseur réel du produit, identification elle-même désormais confirmée)* | RÉALISÉE (Ecoinvent 3.11, 2026-09-16 + 2026-09-22) | 🟣 |

## 9. Données transversales

> **Phase ultérieure — hors diagnostic matériaux prioritaire (Nicolas, 2026-09-15).** Ces dix objets restent pertinents pour l'ACV complète mais ne sont plus une cible active du diagnostic matériaux. Ils sont inclus ici pour l'exhaustivité du tableau, puisque le Lot 2G (complété par le Lot 2G-bis) les a déjà diagnostiqués.

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Électricité d'atelier | P1 | À VÉRIFIER *(non isolé)* | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | PARTIELLE *(limite outil MCP)* | 🟡 |
| Transport entrant | P1 | OK *(candidat générique)* | N/A | À VÉRIFIER *(mix EURO)* | ÉCART *(Global)* | ÉCART | À VÉRIFIER | NON | NON | OUI | RÉALISÉE (2G) | 🟡 |
| Transport sortant | P1 | OK *(candidat générique)* | N/A | À VÉRIFIER *(mix EURO)* | ÉCART *(Global)* | ÉCART | À VÉRIFIER | NON | NON | OUI | RÉALISÉE (2G) | 🟡 |
| Chutes de bois massif | P1 | OK | OK | À VÉRIFIER *(paramètres europ.)* | ÉCART | ÉCART | OUI | NON | NON | OUI | RÉALISÉE (2G) | 🟡 |
| Chutes de panneaux | P1 | ÉCART *(aucun flow dédié)* | N/A | N/A | N/A | ÉCART | À VÉRIFIER | OUI | À VÉRIFIER | OUI | RÉALISÉE (2G) | 🟠 |
| Sciures / poussières d'usinage | P1 | À VÉRIFIER *(co-produit, pas déchet)* | N/A | N/A | N/A | ÉCART | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2G) | 🟡 |
| Gaz naturel / chaleur | P2 | OK *(candidat RoW)* | N/A | À VÉRIFIER | À VÉRIFIER *(RoW)* | ÉCART | À VÉRIFIER | NON | NON | OUI | RÉALISÉE (2G + 2G-bis) | 🟡 |
| Eau de procédé / nettoyage | P2 | OK *(dataset Québec identifié)* | N/A | N/A | OK *(Québec)* | OK | NON | NON | NON | OUI | RÉALISÉE (2G + 2G-bis) | 🟢 |
| Eaux usées | P2 | OK *(candidat RoW)* | N/A | À VÉRIFIER | À VÉRIFIER *(RoW)* | ÉCART | À VÉRIFIER | NON | NON | OUI | RÉALISÉE (2G + 2G-bis) | 🟡 |
| Résidus contaminés (colles, finitions, solvants, chiffons) | P2 | OK *(peinture)* / ÉCART *(autres)* | À VÉRIFIER | À VÉRIFIER | ÉCART | ÉCART | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2G) | 🟠 |

---

## Décompte factuel (ni score, ni métrique quantitative — simple tally des statuts documentés)

Sur les **53 produits métier** recensés dans ce tableau :

| Statut référentiel | Nombre de produits |
|---|---|
| 🟢 Utilisable | 2 |
| 🟡 À valider | 18 |
| 🟠 À adapter | 8 |
| 🟣 À reconstruire | 11 |
| 🔴 Lacune majeure | 14 |

| État de l'analyse Ecoinvent | Nombre de produits |
|---|---|
| RÉALISÉE | 43 |
| PARTIELLE | 2 |
| NON RÉALISÉE | 8 |

**Lecture de ce décompte :** ces chiffres ne mesurent qu'une chose — combien de produits métier portent chaque étiquette de statut ou d'avancement dans les diagnostics déjà sourcés. Ils ne pondèrent pas par masse, par fréquence d'usage réelle en atelier, ni par contribution probable à l'impact du meuble fini ; ils ne doivent donc pas être lus comme une priorisation implicite. La priorisation reste celle établie par Nicolas (sections 7, 8 et par produit ci-dessus) et par les priorités P1/P2 du référentiel.

---

## Points de vigilance transversaux

1. **Les adhésifs et les surfaces de panneaux restent les deux familles les plus systématiquement en `ÉCART`** sur le produit/fonction : Ecoinvent ne propose généralement que des précurseurs chimiques ou des substrats bruts, jamais le produit fini métier — confirmé une seconde fois pour la PVA et la colle contact sur Ecoinvent 3.11 (2026-09-16).
2. **Le statut 🟢 Utilisable regroupe désormais l'eau de procédé/nettoyage** (Lot 2G-bis, dataset régional Québec) **et le carton d'emballage/ondulé** (Lot 2A, reconfirmé indépendamment sur Ecoinvent 3.11, même UUID `2424352b-…`). Le papier mélaminé appliqué en atelier, correspondance partielle forte plutôt que directe, est classé `🟡 À valider` — sa représentativité simple-face/double-face et son échelle atelier vs industrielle restent à trancher.
3. **Anomalie `database_family: "flcac"` résolue.** Une première réconciliation (commit `aaabecd`) avait interrogé la mauvaise base OpenLCA (`cups`) après un changement de poste de travail, et non Ecoinvent — tous ses résultats sont invalidés. Une nouvelle interrogation complète sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` (`database_family` forcé et confirmé à `ecoinvent`, 25 412 processus / 14 051 flux / 0 méthode) remplace ces résultats dans ce tableau. Voir la [note dédiée dans le référentiel](../materiaux-ebenisterie.md#anomalie-résolue--database_family-flcac) et le [diagnostic corrigé](RECQ36_diagnostic_ecoinvent_openLCA.md).
4. **Point distinct, encore ouvert :** même entre deux sessions authentiquement Ecoinvent (Lot 2F pre-`cups` vs Ecoinvent 3.11 2026-09-16), certains produits génériques (`vinyl acetate`, `ethylene vinyl acetate copolymer`, `adhesive, for metal`) reviennent sous des UUID différents — sans lien avec l'anomalie `flcac` désormais résolue, et sans qu'on puisse établir la cause. `À VÉRIFIER`, à ne pas présumer être une erreur.
5. **Le renommage du contreplaqué (merisier/yellow birch/Baltic plywood)** a été réconcilié sur Ecoinvent 3.11 (2026-09-16) : le candidat `plywood production`, Canada-Quebec (`5538194d-…`) — déjà identifié au Lot 2A — est **reconfirmé indépendamment**, avec un écart d'essence documenté explicitement (hardwood générique, jamais bouleau) et une géographie CA-QC qui est une copie administrative du dataset européen, pas une donnée régionale réelle.
6. **Le contreplaqué CA-QC et le carton CA-QC illustrent une distinction méthodologique importante :** deux datasets peuvent tous deux porter l'étiquette `Canada, Quebec`/`Canada, Québec` sans avoir le même niveau de représentativité réelle. Le contreplaqué est une copie administrative de l'échantillon européen (aucune donnée réelle québécoise) ; le carton ondulé a une base méthodologique documentée par Ecoinvent lui-même qui justifie sa représentativité régionale. Localisation ≠ représentativité, mais ce n'est pas non plus vrai que *tous* les datasets CA-QC sont des copies administratives.
7. **La poignée de meuble métallique** portait une discordance interne dans le rapport `cups`, désormais sans objet : la nouvelle interrogation sur Ecoinvent 3.11 confirme sans ambiguïté l'absence de produit fonctionnel.
8. **Recherches encore ouvertes après la passe du 2026-09-16 sur Ecoinvent 3.11 :** procédé générique de polymérisation en émulsion pour une éventuelle reconstruction PVAc, et mousse PE/PP souple sous d'autres terminologies — **les deux fermées le 2026-09-22** par des réponses négatives documentées (la polymérisation en émulsion n'existe que pour le PVC ; aucune mousse PE/PP dans la base, recherche exhaustive sur `foam` seul). Une hypothèse d'identification du matériau d'emballage mystère (film mousse PE) a été posée le 2026-09-22, non confirmée pour le Québec. Reste ouvert : l'approfondissement des procédés de formage métallique, seulement après obtention de données fabricant. Voir la [liste structurée pour la prochaine passe OpenLCA](prochaine-passe-openlca.md).
9. **Dix objets (Données transversales) restent en phase ultérieure** par décision de Nicolas, malgré un diagnostic déjà réalisé (Lot 2G/2G-bis) : ce tableau les conserve pour la traçabilité, mais ils ne doivent pas orienter les priorités de travail immédiates. Ils n'ont pas été touchés par la réconciliation du 2026-09-16.

---

*Ce tableau consolide des analyses déjà sourcées dans le dépôt (`docs/diagnostic/ecoinvent-representativite-qc-lot-2{a..g}.md`, `docs/materiaux-ebenisterie.md`) et le [diagnostic OpenLCA vérifié et corrigé du 2026-09-16](RECQ36_diagnostic_ecoinvent_openLCA.md) (base `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31`), réconciliés le 2026-09-16. Une première réconciliation faite sur la mauvaise base OpenLCA (`cups`) est invalidée en totalité. Voir la version tabulaire complète : [`tableau-transversal-lacunes-ecoinvent.csv`](tableau-transversal-lacunes-ecoinvent.csv).*
