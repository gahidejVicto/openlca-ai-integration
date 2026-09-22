# Référentiel des matériaux et composants — Ébénisterie

> **Statut : V6 — vue consolidée du diagnostic Ecoinvent + validation métier Nicolas (2026-09-15) + réconciliation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16, corrigée) + passe ciblée matériau d'emballage et clôture de recherches (2026-09-22)**
> Ce document reste l'inventaire métier des produits et composants réellement achetés ou utilisés en atelier. Il intègre, pour les matériaux déjà approfondis, les conclusions des diagnostics de représentativité Ecoinvent (Lots 2A à 2G) ainsi que les décisions de validation métier prises en réunion avec Nicolas le 2026-09-15. Cette réunion a confirmé l'approche générale du diagnostic : l'objectif actuel **n'est pas** de calculer quantitativement les impacts ni de régionaliser les datasets, mais d'identifier et de qualifier les écarts entre les données Ecoinvent disponibles et la réalité de l'ébénisterie québécoise. Un rapport final plus synthétique sera produit ultérieurement ; ce document reste volontairement détaillé et traçable. Les matériaux non encore approfondis conservent leur statut prudent d'origine.
>
> **Session sans accès OpenLCA (2026-09-15)** : les décisions de taxonomie/priorisation de Nicolas (renommage du contreplaqué merisier/bouleau jaune, papier mélaminé en atelier, bande de chant PE, précisions adhésifs, quincaillerie, emballages) ont été intégrées comme des décisions **métier**, pas des résultats de recherche Ecoinvent.
>
> **Correction (2026-09-16, passe corrective) :** une première réconciliation OpenLCA avait été intégrée par erreur dans le commit `aaabecd` alors que la mauvaise base OpenLCA (`cups`) était ouverte après un changement de poste de travail — tous ses résultats (UUID, géographies, résultats nuls, conclusions, anomalie `database_family: "flcac"`) sont invalidés. Une nouvelle interrogation complète, réalisée depuis zéro sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` (`database_family` forcé et confirmé à `ecoinvent`, 25 412 processus / 14 051 flux / 0 méthode), remplace intégralement ces résultats dans les fiches ci-dessous. Voir le fichier corrigé [`diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md`](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) et ses deux comptes rendus bruts, [`diagnostic/mcp-ecoinvent-3.11-partie-1.md`](diagnostic/mcp-ecoinvent-3.11-partie-1.md) et [`diagnostic/mcp-ecoinvent-3.11-partie-2.md`](diagnostic/mcp-ecoinvent-3.11-partie-2.md). L'anomalie `database_family: "flcac"` est résolue (cause : mauvaise base ouverte, pas une anomalie Ecoinvent) — voir la section dédiée en fin de document.
>
> Le [tableau transversal des lacunes](diagnostic/tableau-transversal-lacunes-ecoinvent.md) et la [synthèse des spécificités québécoises](specificites-quebecoises.md) complètent ce document.

## Rôle de cet index

Ce document répond à trois questions : **quels matériaux et composants d'ébénisterie devons-nous couvrir**, **quel est l'état du diagnostic Ecoinvent pour chacun**, et **quelle action reste à faire avant une implémentation openLCA**. Il constitue la vue consolidée et lisible du projet ; les preuves techniques détaillées (exchanges, comparaisons quantitatives, UUID complets, recherches process/flow) restent dans les diagnostics de la Section [Diagnostics de représentativité](#diagnostics-de-représentativité) et dans les [fiches d'inventaire détaillé](inventaire/README.md).

La taxonomie part du produit ou du composant acheté : par exemple, une bande de chant ABS, une charnière invisible ou un panneau MDF mélaminé/TFL acheté fini. Une décomposition en matières et procédés n'est envisagée que lorsque Ecoinvent ne propose pas de produit ou de composant suffisamment représentatif — c'est précisément ce que les diagnostics ci-dessous ont vérifié pour 20 matériaux prioritaires.

## Légende des priorités

| Priorité | Signification |
|---|---|
| **P1** | Incontournable ou très fréquent dans la fabrication de meubles et d'éléments d'ébénisterie |
| **P2** | Fréquent, mais dépend davantage du produit, du procédé ou de l'atelier |
| **P1/P2** | Usage réel dont la priorité précise reste à confirmer |

## Légende des statuts

Les statuts indiquent le niveau d'adéquation entre le produit métier utilisé
en ébénisterie québécoise et les données disponibles dans Ecoinvent.

| Statut | Signification |
|---|---|
| 🟢 **Utilisable** | Correspondance suffisante telle quelle ou avec une validation mineure. |
| 🟡 **À valider** | Candidat à valider ou représentativité encore à diagnostiquer. |
| 🟠 **À adapter** | Dataset pertinent, mais sa géographie, sa composition ou sa technologie doit être adaptée au contexte québécois. |
| 🟣 **À reconstruire** | Le produit métier n'existe pas directement dans Ecoinvent, mais une reconstruction à partir de plusieurs datasets ou procédés est plausible. |
| 🔴 **Lacune majeure** | Les données disponibles sont insuffisantes pour construire actuellement un modèle défendable : produit, composition ou procédé essentiel manquant. |

> **Important :** la présence d'un dataset localisé `Canada, Quebec` ne signifie
> pas automatiquement qu'il repose sur des données primaires québécoises.
> La représentativité physique, technologique et géographique est évaluée
> séparément.

---

## 1. Panneaux

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Panneau de particules brut | Dataset identifié | Bonne physiquement | technologie étrangère | 🟠 À adapter |
| P1 | MDF brut | Dataset identifié | Bonne physiquement | technologie étrangère | 🟠 À adapter |
| P1 | Contreplaqué merisier / bouleau jaune (yellow birch) / Baltic plywood | Vérifié sur Ecoinvent 3.11 (2026-09-16) : `plywood production`, Canada-Quebec (proxy, copie administrative) | Proxy (essence hardwood générique ≠ bouleau ; géographie CA-QC non représentative) | essence non représentée ; géographie CA-QC = copie du dataset Europe | 🟠 À adapter |
| P1 | Panneau de particules mélaminé / TFL | Matière + procédé | Partielle | produit fini absent | 🟣 À reconstruire |
| P1 | MDF mélaminé / TFL | Matière + procédé | Partielle | produit fini absent | 🟣 À reconstruire |
| P1 | MDF plaqué bois acheté fini | Lot 2E : substrat seul disponible | Faible | placage + procédé de collage absents | 🔴 Lacune majeure |
| P1 | Panneau de particules plaqué bois acheté fini | Lot 2E : substrat seul disponible | Faible | placage + procédé de collage absents | 🔴 Lacune majeure |
| P2 | HDF brut | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | OSB | Analyse approfondie non réalisée — **déprioritisé (décision Nicolas, 2026-09-15)** | Non établie | hors périmètre actuel | 🟡 À valider *(hors priorité)* |
| P2 | Autre contreplaqué | Dataset identifié — **déprioritisé (décision Nicolas, 2026-09-15)** | Partielle | hors périmètre actuel | 🟠 À adapter *(hors priorité)* |
| P2 | Panneau plaqué en atelier | Pertinent métier confirmé (2026-09-15) ; analyse Ecoinvent non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Les panneaux bruts (particules, MDF) ont un dataset Ecoinvent dont la fonction correspond bien au produit métier, mais dont la recette, l'énergie et les intrants sont d'origine européenne (EPF) et doivent être adaptés avec des données de fabricant québécois. Les panneaux finis mélaminés/TFL n'existent pas comme produit direct dans Ecoinvent : le meilleur modèle plausible combine le panneau brut et un service générique de revêtement mélaminé, ce qui reste une reconstruction non validée. Le contreplaqué constitue un cas particulier, **reprécisé en réunion de validation métier le 2026-09-15** : le produit métier visé n'est pas un « bouleau russe » générique mais un **contreplaqué merisier / yellow birch / Baltic plywood (contreplaqué baltique)**. **Mise à jour (interrogation OpenLCA vérifiée sur Ecoinvent 3.11, 2026-09-16) :** le meilleur candidat disponible est `plywood production`, localisé **Canada, Quebec** (UUID `5538194d-…`) — le même dataset déjà identifié au Lot 2A, désormais **reconfirmé indépendamment** dans Ecoinvent 3.11. Ce n'est toutefois pas une correspondance représentative : c'est une copie administrative du dataset Europe (même échantillon allemand, même colle urée-formaldéhyde), et la localisation CA-QC ne signifie pas représentativité québécoise. Voir la fiche ci-dessous pour le détail. Les panneaux achetés déjà plaqués (bois) disposent désormais d'un diagnostic (Lot 2E) : le substrat brut est connu, mais ni le placage fini ni un procédé de collage/pressage spécifique n'ont été identifiés. Le HDF et le placage en atelier n'ont pas encore fait l'objet d'une analyse Ecoinvent approfondie. L'OSB et l'« autre contreplaqué » sont déprioritisés pour l'instant (décision Nicolas, 2026-09-15) : ils ne sont pas retirés de la taxonomie, mais ne constituent plus une cible active du diagnostic.

> **Règle métier :** les panneaux sont achetés déjà plaqués autant que possible. Le placage en atelier reste néanmoins une pratique pertinente en ébénisterie architecturale (confirmé 2026-09-15) — voir sa fiche ci-dessous. Un dataset localisé `CA-QC` n'est pas représentatif du Québec du seul fait de sa géographie : ses intrants, paramètres et hypothèses technologiques doivent être analysés.

### Panneau de particules brut — P1

#### Produit métier

Panneau de particules brut, non revêtu, acheté par l'atelier comme support de fabrication.

#### Équivalent Ecoinvent identifié

- **Dataset :** `market for particleboard, uncoated` (mix RoW composé à ~78,6 % de production EPF Europe `particleboard production, uncoated, average glue mix` et à ~21,4 % de production `from virgin wood` extrapolée depuis un dataset brésilien à base d'eucalyptus)
- **UUID :** `7690ac93-cf92-32dd-b2cf-68e6c7fcf673` (marché RoW) ; production EPF `1bb7e5df-a7f8-39c2-9a2b-2c5416358f75` ; production virgin wood `7e506572-66ec-3f0d-b73d-4e1343a8e64d`
- **Location :** Rest of World (mélange de technologies non québécoises)
- **Unité / base de comparaison :** m³

#### Correspondance

- **Produit / fonction :** Bonne — le dataset EPF cite explicitement l'usage mobilier (norme EN 312).
- **Composition / matière :** Faible — bois recyclé/résidus européens et eucalyptus brésilien vierge, mix de liants (UF, MF, phénolique, MDI) non confirmé pour le Québec.
- **Technologie / procédé :** Moyenne — le principe du pressage à chaud est générique et potentiellement transférable.
- **Géographie :** Faible — marché mondial mélangeant deux technologies non nord-américaines.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Le marché `RoW` n'est pas une technologie unique mais un mélange de deux origines étrangères (EPF Europe et extrapolation brésilienne). Le mix de bois, le système de liants et le profil énergétique (électricité, gaz naturel, fuel léger) proviennent de données EPF et ne peuvent pas être présumés représentatifs du Québec. Il s'agit d'une lacune de technologie étrangère plutôt que d'une absence de produit : la fonction du panneau est correctement représentée, mais sa composition et son énergie ne le sont pas.

#### Données nécessaires

Essences/mix bois réel, part de bois vierge vs recyclé, système de liant et dosage, densité, consommation électrique et thermique mesurée par le fabricant.

#### Recommandation

**Adapter/régionaliser le dataset existant.** Conserver la structure générique (pressage à chaud) mais remplacer le mix bois/liants/énergie par des données de fabricant québécois avant utilisation dans un modèle défendable.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2B](diagnostic/ecoinvent-representativite-qc-lot-2b.md)

---

### MDF brut — P1

#### Produit métier

MDF brut, non revêtu, acheté par l'atelier comme support de fabrication (plateaux, façades, surfaces profilées, substrat pour peinture/film/placage).

#### Équivalent Ecoinvent identifié

- **Dataset :** `market for medium density fibreboard` (RoW, identique techniquement à la production `medium density fibreboard production, uncoated` Europe)
- **UUID :** marché RoW `eef398de-7420-330d-b894-1440a0afa155` ; production RoW `daa9fa1a-d57f-38d6-a172-3243464ba2b5` ; production Europe `ff6070a5-a826-3cde-a4b7-6c4c95d36423`
- **Location :** Rest of World (copie technologique de la version Europe)
- **Unité / base de comparaison :** m³

#### Correspondance

- **Produit / fonction :** Bonne — la description EPF cite directement les usages mobilier visés.
- **Composition / matière :** Faible — bois européen résiduel et recyclé, système UF + MF non confirmé pour le Québec.
- **Technologie / procédé :** Moyenne — défibrage + pressage à chaud, générique et potentiellement transférable.
- **Géographie :** Faible — le dataset `RoW` est une copie exacte, ligne par ligne, de la version Europe.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

La comparaison quantitative confirme que le dataset `RoW` reproduit exactement les intrants et l'énergie de la version Europe : il n'apporte pas de technologie nord-américaine ou québécoise distincte. La consommation de gaz naturel (1068 MJ) domine le profil énergétique et n'a pas été vérifiée pour le contexte québécois. C'est une lacune de technologie étrangère : la correspondance fonctionnelle est forte, mais l'origine des données ne l'est pas.

#### Données nécessaires

Mix de résines (UF/MF) et dosage réel, essences et part recyclée, densité, consommation électrique et thermique mesurée par le fabricant.

#### Recommandation

**Adapter/régionaliser le dataset existant.** La correspondance métier est forte ; seuls le profil énergétique et le mix matière nécessitent une confrontation aux données de fabricant québécois.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2B](diagnostic/ecoinvent-representativite-qc-lot-2b.md)

---

### Contreplaqué merisier / bouleau jaune (yellow birch) / Baltic plywood — P1

> **Changement d'appellation (validation métier Nicolas, 2026-09-15) :** cette entrée s'appelait auparavant « Contreplaqué de bouleau russe ». Le produit métier réellement visé est un **contreplaqué de merisier / yellow birch / Baltic plywood (contreplaqué baltique)**, et non un contreplaqué de « bouleau russe » à proprement parler. Voir aussi l'entrée « Merisier / bouleau jaune massif » de la section [Bois massif](#4-bois-massif) (Lot 2C, Suède) — chaîne distincte pour le bois massif, à ne pas confondre avec la présente entrée.
>
> **Mise à jour (interrogation OpenLCA vérifiée sur Ecoinvent 3.11, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** une première réconciliation avait été intégrée par erreur alors que la mauvaise base OpenLCA (`cups`) était ouverte ; ses résultats (dataset `plywood, for indoor use`, UUID `a263faad-…`, essence hêtre) sont **invalidés en totalité**. Une nouvelle recherche exhaustive a été menée depuis zéro sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` (`plywood`, `birch`, `yellow birch`, `veneer`, `veneer sheet`, `laminated wood`, `Baltic`, `laminated`, plus exploration complète de la catégorie ISIC 1621). **Aucun dataset « veneer sheet », « Baltic », « yellow birch » ou spécifique au bouleau/merisier n'a été trouvé**, dans cette base et avec ces requêtes.

#### Produit métier

Contreplaqué de merisier / bouleau jaune (yellow birch) / Baltic plywood (contreplaqué baltique), produit distinct dans la taxonomie métier, non substituable d'emblée par un contreplaqué générique.

#### Équivalent Ecoinvent identifié

**Candidats vérifiés sur Ecoinvent 3.11 (2026-09-16) :**

| Dataset | Géographie | Unité | UUID | Constat |
|---|---|---|---|---|
| `market for plywood` | Europe | m³ | `e0fc51ba-b92d-3f5a-909a-6143109d0356` | Générique, non spécifique à l'essence |
| `market for plywood` | Rest of World | m³ | `b21f0829-ca70-3f94-864b-5fe4c57923f6` | Idem |
| `plywood production` | Europe | m³ | `0f52041a-b664-357b-ab50-e48613bff63d` | Basé sur un échantillon **allemand**, bois de sciage/déroulage « hardwood » non spécifié, colle urée-formaldéhyde |
| `plywood production` | Rest of World | m³ | `0b187a5a-6067-3f0f-8fa8-39f3d6ac6721` | **Copie du dataset RER** (« created as copy of the corresponding local dataset for Europe ») |
| `plywood production` | **Canada, Quebec** | m³ | `5538194d-92b2-3020-bb3e-fbc59cb71248` | **Copie du dataset RER**, même échantillon allemand — la description du dataset le dit explicitement — **candidat retenu ci-dessous** |
| `three and five layered board` (production + marché) | Rest of World | m³ | `b878e1de-ef8c-300b-ae44-bcfd95de07ee` | **Rejeté, faux-ami explicite** : lamelles de bois massif sciées, aboutées et collées PVAc — un panneau structurel massif, pas du contreplaqué de placages |
| `hardwood forestry, birch` (sawlog and veneer log) | Sweden | m³ | `885df1ec-96c0-32a2-a869-70779dc48420` | Bois rond en forêt, pas un produit fini |

