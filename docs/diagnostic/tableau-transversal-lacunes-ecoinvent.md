# Tableau transversal des lacunes Ecoinvent — RECQ36

Livrable demandé par Nicolas en réunion de validation métier du **2026-09-15**. Ce tableau rassemble, en une vue unique, l'état du diagnostic de représentativité Ecoinvent pour **tous les produits métier déjà couverts par les Lots 2A à 2G** ainsi que les objets ajoutés le 2026-09-15 (encore non diagnostiqués). Une ligne = un produit métier.

**Session sans accès OpenLCA (2026-09-16).** Ce tableau ne recense aucune nouvelle recherche Ecoinvent : il consolide exclusivement les conclusions déjà sourcées dans `docs/diagnostic/ecoinvent-representativite-qc-lot-2{a..g}.md` et dans `docs/materiaux-ebenisterie.md`. Les objets non encore diagnostiqués sont marqués `NON RÉALISÉE` en dernière colonne, pas `ÉCART`.

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
| Contreplaqué merisier / yellow birch / Baltic plywood *(ex-« bouleau russe »)* | P1 | À VÉRIFIER | ÉCART | ÉCART | ÉCART | ÉCART | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | OUI | PARTIELLE — ancienne appellation seulement (2A) | 🔴 |
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
| Papier mélaminé appliqué en atelier *(nouvel objet, Nicolas 2026-09-15)* | P1/P2 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |

## 3. Bandes de chant

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bande de chant bois véritable préencollée | P1 | ÉCART | N/A | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2D) | 🔴 |
| Bande de chant bois véritable non encollée | P1 | ÉCART | N/A | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2D) | 🔴 |
| Bande de chant ABS | P1 | ÉCART | OK *(matière)* | ÉCART | À VÉRIFIER | ÉCART | À VÉRIFIER | OUI | OUI | OUI | RÉALISÉE (2D) | 🟣 |
| Bande de chant PVC *(place relative à revalider, Nicolas 2026-09-15)* | P1 | ÉCART | OK *(matière)* | À VÉRIFIER *(indice partiel)* | À VÉRIFIER | ÉCART | À VÉRIFIER | OUI | OUI | OUI | RÉALISÉE (2D) | 🟣 |
| Bande de chant PE / polyéthylène *(nouvel objet, Nicolas 2026-09-15)* | P1 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |

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
| Colle PVAc / PVA blanche | P1 | ÉCART *(monomère seul)* | ÉCART | ÉCART | N/A *(Global)* | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2F) | 🔴 |
| Adhésif thermofusible EVA hot-melt | P1 | ÉCART *(résine seule)* | ÉCART | À VÉRIFIER | N/A *(Global)* | ÉCART | N/A | À VÉRIFIER | OUI | OUI | RÉALISÉE (2F) | 🟣 |
| Colle contact *(formulations à base d'eau pertinentes aujourd'hui, Nicolas 2026-09-15)* | P1 | ÉCART *(aucune brique)* | ÉCART | ÉCART | N/A | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2F) | 🔴 |
| Colle polyuréthane / PUR | P2 | ÉCART *(précurseurs seuls)* | ÉCART | ÉCART | À VÉRIFIER | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI | RÉALISÉE (2F) | 🔴 |

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
| Charnière invisible de meuble *(priorisé, Nicolas)* | P1 | ÉCART | ÉCART *(nomenclature absente)* | N/A | N/A | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI *(bloquant)* | RÉALISÉE (2D) | 🔴 |
| Coulisse de tiroir *(priorisé + modèle fournisseur de référence à choisir, Nicolas)* | P1 | ÉCART | ÉCART *(nomenclature absente)* | N/A | N/A | ÉCART | N/A | À VÉRIFIER | À VÉRIFIER | OUI *(bloquant)* | RÉALISÉE (2D) | 🔴 |
| Poignée de meuble métallique *(priorisé, Nicolas)* | P1 | ÉCART | À VÉRIFIER *(alu conditionnel)* | À VÉRIFIER | N/A | ÉCART | N/A | À VÉRIFIER | OUI | OUI | RÉALISÉE (2D) | 🟣 |
| Pied niveleur / niveleur *(priorisé, Nicolas)* | P1 | ÉCART | À VÉRIFIER *(PP conditionnel)* | À VÉRIFIER | N/A | ÉCART | N/A | À VÉRIFIER | OUI | OUI | RÉALISÉE (2D) | 🟣 |
| Ferrure métallique de suspension (French cleat) *(priorisé, Nicolas)* | P1/P2 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |

## 8. Emballage

| Produit métier | Prio | Produit/fonction | Composition | Techno/procédé | Géographie | Données QC | Adapt. géo | Proxy | Reconstr. | Info fourn. | Analyse | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Carton d'emballage / carton ondulé | P1 | OK | À VÉRIFIER *(linerboard)* | OK | OK *(fort, QC)* | À VÉRIFIER *(2008)* | NON | NON | NON | À VÉRIFIER | RÉALISÉE (2A) | 🟡 |
| Film à bulles / papier bulle | P1 | À VÉRIFIER | N/A | N/A | N/A | N/A | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | À VÉRIFIER | NON RÉALISÉE | 🟡 |
| Matériau d'emballage blanc fin en rouleau *(identification à confirmer, nouvel objet Nicolas 2026-09-15)* | P1/P2 | N/A *(identification non confirmée)* | N/A | N/A | N/A | N/A | N/A | N/A | N/A | OUI *(bloquant)* | NON RÉALISÉE | 🟡 |

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
| 🟢 Utilisable | 1 |
| 🟡 À valider | 22 |
| 🟠 À adapter | 7 |
| 🟣 À reconstruire | 9 |
| 🔴 Lacune majeure | 14 |

| État de l'analyse Ecoinvent | Nombre de produits |
|---|---|
| RÉALISÉE | 37 |
| PARTIELLE | 3 |
| NON RÉALISÉE | 13 |

**Lecture de ce décompte :** ces chiffres ne mesurent qu'une chose — combien de produits métier portent chaque étiquette de statut ou d'avancement dans les diagnostics déjà sourcés. Ils ne pondèrent pas par masse, par fréquence d'usage réelle en atelier, ni par contribution probable à l'impact du meuble fini ; ils ne doivent donc pas être lus comme une priorisation implicite. La priorisation reste celle établie par Nicolas (sections 7, 8 et par produit ci-dessus) et par les priorités P1/P2 du référentiel.

---

## Points de vigilance transversaux

1. **Les adhésifs et les surfaces de panneaux sont les deux familles les plus systématiquement en `ÉCART`** sur le produit/fonction : dans les deux cas (Lots 2E et 2F), Ecoinvent ne propose généralement que des précurseurs chimiques ou des substrats bruts, jamais le produit fini métier.
2. **Le statut 🟢 Utilisable n'apparaît qu'une fois** dans l'ensemble du diagnostic à ce stade — l'eau de procédé/nettoyage (Lot 2G-bis, dataset régional Québec identifié). C'est aussi le seul cas où une variante géographique `Québec` a été directement trouvée et validée comme fonctionnellement pertinente.
3. **Le renommage du contreplaqué (merisier/yellow birch/Baltic plywood)** illustre un cas où la taxonomie métier a changé mais où l'analyse Ecoinvent sous-jacente n'a pas encore suivi — d'où le statut `PARTIELLE` distinct de `RÉALISÉE`. Voir la [liste structurée pour la prochaine passe OpenLCA](prochaine-passe-openlca.md).
4. **Six objets nouvellement ajoutés le 2026-09-15** (papier mélaminé en atelier, bande de chant PE, matériau d'emballage blanc en rouleau, et implicitement les priorités quincaillerie reformulées) n'ont encore fait l'objet d'aucune recherche Ecoinvent — ils sont candidats naturels pour la prochaine passe OpenLCA.
5. **Dix objets (Données transversales) sont désormais en phase ultérieure** par décision de Nicolas, malgré un diagnostic déjà réalisé (Lot 2G/2G-bis) : ce tableau les conserve pour la traçabilité, mais ils ne doivent pas orienter les priorités de travail immédiates.

---

*Ce tableau consolide exclusivement des analyses déjà sourcées dans le dépôt (`docs/diagnostic/ecoinvent-representativite-qc-lot-2{a..g}.md`, `docs/materiaux-ebenisterie.md`) et les décisions de validation métier du 2026-09-15. Aucune recherche openLCA/MCP n'a été effectuée pour produire ce document. Voir la version tabulaire complète : [`tableau-transversal-lacunes-ecoinvent.csv`](tableau-transversal-lacunes-ecoinvent.csv).*