> **Cohérence avec le Lot 2A :** le dataset `plywood production | Canada, Quebec` (`5538194d-…`) et son comparatif Europe (`0f52041a-…`) avaient déjà été identifiés au Lot 2A, avant la contamination `cups`. Ils sont ici **reconfirmés indépendamment** par la nouvelle interrogation Ecoinvent 3.11 — l'écart de représentativité constaté au Lot 2A (copie administrative, échantillon allemand) est donc désormais établi deux fois, sur deux bases distinctes.

#### Correspondance

- **Produit / fonction :** Bonne pour un contreplaqué générique ; aucun produit spécifique bouleau/Baltic n'existe.
- **Composition / matière :** **Écart confirmé, pas une supposition** — le dataset documente explicitement une essence « hardwood » générique, non spécifiée, sur un échantillon allemand. Aucune variante ne représente le bouleau/merisier ni le Baltic birch.
- **Technologie / procédé :** Colle urée-formaldéhyde générique, potentiellement différente des colles typiques du Baltic birch (phénol-formaldéhyde) ; nombre de plis et épaisseur non documentés.
- **Géographie :** Le dataset « Canada, Quebec » est une **copie administrative** du dataset Europe (même échantillon allemand) — aucune donnée réelle québécoise (essence, procédé, mix électrique) n'y est intégrée. La localisation CA-QC ne signifie pas représentativité québécoise.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

**Niveau de correspondance : PROXY / ÉCART** (aucune correspondance directe ni partielle spécifique à l'espèce bouleau, confirmé par interrogation directe sur Ecoinvent 3.11). La base ne contient, pour la fonction « contreplaqué », que des datasets à essence « hardwood » générique, avec le même échantillon allemand recopié sous les étiquettes Europe, Rest-of-World et Canada-Quebec — c'est un écart de composition documenté par la base elle-même, pas une supposition externe. Aucun dataset plus spécifique au bouleau/Baltic n'a été trouvé ; ceci documente une **absence dans cette base, avec ces requêtes** — pas une absence générale ou définitive de toute version d'Ecoinvent.

#### Données nécessaires

Essence réelle, type de colle, origine géographique réelle du bois ; configuration des plis, données de fabricant si une reconstruction plus précise est un jour envisagée.

#### Recommandation

**Conserver `plywood production`, Canada-Quebec (UUID `5538194d-92b2-3020-bb3e-fbc59cb71248`) comme meilleur candidat disponible, sans le présenter comme représentatif du Québec** : c'est une copie administrative du dataset Europe, documenter explicitement l'écart d'essence (hardwood générique, jamais bouleau) et l'absence de données réelles québécoises. Rechercher des données fabricant (fournisseurs de Baltic birch plywood) ; envisager une reconstruction à partir de `sawlog and veneer log, hardwood` + procédé de contreplaqué générique si une précision devient nécessaire.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md) (candidat `plywood production`, Canada-Quebec, reconfirmé) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

### Panneau de particules mélaminé / TFL — P1

#### Produit métier

Panneau de particules mélaminé/TFL acheté fini par l'atelier ; la mélamine n'est pas appliquée en atelier.

#### Équivalent Ecoinvent identifié

- **Produit fini :** aucun produit fini pertinent n'a été identifié par les recherches process (`melamine faced particleboard`, `thermally fused laminate`, `decorative particleboard`, `laminated particleboard`, `coated particleboard`) et flow disponibles ; l'absence est fortement indiquée par ces méthodes, sous réserve des limites de l'outil d'interrogation.
- **Briques disponibles :** panneau de particules brut (voir fiche ci-dessus) + `coating service, melamine impregnated paper, double-sided`
- **UUID (service de revêtement) :** `4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78`
- **Location :** Europe (plusieurs usines)
- **Unité / base de comparaison :** m² pour le service (0,604 kg/m² de papier mélaminé, deux faces, 302 g/m²/face) ; m³ pour le substrat — une hypothèse d'épaisseur est nécessaire pour relier les deux unités.

#### Correspondance

- **Produit / fonction :** Partielle — la reconstruction représente le papier décor, son grammage et l'énergie de thermofusion, mais l'atelier achète un panneau fini et ne réalise pas le laminage.
- **Composition / matière :** Bonne physiquement pour le service de revêtement (grammage cohérent, 0,604 kg/m² = 2 × 0,302 kg/m²/face) ; le substrat reste soumis aux lacunes du panneau brut.
- **Technologie / procédé :** Moyenne — service générique déclaré applicable par Ecoinvent à différents panneaux à base de bois, sans validation physique indépendante spécifique au particleboard.
- **Géographie :** Faible — service localisé en Europe.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucun produit fini pertinent n'a été identifié par les recherches process et flow disponibles : l'absence est fortement indiquée par la convergence de ces deux méthodes, sous réserve des limites de l'outil d'interrogation. Le modèle proposé (substrat + service de revêtement) est une reconstruction plausible mais non validée : les émissions atmosphériques de la presse ne sont pas quantifiées, l'infrastructure de laminage n'est pas vérifiée, les pertes ne sont pas documentées, et une hypothèse d'épaisseur est nécessaire pour convertir le m³ du substrat en m² du revêtement. Le liant mélamine-formaldéhyde interne au panneau brut est un liant distinct de la mélamine du papier décor ; il ne faut pas les confondre.

#### Données nécessaires

Épaisseur du panneau, nombre de faces, grammage réel du papier décor, données d'émissions de presse si disponibles, en plus des données nécessaires au panneau de particules brut.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous réserve explicite.** Documenter les limites (émissions non quantifiées, conversion d'unité, généricité du service) avant toute utilisation comme donnée de produit fini.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2B](diagnostic/ecoinvent-representativite-qc-lot-2b.md)

---

### MDF mélaminé / TFL — P1

#### Produit métier

MDF mélaminé/TFL acheté fini par l'atelier ; la mélamine n'est pas appliquée en atelier.

#### Équivalent Ecoinvent identifié

- **Produit fini :** aucun produit fini pertinent n'a été identifié par les recherches process (`thermally fused laminate MDF`, `TFL MDF`, `melamine faced MDF`, `melamine coated MDF`, `decorative MDF`, `coated MDF`, `laminated MDF`) et flow disponibles, qui ne retournent qu'un MDF générique non revêtu ; l'absence est fortement indiquée par ces méthodes, sous réserve des limites de l'outil d'interrogation.
- **Briques disponibles :** MDF brut (voir fiche ci-dessus) + `coating service, melamine impregnated paper, double-sided`
- **UUID (service de revêtement) :** `4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78`
- **Location :** Europe
- **Unité / base de comparaison :** m² pour le service ; m³ pour le substrat, avec la même hypothèse d'épaisseur que pour le particleboard TFL.

#### Correspondance

- **Produit / fonction :** Partielle — même logique de reconstruction que pour le particleboard TFL.
- **Composition / matière :** Moyenne — Ecoinvent affirme la généricité du service pour différents panneaux à base de bois, sans modéliser de dépendance à la porosité, densité ou rugosité du substrat.
- **Technologie / procédé :** Moyenne — hérite des lacunes du MDF brut.
- **Géographie :** Faible.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Comme pour le particleboard, aucun produit fini pertinent n'a été identifié par les méthodes d'interrogation disponibles. La généricité déclarée du service de revêtement (applicable « à différents panneaux à base de bois ») est une déclaration de modèle Ecoinvent, pas une validation physique indépendante du comportement MDF + papier mélaminé. Ce point doit être vérifié séparément s'il s'avère sensible.

#### Données nécessaires

Épaisseur, nombre de faces, grammage réel du papier décor, données d'émissions de presse si disponibles, en plus des données nécessaires au MDF brut.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous réserve explicite.** Vérifier en particulier si le comportement de pressage MDF + papier mélaminé diffère significativement de celui du particleboard avant de réutiliser le même service sans réserve.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2B](diagnostic/ecoinvent-representativite-qc-lot-2b.md)

---

### MDF plaqué bois acheté fini — P1

#### Produit métier

Panneau MDF plaqué bois, acheté fini ; le support et le placage ne sont pas séparés d'emblée dans la taxonomie. **Pratique métier confirmée (2026-09-15) :** l'atelier privilégie l'achat déjà plaqué ; le placage en atelier (cas B ci-dessous) reste une pratique pertinente en ébénisterie architecturale, et le placage peut y être collé à la PVA sous presse chaude.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2E** (fiche « panneau plaqué bois acheté fini », commune au support MDF et particules) :

- **Substrat MDF brut :** `market for medium density fibreboard`, UUID `eef398de-7420-330d-b894-1440a0afa155`, Rest-of-World (copie Europe) — voir fiche MDF brut ci-dessus.
- **Placage fini :** aucun produit fonctionnel identifié (`veneered MDF`, `veneered fibreboard`, `wood faced panel`, `furniture board` et variantes — 0 résultat).
- **Procédé de collage/pressage du placage :** aucun procédé spécifique identifié (`wood lamination`, `wood pressing`, `veneer gluing` — 0 résultat).
- **Adhésif réel de ce collage industriel :** non caractérisé dans ce lot ; sa correspondance Ecoinvent n'a pas été établie (distinct de la colle PVAc/PVA d'atelier documentée dans la fiche Adhésifs, qui concerne un usage différent — le collage en atelier, cas B).

#### Correspondance

- **Produit / fonction :** Aucune pour le produit fini recherché — seul le substrat brut est disponible.
- **Composition / matière :** Substrat connu (MDF, voir fiche ci-dessus) ; placage et adhésif de collage non caractérisés.
- **Technologie / procédé :** Aucun procédé de collage/pressage de placage identifié.
- **Géographie :** Celle du substrat seul (non-QC).
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

**Produit fonctionnel absent.** Le substrat brut (MDF) est disponible et déjà diagnostiqué (Lot 2B), mais ni le placage fini ni un procédé spécifique de collage/pressage n'ont été identifiés avec les méthodes d'interrogation disponibles au Lot 2E ; l'adhésif réel utilisé industriellement pour ce produit reste à déterminer.

#### Données nécessaires

Essence et grammage du placage, type d'adhésif de collage réellement utilisé par le fabricant du panneau (aucune hypothèse de départ disponible), température/pression de pressage si pertinent, substrat réel (MDF confirmé ou variante), pertes de production.

#### Recommandation

**Données insuffisantes pour décider.** Ne pas utiliser le substrat brut seul comme proxy du panneau plaqué fini sans avertissement explicite ; traiter comme en attente jusqu'à ce que la fiche « placage bois » (ci-dessous) évolue et que l'adhésif industriel réel soit caractérisé.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2E](diagnostic/ecoinvent-representativite-qc-lot-2e.md)

---

### Panneau de particules plaqué bois acheté fini — P1

#### Produit métier

Panneau de particules plaqué bois, acheté fini ; le support et le placage ne sont pas séparés d'emblée dans la taxonomie. Mêmes considérations de pratique métier que le MDF plaqué (ci-dessus) : achat déjà plaqué privilégié, placage en atelier pertinent en ébénisterie architecturale, collage à la PVA sous presse chaude possible.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2E**, même fiche que le MDF plaqué (structure d'assemblage commune) :

- **Substrat particules brut :** `market for particleboard, uncoated`, UUID `7690ac93-cf92-32dd-b2cf-68e6c7fcf673`, Rest-of-World (mélange Europe/Brésil) — voir fiche panneau de particules brut ci-dessus.
- **Placage fini et procédé de collage/pressage :** mêmes constats que pour le MDF plaqué — aucun produit ni procédé identifiés.

#### Correspondance

Identique au MDF plaqué bois acheté fini ci-dessus, avec le substrat particules (Lot 2B) au lieu du MDF.

#### Lacune Ecoinvent

Même lacune que le MDF plaqué : **produit fonctionnel absent**, seul le substrat brut est disponible.

#### Données nécessaires

Identiques au MDF plaqué bois acheté fini ci-dessus, avec confirmation du substrat réel (particules).

#### Recommandation

**Données insuffisantes pour décider.** Même réserve que pour le MDF plaqué : ne pas utiliser le substrat seul comme proxy sans avertissement explicite.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2E](diagnostic/ecoinvent-representativite-qc-lot-2e.md)

---

### HDF brut — P2

#### Produit métier

Panneau HDF brut, non revêtu.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. Par analogie méthodologique avec le MDF et le panneau de particules bruts (Lot 2B), un dataset générique européen est plausible, mais cela reste à vérifier et ne doit pas être présumé.

#### Données nécessaires

À déterminer.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### OSB — P2

> **Déprioritisé (décision Nicolas, 2026-09-15) :** cet objet reste dans la taxonomie mais n'est plus une cible active du diagnostic pour l'instant. Il n'est pas retiré, seulement mis en attente au profit des familles jugées prioritaires par Nicolas.

#### Produit métier

Panneau OSB.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade — hors périmètre actuel.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit ; sa recherche est reportée à une phase ultérieure.

#### Données nécessaires

À déterminer si cet objet redevient prioritaire.

#### Recommandation

**Données insuffisantes pour décider ; hors périmètre actuel.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Autre contreplaqué — P2

> **Déprioritisé (décision Nicolas, 2026-09-15) :** cet objet reste dans la taxonomie mais n'est plus une cible active du diagnostic pour l'instant.

#### Produit métier

Contreplaqué générique, catégorie d'usage réel distincte du contreplaqué merisier/yellow birch/Baltic plywood (voir entrée ci-dessus, reprécisée le 2026-09-15) ; candidat à vérifier selon le contreplaqué réellement utilisé.

#### Équivalent Ecoinvent identifié

- **Dataset :** `plywood production | plywood | Cutoff, U` — le même dataset générique évalué en détail pour l'entrée contreplaqué merisier/yellow birch/Baltic plywood ci-dessus (ex-« bouleau russe »), **reconfirmé indépendamment sur Ecoinvent 3.11 le 2026-09-16**.
- **UUID :** `5538194d-92b2-3020-bb3e-fbc59cb71248`
- **Location :** Canada, Quebec (déclaré copie du modèle européen, données allemandes)
- **Unité / base de comparaison :** m³

#### Correspondance

- **Produit / fonction :** Bonne — le produit générique correspond à cette catégorie d'usage « autre contreplaqué ».
- **Composition / matière :** Faible — les quantités technologiques centrales inspectées (sawlog/veneer log hardwood, résine urée-formaldéhyde, énergie) sont identiques ou se recomposent à la même somme qu'à la version RER.
- **Technologie / procédé :** Faible — copie technologique allemande.
- **Géographie :** Trompeuse — la mention `Canada, Quebec` ne démontre pas de données primaires québécoises.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Même lacune technique que pour l'entrée contreplaqué merisier/yellow birch/Baltic plywood ci-dessus : un **dataset CA-QC utilisant en réalité des données étrangères**. La différence tient au produit métier visé : ici, la catégorie « autre contreplaqué » n'exige pas une essence précise, ce qui rend ce dataset générique plus directement utilisable comme candidat, sous réserve d'adaptation de la technologie et de la géographie déclarée.

#### Données nécessaires

Essence et configuration réelles du contreplaqué visé par cette catégorie, données de fabricant pour confirmer ou corriger la recette technologique (bois, résine, énergie).

#### Recommandation

**Adapter/régionaliser le dataset existant.** Utiliser comme candidat générique documenté, en corrigeant les hypothèses technologiques avant tout usage défendable ; voir aussi la [fiche pilote CA-QC](inventaire/panneaux/plywood-ca-qc.md).

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md)

---

### Panneau plaqué en atelier — P2

> **Pertinence métier confirmée (décision Nicolas, 2026-09-15) :** le placage en atelier est une pratique pertinente en ébénisterie architecturale ; il ne doit pas être traité comme un simple cas secondaire résiduel. Le placage peut y être collé à la PVA sous presse chaude — cette précision est une information métier communiquée par Nicolas, pas un résultat de recherche Ecoinvent.

#### Produit métier

Cas où le panneau fini plaqué n'est pas acheté tel quel : support, placage et adhésif (PVA sous presse chaude, selon la pratique atelier) sont alors comptabilisés séparément. Pertinent notamment en ébénisterie architecturale.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.** Ce cas dépend des fiches « panneau brut » (diagnostiquée, Lot 2B), « placage de bois naturel » (diagnostiquée, Lot 2E — produit absent) et « Colle PVAc/PVA blanche » (diagnostiquée, Lot 2F — voir section Adhésifs) ; leurs conclusions respectives s'appliquent mais n'ont pas encore été combinées spécifiquement pour ce cas d'usage atelier avec presse chaude.

#### Correspondance

Non établie pour l'assemblage complet ; voir les fiches composantes individuelles (panneau brut, placage bois, colle PVAc/PVA) pour l'état de chacune.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent dédiée à l'assemblage « support + placage + PVA sous presse chaude » n'a encore été menée. Le placage bois fini lui-même est déjà documenté comme absent d'Ecoinvent (Lot 2E, voir section Surfaces), ce qui limite d'emblée toute reconstruction de ce cas d'atelier tant que cette lacune n'est pas résolue.

#### Données nécessaires

Essence et grammage du placage utilisé en atelier, paramètres de la presse chaude (température, pression, durée), grammage/consommation de colle PVA, en plus des données déjà identifiées pour le panneau brut et le placage.

#### Recommandation

**Données insuffisantes pour décider.** Ce cas dépend directement de la résolution de la lacune « placage bois fini » (Lot 2E) ; prioriser cette dernière avant de tenter une reconstruction complète du panneau plaqué en atelier.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2E](diagnostic/ecoinvent-representativite-qc-lot-2e.md) (placage bois, produit absent) ; [Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md) (colle PVAc/PVA) ; pratique métier confirmée 2026-09-15.

---

## 2. Surfaces

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Stratifié HPL | Lot 2E : aucune brique de liaison identifiée | Aucune | chaîne de représentation absente | 🔴 Lacune majeure |
| P1 | Placage de bois naturel | Lot 2E : produit fini absent, seule la grume existe | Aucune | transformation grume→placage absente | 🔴 Lacune majeure |
| P1/P2 | Papier mélaminé appliqué en atelier | Datasets vérifiés sur Ecoinvent 3.11 (matière + marché + service d'application) | Partielle forte | simple-face vs double-face non tranché ; échelle atelier vs industriel | 🟡 À valider |

### Lecture rapide

Le Lot 2E a diagnostiqué le stratifié HPL et le placage de bois naturel : dans les deux cas, aucun produit fini n'a été identifié avec les méthodes d'interrogation disponibles, et la chaîne de reconstruction s'arrête plus tôt que pour le TFL (Lot 2B) — le HPL ne dispose que de deux précurseurs chimiques isolés (résine phénolique, papier kraft non imprégné) sans procédé de liaison identifié, et le placage bois s'arrête à la grume forestière générique, plusieurs étapes avant la feuille de placage elle-même. Le placage de bois naturel partage donc, en amont, certaines des lacunes déjà documentées pour le bois massif (essence, traçabilité — voir Lot 2C), mais la lacune principale du placage lui-même est plus fondamentale : aucune transformation (tranchage/déroulage) n'a été identifiée. **Nouveauté (validation métier Nicolas, 2026-09-15) :** le papier mélaminé n'arrive pas toujours déjà appliqué sur le panneau — certaines entreprises réalisent cette opération en atelier, ce qui leur permet de proposer leurs propres collections/couleurs. **Mise à jour (interrogation OpenLCA vérifiée sur Ecoinvent 3.11, 2026-09-16) :** ce cas d'usage a été diagnostiqué de nouveau depuis zéro (la première réconciliation, faite sur la mauvaise base `cups`, est invalidée) — c'est une correspondance partielle forte, la meilleure obtenue à ce jour dans l'ensemble du diagnostic RECQ36 pour un produit fini/appliqué (papier, marché et service d'application distinctement documentés, sans risque de double comptage avec le panneau support), sous réserve du simple-face vs double-face et de l'échelle atelier vs industrielle.

### Stratifié HPL — P1

#### Produit métier

Revêtement stratifié haute pression, utilisé notamment avec une colle contact.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2E**. Recherches process/flow (`high pressure laminate`, `HPL`, `decorative laminate`, `phenolic laminate`, `melamine laminate`, `impregnated paper`, `kraft paper`, ~15 variantes au total) : aucun produit fini, aucune surface, aucun procédé de liaison identifiés. Un faux positif plausible (`three layered laminated board production`, UUID `233c8e26-b01d-3b04-80b0-99cab77f2516`, Rest-of-World) a été inspecté et rejeté : il s'agit d'un panneau structurel massif 3 plis en épicéa collé au PVAc (produit de construction), pas d'un stratifié décoratif. Seules deux briques chimiques isolées, sans lien établi entre elles ni avec le produit : `kraft paper, bleached/unbleached` (papier non imprégné) et une résine phénolique brute (Lot 1).

#### Correspondance

- **Produit / fonction :** Aucune.
- **Composition / matière :** Très faible — seulement deux précurseurs chimiques isolés, sans lien établi avec le produit.
- **Technologie / procédé :** Aucune — recherches `lamination` et `hot pressing` sans résultat.
- **Géographie :** Sans objet.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

**Aucune chaîne de représentation exploitable identifiée** avec les méthodes d'interrogation disponibles au Lot 2E — contrairement au TFL (Lot 2B) qui dispose d'un service de revêtement complet et documenté, le HPL ne dispose d'aucune brique intermédiaire (imprégnation, empilage, pressage haute pression) reliant ses deux seuls précurseurs chimiques potentiels au produit fini.

#### Données nécessaires

Structure du produit (grammage, nombre de couches), composition/formulation réelle, masse surfacique/épaisseur du HPL fini, procédé de fabrication réel du fournisseur.

#### Recommandation

**Ne pas tenter de reconstruction avant l'obtention de données fournisseur** sur la composition/formulation réelle et la structure en couches.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2E](diagnostic/ecoinvent-representativite-qc-lot-2e.md)

---

### Placage de bois naturel — P1

#### Produit métier

Placage de bois naturel utilisé pour le cas de placage en atelier (pertinence confirmée en ébénisterie architecturale, voir section Panneaux).

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2E**. Recherches process/flow (`veneer`, `wood veneer`, `veneer sheet`, `sliced veneer`, `rotary veneer`, `decorative veneer`, `veneer production`, `veneered`, ~10 variantes) : aucun résultat pertinent, à tous les niveaux testés. Seule brique en amont : les flows de grume `sawlog and veneer log, [essence]` déjà documentés aux Lots 1/2C (foresterie uniquement, essences européennes : oak/Allemagne, birch/Suède, beech) — la chaîne s'arrête à la grume forestière, plusieurs étapes avant la feuille de placage elle-même (tranchage/déroulage, séchage, découpe aux dimensions non représentés).

#### Correspondance

- **Produit / fonction :** Aucune.
- **Composition / matière :** Faible — grume générique hardwood seulement, essence limitée aux cas déjà documentés au Lot 2C.
- **Technologie / procédé :** Aucune — aucun procédé de tranchage/déroulage identifié.
- **Géographie :** Européenne pour la grume (Allemagne/Suède selon l'essence), sans rapport avec le Québec.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

**Produit fonctionnel absent, et aucune transformation identifiée entre la grume et le placage fini.** La perte de traçabilité de l'essence déjà documentée au Lot 2C (l'essence disparaît au passage du nom de process vers le flow générique `hardwood`) reste valable pour la grume elle-même, mais devient secondaire puisque la chaîne ne va de toute façon pas plus loin que la grume.

#### Données nécessaires

Essence réelle du placage, épaisseur/grammage, méthode de production (tranché/déroulé), dimensions de feuille, rendement de production grume→placage, pertes.

#### Recommandation

**Données insuffisantes pour décider.** Données fournisseur indispensables (essence, grammage, méthode de production) avant toute tentative de proxy ; aucune brique de tranchage n'est actuellement disponible dans Ecoinvent pour amorcer une reconstruction.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2E](diagnostic/ecoinvent-representativite-qc-lot-2e.md)

---

### Papier mélaminé appliqué en atelier — P1/P2

> **Nouvel objet (validation métier Nicolas, 2026-09-15).** Il ne faut pas supposer que le papier mélaminé arrive toujours déjà appliqué sur le panneau : certaines entreprises réalisent elles-mêmes cette opération en atelier, ce qui leur permet de proposer leurs propres collections et couleurs. Cet objet est distinct du panneau mélaminé/TFL acheté fini (voir section Panneaux), qui reste le cas d'achat par défaut.
>
> **Mise à jour (interrogation OpenLCA vérifiée sur Ecoinvent 3.11, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** une première réconciliation avait été intégrée par erreur alors que la mauvaise base OpenLCA (`cups`) était ouverte ; ses UUID (`b2e9c4ee-…`, `55d422f8-…`, `57d226d1-…`) sont **invalidés**. Une nouvelle recherche a été menée depuis zéro sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31`. Ecoinvent distingue effectivement le papier, la résine et le service d'application, sans les confondre avec un panneau déjà mélaminé fini — mais le niveau de correspondance obtenu est **partiel fort**, pas direct : le simple-face vs double-face et l'échelle atelier vs industrielle restent à trancher.

#### Produit métier

Papier décor mélaminé appliqué sur panneau support (particules ou MDF) directement en atelier, plutôt qu'acheté déjà revêtu.

#### Équivalent Ecoinvent identifié

**Candidats vérifiés sur Ecoinvent 3.11 (2026-09-16) :**

| Dataset | Rôle | Géographie | Unité | UUID | Détail vérifié |
|---|---|---|---|---|---|
| `market for paper, melamine impregnated` | Le papier imprégné lui-même | Rest of World | kg | `0a2370fe-1a4c-3401-abae-9143beb78198` | Marché du papier mélaminé |
| `melamine impregnated paper production` | Production du papier | Europe | kg | `8d5fa368-3900-3ebb-9760-9b6d5939bcc7` | Composition détaillée : 0,344 kg kraft paper + 0,377 kg résine mélamine-formaldéhyde + 0,218 kg résine urée-formaldéhyde pour 1 kg de papier fini ; grammage 302 g/m² (dont 104 g/m² de papier de base) |
| `market for coating, with melamine impregnated paper` | **Service d'application** (le procédé recherché) | Global | m² | `24ceb336-520a-3e11-bcd1-9c13efd69c6f` | **Exclut explicitement le panneau support** (« input of wood-based board is excluded and should be added manually ») |
| `coating service, melamine impregnated paper, double-sided` | Application **double face** industrielle | Europe | m² | `4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78` | Consomme 0,604 kg de papier mélaminé par m² de panneau enrobé double face |

> **Cohérence avec le Lot 2B :** le service `coating service, melamine impregnated paper, double-sided` (`4bce9bba-…`) avait déjà été documenté au Lot 2B, avant la contamination `cups`. Il est ici **reconfirmé indépendamment** par cette interrogation Ecoinvent 3.11 — sous le même UUID.
>
> **Distinction préservée / pas de double comptage :** le panneau support et le service d'application du papier mélaminé restent deux flux distincts. Aucun produit « panneau déjà mélaminé fini » n'existe comme dataset unique dans cette base, ce qui évite la confusion signalée dans le mandat.

#### Correspondance

- **Produit / fonction :** Bonne pour le couple matière + service d'application (correspond structurellement à « application en atelier », par opposition à un panneau acheté déjà revêtu).
- **Composition / matière :** Forte — composition et grammage du papier documentés précisément (302 g/m², dont 104 g/m² de support).
- **Technologie / procédé :** **À vérifier** — le service `coating, with melamine impregnated paper` documenté (Global et Europe double-face) est calibré pour une **ligne industrielle**, potentiellement simple face en atelier de PME plutôt que double face ; la représentativité de cette échelle n'est pas confirmée.
- **Géographie :** Rest of World / Europe / Global — aucune résolution CA-QC.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

**Niveau de correspondance : PARTIELLE FORTE / À VÉRIFIER.** Ecoinvent distingue bien matière et procédé d'application, et exclut le panneau support — ce qui correspond structurellement au besoin métier. La lacune résiduelle porte sur la **représentativité d'échelle** (application simple face d'atelier vs ligne double face industrielle) et sur la **géographie** (aucune variante québécoise).

#### Données nécessaires

Vérifier si une application simple face est modélisable en ne prenant qu'une partie du flux « coating » double face (sous réserve de validation méthodologique) ; grammage réellement utilisé en atelier québécois ; nombre de faces réellement traitées, panneau support réel (particules ou MDF).

#### Recommandation

**Utiliser le couple `paper, melamine impregnated` + `coating, with melamine impregnated paper` comme correspondance documentée « partielle forte », pas directe.** Vérifier la représentativité simple-face/double-face et l'échelle atelier vs industrielle avant intégration dans un modèle de quantification.

#### Source du diagnostic

[Lot 2B](diagnostic/ecoinvent-representativite-qc-lot-2b.md) (service de revêtement, UUID reconfirmé) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

## 3. Bandes de chant

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Bande de chant en bois véritable préencollée | Produit direct absent | Faible | produit fini absent | 🔴 Lacune majeure |
| P1 | Bande de chant en bois véritable non encollée | Produit direct absent | Faible | produit fini absent | 🔴 Lacune majeure |
| P1 | Bande de chant ABS | Matière + procédé | Faible | procédé absent | 🟣 À reconstruire |
| P1 | Bande de chant PVC | Matière + procédé | Partielle | procédé absent ; **place relative à revérifier (2026-09-15)** | 🟣 À reconstruire |
| P1 | Bande de chant PE / polyéthylène | Absence confirmée (produit fonctionnel) ; matières génériques disponibles | Aucune | procédé absent (même le film ne reproduit pas un profilé) | 🟣 À reconstruire |

### Lecture rapide

Aucune bande de chant n'existe comme produit fini direct dans Ecoinvent — confirmé pour le bois véritable (Lot 2D) et, par une interrogation vérifiée sur Ecoinvent 3.11 (2026-09-16), également confirmé pour le PE (0 résultat sur `process` et `flows`, requêtes `edge band`/`edge banding`/`edging`). Pour le bois véritable (préencollé ou non), aucune brique de placage ou de bande mince exploitable n'a été trouvée : la lacune commence dès la composante bois elle-même, avant même la question de l'adhésif. Pour l'ABS, le PVC et le PE, la matière de base existe et des procédés de transformation plastique proches existent aussi, mais aucun ne reproduit la géométrie exacte d'une bande de chant ; le PVC dispose d'un indice supplémentaire (un flux de déchet de calandrage spécifique au PVC) qui en fait un proxy légèrement mieux étayé que l'ABS et le PE, sans que cela constitue une validation. Le PVC est conservé dans le référentiel ; sa variante « suspension polymerised » (Lot 2D) a désormais été **reconfirmée indépendamment** sur Ecoinvent 3.11 (voir fiche PVC), mais sa place relative face au PE et à l'ABS reste à revalider sur le plan métier (décision Nicolas, 2026-09-15).

> **Rappel métier :** l'ABS, le PVC et le PE sont décrits ici selon leur usage en bande de chant, et non comme familles de matière autonomes.

### Bande de chant en bois véritable préencollée — P1

#### Produit métier

Bande de chant en bois véritable, achetée avec son adhésif déjà appliqué.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié. Les recherches `edge band`, `edgebanding`, `veneer tape`, `sliced veneer` et `veneer sheet` n'ont retourné aucun produit fini ni brique de placage mince exploitable ; les flows de type `sawlog and veneer log` sont plusieurs étapes trop en amont dans la chaîne de transformation.

#### Correspondance

- **Produit / fonction :** Non établie — aucun produit ou brique de forme utile.
- **Composition / matière :** Non établie.
- **Technologie / procédé :** Non établie.
- **Géographie :** Sans objet.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

C'est un cas de **produit fonctionnel absent** doublé d'une **absence de brique de composition** : il n'existe dans Ecoinvent aucun bois mince/placage exploitable pour amorcer une reconstruction, et la question de l'adhésif préappliqué ne peut donc même pas être posée en second temps.

#### Données nécessaires

Essence, masse ou grammage/épaisseur, largeur, type et grammage de colle, pertes éventuelles à la pose.

#### Recommandation

**Données insuffisantes pour décider.** Une reconstruction n'est pas suffisamment étayée dans Ecoinvent sans brique de placage/bois mince ; obtenir d'abord les données fournisseur avant d'envisager quoi que ce soit.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Bande de chant en bois véritable non encollée — P1

#### Produit métier

Bande de chant en bois véritable, sans adhésif préappliqué ; l'adhésif est comptabilisé séparément en atelier.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié, pour la même raison que la variante préencollée : aucune brique de bois mince/placage exploitable dans Ecoinvent.

#### Correspondance

- **Produit / fonction :** Non établie.
- **Composition / matière :** Non établie.
- **Technologie / procédé :** Non établie.
- **Géographie :** Sans objet.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Même lacune de **produit fonctionnel absent** que la variante préencollée, sans même la complexité additionnelle de l'adhésif.

#### Données nécessaires

Essence, masse ou grammage/épaisseur, largeur, pertes éventuelles.

#### Recommandation

**Données insuffisantes pour décider.** Obtenir d'abord les données fournisseur.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Bande de chant ABS — P1

#### Produit métier

Bande de chant en ABS, décrite selon son usage plutôt que comme famille de matière autonome.

#### Équivalent Ecoinvent identifié

- **Matière :** `market for acrylonitrile-butadiene-styrene copolymer`, UUID `ca074112-8461-32ac-b814-2d7749b7b862`, GLO.
- **Procédé candidat :** `extrusion, plastic pipes`, UUID `8bb6fcd6-e6dc-3397-ae07-499a2f71be3c`, RoW — géométrie de tuyau, pas de bande rigide plate.
- **Location :** GLO (matière) / RoW (procédé, dont la variante CA-QC est déclarée copie des exchanges globaux).
- **Unité / base de comparaison :** kg pour la matière ; unité du service d'extrusion à confirmer.

> **Reconfirmé sur Ecoinvent 3.11 (2026-09-16) :** une première réconciliation avait rapporté ce même produit sous un UUID différent (`1367e2a2-…`) — résultat obtenu alors que la mauvaise base OpenLCA (`cups`) était ouverte, désormais invalidé. Une nouvelle interrogation vérifiée sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` **reconfirme le UUID du Lot 2D** (`ca074112-8461-32ac-b814-2d7749b7b862`) pour `market for acrylonitrile-butadiene-styrene copolymer`.

#### Correspondance

- **Produit / fonction :** Faible — aucune bande de chant ABS finie identifiée ; le procédé d'extrusion disponible ne correspond pas à la géométrie d'une bande rigide plate.
- **Composition / matière :** Bonne physiquement pour la matière ABS elle-même.
- **Technologie / procédé :** Faible — aucun indice observé ne démontre une spécificité ABS du procédé d'extrusion disponible.
- **Géographie :** Trompeuse pour la variante CA-QC du service d'extrusion, déclarée copie des exchanges globaux.
- **Données primaires québécoises :** Aucune démontrée.

#### Lacune Ecoinvent

C'est un cas de **procédé absent** pour la forme réelle du produit : la matière ABS existe, mais aucun procédé de transformation ne reproduit la géométrie d'une bande de chant. Le procédé d'extrusion de tuyaux disponible est un proxy de faible confiance, sans indice quantitatif spécifique à la bande de chant.

#### Données nécessaires

Masse par mètre, largeur, épaisseur, formulation/additifs, procédé réel de mise en forme.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous réserve explicite.** Traiter comme proxy à tester, pas comme modèle validé.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Bande de chant PVC — P1

> **Place relative à revérifier (décision Nicolas, 2026-09-15) :** le PVC est conservé dans le référentiel ; il n'est pas retiré arbitrairement. Sa priorité relative face au PE (nouvel objet ci-dessous) et à l'ABS doit toutefois être revérifiée plutôt que présumée, notamment à la lumière des tendances métier vers des bandes de chant PE.

#### Produit métier

Bande de chant en PVC, décrite selon son usage plutôt que comme famille de matière autonome.

#### Équivalent Ecoinvent identifié

- **Matière :** `market for polyvinyl chloride, suspension polymerised`, UUID `fa6532b7-7f96-3bbb-8f42-c300d800d5ff`.
- **Procédé candidat :** `calendering, rigid sheets`, UUID `d0a9fc16-0991-3ab1-b75e-340dbf4c0506`, Europe.
- **Location :** Europe (procédé).
- **Unité / base de comparaison :** kg pour la matière ; unité du service de calandrage à confirmer.

> **Reconfirmé sur Ecoinvent 3.11 (2026-09-16) :** une première réconciliation avait plutôt rapporté `market for polyvinylchloride, bulk polymerised` (UUID `17671bec-…`, Global) — résultat obtenu alors que la mauvaise base OpenLCA (`cups`) était ouverte, désormais invalidé. Une nouvelle interrogation vérifiée sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` **reconfirme la variante « suspension polymerised » du Lot 2D** (`fa6532b7-7f96-3bbb-8f42-c300d800d5ff`), avec un second UUID pour le même produit relevé cette session (`68a7d84c-01f2-3731-9d49-67a4054f6c90`, à vérifier s'il s'agit d'un doublon ou d'une variante distincte).

#### Correspondance

- **Produit / fonction :** Partielle — aucune bande de chant PVC finie identifiée, mais le calandrage de feuilles rigides est géométriquement plus proche que l'extrusion de tuyaux évaluée pour l'ABS.
- **Composition / matière :** Bonne physiquement pour la matière PVC.
- **Technologie / procédé :** Moyenne — un exchange `waste polyvinylchloride` (0,00339 kg/kg) constitue un indice quantitatif fort que le procédé de calandrage est modélisé spécifiquement pour une transformation du PVC, même si le nom du dataset reste générique. Cet indice ne démontre ni l'origine empirique précise du dataset ni son applicabilité aux chants de meuble.
- **Géographie :** Europe ; documentation indiquant un dataset ancien hérité d'Ecoinvent v2.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

C'est un cas de **procédé absent** pour la forme exacte du produit, atténué par un indice de spécificité matière (le flux de déchet PVC) qui rend `PVC + calandrage rigide` un proxy potentiel à tester. `PVC + extrusion` n'a pas été démontré par ce lot. Le dataset de calandrage est par ailleurs ancien, ce qui ajoute une réserve supplémentaire sur sa représentativité technologique actuelle.

#### Données nécessaires

Masse par mètre, dimensions, formulation/additifs, procédé réel de mise en forme.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous réserve explicite.** `PVC + calandrage rigide` est un proxy potentiel à tester ; documenter l'ancienneté du dataset avant utilisation.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Bande de chant PE / polyéthylène — P1

> **Nouvel objet (validation métier Nicolas, 2026-09-15).** Ajouté explicitement au périmètre du diagnostic.
>
> **Mise à jour (interrogation OpenLCA vérifiée sur Ecoinvent 3.11, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** une première réconciliation avait été intégrée par erreur alors que la mauvaise base OpenLCA (`cups`) était ouverte ; ses UUID sont **invalidés**. Une nouvelle recherche a été menée depuis zéro sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` : `edge band`, `edge banding`, `edging` (process ET flows, 0 résultat dans les deux cas), puis `polyethylene, low density`, `polypropylene, granulate`, `acrylonitrile-butadiene-styrene copolymer`, `polyvinylchloride`, `extrusion, plastic`.
>
> **Note (collecte de données fabricants, relecture du 2026-09-22) :** cette absence dans Ecoinvent concerne uniquement la base de données ACV — elle ne signifie pas qu'aucune bande de chant PE n'existe commercialement. Une référence commerciale réelle a été identifiée (Naber, réf. `1112007`, « Bande de chant en polyéthylène », mousse PE à cellules fermées 33 kg/m³, fabriquée par Stauffer Schallschutz + Akustik), mais sa fonction déclarée (espacement/insonorisation entre les faces d'un plan de travail) diffère de la fonction décorative/protectrice de chant de panneau visée ici — la correspondance avec l'usage métier RECQ36 reste une question ouverte. Voir [`inventaire/bandes-de-chant/pe-recherche-negative-2026-09-22.md`](inventaire/bandes-de-chant/pe-recherche-negative-2026-09-22.md) pour le détail complet ; cette note ne modifie pas la conclusion Ecoinvent ci-dessous, qui reste valide.

#### Produit métier

Bande de chant en PE (polyéthylène), décrite selon son usage plutôt que comme famille de matière autonome.

#### Équivalent Ecoinvent identifié

**Produit fonctionnel : absence confirmée (0 résultat sur process et flows)**, dans cette base et avec ces requêtes.

**Briques génériques vérifiées sur Ecoinvent 3.11, potentiellement utiles pour une reconstruction bottom-up (aucune ne constitue une correspondance directe) :**

| Dataset | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|
| `market for polyethylene, low density, granulate` | Global | kg | `08d7cf9a-4301-321f-947c-06849afd126c` | Matière première seule, aucune forme de profilé/bande |
| `market for polypropylene, granulate` | à vérifier | kg | `881eed86-35c6-3cc2-a352-263e9c4c34ee` | Idem, PP — mentionné par cohérence avec la recherche, pas un candidat PE |
| `market for acrylonitrile-butadiene-styrene copolymer` | à vérifier | kg | `ca074112-8461-32ac-b814-2d7749b7b862` | Idem, ABS — reconfirme le Lot 2D, voir fiche ABS ci-dessus |
| `market for polyvinyl chloride, suspension polymerised` | à vérifier | kg | `fa6532b7-7f96-3bbb-8f42-c300d800d5ff` / `68a7d84c-01f2-3731-9d49-67a4054f6c90` | Idem, PVC — reconfirme le Lot 2D, voir fiche PVC ci-dessus |

Procédés de transformation disponibles : `extrusion, plastic pipes` (profil rond) et `extrusion, plastic film` (film mince) — **aucun ne correspond** à une extrusion de profilé plat de type bande de chant.

#### Correspondance

**Aucune correspondance satisfaisante** (niveau : **ABSENT / RECONSTRUCTION** pour le produit fonctionnel).

- **Produit / fonction :** Aucune — absence confirmée.
- **Composition / matière :** La matière PE générique existe (Global, kg), sans lien à un profilé de bande de chant.
- **Technologie / procédé :** Aucun procédé d'extrusion de profilé mince/bande n'a été trouvé — seuls existent un procédé de tuyau (rond) et un procédé de film (mince).
- **Géographie :** Global pour la matière ; sans objet pour un procédé, faute de procédé identifié.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Produit fonctionnel totalement absent, confirmé sur process et flows. Ne pas transformer arbitrairement la matière PE générique en correspondance directe : c'est, au mieux, une brique de reconstruction, dans la même situation que l'ABS et le PVC (Lot 2D) mais sans procédé d'extrusion reproduisant la géométrie d'une bande de chant plate.

#### Données nécessaires

Masse linéique (g/m), épaisseur, largeur, et composition exacte (PE pur ou compound avec charges/pigments) pour bâtir un proxy par la masse.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous réserve explicite** — ne pas conclure qu'un des polymères génériques (PE, PP, ABS, PVC) est LE bon proxy sans données fabricant. Documenter comme lacune ouverte nécessitant une reconstruction bottom-up (masse de matière + procédé de transformation le plus proche disponible, à défaut d'un procédé de profilé dédié).

#### Source du diagnostic

[Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

## 4. Bois massif

Le bois massif est acheté brut et séché, principalement en épaisseur 4/4 ; les épaisseurs 6/4 et 8/4 sont plus occasionnelles. Les essences restent séparées dans la taxonomie métier.

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Érable massif, brut séché | Dataset identifié (générique) | Faible | essence | 🔴 Lacune majeure |
| P1 | Frêne massif, brut séché | Dataset identifié (générique) | Faible | essence | 🔴 Lacune majeure |
| P1 | Merisier / bouleau jaune massif, brut séché | Dataset identifié (générique) | Partielle | essence | 🟠 À adapter |
| P1 | Chêne rouge massif, brut séché | Dataset identifié (générique) | Partielle | essence | 🟠 À adapter |
| P1/P2 | Tilleul massif, brut séché | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1/P2 | Bois feuillu exotique, brut séché | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Une chaîne complète foresterie → sciage → séchage existe dans Ecoinvent au niveau générique `hardwood`, avec un rendement de sciage générique de 65–67 % et un séchage standardisé à u=10 %. Cette chaîne représente correctement la fonction (bois scié, séché, brut/non raboté) mais perd systématiquement la spécificité d'essence : pour l'érable et le frêne, aucune trace de l'essence n'a été trouvée à aucun étage, y compris à la foresterie. Pour le merisier/bouleau jaune et le chêne rouge, un procédé forestier portant un nom vernaculaire proche (`birch`, `oak`) existe, mais en Suède et en Allemagne respectivement, sans confirmation botanique ni géographique. Le dataset de sciage porte une variante `Canada, Quebec`, mais celle-ci est déclarée identique au modèle mondial pour permettre le linking régional, sans démontrer de technologie de sciage québécoise. Le tilleul et le bois exotique n'ont pas encore été examinés spécifiquement.

> **Rappel méthodologique :** l'existence d'un dataset générique `hardwood` ne représente pas automatiquement l'essence québécoise ciblée. Dès que la transformation entre dans la catégorie générique, la traçabilité de l'essence est perdue dans le flow Ecoinvent.

### Érable massif, brut séché — P1

#### Produit métier

Érable massif, brut, séché, acheté principalement en épaisseur 4/4.

#### Équivalent Ecoinvent identifié

- **Dataset :** `sawnwood, board, hardwood, raw, dried (u=10%)` (flow final d'une chaîne sciage + séchage générique `hardwood`)
- **UUID :** `8f082e64-e307-450f-ba63-d07e65ab4954`
- **Location :** sciage disponible en Suisse (`bc9f5858-6781-3025-9357-997d6f7b1f5a`) et en Canada, Quebec (`6f452c2d-38ee-3916-bea2-b725fecb8d97`, déclaré identique au dataset mondial) ; séchage disponible en RoW/Suisse/Europe sans Suisse, sans variante CA-QC.
- **Unité / base de comparaison :** m³ de bois scié séché.

#### Correspondance

- **Produit / fonction :** Bonne physiquement — le flow `raw, dried (u=10%)` correspond bien au bois massif brut/non raboté acheté par l'ébéniste.
- **Composition / matière :** Faible — aucune trace de l'essence érable (recherches `maple` et `Acer` sans résultat pertinent) ; densité spécifique non représentée.
- **Technologie / procédé :** Moyenne — principe générique du sciage et du séchage, potentiellement transférable en structure.
- **Géographie :** Faible — le sciage québécois est une copie déclarée du modèle mondial ; le séchage n'a aucune variante CA-QC.
- **Données primaires québécoises :** Aucune démontrée.

#### Lacune Ecoinvent

La lacune commence dès la foresterie : aucun dataset ni flow ne porte la trace de l'essence érable à aucune étape de la chaîne. Le dataset générique `hardwood` représente correctement la structure physique du sciage et du séchage (rendement ~65–67 %, ratio bois humide/sec ~1,087), mais pas l'essence elle-même. C'est un cas de **mauvaise essence** : le produit générique ne doit pas être présenté comme de l'érable.

#### Données nécessaires

Confirmation botanique de l'essence livrée, densité, rendement de sciage, humidité cible, provenance et distance d'approvisionnement, consommation énergétique du sciage/séchage si disponible.

#### Recommandation

**Adapter/régionaliser le dataset existant**, en documentant explicitement l'absence de spécificité d'essence. Le proxy hardwood ne doit pas être utilisé tel quel comme preuve de représentativité de l'érable.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2C](diagnostic/ecoinvent-representativite-qc-lot-2c.md)

---

### Frêne massif, brut séché — P1

#### Produit métier

Frêne massif, brut, séché, acheté principalement en épaisseur 4/4.

#### Équivalent Ecoinvent identifié

- **Dataset :** `sawnwood, board, hardwood, raw, dried (u=10%)` — même flow générique que pour l'érable.
- **UUID :** `8f082e64-e307-450f-ba63-d07e65ab4954`
- **Location :** identique au cas érable (sciage Suisse/CA-QC copié, séchage sans variante CA-QC).
- **Unité / base de comparaison :** m³ de bois scié séché.

#### Correspondance

- **Produit / fonction :** Bonne physiquement.
- **Composition / matière :** Faible — recherche `Fraxinus` sans résultat ; le terme `ash` produit des faux positifs liés aux cendres et n'aide pas la recherche.
- **Technologie / procédé :** Moyenne — structure générique transférable.
- **Géographie :** Faible.
- **Données primaires québécoises :** Aucune démontrée.

#### Lacune Ecoinvent

Même lacune que l'érable : **mauvaise essence**, aucune trace du frêne à aucun stade de la chaîne. La recherche est en outre compliquée par une homonymie linguistique (`ash` = cendre), ce qui a nécessité une vérification supplémentaire sans changer la conclusion.

#### Données nécessaires

Confirmation botanique, densité, rendement de sciage, humidité cible, provenance, consommation énergétique si disponible.

#### Recommandation

**Adapter/régionaliser le dataset existant**, avec la même réserve explicite que pour l'érable sur l'absence de spécificité d'essence.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2C](diagnostic/ecoinvent-representativite-qc-lot-2c.md)

---

### Merisier / bouleau jaune massif, brut séché — P1

#### Produit métier

Merisier / bouleau jaune massif, brut, séché, acheté principalement en épaisseur 4/4. Le diagnostic Lot 2C désigne ce produit métier par le terme commercial « merisier / bouleau jaune (yellow birch) » ; cette désignation est celle du diagnostic et n'est pas reformulée ici en une affirmation botanique plus précise.

#### Équivalent Ecoinvent identifié

- **Dataset forestier :** `hardwood forestry, birch, sustainable forest management`, en Suède.
- **UUID :** `885df1ec-96c0-32a2-a869-70779dc48420` (flow de sortie générique `sawlog and veneer log, hardwood`)
- **Transformation :** sciage + séchage génériques hardwood, sans variante spécifique `birch`.
- **Location :** Suède (foresterie) ; Suisse/Europe/RoW (sciage/séchage génériques).
- **Unité / base de comparaison :** m³ de bois rond en foresterie ; m³ de bois scié séché pour la transformation générique.

#### Correspondance

- **Produit / fonction :** Partielle — un procédé forestier `birch` existe, mais dès la sortie de la foresterie, la chaîne retombe dans le hardwood générique.
- **Composition / matière :** Non établie précisément — Ecoinvent ne précise pas l'espèce botanique au-delà du nom vernaculaire `birch`, sans mention de l'espèce nord-américaine visée.
- **Technologie / procédé :** Moyenne pour la transformation générique ; le système forestier suédois lui-même n'est pas validé pour le Québec.
- **Géographie :** Faible — foresterie modélisée pour la Suède.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

La lacune commence en substance dès la foresterie : la présence du mot `birch` dans le nom du process ne suffit pas à établir une correspondance avec l'essence métier visée, et la géographie suédoise n'est pas représentative du Québec sans validation. C'est un cas d'**essence non confirmée combinée à une géographie inadéquate**, moins sévère que l'absence totale observée pour l'érable et le frêne puisqu'un procédé forestier portant un nom vernaculaire proche existe.

#### Données nécessaires

Confirmation botanique de l'essence réellement livrée, densité, rendement de sciage, humidité cible, provenance et distance d'approvisionnement.

#### Recommandation

**Adapter/régionaliser le dataset existant**, en confirmant d'abord l'essence puis en adaptant le système forestier, l'énergie et le transport aux conditions québécoises.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2C](diagnostic/ecoinvent-representativite-qc-lot-2c.md)

---

### Chêne rouge massif, brut séché — P1

#### Produit métier

Chêne rouge massif, brut, séché, acheté principalement en épaisseur 4/4.

#### Équivalent Ecoinvent identifié

- **Dataset forestier :** `hardwood forestry, oak, sustainable forest management`, en Allemagne.
- **UUID :** `1050da18-ecb1-3414-8011-a04a3151ff23` (flow de sortie générique `sawlog and veneer log, hardwood`)
- **Transformation :** sciage + séchage génériques hardwood, sans variante spécifique `oak`.
- **Location :** Allemagne (foresterie) ; Suisse/Europe/RoW (transformation générique).
- **Unité / base de comparaison :** m³ de bois rond en foresterie ; m³ de bois scié séché pour la transformation générique.

#### Correspondance

- **Produit / fonction :** Partielle — procédé forestier `oak` existant, mais transformation générique dès l'étape suivante.
- **Composition / matière :** Non établie précisément — nom vernaculaire `oak` sans précision de *Quercus rubra*.
- **Technologie / procédé :** Moyenne pour la transformation générique ; système forestier allemand (12,27 semis/m³, 37,1 m²·an de voirie, 15,20 MJ/m³ de diesel, 0,375 h/m³ de tronçonnage) non validé pour le Québec.
- **Géographie :** Faible — foresterie modélisée pour l'Allemagne.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Même structure de lacune que le merisier/bouleau jaune : **essence non confirmée** (nom vernaculaire `oak` sans confirmation de l'espèce nord-américaine) **combinée à une géographie inadéquate** (système forestier allemand). La transformation ultérieure est générique et ne conserve pas la trace de l'essence.

#### Données nécessaires

Confirmation botanique, densité, rendement de sciage, humidité cible, provenance et distance d'approvisionnement.

#### Recommandation

**Adapter/régionaliser le dataset existant**, en confirmant d'abord l'essence puis en adaptant le système forestier, l'énergie et le transport.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2C](diagnostic/ecoinvent-representativite-qc-lot-2c.md)

---

### Tilleul massif, brut séché — P1/P2

#### Produit métier

Tilleul massif, brut, séché, utilisé notamment pour le prototypage.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.** Le dataset générique `sawnwood production, hardwood, dried` (CH / Europe / RoW), repéré comme candidat générique dans la taxonomie initiale, n'a pas été analysé spécifiquement pour cette essence et ne lui est affecté à ce stade.

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent spécifique au tilleul n'a été menée. Par analogie méthodologique avec l'érable et le frêne (Lot 2C), il est plausible que la chaîne hardwood générique perde également la spécificité de cette essence, mais cela reste à vérifier et ne doit pas être présumé.

#### Données nécessaires

À déterminer lors du diagnostic approfondi. Par analogie méthodologique avec l'érable et le frêne (Lot 2C), les paramètres à confirmer en priorité seraient l'essence botanique, la densité, le rendement de sciage, l'humidité cible et la provenance — cette liste reste une hypothèse de travail, pas une conclusion établie pour le tilleul.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Bois feuillu exotique / bois africain exotique, brut séché — P1/P2

#### Produit métier

Catégorie d'usage réel regroupant les essences exotiques utilisées en atelier, sans reproduire une liste exhaustive de catalogue fournisseur.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent spécifique n'a été menée pour cette catégorie.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer l'essence ou les essences botaniques réellement utilisées, la densité, le rendement de sciage, l'humidité cible et la provenance.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

## 5. Adhésifs

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Colle PVAc / PVA blanche | Lot 2F + reconfirmé sur Ecoinvent 3.11 (2026-09-16) : monomère seul (vinyl acetate) | Aucune | correspondance Ecoinvent non établie (ABSENT, produit fonctionnel) | 🔴 Lacune majeure |
| P1 | Adhésif thermofusible EVA / EVA hot-melt | Lot 2F + reconfirmé (2026-09-16) : copolymère seul | Faible à moyenne | formulation hot-melt absente | 🟣 À reconstruire |
| P1 | Colle contact *(formulations à base d'eau prioritaires, Nicolas)* | Lot 2F + reconfirmé sur Ecoinvent 3.11 (2026-09-16) : aucune brique identifiée | Aucune | aucune brique chimique identifiée (ABSENT) | 🔴 Lacune majeure |
| P2 | Colle polyuréthane / PUR | Lot 2F : précurseurs seuls (polyol, MDI) ; **produit formulé trouvé (2026-09-16) mais pour usage structural (CLT), non équivalent** | Faible | chimie/usage distincts d'une colle multimatériaux d'atelier | 🔴 Lacune majeure |

### Lecture rapide

Les quatre adhésifs d'atelier ont été diagnostiqués au **Lot 2F** ; les quatre ont été **reconfirmés par une interrogation OpenLCA vérifiée sur Ecoinvent 3.11 le 2026-09-16** (une première réconciliation, faite par erreur sur la mauvaise base `cups`, est invalidée). Dans aucun des quatre cas un adhésif *formulé et équivalent* n'a été identifié : Ecoinvent ne propose, pour la PVA, qu'un précurseur chimique isolé (monomère vinyl acetate) et pour l'EVA hot-melt qu'un copolymère non formulé ; pour le PUR, la session du 2026-09-16 a cette fois trouvé un adhésif **formulé** (`market for polyurethane adhesive`), mais destiné au bois lamellé structural (CLT), de chimie et d'usage distincts d'une colle multimatériaux d'atelier — une nouvelle colle formulée pour glulam (MUF) a également été trouvée, avec la même réserve de non-équivalence. Pour la colle contact, même l'étape de précurseur fait défaut, confirmé indépendamment dans les deux sessions (Lot 2F et 2026-09-16, requête `adhesive` exhaustive à 19 résultats, tous hors sujet). Le Lot 2D avait par ailleurs déjà établi que, pour la bande de chant en bois véritable préencollée, les briques d'adhésif disponibles ne résolvent pas la lacune principale de cette bande (l'absence de la composante bois elle-même) — ce constat concerne l'usage en bande de chant, distinct des présentes fiches.

> **Rappel méthodologique :** les adhésifs UF et MUF ne sont pas utilisés directement en atelier et ne figurent pas dans cette taxonomie ; ils relèvent des intrants industriels des panneaux (voir famille Panneaux). La colle PUR d'assemblage multimatériaux ne doit pas être confondue avec l'adhésif EVA hot-melt de l'encolleuse de chants.

### Colle PVAc / PVA blanche — P1

> **Reconfirmé par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** une première réconciliation, faite alors que la mauvaise base OpenLCA (`cups`) était ouverte, est invalidée (UUID `9381f4dc-…` pour vinyl acetate, `44da54f3-…` pour la dispersion acrylique, `e1e8f512-…` pour adhesive-for-metal — tous invalidés). Une nouvelle recherche a été menée depuis zéro sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` (`polyvinylacetate`, `polyvinyl acetate`, `vinyl acetate`, `wood glue`, `dispersion adhesive`, `contact adhesive`, `emulsion` [101 résultats, tous liés aux peintures/déchets], `adhesive` [recherche exhaustive, 19 résultats]). **Absence de produit fonctionnel reconfirmée indépendamment.**
>
> **Note (collecte de données fabricants, relecture du 2026-09-22) :** la nomenclature fournisseur demandée en « Recommandation » ci-dessous a été obtenue pour une référence précise. La FDS et la fiche technique papier de la **colle Royale 404 (Abradhésif inc., St-Bruno-de-Montarville, QC)** confirment qu'il s'agit d'une émulsion aqueuse d'acétate de polyvinyle (PVAc) — « acétate polyvinylique en émulsion » (FDS) / « acétate de polyvinyle » (fiche technique) — avec un taux de solides de 51 % (± 1 %) et une densité relative de 1,06 (FDS) ou 1,1 kg/L (fiche technique, écart non résolu entre les deux documents). La formulation détaillée (identité exacte du polymère, additifs) demeure confidentielle. Voir [`inventaire/adhesifs/royale-404-abradhesif.md`](inventaire/adhesifs/royale-404-abradhesif.md) pour le détail complet, y compris un bilan massique simplifié explicitement présenté comme un calcul. **Cette note ne modifie pas la conclusion Ecoinvent ci-dessous** (l'absence d'un procédé PVAc formulé dans Ecoinvent reste valide) ; elle documente une donnée fabricant utile à une future reconstruction bottom-up.

#### Produit métier

Colle PVAc/PVA blanche utilisée pour le collage et l'assemblage du bois.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**, reconfirmé sur Ecoinvent 3.11 le **2026-09-16**. Aucun adhésif formulé identifié dans les deux sessions.

| Dataset | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|
| `market for vinyl acetate` | — | kg | `a4bd8120-5784-3dd9-bee6-a8473d385b7f` | **Monomère précurseur**, pas le polymère PVAc. Cet UUID diffère de celui cité au Lot 2F (`9381f4dc-…`) — écart non résolu, à noter sans le présumer être une erreur (versions/échantillonnages différents possibles) |
| `market for ethylene vinyl acetate copolymer` | — | kg | `c773d766-c8ff-3493-88ea-09492fbc0048` | Copolymère EVA — chimie différente (hot-melt/mousses), pas la colle blanche PVAc classique |
| `adhesive, for metal` | — | kg | `4a5da11b-2019-326b-990e-254d96e9acb3` | Hors sujet (colle métal). UUID à nouveau différent des citations précédentes (Lot 2F : `3bd4e097-…`) — écart non résolu |
| `adhesive mortar` / `bitumen adhesive compound` | — | — | — | Hors sujet (construction/étanchéité) |

#### Correspondance

**Analyse Ecoinvent réalisée (Lot 2F + reconfirmation sur Ecoinvent 3.11) / correspondance non établie — niveau ABSENT pour le produit fonctionnel.** Aucun adhésif PVAc formulé n'a été identifié ; le seul dataset disponible (vinyl acetate) représente le monomère, pas la colle prête à l'emploi.

- **Produit / fonction :** Aucune (monomère, pas un adhésif).
- **Technologie :** Faible — brique chimique amont potentielle uniquement.
- **Forme / application :** Aucune (le métier utilise un liquide prêt à l'emploi ; le dataset est un monomère industriel).
- **Unité :** kg — écart avec l'unité métier probable (pot/litre).
- **Géographie :** Non systématiquement précisée dans cette session.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucune étape entre le monomère vinyl acetate et la colle prête à l'emploi n'a été identifiée, avec deux sessions de recherche indépendantes (Lot 2F et Ecoinvent 3.11, 2026-09-16). Ceci documente une absence dans cette base, avec ces requêtes — pas une absence générale de toute version d'Ecoinvent. **Ne jamais présenter le vinyl acetate, l'EVA ou l'adhesive-for-metal comme équivalents directs** : chimie et/ou fonction différentes.

#### Données nécessaires

Formulation/composition réelle du produit (à confirmer via la FDS du produit atelier de référence), teneur en solides si pertinente, densité si nécessaire à une conversion, consommation réelle, masse achetée ou unité d'achat.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Aucune reconstruction sérieuse n'est possible à partir du seul monomère. Une piste de reconstruction reste ouverte via un procédé générique de polymérisation en émulsion (existence non vérifiée dans cette base, hors périmètre de cette recherche) ; à défaut, recours à des données fabricant/fiche technique (EPD fournisseur).

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (reconfirmation indépendante sur Ecoinvent 3.11).

---

### Adhésif thermofusible EVA / EVA hot-melt — P1

#### Produit métier

Adhésif thermofusible EVA utilisé dans l'encolleuse de chants.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**, reconfirmé par une interrogation vérifiée sur Ecoinvent 3.11 le 2026-09-16 (la requête `adhesive` exhaustive de cette session n'a fait remonter aucun adhésif hot-melt formulé ni produit spécifique à l'encollage de chants). Seule brique identifiée cette session : `market for ethylene vinyl acetate copolymer` (résine, non formulée en adhésif), UUID `c773d766-c8ff-3493-88ea-09492fbc0048`, unité kg — cet UUID diffère de celui cité au Lot 2F (`fe0fb6f7-…`), écart non résolu, à ne pas présumer être une erreur.

#### Correspondance

- **Produit / fonction :** Aucune (résine, pas un adhésif prêt à l'emploi).
- **Technologie :** Moyenne — bonne famille polymère de base, plus proche du produit fini qu'un simple monomère (cf. PVA ci-dessus).
- **Forme / application :** Inconnue — aucun procédé d'encollage de chants identifié.
- **Unité :** kg.
- **Géographie :** Global.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Le copolymère EVA constitue une brique matière intermédiaire, mais la formulation hot-melt réelle (additifs, charges) et la chaîne vers le produit métier n'ont pas été établies avec les méthodes d'interrogation disponibles au Lot 2F.

#### Données nécessaires

Composition/formulation réelle, fractions massiques des constituants si disponibles, consommation réelle par unité métier pertinente (grammage par mètre linéaire de chant si disponible), densité/masse si nécessaire, paramètres d'application si nécessaires et disponibles.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Une reconstruction documentée est envisageable si la formulation réelle est obtenue — meilleure base de départ que la PVA (résine plutôt que monomère).

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md)

---

### Colle contact — P1

> **Précision métier (validation Nicolas, 2026-09-15) :** les formulations à base d'eau sont particulièrement pertinentes aujourd'hui pour ce produit.
>
> **Reconfirmé par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** une première réconciliation, faite sur la mauvaise base `cups`, est invalidée. Une nouvelle recherche exhaustive (`polyvinylacetate`, `polyvinyl acetate`, `vinyl acetate`, `wood glue`, `dispersion adhesive`, `contact adhesive`, `emulsion` [101 résultats, tous liés aux peintures/déchets], `adhesive` [19 résultats]) n'a fait apparaître aucun résultat pour la colle contact, y compris pour les formulations à base d'eau. **Absence confirmée une seconde fois, indépendamment.** Le dataset `market for polychloroprene` (UUID `d1147a50-260c-353a-93c0-def3ebd131d0`, cité au Lot 1) n'a de nouveau pas pu être retrouvé.

#### Produit métier

Colle contact utilisée pour le collage du stratifié HPL, en tenant compte de la pertinence actuelle des formulations à base d'eau.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**, reconfirmé sur Ecoinvent 3.11 le **2026-09-16**. Recherches process/flow (`contact adhesive`, `contact glue`, `contact cement`, `solvent based adhesive`, `rubber adhesive`, `neoprene adhesive`, `polychloroprene adhesive`, `polychloroprene` seul, `chloroprene`, `laminate adhesive`, `synthetic rubber`, `dispersion`, `emulsion`, `adhesive` générique) : aucun adhésif contact formulé, ni aucune brique chimique confirmée, n'a été identifié dans l'une ou l'autre session — y compris pour une formulation à base d'eau. Le dataset `market for polychloroprene` cité dans un lot antérieur (UUID `d1147a50-260c-353a-93c0-def3ebd131d0`) n'a pu être reconfirmé ni au Lot 2F ni le 2026-09-16.

#### Correspondance

**Analyse Ecoinvent réalisée deux fois (Lot 2F et Ecoinvent 3.11, 2026-09-16) / correspondance non établie — niveau ABSENT**, y compris à l'étape des précurseurs.

- **Produit / fonction :** Aucune.
- **Technologie :** Inconnue — chimie réelle du produit métier non présumée.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucun adhésif contact formulé, ni aucune brique chimique confirmée (résine ou polymère), n'a pu être identifié — confirmé indépendamment à deux reprises (Lot 2F, 2026-09-16), y compris pour les formulations à base d'eau désormais explicitement recherchées — situation plus défavorable que la PVA et l'EVA, qui disposent au moins d'un précurseur ou d'une résine. Ceci documente une absence dans cette base, avec ces requêtes, pas une absence générale de toute version d'Ecoinvent.

#### Données nécessaires

Composition/formulation réelle du produit (à confirmer via la FDS du produit en pot utilisé en atelier, **en priorisant les formulations à base d'eau** selon la précision métier 2026-09-15), teneur en solides si pertinente, présence et nature des solvants si applicable, densité si nécessaire, consommation réelle.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur**, en ciblant les formulations à base d'eau. La reconfirmation du 2026-09-16 sur Ecoinvent 3.11 rend une nouvelle recherche Ecoinvent peu prioritaire pour l'instant ; si un proxy doit malgré tout être construit pour avancer une quantification, le signaler explicitement comme approximation de dernier recours, jamais comme une correspondance.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (reconfirmation indépendante sur Ecoinvent 3.11).

---

### Colle polyuréthane / PUR — P2

#### Produit métier

Colle PUR utilisée occasionnellement pour le collage métal-bois ou plastique-bois.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F** : aucun adhésif PU formulé identifié (recherches `polyurethane adhesive`, `PU adhesive`, `PUR adhesive`, `structural adhesive`, `assembly adhesive`, `polyurethane` générique, `polyurethane resin`, `polyol`, `methylene diphenyldiisocyanate`) ; seules deux briques chimiques amont potentielles, non combinées : `polyol` et `methylene diphenyldiisocyanate` (MDI, déjà rencontré au Lot 2B comme liant interne de panneaux — usage différent).

> **Mise à jour (interrogation OpenLCA vérifiée sur Ecoinvent 3.11, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** cette session a cette fois trouvé un adhésif PUR **formulé** : `market for polyurethane adhesive`, UUID `ad1da3c6-5cb8-364d-8fb5-e96e9dca9e93`, Global, kg — isocyanate, sans formaldéhyde, mais **destiné au bois lamellé structural (CLT)**, un usage industriel différent du collage occasionnel métal-bois/plastique-bois d'atelier. **Ne pas présenter comme équivalent direct** sans confirmation que sa formulation convient à cet usage. Une colle MUF formulée pour glulam (`market for melamine urea formaldehyde adhesive`, UUID `e7001c37-5a60-335b-bf15-ad7395226509`, Global, kg) a également été trouvée, avec la même réserve — les adhésifs UF/MUF ne sont de toute façon pas utilisés directement en atelier dans cette taxonomie (voir rappel méthodologique de la section).

#### Correspondance

- **Produit / fonction :** Un adhésif PUR formulé existe désormais dans la base, mais pour un usage structural (CLT) distinct du collage occasionnel d'atelier ; non retenu comme correspondance sans confirmation.
- **Composition / matière :** Faible pour l'usage métier visé — précurseurs (polyol, MDI) de la bonne famille chimique, ou produit fini d'usage différent (CLT).
- **Unité :** kg.
- **Géographie :** Global pour le produit formulé (2026-09-16) ; non vérifiée spécifiquement pour polyol/MDI au Lot 2F.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucun adhésif PUR formulé pour un usage de collage occasionnel métal-bois/plastique-bois d'atelier n'a été identifié. Le produit formulé trouvé le 2026-09-16 (`ad1da3c6-…`) est un adhésif structural pour CLT ; l'utiliser comme proxy nécessiterait de documenter explicitement l'écart de chimie/usage, pas de le présenter comme un équivalent.

#### Données nécessaires

Type et technologie réelle du produit, composition/formulation fabricant, fractions massiques pertinentes si disponibles, densité si nécessaire, consommation réelle.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Si un proxy doit être construit avant l'obtention de ces données, `market for polyurethane adhesive` (CLT) est plus proche d'un produit fini que les précurseurs polyol/MDI seuls, mais doit être documenté comme approximation sous réserve explicite (usage structural, pas d'atelier), jamais comme une correspondance directe.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

## 6. Finitions

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Vernis / laque | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Scellant | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | Teinture | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | Solvants / diluants auxiliaires | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Aucun produit de finition n'a encore fait l'objet d'un diagnostic Ecoinvent approfondi dans les Lots 2A–2D. Ces produits restent au stade « à rechercher » de la taxonomie initiale ; leurs variantes à base d'eau ou de solvant devront être distinguées lors d'une future analyse.

### Vernis / laque — P1

#### Produit métier

Vernis ou laque de finition, en variantes à base d'eau ou à base de solvant.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la formulation (eau ou solvant), le taux de matière sèche et la méthode d'application.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Scellant — P1

#### Produit métier

Scellant de finition, en variantes à base d'eau ou à base de solvant.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la formulation, le taux de matière sèche et la méthode d'application.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Teinture — P2

#### Produit métier

Teinture de finition, en variantes à base d'eau ou à base de solvant.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la formulation exacte.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Solvants / diluants auxiliaires — P2

#### Produit métier

Acétone pour nettoyage/décrassage ; thinner pour dilution des produits à solvants. Le thinner n'est pas une substance unique.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. La composition du thinner reste elle-même à déterminer à partir du produit/FDS réel avant toute recherche de dataset.

#### Données nécessaires

Composition exacte du thinner à partir de la FDS ; l'acétone est une substance identifiable séparément.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

## 7. Quincaillerie

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Vis d'assemblage #6 | Matière + procédé | Partielle | composition inconnue | 🟣 À reconstruire |
| P1 | Vis d'assemblage #8 | Matière + procédé | Partielle | composition inconnue | 🟣 À reconstruire |
| P1 | Charnière invisible de meuble | Absence confirmée (2×, dont Ecoinvent 3.11 2026-09-16) ; services génériques de transformation métallique identifiés (sans UUID retenu) | Faible | composition inconnue (nomenclature bloquante) | 🔴 Lacune majeure |
| P1 | Coulisse de tiroir | Absence confirmée (2×, dont Ecoinvent 3.11 2026-09-16) ; mêmes services génériques | Faible | composition inconnue (nomenclature bloquante) | 🔴 Lacune majeure |
| P1 | Poignée de meuble métallique | Matière + procédé (Lot 2D) ; absence reconfirmée sans ambiguïté sur Ecoinvent 3.11 (2026-09-16) | Faible | composition inconnue | 🟣 À reconstruire |
| P1 | Pied niveleur / niveleur | Matière + procédé ; absence reconfirmée sur Ecoinvent 3.11 (2026-09-16) | Conditionnelle | composition inconnue | 🟣 À reconstruire |
| P1/P2 | Ferrure métallique de suspension (clé française) | Absence confirmée sur Ecoinvent 3.11 (2026-09-16) — désormais couvert | Faible | composition/dimensions inconnues | 🟣 À reconstruire |

### Lecture rapide

Aucun composant de quincaillerie ne dispose d'un produit fonctionnel direct dans Ecoinvent — confirmé pour l'ensemble des familles (charnière, coulisse, poignée, pied niveleur, ferrure de suspension, vis) par une interrogation vérifiée sur Ecoinvent 3.11 le 2026-09-16 (0 résultat process + flows pour chaque famille, exploration complémentaire de la catégorie ISIC 259 — 473 process, échantillon de 30 examiné — qui ne contient que des services de transformation métallique génériques et des matières premières, aucun produit fini de quincaillerie meuble). Une première réconciliation faite sur la mauvaise base `cups` (incluant des UUID de briques génériques et un statut de recherche incohérent pour la poignée) est invalidée : la nouvelle session ne rapporte aucun UUID de brique nommément, seulement des noms de process (emboutissage, extrusion d'aluminium, revêtement zinc, tournage, fraisage). Pour les vis et le pied niveleur, une reconstruction matière + procédé est plausible mais reste conditionnelle à la confirmation, par le fournisseur, de la composition, du revêtement et du procédé réels — l'absence de distinction de taille dans Ecoinvent ne démontre pas que la masse est la seule différence réelle entre les produits. Pour la charnière invisible et la coulisse de tiroir, la lacune est plus profonde : même la nomenclature physique du composant (matériaux constitutifs, parts, revêtement) est absente, ce qui bloque toute reconstruction avant d'obtenir cette donnée. La ferrure de suspension et la poignée, non couvertes ou ambiguës lors des passes précédentes, sont désormais explicitement confirmées absentes.

> **Priorisation métier (validation Nicolas, 2026-09-15) :** ne pas chercher à créer une précision excessive sur les vis — un modèle simplifié basé sur la masse et la matière pourra probablement suffire, et ce composant n'est **pas** un chantier de modélisation détaillée prioritaire pour l'instant. Prioriser plutôt, dans cet ordre d'attention : **charnières, coulisses de tiroir, poignées, pieds/niveleurs, puis ferrures de suspension (French cleat)**.

> **Rappel méthodologique :** rechercher d'abord le composant fonctionnel, puis un produit proche ; une reconstruction à partir de matières et de procédés ne vient qu'en dernier recours. L'acier, l'aluminium, le zinc et le plastique ne constituent pas des familles principales autonomes.

### Vis d'assemblage #6 — P1

> **Priorisation métier (Nicolas, 2026-09-15) :** ne pas chercher une précision excessive ici — un modèle simplifié basé sur la masse et la matière pourra probablement suffire ; ce n'est pas, pour l'instant, un chantier de modélisation détaillée prioritaire. Les fiches ci-dessous restent inchangées à titre de traçabilité du diagnostic déjà réalisé (Lot 2D).

#### Produit métier

Vis d'assemblage #6, composant fonctionnel plutôt que métal générique.

#### Équivalent Ecoinvent identifié

- **Produit fonctionnel :** absent — les résultats de recherche `screw` observés étaient des faux positifs liés aux compresseurs.
- **Briques matière/procédé disponibles :** `market for steel, low-alloyed` (`1af29f22-5a0a-3130-a65d-6ea9928f522a`), `wire drawing, steel` (`5563eb07-b684-33b5-bf13-a8f604fe5b06`), `zinc coating, pieces` (`9cc6fb22-00d5-3d78-8971-0d46751d263c`).
- **Étapes non identifiées :** frappe à froid et roulage du filet.
- **Unité / base de comparaison :** kg (briques matière) ; masse par pièce à établir séparément.

#### Correspondance

- **Produit / fonction :** Non établie — aucun produit vis n'existe.
- **Composition / matière :** Partielle — acier bas allié, tréfilage et revêtement zinc sont des briques plausibles, mais leur combinaison exacte n'est pas confirmée pour la vis #6.
- **Technologie / procédé :** Non établie pour la frappe à froid et le roulage du filet.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Le produit fonctionnel est absent et la **composition réelle reste inconnue** : Ecoinvent ne démontre pas qu'un modèle commun matière + procédé suffit, et son absence de distinction par taille de vis ne prouve pas que la masse par pièce est la seule différence réelle entre les vis #6 et #8. Un même modèle générique ne peut être envisagé que si le fournisseur confirme une composition, un procédé et un revêtement équivalents.

#### Données nécessaires

Composition matérielle confirmée, revêtement, procédé de fabrication complet, masse par pièce.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous confirmation fournisseur.** Ne pas présumer que la masse est la seule variable différenciante avant confirmation.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Vis d'assemblage #8 — P1

#### Produit métier

Vis d'assemblage #8, composant fonctionnel plutôt que métal générique.

#### Équivalent Ecoinvent identifié

Mêmes briques matière/procédé que pour la vis #6 : `market for steel, low-alloyed` (`1af29f22-5a0a-3130-a65d-6ea9928f522a`), `wire drawing, steel` (`5563eb07-b684-33b5-bf13-a8f604fe5b06`), `zinc coating, pieces` (`9cc6fb22-00d5-3d78-8971-0d46751d263c`). Aucun produit fonctionnel vis n'a été identifié.

#### Correspondance

- **Produit / fonction :** Non établie.
- **Composition / matière :** Partielle, mêmes réserves que la vis #6.
- **Technologie / procédé :** Non établie pour la frappe à froid et le roulage du filet.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Même lacune que la vis #6 : **composition inconnue**. Un même modèle pour #6 et #8 n'est envisageable que si le fournisseur confirme une composition, un procédé et un revêtement équivalents entre les deux tailles ; les paramètres propres à la vis #8 (masse, longueur) restent à établir séparément.

#### Données nécessaires

Composition matérielle confirmée, revêtement, procédé de fabrication complet, masse par pièce.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous confirmation fournisseur.** Appliquer la même architecture que la vis #6 seulement si l'équivalence est confirmée par le fournisseur.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Charnière invisible de meuble — P1

> **Reconfirmé par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** absence de produit fonctionnel reconfirmée (0 résultat sur `process` ET `flows` pour `hinge`), complétée par une exploration de la catégorie ISIC 259 (473 process, échantillon de 30). Une première réconciliation faite sur la mauvaise base `cups` (avec un tableau détaillé de briques génériques et leurs UUID) est **invalidée en totalité** — la nouvelle session ne rapporte aucun UUID de brique nommément pour la charnière, seulement des noms de process génériques.

#### Produit métier

Charnière invisible de meuble ; Blum est un exemple atelier, pas le nom principal du composant.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié, confirmé indépendamment au Lot 2D et sur Ecoinvent 3.11 (2026-09-16). Services et matières génériques identifiés cette session pour une éventuelle reconstruction bottom-up par masse (noms de process seulement, **aucun UUID retenu**) : acier ou laiton comme matière de base, `deep drawing, steel` (emboutissage) comme mise en forme, `turning`/`milling` (tournage/fraisage) pour l'usinage, `zinc coating, pieces` comme revêtement anticorrosion. La catégorie ISIC 259 ne contient, de façon générale, que des services de transformation métallique génériques et des matières premières — aucun produit fini de quincaillerie meuble.

#### Correspondance

- **Produit / fonction :** Non établie (absence confirmée deux fois — Lot 2D, Ecoinvent 3.11 2026-09-16).
- **Composition / matière :** Faible — aucune nomenclature du produit réel disponible ; matières génériques (acier, laiton) identifiées mais non assignées à un produit précis.
- **Technologie / procédé :** Non établie pour le produit réel ; noms de process génériques de mise en forme/revêtement identifiés pour une reconstruction bottom-up, sans UUID retenu cette session.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

C'est le cas le plus bloquant du lot : la **nomenclature physique/composition du composant est elle-même la première donnée manquante**. Sans elle, aucune reconstruction matière + procédé ne peut être envisagée. Niveau de correspondance : **ABSENT** (produit) / **RECONSTRUCTION** envisageable une fois la nomenclature obtenue.

#### Données nécessaires

Masse totale, matériaux constitutifs et leurs parts, revêtement, nombre de pièces, origine de fabrication.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur** (masse par pièce, matière — acier zingué le plus souvent). Cette donnée reste bloquante avant toute tentative de modélisation ; une fois obtenue, construire un proxy manuel : masse d'acier (`market for steel, low-alloyed`) + revêtement zinc + une combinaison raisonnable d'opérations de formage (emboutissage + perçage) — sans réutiliser les UUID de briques génériques cités dans une réconciliation antérieure faite sur la mauvaise base.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

### Coulisse de tiroir — P1

> **Priorisation et méthode (validation Nicolas, 2026-09-15) :** la coulisse de tiroir est l'un des composants de quincaillerie prioritaires (avec charnières, poignées, pieds/niveleurs et ferrures de suspension). Ne pas subdiviser inutilement toutes les technologies et dimensions de coulisses : prévoir plutôt l'utilisation future d'un **modèle standard représentatif**, en privilégiant un produit dont la documentation fournisseur est suffisamment détaillée. **Action : `À vérifier / choisir modèle fournisseur de référence`.**
>
> **Reconfirmé par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16) :** absence de produit fonctionnel reconfirmée (0 résultat pour `drawer slide`). Une réconciliation antérieure faite sur la mauvaise base `cups` est invalidée. Des services génériques de reconstruction bottom-up ont été identifiés (formage à froid de l'acier, extrusion d'aluminium — `impact extrusion of aluminium`), sans UUID retenu cette session.

#### Produit métier

Coulisse de tiroir ; exemple atelier Blum, profondeurs typiques de 10 à 22 pouces.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié (`drawer slide`, `drawer runner`, `telescopic rail` ou équivalent), confirmé indépendamment au Lot 2D et sur Ecoinvent 3.11 (2026-09-16). Aucun système de roulement ou procédé spécifique n'a été caractérisé. Pour une reconstruction bottom-up : acier (tôle/profilé) + services de formage à froid, ou extrusion d'aluminium (`impact extrusion of aluminium`) — noms de process identifiés cette session, sans UUID retenu.

#### Correspondance

- **Produit / fonction :** Non établie.
- **Composition / matière :** Faible — même le matériau dominant n'est pas établi pour le produit réel.
- **Technologie / procédé :** Non établie pour le produit réel.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Comme pour la charnière, la **composition et le système fonctionnel du composant sont la première donnée manquante**. Niveau de correspondance : **ABSENT** (produit) / **RECONSTRUCTION** envisageable une fois le modèle fournisseur de référence choisi et sa nomenclature obtenue.

#### Données nécessaires

Masse, matériaux constitutifs et leurs parts, revêtement, longueur, origine — à établir pour le **modèle fournisseur de référence unique** retenu (voir action ci-dessus), pas pour l'ensemble des technologies/dimensions existantes.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur** du modèle de référence choisi.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (reconfirmation + pistes de reconstruction bottom-up).

---

### Poignée de meuble métallique — P1

> **Statut clarifié par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)).** Une première réconciliation, faite sur la mauvaise base `cups`, contenait une incohérence interne non résolue sur ce produit (deux affirmations contradictoires sur le statut de la recherche) — ce point est désormais **sans objet** : cette réconciliation est invalidée en totalité. La nouvelle interrogation, menée depuis zéro (`furniture handle`, plus l'exploration de la catégorie ISIC 259), confirme sans ambiguïté l'**absence de produit fonctionnel** (0 résultat).

#### Produit métier

Poignée de meuble métallique.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié, confirmé au Lot 2D et sur Ecoinvent 3.11 (2026-09-16). `section bar extrusion, aluminium` (Lot 2D) constitue une brique potentiellement intéressante, **uniquement si** une poignée réelle est confirmée comme profilé aluminium ; la session du 2026-09-16 identifie, plus généralement, zinc/laiton/acier + moulage/usinage comme familles de matières et procédés génériques plausibles, sans UUID retenu.

#### Correspondance

- **Produit / fonction :** Non établie.
- **Composition / matière :** Conditionnelle — le matériau réel (aluminium supposé) n'est pas confirmé.
- **Technologie / procédé :** Conditionnelle à la confirmation du matériau.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Le **matériau réel n'est pas confirmé** : la brique d'extrusion d'aluminium n'est pertinente que si la poignée est effectivement un profilé aluminium, ce qui ne doit pas être présumé.

#### Données nécessaires

Matériau réel (variable bloquante), masse, finition, procédé, fixation incluse ou non, origine.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous confirmation fournisseur.** Confirmer le matériau avant de modéliser quoi que ce soit.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (absence reconfirmée sans ambiguïté).

---

### Pied niveleur / niveleur — P1

> **Couvert par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)).** Absence de produit fonctionnel confirmée (`levelling foot`, 0 résultat) ; auparavant non couvert, ce point n'est donc plus ouvert pour la recherche Ecoinvent elle-même — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md) pour ce qui reste à faire (données fabricant).

#### Produit métier

Pied de nivellement, composant actuellement en plastique.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié (les résultats `foot` étaient des faux positifs, au Lot 2D comme le 2026-09-16). Une piste `polypropylene + injection moulding` peut représenter une partie plastique **si cette composition est confirmée**, mais elle ne couvre pas un éventuel insert métallique fileté (acier).

#### Correspondance

- **Produit / fonction :** Non établie.
- **Composition / matière :** Conditionnelle — composition complète non confirmée, insert métallique non couvert par la piste plastique.
- **Technologie / procédé :** Conditionnelle.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

La **composition complète du composant** (corps plastique et insert métallique éventuel) n'est pas confirmée ; la piste polypropylène + moulage par injection ne couvre qu'une partie plausible du produit.

#### Données nécessaires

Composition complète (corps et insert), masse par pièce.

#### Recommandation

**Reconstruire à partir de matière + procédé, sous confirmation fournisseur.** Confirmer corps/insert et masses avant modélisation.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

### Ferrure métallique de suspension pour meuble mural — P1/P2

> **Couvert par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)).** Absence de produit fonctionnel confirmée (`French cleat`, 0 résultat) ; auparavant non couvert, désormais diagnostiqué.

#### Produit métier

Ferrure métallique de suspension, type clé française / French cleat.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié (recherche `French cleat`, 0 résultat, plus exploration de la catégorie ISIC 259). Comme pour les autres familles de quincaillerie, seuls des services génériques de transformation métallique (acier plié/percé) sont disponibles comme pistes de reconstruction, sans UUID retenu cette session.

#### Correspondance

- **Produit / fonction :** Non établie — absence confirmée.
- **Composition / matière :** Non établie pour le produit réel.
- **Technologie / procédé :** Non établie ; pistes génériques (acier plié/percé) seulement.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

**Produit fonctionnel absent**, confirmé par recherche directe sur Ecoinvent 3.11. Comme pour la charnière et la coulisse, la nomenclature physique du composant (matériau, masse, dimensions) est la première donnée manquante avant toute reconstruction.

#### Données nécessaires

Matériau, masse, dimensions et procédé de fabrication réels.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Ne pas surinvestir avant d'avoir ces données.

#### Source du diagnostic

[Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

## 8. Emballage

Les emballages sont suivis séparément des matériaux constitutifs du meuble.

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Carton d'emballage / carton ondulé | Dataset QC (Lot 2A) **reconfirmé indépendamment sur Ecoinvent 3.11** (2026-09-16) | OK — correspondance directe, régionalité crédible | linerboard et électricité non vérifiés ; données de 2008 | 🟢 Utilisable |
| P1 | Film à bulles / papier bulle | Absence confirmée sur Ecoinvent 3.11 (2026-09-16, plusieurs synonymes testés, 0 résultat) | Aucune | absent de cette base, avec ces requêtes | 🔴 Lacune majeure |
| P1/P2 | Matériau d'emballage blanc fin en rouleau (film mousse PE — hypothèse forte, non confirmée pour le Québec) | Hypothèse d'identification posée (2026-09-22) ; recherche exhaustive sur Ecoinvent 3.11 (`foam` + 14 variantes lexicales) : aucune mousse PE trouvée | Aucune | identification fournisseur requise ; aucun procédé de moussage adapté au PE disponible | 🟡 À valider |

### Lecture rapide

Le carton ondulé est, d'après le Lot 2A, le cas le plus favorablement régionalisé identifié dans l'ensemble des diagnostics : le marché québécois s'appuyait sur un procédé de fabrication et sur un intrant majeur (le fluting medium) réellement documentés à partir d'une usine québécoise. **Mise à jour (interrogation OpenLCA vérifiée sur Ecoinvent 3.11, 2026-09-16) :** une première réconciliation, faite alors que la mauvaise base OpenLCA (`cups`) était ouverte, avait rapporté une variante Global seulement — ce résultat est invalidé. La nouvelle interrogation **reconfirme indépendamment la variante `Canada, Québec`** (même UUID qu'au Lot 2A), avec une justification méthodologique renforcée : Ecoinvent documente lui-même ce type de marché comme négocié localement, pas globalement — **contrairement au contreplaqué CA-QC, ce dataset résiste à la vérification.** Le film à bulles a été recherché de nouveau sur Ecoinvent 3.11 (`bubble wrap`, `stretch film`, `foam sheet`, `polyethylene foam`, `expanded polystyrene`, `polystyrene foam` — tous à 0 résultat pertinent ou hors sujet) : absence confirmée dans cette base, avec ces requêtes. **Mise à jour (2026-09-22) :** le matériau d'emballage blanc en rouleau (validation métier Nicolas, 2026-09-15) fait désormais l'objet d'une hypothèse d'identification précise — **film mousse de polyéthylène (PE) en rouleau**, par rapprochement avec un produit commercial de référence externe, non confirmée pour les entreprises québécoises concernées. Une recherche exhaustive sur Ecoinvent 3.11 (le terme `foam` seul, plus 14 variantes lexicales ciblées) confirme l'absence de toute mousse PE dans la base ; seule une résine PE-LD vierge existe comme brique matière, et le seul procédé de moussage générique disponible est documenté par Ecoinvent lui-même comme calibré pour le polystyrène — voir la fiche ci-dessous.

### Carton d'emballage / carton ondulé — P1

> **Reconfirmé indépendamment par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)).** Une première réconciliation, faite alors que la mauvaise base OpenLCA (`cups`) était ouverte, avait rapporté un UUID différent (`b8c827da-…`), localisé Global et décrit comme une boîte formée — **ce résultat est invalidé**. La nouvelle interrogation, menée depuis zéro, retrouve le **même UUID** que le Lot 2A (`2424352b-…`), toujours localisé **Canada, Québec**, avec une justification renforcée : la documentation Ecoinvent précise elle-même que ce type de produit se négocie localement, pas globalement. **C'est un contre-exemple important au contreplaqué CA-QC** (voir fiche ci-dessus) : deux datasets peuvent tous deux porter l'étiquette `CA-QC` sans avoir le même niveau de représentativité réelle — le contreplaqué est une copie administrative du dataset européen, alors que le carton ondulé a une base méthodologique qui justifie sa représentativité québécoise.

#### Produit métier

Carton d'emballage / carton ondulé.

#### Équivalent Ecoinvent identifié

**Dataset vérifié et reconfirmé (Lot 2A + Ecoinvent 3.11, 2026-09-16) :**

- **Dataset (marché) :** `market for corrugated board box`
- **UUID :** `2424352b-3df3-3415-9fbf-a6b1eff0ce60`
- **Location :** Canada, Québec — **marché explicitement régional** d'après la documentation Ecoinvent elle-même
- **Unité / base de comparaison :** kg
- **Briques en amont (Lot 2A) :** `corrugated board box production` (`17317a18-28b4-335a-a96d-68789b9bfb70`, Canada, Quebec, collecte documentée sur une usine réelle, mix de production daté de 2008 — cet UUID est également celui relevé par la session du 2026-09-16 parmi « et autres » géographies) ; `containerboard production, fluting medium, semichemical, 40% recycled content` (`27a2145c-86e5-3f1e-8219-5d1720d12cab`, Canada, Québec, décrit comme issu d'une usine québécoise réelle).

#### Correspondance

- **Produit / fonction :** Bonne — correspondance directe, reconfirmée deux fois.
- **Composition / matière :** Moyenne — le fluting medium est confirmé québécois ; le linerboard, plus gros intrant en masse (0,7434 kg), n'a pas été vérifié ; des intrants chimiques mineurs (amidon de maïs, encre offset) restent génériques.
- **Technologie / procédé :** Forte — procédé de fabrication des boîtes documenté sur une usine réelle.
- **Géographie :** Forte, et **désormais confirmée à deux reprises** (marché, production, fluting medium) sur deux sessions indépendantes.
- **Données primaires québécoises :** Forte mais partiellement ancienne (données de fabrication datées de 2008) ; électricité non résolue comme CA-QC.

#### Lacune Ecoinvent

La régionalisation descend jusqu'au procédé de production et à un intrant majeur (fluting medium), ce qui distingue nettement ce cas des autres datasets `CA-QC` examinés (notamment le contreplaqué, copie administrative du dataset européen). La lacune résiduelle porte sur les **données primaires québécoises absentes ou non vérifiées** pour le linerboard (le plus gros intrant en masse) et pour l'électricité, ainsi que sur l'ancienneté (2008) des données de fabrication des boîtes.

#### Données nécessaires

Vérification de la géographie et de la composition du linerboard, résolution géographique de l'électricité, actualisation éventuelle des données de fabrication.

#### Recommandation

**Utiliser comme référence documentée et représentative**, sous réserve du linerboard et de l'énergie non vérifiés, et de l'ancienneté (2008) des données de fabrication.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (reconfirmation indépendante, même UUID).

---

### Film à bulles / papier bulle — P1

> **Recherché par interrogation OpenLCA vérifiée sur Ecoinvent 3.11 (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** une première réconciliation, faite sur la mauvaise base `cups`, est invalidée. Une nouvelle recherche a été menée sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` avec plusieurs synonymes : `corrugated board` (8 résultats), `bubble wrap` (0), `polyethylene foam` (0), `expanded polystyrene` (16, tous déchets/traitement), `polystyrene foam` (14, tous isolation périmétrique rigide), `stretch film` (0), `packaging film` (3), `foam sheet` (0).

#### Produit métier

Film à bulles / papier bulle d'emballage.

#### Équivalent Ecoinvent identifié

**Absence confirmée dans cette base, avec ces requêtes** — aucun résultat pertinent sur `bubble wrap`, `stretch film`, `foam sheet` ; `expanded polystyrene` et `polystyrene foam` retournent des résultats mais tous hors sujet (déchets/traitement, ou mousse rigide d'isolation périmétrique — voir fiche « Matériau d'emballage blanc » ci-dessous).

#### Correspondance

Non établie — niveau **ABSENT**.

#### Lacune Ecoinvent

Absence confirmée pour l'ensemble des synonymes usuels testés sur deux sessions indépendantes. Sa composition exacte reste elle-même à confirmer auprès du fournisseur avant tout mapping ultérieur si de nouveaux synonymes devaient être testés.

#### Données nécessaires

Composition exacte du film (à confirmer auprès du fournisseur).

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** La recherche Ecoinvent est jugée suffisamment exhaustive sur les synonymes usuels testés ; ne pas multiplier davantage les recherches Ecoinvent pour ce produit.

#### Source du diagnostic

[Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

### Matériau d'emballage blanc fin en rouleau (film mousse PE — identification fortement plausible, non confirmée pour les entreprises québécoises) — P1/P2

> **Nouvel objet (validation métier Nicolas, 2026-09-15).** Matériau blanc, très fin, vendu en gros rouleau, utilisé pour envelopper/protéger les meubles à l'expédition. Ne pas confondre avec le film à bulles (ci-dessus), qui est un produit distinct déjà identifié dans la taxonomie.
>
> **Hypothèse d'identification (2026-09-22) — interprétation, pas un fait établi :** la description de Nicolas (matériau blanc, très léger et fin, vendu en gros rouleaux, utilisé pour envelopper/protéger des meubles) correspond au profil commercial d'un **film mousse de polyéthylène (PE) en rouleau**, tel que vendu par exemple par [sedemballage.com](https://sedemballage.com/produit/rouleau-de-film-mousse/) : mousse PE blanche, souple et légère, en rouleau, pour calage/séparation/protection, épaisseurs courantes 1 à 8 mm. **Ce rapprochement est fondé sur une référence externe générale, pas sur une fiche produit d'une entreprise québécoise cliente** — il reste une hypothèse forte, à confirmer par une fiche technique ou un échantillon du rouleau réellement utilisé en atelier avant toute utilisation dans un modèle. Mettre à jour cette fiche si la confirmation ou l'infirmation arrive.
>
> **Mise à jour (interrogation OpenLCA vérifiée sur Ecoinvent 3.11, 2026-09-22 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** recherche ciblée sur l'hypothèse « mousse PE en rouleau », en plus des termes déjà testés le 2026-09-16 (`corrugated board`, `bubble wrap`, `polyethylene foam`, `expanded polystyrene`, `polystyrene foam`, `stretch film`, `packaging film`, `foam sheet`). Nouveaux termes testés le 2026-09-22 : `PE foam`, `packaging foam`, `foam packaging`, `expanded polyethylene`, `EPE`, `LDPE foam`, `polyethylene foam film`, `foil`, `wrap`, `interleaving`, `nonwoven`, `polyolefin foam`, `cushioning`, `expanded plastic`, `cross-linked polyethylene`, plus une recherche exhaustive du terme générique `foam` seul (55 process / 15 flux, tous inspectés). **Aucun résultat pertinent** pour une mousse PE — voir détail ci-dessous.

#### Produit métier

Matériau d'emballage blanc fin, en gros rouleau, pour l'enveloppement/protection des meubles. **Interprétation (2026-09-22) :** très probablement un film mousse de polyéthylène (PE) en rouleau, sur la base du rapprochement avec un produit commercial de référence externe (voir hypothèse ci-dessus) — pas encore une identification confirmée pour les entreprises québécoises concernées.

#### Équivalent Ecoinvent identifié

**Fait observé dans Ecoinvent 3.11 (2026-09-22) :** aucun dataset process ni flux ne correspond aux termes `polyethylene foam`, `PE foam`, `packaging foam`, `foam packaging`, `expanded polyethylene`, `LDPE foam`, `polyethylene foam film`, `interleaving`, `polyolefin foam`, `cushioning`, `expanded plastic`, `cross-linked polyethylene` (0 résultat pour chacun). `EPE` retourne 4 process / 1 flux, mais il s'agit d'un faux positif de sous-chaîne (« di**e**thylenetriamine**pe**ntaacetic acid », DTPA — un chélatant, sans rapport). `foil`, `wrap` et `nonwoven` retournent des résultats hors sujet (feuille collectrice de batterie Li-ion, film EVA, service de laminage à liant acrylique, papier d'emballage alimentaire à usage unique, textiles non-tissés en polyester/polypropylène pour l'industrie textile) — aucun n'est une mousse PE d'emballage.

La recherche exhaustive du terme `foam` seul (55 correspondances process, 15 flux, toutes inspectées) confirme qu'**aucune mousse de polyéthylène n'existe dans cette base**, quel que soit le terme utilisé. L'univers complet des « foam » disponibles est : mousse de polyuréthane (flexible et rigide, plusieurs variantes), mousse de polystyrène rigide (`polystyrene foam slab`, isolation périmétrique), mousse urée-formaldéhyde rigide (isolation), verre mousse (`foam glass`, construction), un agent moussant générique (`foaming agent`), un matelas en mousse PU (`mattress production, polyurethane foam`), et un procédé générique **`polymer foaming`** (voir ci-dessous) — aucun n'est une mousse PE souple d'emballage.

**Briques disponibles pour une reconstruction, avec leurs limites documentées :**

| Brique | Dataset | Géographie | Unité | UUID | Constat |
|---|---|---|---|---|---|
| Matière (résine PE-LD vierge) | `market for polyethylene, low density, granulate` | Global | kg | `08d7cf9a-4301-321f-947c-06849afd126c` | Ecoinvent documente cette résine comme utilisée notamment pour « films, e.g. for the production of plastic bags, packaging material » — cohérent comme matière de départ, mais c'est une résine solide, pas une mousse. |
| Procédé de moussage générique | `polymer foaming` (Europe `2b9297ce-…`, Rest of World `04468313-…`, **Canada, Quebec** `df7d95f6-…`) | Europe / RoW / CA-QC | kg | voir liste | **Rejeté comme proxy sans réserve majeure.** Ecoinvent documente lui-même ce procédé : « 1 kg of this process equals 1 kg of expanded plastics (**usually polystyrene**) ». L'agent gonflant utilisé est le **pentane** (0,015 kg/kg), typique du moussage par perles de polystyrène expansible (EPS), pas de la mousse PE (généralement extrudée, agents gonflants différents, parfois réticulée). Les trois variantes géographiques ont des intrants matière identiques (même recette, même dosage de pentane) — seule l'électricité/chaleur diffère par marché régional ; **la variante Canada-Quebec n'apporte aucune donnée primaire québécoise**, même schéma que le contreplaqué CA-QC. |
| Faux-ami écarté | `market for plastic profiles` / `plastic converting, plastic profiles` (Europe, `f5cfa5ea-…` / `408028e6-…`) | Europe | kg | — | **Rejeté, faux-ami explicite.** Catégorie « Materials recovery » (déchets) : décrit la conversion d'un **mélange de plastiques recyclés post-consommation** (PE/PP/LDPE/PA) en profilés (type bois plastique recyclé), pas une mousse PE vierge en rouleau — composition et filière incompatibles. |

#### Correspondance

- **Produit / fonction :** Aucune correspondance directe ni partielle, y compris pour l'hypothèse « mousse PE » désormais posée. **ABSENT.**
- **Composition / matière :** Une brique matière PE-LD vierge existe et est plausible (`08d7cf9a-…`), mais elle représente une résine, pas une mousse.
- **Technologie / procédé :** Le seul procédé de moussage générique disponible (`polymer foaming`) est documenté par Ecoinvent lui-même comme calibré pour le polystyrène (agent gonflant pentane) — l'appliquer à du PE ajouterait une hypothèse non documentée supplémentaire, plus faible que son usage déjà approximatif pour le polystyrène.
- **Géographie :** La variante « Canada, Quebec » du procédé de moussage est, comme pour le contreplaqué, une reprise du même schéma d'intrants que les autres géographies — pas une donnée primaire québécoise.
- **Données primaires québécoises :** Aucune identifiée, pour la matière comme pour le procédé.

#### Lacune Ecoinvent

**Produit fonctionnel absent (fait établi par une recherche exhaustive sur le terme `foam` et 14 variantes lexicales ciblées).** Une reconstruction matière + procédé reste théoriquement possible (PE-LD vierge + moussage), mais le seul procédé de moussage de la base est documenté comme spécifique au polystyrène (agent gonflant, chimie de moussage) — l'utiliser pour du PE constituerait une hypothèse non validée par Ecoinvent lui-même, à ne présenter que comme un proxy de dernier recours, explicitement signalé comme tel.

#### Données nécessaires

**Confirmation ou infirmation de l'hypothèse « film mousse PE »** auprès des entreprises québécoises concernées (fiche technique ou échantillon du rouleau réellement utilisé) — l'identification par comparaison à un fournisseur générique externe (sedemballage.com) n'est pas une preuve pour leur produit exact. Si confirmée : grammage, épaisseur (1 à 8 mm selon la référence externe), largeur de rouleau, procédé de fabrication réel (extrusion, réticulation) pour juger de la pertinence du procédé `polymer foaming` ou pour documenter son inadéquation plus précisément.

#### Recommandation

**Traiter « film mousse PE » comme l'hypothèse de travail par défaut**, sans la présenter comme confirmée pour les entreprises québécoises. Ne pas utiliser `polymer foaming` comme proxy sans avertissement explicite de son calibrage polystyrène. Continuer à écarter `packaging film, LDPE` (film plat non alvéolé) et `polystyrene foam slab` (mousse rigide XPS) comme non pertinents pour une mousse PE souple. Obtenir en priorité une fiche technique ou un échantillon auprès de l'atelier/fournisseur avant toute intégration dans un modèle.

#### Source du diagnostic

[Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) ; recherche ciblée complémentaire sur l'hypothèse « mousse PE » et clôture du terme `foam`, 2026-09-22 (voir mise à jour dans ce même rapport).

---

## 9. Données transversales

> **Phase ultérieure — hors diagnostic matériaux prioritaire (validation métier Nicolas, 2026-09-15).** Électricité d'atelier, transports entrants/sortants, chutes de bois/panneaux, poussières, gaz/chaleur, eau et les autres données transversales listées ci-dessous restent pertinentes pour l'ACV complète, mais ne sont **pas prioritaires actuellement**. Elles sont conservées dans le référentiel et la méthode, sans être retirées.
>
> **Mise à jour de traçabilité :** le [Lot 2G](diagnostic/ecoinvent-representativite-qc-lot-2g.md) (complété par le Lot 2G-bis pour le gaz naturel/chaleur, l'eau de procédé et les eaux usées) a depuis approfondi ces dix objets transversaux avec des conclusions plus précises que celles reflétées ci-dessous, qui datent des Lots 2A–2D. Cette section n'a pas été resynchronisée en détail dans cette passe, conformément à sa mise en phase ultérieure ; se référer au Lot 2G et au [tableau transversal des lacunes](diagnostic/tableau-transversal-lacunes-ecoinvent.md) pour l'état le plus à jour de chacun de ces dix objets.

Ces flux et processus sont volontairement séparés des matériaux et composants achetés.

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Électricité d'atelier | Dataset non isolé | Non établie | accès/outil insuffisant | 🟡 À valider |
| P1 | Transport entrant des matériaux et composants | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Transport sortant du meuble fini | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Chutes de bois massif | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Chutes de panneaux | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Sciures / poussières d'usinage | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | Gaz naturel / chaleur | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | Eau de procédé / nettoyage | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | Eaux usées | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | Résidus contaminés (colles, finitions, solvants, chiffons) | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Seule l'électricité d'atelier a fait l'objet d'une tentative d'inspection dans les Lots 2A–2D, et celle-ci a échoué pour des raisons d'outillage plutôt que de contenu : le dataset `CA-QC` n'a pas pu être isolé avec l'interface disponible, ce qui ne permet ni de le classer, ni de conclure à son absence dans Ecoinvent. Tous les autres flux et processus transversaux (transport, chutes, sciures, énergie thermique, eau, résidus) restent à ce stade non approfondis.

### Électricité d'atelier — P1

#### Produit métier

Électricité d'atelier ; vérifier et représenter le mix électrique québécois réellement applicable.

#### Équivalent Ecoinvent identifié

Cible visée : `market for electricity, medium voltage`, location `CA-QC`. **Ce dataset n'a pas pu être isolé** avec l'interface MCP utilisée : la recherche par nom retourne 223 processus homonymes sans exposer la géographie, la recherche du terme `Quebec` dans les noms retourne zéro résultat, les providers d'exchanges sont retournés en texte sans UUID ni localisation, et une extraction en masse de la catégorie électrique a expiré après plusieurs minutes. Un dataset provincial pour l'Île-du-Prince-Édouard a été observé, confirmant l'existence d'une modélisation provinciale canadienne dans Ecoinvent, sans permettre de déduire le contenu du dataset québécois.

#### Correspondance

- **Produit / fonction :** Non établie — dataset non isolé.
- **Composition / matière :** Non établie.
- **Technologie / procédé :** Non établie.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Non établi.

#### Lacune Ecoinvent

Il s'agit d'une **limite d'accès/outil**, distincte d'une lacune Ecoinvent démontrée : l'impossibilité de résoudre l'électricité `CA-QC` via l'interface MCP ne prouve pas l'absence du dataset dans la base. Tant que le dataset n'est pas isolé directement (par exemple via un filtre `location = CA-QC` dans openLCA ou une requête locale plus adaptée), aucun critère de représentativité ne peut être évalué.

#### Données nécessaires

Accès permettant un filtre direct par géographie pour isoler le dataset électricité `CA-QC`, puis analyse de sa technologie, ses intrants et ses données primaires.

#### Recommandation

**Données insuffisantes pour décider.** Résoudre d'abord la limite d'accès avant toute classification A/B/C/D.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md)

---

### Transport entrant des matériaux et composants — P1

#### Produit métier

Transport entrant des matériaux et composants vers l'atelier.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. Les distances, charges et véhicules représentatifs restent à définir.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer les distances, les charges et les types de véhicules représentatifs.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Transport sortant du meuble fini — P1

#### Produit métier

Transport sortant du meuble fini depuis l'atelier.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. Les distances, charges et véhicules représentatifs restent à définir.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer les distances, les charges et les types de véhicules représentatifs.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Chutes de bois massif — P1

#### Produit métier

Chutes de bois massif générées en atelier.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. La quantité produite doit être associée à la pratique réelle du fabricant avant de choisir un scénario ou un dataset.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la quantité produite et la pratique réelle du fabricant (déchèterie, incinération, recyclage/valorisation).

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Chutes de panneaux — P1

#### Produit métier

Chutes de panneaux générées en atelier, distinctes des chutes de bois massif.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la quantité produite et la pratique réelle du fabricant.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Sciures / poussières d'usinage — P1

#### Produit métier

Sciures et poussières d'usinage.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. La collecte et la pratique réelle du fabricant doivent être caractérisées.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer le mode de collecte et la pratique réelle du fabricant.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Gaz naturel / chaleur — P2

#### Produit métier

Gaz naturel / chaleur, à inclure uniquement si réellement utilisé dans le périmètre.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. L'usage réel dans le périmètre reste à confirmer.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer l'usage réel dans le périmètre et les quantités.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Eau de procédé / nettoyage — P2

#### Produit métier

Eau de procédé et de nettoyage.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. Les usages et quantités réels restent à vérifier.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer les usages réels et les quantités.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Eaux usées — P2

#### Produit métier

Eaux usées de l'atelier.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. Le traitement réellement appliqué reste à établir.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer le traitement réellement appliqué.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Résidus contaminés par colles, finitions, solvants ou chiffons — P2

#### Produit métier

Résidus contaminés par colles, finitions, solvants ou chiffons.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. Les flux et pratiques réels doivent être caractérisés séparément pour chaque type de résidu.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la nature exacte des résidus et la pratique réelle du fabricant.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

## Diagnostics de représentativité

Les diagnostics techniques détaillés, incluant les exchanges complets, les comparaisons quantitatives entre géographies et les grilles de contrôle méthodologiques, sont disponibles séparément :

- [Lot 2A — Contreplaqué CA-QC, carton ondulé, électricité d'atelier](diagnostic/ecoinvent-representativite-qc-lot-2a.md)
- [Lot 2B — Panneau de particules brut, MDF brut, TFL sur panneau de particules, TFL sur MDF](diagnostic/ecoinvent-representativite-qc-lot-2b.md)
- [Lot 2C — Érable, frêne, merisier/bouleau jaune, chêne rouge](diagnostic/ecoinvent-representativite-qc-lot-2c.md)
- [Lot 2D — Bandes de chant et quincaillerie](diagnostic/ecoinvent-representativite-qc-lot-2d.md)
- [Lot 2E — Stratifié HPL, placage bois, panneau plaqué bois acheté fini](diagnostic/ecoinvent-representativite-qc-lot-2e.md)
- [Lot 2F — Adhésifs : PVA/PVAc, EVA hot-melt, colle contact, polyuréthane](diagnostic/ecoinvent-representativite-qc-lot-2f.md)
- [Lot 2G — Données transversales de fabrication (électricité, transport, chutes, sciures, gaz/chaleur, eau, eaux usées, résidus contaminés)](diagnostic/ecoinvent-representativite-qc-lot-2g.md)
- [Diagnostic OpenLCA vérifié — 2026-09-16, corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) — interrogation réelle et vérifiée de `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` via le connecteur MCP OpenLCA (contreplaqué merisier/Baltic, papier mélaminé atelier, bande de chant PE, colles PVAc/colle contact, quincaillerie, emballages). Remplace intégralement une première réconciliation invalidée (commit `aaabecd`), faite par erreur sur la mauvaise base OpenLCA (`cups`). Comptes rendus bruts de session : [`diagnostic/mcp-ecoinvent-3.11-partie-1.md`](diagnostic/mcp-ecoinvent-3.11-partie-1.md) et [`diagnostic/mcp-ecoinvent-3.11-partie-2.md`](diagnostic/mcp-ecoinvent-3.11-partie-2.md).

Trois documents transversaux complètent désormais ces lots individuels :

- [Tableau transversal des lacunes Ecoinvent](diagnostic/tableau-transversal-lacunes-ecoinvent.md) — une ligne par produit métier, toutes familles confondues.
- [Synthèse des spécificités québécoises](specificites-quebecoises.md) — ce qui est démontré par les analyses existantes vs ce qui reste une hypothèse à vérifier.
- [Liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md) — recherches à effectuer par une instance disposant du connecteur OpenLCA.

Ces sept lots ont établi plusieurs enseignements méthodologiques transversaux, reflétés dans les fiches ci-dessus :

1. Une localisation `CA-QC` ne prouve pas la présence de données primaires québécoises ; elle doit être distinguée de la déclaration narrative, de la comparaison quantitative avec une version étrangère équivalente et de la profondeur réelle de régionalisation.
2. Pour chaque matériau, il faut distinguer **produit métier réel → équivalent Ecoinvent → correspondance physique → représentativité québécoise → lacune → donnée nécessaire pour corriger cette lacune.**
3. Pour les composants manufacturés, il faut distinguer produit fonctionnel absent, nomenclature/composition absente, procédé absent, et reconstruction possible mais non validée.
4. Une matière disponible dans Ecoinvent ne signifie pas que le composant fonctionnel est correctement représenté.
5. Pour les bois massifs, l'existence d'un dataset générique `hardwood` ne représente pas automatiquement l'essence québécoise ciblée ; la transformation détruit généralement la traçabilité de l'essence dans le flow générique.
6. Pour le PVC, un exchange `waste polyvinylchloride` est un indice quantitatif de spécificité matière du procédé de calandrage, pas une preuve que le dataset représente une ligne réelle de chants PVC.
7. Pour les vis #6 et #8, un modèle commun ne peut être envisagé que si le fournisseur confirme composition, procédé et revêtement équivalents.
8. Pour charnières et coulisses, la première donnée manquante est la nomenclature physique/composition du composant acheté.
9. La richesse de représentation d'Ecoinvent pour les technologies de surface de panneaux n'est pas uniforme entre technologies concurrentes visant la même fonction (TFL bien documenté vs HPL et placage bois quasiment absents, Lot 2E).
10. Pour les adhésifs, Ecoinvent propose au mieux des précurseurs chimiques isolés (monomère, résine ou polymère de base) rarement reliés par une formulation ou un procédé au produit métier réellement utilisé (Lot 2F) ; l'absence d'un adhésif dans nos recherches ne prouve pas son absence générale dans la base, puisque d'autres familles d'adhésifs formulés y existent (ex. adhésif époxy pour cadres de fenêtres).
11. **Deux causes distinctes peuvent expliquer un UUID différent pour un nom de produit identique entre deux sessions.** La première, désormais **résolue** : une session entière (intégrée par erreur dans le commit `aaabecd`) a interrogé la mauvaise base OpenLCA (`cups`), pas Ecoinvent — tous ses UUID sont invalidés, voir la note dédiée ci-dessous. La seconde reste **ouverte et distincte** : même entre le Lot 2F (pre-`cups`, MCP) et la nouvelle interrogation vérifiée sur Ecoinvent 3.11 (2026-09-16), certains produits génériques (`vinyl acetate`, `ethylene vinyl acetate copolymer`, `adhesive, for metal`) sont revenus sous des UUID différents alors que les deux sessions ont interrogé une base authentiquement Ecoinvent — sans qu'on puisse établir s'il s'agit d'un changement de version, d'un échantillonnage différent parmi des doublons, ou d'une autre cause. Ce second cas n'est pas résolu et ne doit pas être présumé être une erreur. Dans les deux cas, la prudence méthodologique du point 1 s'applique : ne jamais présumer qu'un UUID cité dans un lot antérieur reste valide sans le revérifier.

## Anomalie résolue — `database_family: "flcac"`

> **Statut : RÉSOLU (2026-09-16, passe corrective).** `flcac` n'est pas une anomalie intrinsèque d'Ecoinvent ; ce n'était que le nom de la mauvaise base OpenLCA restée ouverte.

Une première session (intégrée par erreur dans le commit `aaabecd`) avait rapporté que l'appel `database_info` du connecteur MCP retournait `database_family: "flcac"`, avec 14 912 process / 23 142 flows / 45 méthodes d'impact / 8 systèmes de produits — des compteurs qui ne correspondent à aucune version d'Ecoinvent connue, malgré une nomenclature de process superficiellement compatible (suffixe `Cutoff, U`, arborescence NACE).

**Cause identifiée :** après un changement de poste de travail, c'est la base OpenLCA `cups` qui était restée ouverte dans le logiciel au moment de cette session, et non `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31`. Tous les résultats obtenus durant cette session (UUID, géographies, résultats nuls, conclusions) sont donc invalidés comme preuves Ecoinvent — voir le [diagnostic corrigé](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) pour le détail de ce qui a été retiré ou remplacé.

**Résolution :** après ouverture manuelle de `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` et forçage explicite de `database_family` à `ecoinvent`, `database_info` retourne **25 412 processus, 14 051 flux, 0 méthode d'impact chargée** — cohérent avec cette version d'Ecoinvent sans méthodes chargées. C'est la base effectivement interrogée pour l'ensemble des résultats intégrés dans ce document depuis la passe corrective du 2026-09-16.

**Point distinct, encore ouvert (voir point méthodologique 11 ci-dessus) :** cette résolution n'explique pas tous les écarts d'UUID observés entre sessions. Certains produits génériques (`vinyl acetate`, `ethylene vinyl acetate copolymer`, `adhesive, for metal`) sont revenus sous des UUID différents entre le Lot 2F (MCP, pre-`cups`) et la nouvelle interrogation Ecoinvent 3.11 — deux sessions authentiquement Ecoinvent. Ce point reste `À VÉRIFIER`, sans lien avec l'anomalie `flcac` désormais résolue.

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

La présence d'un nom ou d'une géographie `CA-QC` dans ce document **ne signifie pas que le dataset est validé ni représentatif du Québec**. Un procédé québécois peut dépendre d'intrants RoW, de valeurs européennes ou d'hypothèses technologiques non représentatives. Les datasets indiqués, y compris ceux déjà approfondis dans les Lots 2A–2D, restent des candidats jusqu'à validation et adaptation documentées avec des données de fabricant québécois.
