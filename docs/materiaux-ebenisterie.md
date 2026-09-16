# Référentiel des matériaux et composants — Ébénisterie

> **Statut : V4 — vue consolidée du diagnostic Ecoinvent + validation métier Nicolas (2026-09-15) + réconciliation OpenLCA vérifiée (2026-09-16)**
> Ce document reste l'inventaire métier des produits et composants réellement achetés ou utilisés en atelier. Il intègre, pour les matériaux déjà approfondis, les conclusions des diagnostics de représentativité Ecoinvent (Lots 2A à 2G) ainsi que les décisions de validation métier prises en réunion avec Nicolas le 2026-09-15. Cette réunion a confirmé l'approche générale du diagnostic : l'objectif actuel **n'est pas** de calculer quantitativement les impacts ni de régionaliser les datasets, mais d'identifier et de qualifier les écarts entre les données Ecoinvent disponibles et la réalité de l'ébénisterie québécoise. Un rapport final plus synthétique sera produit ultérieurement ; ce document reste volontairement détaillé et traçable. Les matériaux non encore approfondis conservent leur statut prudent d'origine.
>
> **Session sans accès OpenLCA (2026-09-15)** : les décisions de taxonomie/priorisation de Nicolas (renommage du contreplaqué merisier/bouleau jaune, papier mélaminé en atelier, bande de chant PE, précisions adhésifs, quincaillerie, emballages) ont été intégrées comme des décisions **métier**, pas des résultats de recherche Ecoinvent.
>
> **Réconciliation avec une interrogation OpenLCA réelle (2026-09-16)** : le fichier [`diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md`](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md), produit par interrogation directe du connecteur MCP OpenLCA, a été réconcilié avec les fiches ci-dessous. La plupart des points `À vérifier dans OpenLCA` issus de la passe du 2026-09-15 sont désormais résolus (résultats intégrés, y compris les absences confirmées) ; les points encore ouverts, ainsi que les nouvelles réserves et discrépances constatées entre sessions, sont documentés fiche par fiche et dans la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md). Une anomalie de configuration (`database_family: "flcac"`) reste non résolue — voir la section dédiée en fin de document, avant [Méthode de travail](#méthode-de-travail).
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
| P1 | Contreplaqué merisier / bouleau jaune (yellow birch) / Baltic plywood | Vérifié 2026-09-16 : `market for plywood, for indoor use` (proxy) | Proxy (essence hêtre/hardwood ≠ bouleau) | essence non représentée ; géographie non québécoise | 🟠 À adapter |
| P1 | Panneau de particules mélaminé / TFL | Matière + procédé | Partielle | produit fini absent | 🟣 À reconstruire |
| P1 | MDF mélaminé / TFL | Matière + procédé | Partielle | produit fini absent | 🟣 À reconstruire |
| P1 | MDF plaqué bois acheté fini | Lot 2E : substrat seul disponible | Faible | placage + procédé de collage absents | 🔴 Lacune majeure |
| P1 | Panneau de particules plaqué bois acheté fini | Lot 2E : substrat seul disponible | Faible | placage + procédé de collage absents | 🔴 Lacune majeure |
| P2 | HDF brut | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | OSB | Analyse approfondie non réalisée — **déprioritisé (décision Nicolas, 2026-09-15)** | Non établie | hors périmètre actuel | 🟡 À valider *(hors priorité)* |
| P2 | Autre contreplaqué | Dataset identifié — **déprioritisé (décision Nicolas, 2026-09-15)** | Partielle | hors périmètre actuel | 🟠 À adapter *(hors priorité)* |
| P2 | Panneau plaqué en atelier | Pertinent métier confirmé (2026-09-15) ; analyse Ecoinvent non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Les panneaux bruts (particules, MDF) ont un dataset Ecoinvent dont la fonction correspond bien au produit métier, mais dont la recette, l'énergie et les intrants sont d'origine européenne (EPF) et doivent être adaptés avec des données de fabricant québécois. Les panneaux finis mélaminés/TFL n'existent pas comme produit direct dans Ecoinvent : le meilleur modèle plausible combine le panneau brut et un service générique de revêtement mélaminé, ce qui reste une reconstruction non validée. Le contreplaqué constitue un cas particulier, **reprécisé en réunion de validation métier le 2026-09-15** : le produit métier visé n'est pas un « bouleau russe » générique mais un **contreplaqué merisier / yellow birch / Baltic plywood (contreplaqué baltique)**. **Mise à jour (interrogation OpenLCA directe, 2026-09-16) :** le meilleur candidat vérifié est `market for plywood, for indoor use` (Rest-of-World) — un proxy dont l'écart d'essence est désormais documenté explicitement (hêtre en Europe, hardwood non spécifié en RoW, jamais bouleau) ; ce candidat est distinct de celui du Lot 2A (`plywood production`, autre nom de produit, jamais reconfirmé le 2026-09-16). Voir la fiche ci-dessous pour le détail. Les panneaux achetés déjà plaqués (bois) disposent désormais d'un diagnostic (Lot 2E) : le substrat brut est connu, mais ni le placage fini ni un procédé de collage/pressage spécifique n'ont été identifiés. Le HDF et le placage en atelier n'ont pas encore fait l'objet d'une analyse Ecoinvent approfondie. L'OSB et l'« autre contreplaqué » sont déprioritisés pour l'instant (décision Nicolas, 2026-09-15) : ils ne sont pas retirés de la taxonomie, mais ne constituent plus une cible active du diagnostic.

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
> **Mise à jour (interrogation OpenLCA directe, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** une recherche dédiée aux termes reprécisés a été effectuée (`plywood`, `birch plywood`, `birch`, `veneer`, `laminated veneer`, `Baltic`, `veneer sheet`). **Aucun dataset « birch plywood », « Baltic birch plywood » ou « veneer sheet » spécifique n'a été trouvé (0 résultat)**, dans cette base et avec ces requêtes. Les candidats génériques ci-dessous ont en revanche été vérifiés directement par `process_details`.

#### Produit métier

Contreplaqué de merisier / bouleau jaune (yellow birch) / Baltic plywood (contreplaqué baltique), produit distinct dans la taxonomie métier, non substituable d'emblée par un contreplaqué générique.

#### Équivalent Ecoinvent identifié

**Candidats vérifiés par interrogation OpenLCA directe (2026-09-16) :**

| Dataset | Géographie | Unité | UUID | Constat |
|---|---|---|---|---|
| `market for plywood, for indoor use` | Rest-of-World | m³ | `a263faad-eca2-3956-a706-7e9a7b30364f` | Marché générique, usage intérieur — **candidat retenu ci-dessous** |
| `plywood production, for indoor use` | Europe | m³ | `365758ba-1bb5-32e9-836b-0d45247fa93d` | Intrant bois rond = **hêtre (beech)**, résine urée-formaldéhyde ; données d'un site suisse (1996) déclarées représentatives de l'Europe |
| `plywood production, for indoor use` | Rest-of-World | m³ | `a37de0e5-9ea2-3c17-b652-be171d206f5c` | Même structure, approvisionné via le marché générique « sawlog and veneer log, hardwood » (mélange d'essences non spécifié) |
| `market for plywood, for outdoor use` | Rest-of-World | m³ | `b37a4e46-b1f2-3e0c-a961-90411e492df8` | Usage extérieur — hors périmètre probable pour de l'ébénisterie |
| `hardwood forestry, birch, sustainable forest management` (bois rond, plusieurs flux) | géographies multiples (non détaillées) | m³ / kg | ex. `f04b0987-f44e-3f49-871f-253a8c4df77f` | Bouleau en forêt **existe**, mais n'est **pas relié** à un process de contreplaqué dans la base — c'est une bûche, pas un panneau |

> **Point de vigilance — écart avec le candidat du Lot 2A :** le Lot 2A avait précédemment retenu `plywood production \| plywood \| Cutoff, U`, UUID `5538194d-92b2-3020-bb3e-fbc59cb71248` (comparatif RER `0f52041a-b664-357b-ab50-e48613bff63d`), localisé **Canada, Quebec** et décrit comme une copie d'un échantillon **allemand**. Ce dataset porte un nom de produit de référence différent (`plywood` générique, pas `plywood, for indoor use`) et n'a été ni retrouvé ni infirmé par la recherche du 2026-09-16 — les deux sessions n'ont pas interrogé le même reference product. Aucune variante `Canada, Quebec` n'a été rapportée dans les résultats du 2026-09-16 pour la famille `plywood, for indoor/outdoor use`. **Ce point reste `À VÉRIFIER`** : il n'est pas établi si le dataset CA-QC du Lot 2A existe toujours, a été renommé, ou relève d'une version/famille de base différente (voir la note sur l'anomalie `database_family` en fin de document). Les deux jeux de résultats sont conservés ici sans qu'aucun n'efface l'autre.

#### Correspondance

- **Produit / fonction :** Partielle — un contreplaqué générique « usage intérieur » existe, mais aucun produit spécifique bouleau/Baltic.
- **Composition / matière :** **Écart confirmé, pas une supposition** — la variante Europe documente explicitement le **hêtre (beech)** comme bois rond d'entrée ; la variante Rest-of-World s'approvisionne via un marché « hardwood » **non spécifié à l'espèce**. Aucune des deux ne représente le bouleau.
- **Technologie / procédé :** Non spécifiée dans la description (nombre de plis, épaisseur, type de collage non documentés au-delà de la résine urée-formaldéhyde pour la variante Europe).
- **Géographie :** Européenne (site suisse 1996, jugé représentatif de l'Europe) ou Rest-of-World ; aucune donnée nord-américaine ou québécoise trouvée pour cette famille de datasets.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

**Niveau de correspondance : PROXY** (aucune correspondance directe ni partielle spécifique à l'espèce bouleau, confirmé par interrogation directe). La base ne contient, pour la fonction « contreplaqué usage intérieur », que des datasets à base de hêtre (Europe) ou de hardwood non spécifié (RoW) — c'est un écart de composition documenté par la base elle-même (intrant bois rond déclaré), pas une supposition externe. Aucun dataset plus spécifique au bouleau/Baltic n'a été trouvé avec les requêtes effectuées le 2026-09-16 ; ceci documente une **absence dans cette base, avec ces requêtes** — pas une absence générale ou définitive de toute version d'Ecoinvent.

#### Données nécessaires

Composition exacte en essence si une précision au-delà du proxy hêtre/hardwood est requise pour la quantification ; configuration des plis, origine de fabrication, adhésif utilisé, données de fabricant si une reconstruction plus précise est un jour envisagée.

#### Recommandation

**Conserver le proxy générique `market for plywood, for indoor use` (RoW, UUID `a263faad-eca2-3956-a706-7e9a7b30364f`)** en documentant explicitement l'écart d'essence (hêtre en Europe / hardwood non spécifié en RoW, jamais bouleau). Ne pas rechercher davantage dans Ecoinvent pour l'instant : la recherche du 2026-09-16 est jugée suffisamment exhaustive sur les termes testés. Prioriser l'obtention de données fabricant si une précision d'essence devient nécessaire pour la quantification. Vérifier séparément (voir point de vigilance ci-dessus) si le dataset CA-QC du Lot 2A correspond à un produit distinct toujours disponible.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md) (candidat historique `plywood production`, non reconfirmé) ; [Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (candidats `plywood, for indoor/outdoor use`, essence documentée).

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

- **Dataset :** `plywood production | plywood | Cutoff, U` — le même dataset générique évalué en détail pour l'entrée contreplaqué merisier/yellow birch/Baltic plywood ci-dessus (ex-« bouleau russe »).
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
| P1/P2 | Papier mélaminé appliqué en atelier | Datasets vérifiés (papier + marché + service d'application) | Partielle à directe | réserve d'échelle atelier vs industriel | 🟢 Utilisable *(avec réserve)* |

### Lecture rapide

Le Lot 2E a diagnostiqué le stratifié HPL et le placage de bois naturel : dans les deux cas, aucun produit fini n'a été identifié avec les méthodes d'interrogation disponibles, et la chaîne de reconstruction s'arrête plus tôt que pour le TFL (Lot 2B) — le HPL ne dispose que de deux précurseurs chimiques isolés (résine phénolique, papier kraft non imprégné) sans procédé de liaison identifié, et le placage bois s'arrête à la grume forestière générique, plusieurs étapes avant la feuille de placage elle-même. Le placage de bois naturel partage donc, en amont, certaines des lacunes déjà documentées pour le bois massif (essence, traçabilité — voir Lot 2C), mais la lacune principale du placage lui-même est plus fondamentale : aucune transformation (tranchage/déroulage) n'a été identifiée. **Nouveauté (validation métier Nicolas, 2026-09-15) :** le papier mélaminé n'arrive pas toujours déjà appliqué sur le panneau — certaines entreprises réalisent cette opération en atelier, ce qui leur permet de proposer leurs propres collections/couleurs. **Mise à jour (2026-09-16) :** ce cas d'usage a depuis été diagnostiqué par interrogation OpenLCA directe — c'est, à ce jour, la meilleure correspondance obtenue dans l'ensemble du diagnostic RECQ36 (papier, marché et service d'application distinctement documentés, sans risque de double comptage avec le panneau support).

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
> **Mise à jour (interrogation OpenLCA directe, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** recherche dédiée effectuée (`melamine`). **C'est le meilleur résultat de correspondance de tout le diagnostic RECQ36 à ce jour** — Ecoinvent distingue effectivement le papier, la résine et le service d'application, sans les confondre avec un panneau déjà mélaminé fini.

#### Produit métier

Papier décor mélaminé appliqué sur panneau support (particules ou MDF) directement en atelier, plutôt qu'acheté déjà revêtu.

#### Équivalent Ecoinvent identifié

**Candidats vérifiés par interrogation OpenLCA directe (2026-09-16) :**

| Dataset | Rôle | Géographie | Unité | UUID | Détail vérifié |
|---|---|---|---|---|---|
| `melamine impregnated paper production` | Papier lui-même | Rest-of-World | kg | `b2e9c4ee-c34a-3ad7-9662-0ef0b050cda8` | 0,344 kg kraft brut + 0,377 kg résine mélamine-formaldéhyde + 0,218 kg résine urée-formaldéhyde + 0,388 kg formaldéhyde pour 1 kg de papier fini ; grammage 302 g/m² (dont 104 g/m² de papier support) |
| `market for paper, melamine impregnated` | Marché du papier ci-dessus | Global | kg | `55d422f8-6b1d-358e-9691-8de4be164462` | Marché mondial du papier imprégné |
| `coating service, melamine impregnated paper, double-sided` | **Service d'application** (le procédé recherché) | Rest-of-World | m² | `57d226d1-43bb-37cc-81a2-0b4cda274608` (doublon `6c179811-5e5b-3527-bc52-9b5d679bb29a`) | Consomme 0,604 kg de papier mélaminé (marché) par m² de panneau enrobé double face. **Exclut explicitement le panneau support** (vérifié dans les exchanges — le panneau n'apparaît pas comme intrant) |
| `particle board production/market, uncoated, average glue mix` | Panneau support **nu**, pour composer séparément | RoW / marché | m³ | `87141283-b718-30d4-84b0-39c6c71cc8cf` (production) / `ff40ec39-1d3e-3168-bebc-e5ac10e28ad2` (marché) | Confirme qu'Ecoinvent modélise ce cas de façon **découplée** (substrat nu + service de placage), jamais comme un panneau déjà fini |

> **Distinction préservée / pas de double comptage :** le panneau support (m³) et le service d'application du papier mélaminé (m²) sont deux flux distincts, à additionner (avec une hypothèse d'épaisseur pour convertir m³↔m²), jamais l'un à la place de l'autre. Cette distinction, déjà présente dans la structure Ecoinvent (aucun panneau « déjà mélaminé » fini n'existe comme produit unique), est directement confirmée par l'inspection des exchanges du service d'application.
>
> **Point de vigilance — écart d'UUID avec le Lot 2B :** le Lot 2B avait documenté le même service sous l'UUID `4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78` (Europe), différent des UUID `57d226d1-…`/`6c179811-…` (Rest-of-World) trouvés le 2026-09-16. Il pourrait s'agir de variantes géographiques légitimement distinctes du même service (Europe vs RoW), mais cela n'a pas été confirmé — voir la note sur l'anomalie `database_family` en fin de document. De même, les UUID du panneau de particules brut ci-dessus diffèrent de ceux du Lot 2B (`7690ac93-…`, `1bb7e5df-…`, `7e506572-…`) — **à vérifier**, sans présumer qu'il s'agit d'erreurs.

#### Correspondance

- **Produit / fonction :** Forte pour le service d'application lui-même (correspond bien à « application en atelier », par opposition à un panneau acheté déjà revêtu).
- **Composition / matière :** Forte — composition et grammage du papier documentés précisément (302 g/m², dont 104 g/m² de support).
- **Technologie / procédé :** **Réserve d'échelle** — le procédé documenté est une presse industrielle continue ; sa représentativité pour une presse d'atelier de PME n'est pas confirmée.
- **Géographie :** Rest-of-World / Global — aucune résolution CA-QC.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

**Niveau de correspondance : PARTIEL à DIRECT** (la meilleure correspondance obtenue à ce jour dans le diagnostic RECQ36). La lacune résiduelle porte sur la **représentativité d'échelle** (presse industrielle vs presse d'atelier de PME) et sur la **géographie** (Rest-of-World/Global, pas de variante québécoise).

#### Données nécessaires

Vérifier que le grammage documenté (302 g/m²) correspond à ce qui est réellement utilisé en atelier ; confirmer si le procédé de presse industrielle continue est représentatif d'une presse d'atelier ; nombre de faces réellement traitées, panneau support réel (particules ou MDF).

#### Recommandation

**Utiliser le couple `market for paper, melamine impregnated` + `coating service, melamine impregnated paper, double-sided` comme correspondance documentée « partielle à directe ».** Vérifier le grammage et la représentativité d'échelle (atelier vs industriel) avant intégration définitive dans un modèle de quantification.

#### Source du diagnostic

Service documenté en contexte industriel : [Lot 2B](diagnostic/ecoinvent-representativite-qc-lot-2b.md) (UUID distinct, non reconfirmé). Candidats vérifiés pour l'usage atelier : [Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

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

Aucune bande de chant n'existe comme produit fini direct dans Ecoinvent — confirmé pour le bois véritable (Lot 2D) et, depuis le 2026-09-16, également confirmé par interrogation OpenLCA directe pour le PE (0 résultat sur `process` et `flows`, requêtes `edge band`/`edge banding`). Pour le bois véritable (préencollé ou non), aucune brique de placage ou de bande mince exploitable n'a été trouvée : la lacune commence dès la composante bois elle-même, avant même la question de l'adhésif. Pour l'ABS, le PVC et le PE, la matière de base existe et des procédés de transformation plastique proches existent aussi, mais aucun ne reproduit la géométrie exacte d'une bande de chant ; le PVC dispose d'un indice supplémentaire (un flux de déchet de calandrage spécifique au PVC) qui en fait un proxy légèrement mieux étayé que l'ABS et le PE, sans que cela constitue une validation. Le PVC est conservé dans le référentiel, mais sa place relative face au PE et à l'ABS reste à revérifier (variante « suspension polymerised » non reconfirmée le 2026-09-16, voir fiche PVC).

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

> **Point de vigilance (2026-09-16) :** une interrogation OpenLCA directe menée le 2026-09-16 pour la bande de chant PE (voir plus bas) a retrouvé le même produit `acrylonitrile-butadiene-styrene copolymer` sous un **UUID différent** (`1367e2a2-b284-3325-a907-6183bf2d126e`, Global). Les deux UUID n'ont pas été confrontés directement ; `À VÉRIFIER`, voir la note sur l'anomalie `database_family` en fin de document.

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

> **Point de vigilance (2026-09-16) — variante à revérifier :** l'interrogation OpenLCA directe du 2026-09-16 (recherche bande de chant PE) a plutôt retrouvé `market for polyvinylchloride, bulk polymerised`, UUID `17671bec-6cbf-361f-9318-081db8c739ac`, Global — une variante de **polymérisation différente** (masse/bulk vs suspension) de celle documentée ici. La variante « suspension polymerised » ci-dessus n'a pas été reconfirmée le 2026-09-16 ; son existence n'est pas remise en cause (elle reste sourcée au Lot 2D), mais **reste `À VÉRIFIER`** — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

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
> **Mise à jour (interrogation OpenLCA directe, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** recherches effectuées : `edge band`, `edge banding` (process ET flows, 0 résultat dans les deux cas), puis `polyethylene, low density`, `polypropylene, granulate`, `acrylonitrile-butadiene-styrene copolymer`, `polyvinylchloride`, `extrusion, plastic`.

#### Produit métier

Bande de chant en PE (polyéthylène), décrite selon son usage plutôt que comme famille de matière autonome.

#### Équivalent Ecoinvent identifié

**Produit fonctionnel : absence confirmée (0 résultat sur `search_processes` ET `search_flows`)**, dans cette base et avec ces requêtes.

**Briques génériques vérifiées, potentiellement utiles pour une reconstruction bottom-up (aucune ne constitue une correspondance directe) :**

| Dataset | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|
| `market for polyethylene, low density, granulate` | Global | kg | `f73b01f9-8ddb-30d0-9f82-2a30a6f689a0` | Matière première seule, aucune forme de profilé/bande |
| `market for polypropylene, granulate` | Global | kg | `9c11da4a-05b2-3f03-878d-34c133548b5c` | Idem, PP — mentionné par cohérence avec la recherche, pas un candidat PE |
| `market for acrylonitrile-butadiene-styrene copolymer` | Global | kg | `1367e2a2-b284-3325-a907-6183bf2d126e` | Idem, ABS — voir point de vigilance UUID dans la fiche ABS ci-dessus |
| `market for polyvinylchloride, bulk polymerised` | Global | kg | `17671bec-6cbf-361f-9318-081db8c739ac` | Idem, PVC — variante « bulk », voir point de vigilance dans la fiche PVC ci-dessus |
| `extrusion, plastic film` (marché non revérifié individuellement ; production existe) | — | kg | `06fcff5d-7113-327d-ab1b-8ceae6c2b17e` (marché) | Procédé de transformation générique conçu pour du **film**, pas un profilé de bande de chant — approximation possible mais non spécifique |

#### Correspondance

**Aucune correspondance satisfaisante** (niveau : **ABSENT** pour le produit fonctionnel).

- **Produit / fonction :** Aucune — absence confirmée.
- **Composition / matière :** La matière PE générique existe (Global, kg), sans lien à un profilé de bande de chant.
- **Technologie / procédé :** Aucun procédé d'extrusion de profilé mince/bande n'a été trouvé — seuls existent un procédé de film et (par analogie ABS/PVC, Lot 2D) des procédés de tuyau/calandrage pour d'autres polymères.
- **Géographie :** Global pour la matière ; sans objet pour un procédé, faute de procédé identifié.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Produit fonctionnel totalement absent, confirmé sur `process` et `flows`. Ne pas transformer arbitrairement la matière PE générique en correspondance directe : c'est, au mieux, une brique de reconstruction, dans la même situation que l'ABS et le PVC (Lot 2D) mais avec un procédé de transformation encore moins spécifique (film, pas même une géométrie de tuyau ou de feuille rigide).

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
| P1 | Colle PVAc / PVA blanche | Lot 2F + reconfirmé 2026-09-16 : monomère seul (vinyl acetate) | Aucune | correspondance Ecoinvent non établie (ABSENT, produit fonctionnel) | 🔴 Lacune majeure |
| P1 | Adhésif thermofusible EVA / EVA hot-melt | Lot 2F : copolymère seul | Faible à moyenne | formulation hot-melt absente | 🟣 À reconstruire |
| P1 | Colle contact *(formulations à base d'eau prioritaires, Nicolas)* | Lot 2F + reconfirmé 2026-09-16 : aucune brique identifiée | Aucune | aucune brique chimique identifiée (ABSENT) | 🔴 Lacune majeure |
| P2 | Colle polyuréthane / PUR | Lot 2F : précurseurs seuls (polyol, MDI) | Faible | correspondance Ecoinvent non établie | 🔴 Lacune majeure |

### Lecture rapide

Les quatre adhésifs d'atelier ont été diagnostiqués au **Lot 2F** ; la colle PVAc/PVA et la colle contact ont été **reconfirmées par interrogation OpenLCA directe le 2026-09-16**, avec le même résultat d'absence. Dans aucun des quatre cas un adhésif *formulé* correspondant n'a été identifié avec les recherches process/flow disponibles : Ecoinvent ne propose, au mieux, que des précurseurs chimiques isolés (monomère vinyl acetate pour la PVA, copolymère EVA pour l'adhésif hot-melt, polyol et MDI séparés pour le PUR), sans formulation ni chaîne établie vers le produit métier. La session du 2026-09-16 a par ailleurs identifié une **dispersion acrylique** (UUID `44da54f3-7ab8-308d-9c33-6efa0f247130`, Global) comme candidat rejeté pour la PVA — famille chimique différente, non équivalente, mentionnée uniquement comme piste de reconstruction de dernier recours si nécessaire. Pour la colle contact, même l'étape de précurseur fait défaut, désormais confirmé deux fois indépendamment (Lot 2F et 2026-09-16), y compris pour le polychloroprène cité dans un lot antérieur (dataset non reconfirmé dans les deux sessions). Le Lot 2D avait par ailleurs déjà établi que, pour la bande de chant en bois véritable préencollée, les briques d'adhésif disponibles ne résolvent pas la lacune principale de cette bande (l'absence de la composante bois elle-même) — ce constat concerne l'usage en bande de chant, distinct des présentes fiches.

> **Rappel méthodologique :** les adhésifs UF et MUF ne sont pas utilisés directement en atelier et ne figurent pas dans cette taxonomie ; ils relèvent des intrants industriels des panneaux (voir famille Panneaux). La colle PUR d'assemblage multimatériaux ne doit pas être confondue avec l'adhésif EVA hot-melt de l'encolleuse de chants.

### Colle PVAc / PVA blanche — P1

> **Reconfirmé par interrogation OpenLCA directe (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** requêtes `polyvinylacetate` (0 résultat), `vinyl acetate`, `adhesive`, `dispersion`. **Absence de produit fonctionnel confirmée indépendamment une seconde fois.** Le dataset `market for vinyl acetate` a été retrouvé sous le **même UUID** qu'au Lot 2F (`9381f4dc-deda-3e02-9cf8-4ef4321b137e`) — cohérence confirmée entre les deux sessions pour ce dataset précis.

#### Produit métier

Colle PVAc/PVA blanche utilisée pour le collage et l'assemblage du bois.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**, reconfirmé le **2026-09-16**. Recherches process/flow (`polyvinyl acetate adhesive`, `PVAc adhesive`, `PVA glue`, `wood adhesive`, `wood glue`, `white glue`, `dispersion adhesive`, `water based adhesive`, `adhesive for wood`, `polyvinylacetate`, `vinyl acetate`, `adhesive`, `dispersion`) : aucun adhésif formulé identifié dans les deux sessions.

- Un candidat générique `adhesive, for metal` a été inspecté et rejeté dans les deux sessions (adhésif époxy pour cadres de fenêtres en aluminium, sans rapport avec une colle à bois) — UUID `3bd4e097-7f01-3790-b602-33a7cac44444` (Lot 2F) vs UUID `e1e8f512-fa21-320c-92f8-e3f345cda6b8` (2026-09-16) : **UUID différents pour un même nom de produit**, `À VÉRIFIER` (voir note sur l'anomalie `database_family` en fin de document).
- Deux autres candidats hors sujet ont également été écartés le 2026-09-16 : `bitumen adhesive compound production, hot/cold` (colle bitumineuse de construction) et `adhesive mortar production`, UUID `3f5bd6a3-cd8c-3161-b48e-9b193858e30d` (mortier-colle de construction) — aucun rapport avec une colle à bois.
- Nouveau candidat identifié le 2026-09-16 et rejeté : `market for acrylic dispersion, without water, in 65% solution state`, UUID `44da54f3-7ab8-308d-9c33-6efa0f247130`, Global — **famille chimique différente** (acrylique, pas acétate de vinyle), utilisée plutôt en peinture/revêtement. **Ne pas présenter comme équivalent chimique** de la PVAc ; mentionné uniquement comme piste de reconstruction de dernier recours si nécessaire, explicitement approximative.
- Seule brique confirmée dans les deux sessions : `market for vinyl acetate` (monomère, non polymérisé, non formulé), UUID `9381f4dc-deda-3e02-9cf8-4ef4321b137e`, location Global, unité kg. La description précise que ce produit est généralement utilisé sur le site de production même (pas vraiment un bien de marché transportable).

#### Correspondance

**Analyse Ecoinvent réalisée (Lot 2F + reconfirmation 2026-09-16) / correspondance non établie — niveau ABSENT pour le produit fonctionnel.** Aucun adhésif PVAc formulé n'a été identifié ; le seul dataset disponible (vinyl acetate) représente le monomère, pas la colle prête à l'emploi.

- **Produit / fonction :** Aucune (monomère, pas un adhésif).
- **Technologie :** Faible — brique chimique amont potentielle uniquement.
- **Forme / application :** Aucune (le métier utilise un liquide prêt à l'emploi ; le dataset est un monomère industriel).
- **Unité :** kg — écart avec l'unité métier probable (pot/litre).
- **Géographie :** Global.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucune étape entre le monomère vinyl acetate et la colle prête à l'emploi n'a été identifiée, avec deux sessions de recherche indépendantes (Lot 2F et 2026-09-16). Ceci documente une absence dans cette base, avec ces requêtes — pas une absence générale de toute version d'Ecoinvent.

#### Données nécessaires

Formulation/composition réelle du produit (à confirmer via la FDS du produit atelier de référence), teneur en solides si pertinente, densité si nécessaire à une conversion, consommation réelle, masse achetée ou unité d'achat.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Aucune reconstruction sérieuse n'est possible à partir du seul monomère ; si un proxy doit malgré tout être construit pour avancer une quantification, le signaler explicitement comme approximation de dernier recours (ex. dispersion acrylique 65 % comme ordre de grandeur), jamais comme une correspondance.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (reconfirmation indépendante).

---

### Adhésif thermofusible EVA / EVA hot-melt — P1

#### Produit métier

Adhésif thermofusible EVA utilisé dans l'encolleuse de chants.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**. Recherches process/flow (`hot melt adhesive`, `EVA adhesive`, `EVA hot melt`, `ethylene vinyl acetate adhesive`, `thermoplastic adhesive`, `edge banding adhesive`) : aucun adhésif hot-melt formulé ni produit spécifique à l'encollage de chants identifiés. Seule brique identifiée : `market for ethylene vinyl acetate copolymer` (résine, non formulée en adhésif), UUID `fe0fb6f7-fd33-3303-a767-fc1464446ce1`, location Global, unité kg.

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
> **Reconfirmé par interrogation OpenLCA directe (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** requêtes `contact adhesive`, `dispersion` (mêmes familles de termes que le Lot 2F ; aucun terme supplémentaire n'a fait apparaître de résultat distinct pour la colle contact, y compris pour les formulations à base d'eau). **Absence confirmée une seconde fois, indépendamment.** Le dataset `market for polychloroprene` (UUID `d1147a50-260c-353a-93c0-def3ebd131d0`, cité au Lot 1) n'a de nouveau pas pu être retrouvé.

#### Produit métier

Colle contact utilisée pour le collage du stratifié HPL, en tenant compte de la pertinence actuelle des formulations à base d'eau.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**, reconfirmé le **2026-09-16**. Recherches process/flow (`contact adhesive`, `contact glue`, `contact cement`, `solvent based adhesive`, `rubber adhesive`, `neoprene adhesive`, `polychloroprene adhesive`, `polychloroprene` seul, `chloroprene`, `laminate adhesive`, `synthetic rubber`, `dispersion`) : aucun adhésif contact formulé, ni aucune brique chimique confirmée, n'a été identifié dans l'une ou l'autre session — y compris pour une formulation à base d'eau. Le dataset `market for polychloroprene` cité dans un lot antérieur (UUID `d1147a50-260c-353a-93c0-def3ebd131d0`) n'a pu être reconfirmé ni au Lot 2F ni le 2026-09-16.

#### Correspondance

**Analyse Ecoinvent réalisée deux fois (Lot 2F et 2026-09-16) / correspondance non établie — niveau ABSENT**, y compris à l'étape des précurseurs.

- **Produit / fonction :** Aucune.
- **Technologie :** Inconnue — chimie réelle du produit métier non présumée.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucun adhésif contact formulé, ni aucune brique chimique confirmée (résine ou polymère), n'a pu être identifié — confirmé indépendamment à deux reprises (Lot 2F, 2026-09-16), y compris pour les formulations à base d'eau désormais explicitement recherchées — situation plus défavorable que la PVA et l'EVA, qui disposent au moins d'un précurseur ou d'une résine. Ceci documente une absence dans cette base, avec ces requêtes, pas une absence générale de toute version d'Ecoinvent.

#### Données nécessaires

Composition/formulation réelle du produit (à confirmer via la FDS du produit en pot utilisé en atelier, **en priorisant les formulations à base d'eau** selon la précision métier 2026-09-15), teneur en solides si pertinente, présence et nature des solvants si applicable, densité si nécessaire, consommation réelle.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur**, en ciblant les formulations à base d'eau. La reconfirmation du 2026-09-16 par interrogation OpenLCA directe rend une nouvelle recherche Ecoinvent peu prioritaire pour l'instant ; si un proxy doit malgré tout être construit pour avancer une quantification, le signaler explicitement comme approximation de dernier recours, jamais comme une correspondance.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (reconfirmation indépendante).

---

### Colle polyuréthane / PUR — P2

#### Produit métier

Colle PUR utilisée occasionnellement pour le collage métal-bois ou plastique-bois.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**. Recherches process/flow (`polyurethane adhesive`, `PU adhesive`, `PUR adhesive`, `structural adhesive`, `assembly adhesive`, `polyurethane` générique, `polyurethane resin`, `polyol`, `methylene diphenyldiisocyanate`) : aucun adhésif PU formulé identifié. Les seuls produits « polyurethane » trouvés sont des mousses et joints (`polyurethane, rigid/flexible foam`, `waste polyurethane foam/seal`) — fonction radicalement différente, écartés comme faux positifs. Deux briques chimiques amont potentielles, non combinées : `polyol` et `methylene diphenyldiisocyanate` (MDI, déjà rencontré au Lot 2B comme liant interne de panneaux — usage différent).

#### Correspondance

- **Produit / fonction :** Aucune.
- **Technologie :** Faible — précurseurs de la bonne famille chimique seulement.
- **Unité :** kg pour les deux précurseurs.
- **Géographie :** Non vérifiée spécifiquement pour polyol/MDI au Lot 2F.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucun lien quantitatif ni formulation reliant les deux briques chimiques identifiées (polyol, MDI) à l'adhésif métier n'a été établi avec les méthodes d'interrogation disponibles au Lot 2F.

#### Données nécessaires

Type et technologie réelle du produit, composition/formulation fabricant, fractions massiques pertinentes si disponibles, densité si nécessaire, consommation réelle.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Situation comparable à la PVA (précurseurs identifiés, sans formulation ni produit fini pertinent).

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md)

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
| P1 | Charnière invisible de meuble | Absence confirmée (2× ) ; briques génériques vérifiées 2026-09-16 | Faible | composition inconnue (nomenclature bloquante) | 🔴 Lacune majeure |
| P1 | Coulisse de tiroir | Absence confirmée (2×) ; mêmes briques génériques | Faible | composition inconnue (nomenclature bloquante) | 🔴 Lacune majeure |
| P1 | Poignée de meuble métallique | Matière + procédé (Lot 2D) ; statut de recherche 2026-09-16 incohérent dans le rapport source | Conditionnelle | composition inconnue ; `À VÉRIFIER` (voir fiche) | 🟣 À reconstruire |
| P1 | Pied niveleur / niveleur | Matière + procédé | Conditionnelle | composition inconnue | 🟣 À reconstruire |
| P1/P2 | Ferrure métallique de suspension (clé française) | Analyse approfondie non réalisée — confirmé non couvert le 2026-09-16 | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Aucun composant de quincaillerie ne dispose d'un produit fonctionnel direct dans Ecoinvent — confirmé pour charnière et coulisse par une seconde interrogation indépendante le 2026-09-16 (0 résultat process + flows). Pour les vis et le pied niveleur, une reconstruction matière + procédé est plausible mais reste conditionnelle à la confirmation, par le fournisseur, de la composition, du revêtement et du procédé réels — l'absence de distinction de taille dans Ecoinvent ne démontre pas que la masse est la seule différence réelle entre les produits. Pour la poignée, le statut de la recherche du 2026-09-16 est **incohérent dans le rapport source lui-même** (voir sa fiche) et n'est donc pas retenu comme confirmation. Pour la charnière invisible et la coulisse de tiroir, la lacune est plus profonde : même la nomenclature physique du composant (matériaux constitutifs, parts, revêtement) est absente, ce qui bloque toute reconstruction avant d'obtenir cette donnée — malgré la disponibilité, désormais mieux documentée (2026-09-16), de briques génériques acier/inox + mise en forme + revêtement zinc pour une reconstruction bottom-up par masse. La ferrure de suspension reste non examinée, confirmé le 2026-09-16.

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

> **Reconfirmé et complété par interrogation OpenLCA directe (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** absence de produit fonctionnel reconfirmée (0 résultat sur `process` ET `flows` pour `hinge`/`furniture hinge`/`cabinet hinge`). Des briques génériques de reconstruction bottom-up ont en revanche été vérifiées — voir ci-dessous.

#### Produit métier

Charnière invisible de meuble ; Blum est un exemple atelier, pas le nom principal du composant.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié, confirmé indépendamment au Lot 2D et le 2026-09-16. Briques génériques vérifiées pour une éventuelle reconstruction bottom-up par masse (2026-09-16) :

| Dataset | Rôle | UUID | Commentaire |
|---|---|---|---|
| `market for steel, low-alloyed, hot rolled` | Matière (acier standard) | `eba0e6ba-5f96-3ac9-a0c0-2f0d4fc74b8a` | Plausible pour quincaillerie d'entrée de gamme |
| `market for steel, chromium steel 18/8, hot rolled` | Matière (inox) | `288bd21b-b97b-32b7-8383-cc0d2126fe72` | Pertinent pour quincaillerie de qualité supérieure |
| `sheet rolling, steel` (marché) | Mise en forme (laminage) | `72416073-2dc0-3d01-a3e4-91c7b0f0dfe3` | Procédé de mise en forme générique |
| `wire drawing, steel` (marché) | Mise en forme (ressorts/tiges) | `641bc156-ed49-3cfa-a712-c27b40902d93` | Pertinent pour ressorts/mécanismes de charnière |
| `zinc coating, pieces` (marché) | Revêtement anticorrosion | `ada0a646-2258-3a16-8223-a31f812325aa` | Revêtement typique de ce type de quincaillerie |
| `market for metal working, average for steel/chromium steel/aluminium product manufacturing` | Service générique de mise en forme/usinage | `b76ed063-3770-3e6a-b065-c09d9d1891ee` (acier) / `00dd895a-1607-35dc-8226-2ba0f5cd9f64` (acier chromé) / `e41d54f1-64cf-3ba3-87c9-1d481bc79d76` (aluminium) | Unité de reconstruction la plus utile pour approximer la fabrication d'une pièce par sa masse |

> **Point de vigilance — UUID différents pour un même nom de produit :** `wire drawing, steel` et `zinc coating, pieces` portent ici des UUID différents de ceux déjà cités pour les vis d'assemblage (`5563eb07-b684-33b5-bf13-a8f604fe5b06` et `9cc6fb22-00d5-3d78-8971-0d46751d263c` respectivement, Lot 2D). **`À VÉRIFIER`** — voir la note sur l'anomalie `database_family` en fin de document ; ne pas présumer qu'il s'agit d'une erreur ni que les deux UUID sont interchangeables sans vérification.

#### Correspondance

- **Produit / fonction :** Non établie (absence confirmée deux fois — Lot 2D, 2026-09-16).
- **Composition / matière :** Faible — aucune nomenclature du produit réel disponible ; briques génériques (acier, inox) identifiées mais non assignées à un produit précis.
- **Technologie / procédé :** Non établie pour le produit réel ; briques génériques de mise en forme/revêtement disponibles pour une reconstruction bottom-up.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

C'est le cas le plus bloquant du lot : la **nomenclature physique/composition du composant est elle-même la première donnée manquante**. Sans elle, aucune reconstruction matière + procédé ne peut être envisagée, malgré la disponibilité désormais mieux documentée des briques génériques (acier/inox + mise en forme + revêtement zinc). Niveau de correspondance : **ABSENT** (produit) / **RECONSTRUCTION** envisageable une fois la nomenclature obtenue.

#### Données nécessaires

Masse totale, matériaux constitutifs et leurs parts, revêtement, nombre de pièces, origine de fabrication.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Cette donnée reste bloquante avant toute tentative de modélisation, malgré la disponibilité de briques génériques pour la reconstruction bottom-up (acier/inox + mise en forme + revêtement).

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (briques de reconstruction bottom-up).

---

### Coulisse de tiroir — P1

> **Priorisation et méthode (validation Nicolas, 2026-09-15) :** la coulisse de tiroir est l'un des composants de quincaillerie prioritaires (avec charnières, poignées, pieds/niveleurs et ferrures de suspension). Ne pas subdiviser inutilement toutes les technologies et dimensions de coulisses : prévoir plutôt l'utilisation future d'un **modèle standard représentatif**, en privilégiant un produit dont la documentation fournisseur est suffisamment détaillée. **Action : `À vérifier / choisir modèle fournisseur de référence`.**
>
> **Reconfirmé par interrogation OpenLCA directe (2026-09-16) :** absence de produit fonctionnel reconfirmée (0 résultat pour `drawer slide`/`drawer runner`/`telescopic rail`). Les mêmes briques génériques de reconstruction bottom-up que pour la charnière (ci-dessus) ont été identifiées comme potentiellement pertinentes (acier/inox + mise en forme + revêtement zinc).

#### Produit métier

Coulisse de tiroir ; exemple atelier Blum, profondeurs typiques de 10 à 22 pouces.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié (`drawer slide`, `drawer runner`, `telescopic rail` ou équivalent), confirmé indépendamment au Lot 2D et le 2026-09-16. Aucun système de roulement ou procédé spécifique n'a été caractérisé. Les briques génériques listées dans la fiche « Charnière invisible » ci-dessus (acier low-alloyed/chromium 18/8, laminage, tréfilage/`wire drawing`, revêtement zinc, `metal working` moyen) sont les mêmes candidates potentielles pour une reconstruction bottom-up de la coulisse.

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

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (reconfirmation + briques de reconstruction bottom-up).

---

### Poignée de meuble métallique — P1

> **Statut incertain après le rapport OpenLCA du 2026-09-16 — `À VÉRIFIER`, ne pas trancher.** Le [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) contient une **incohérence interne non résolue** sur ce produit : son tableau « Produits métier et résultat par famille » indique « Non — 0 résultat sur process ET flows » pour `furniture handle` (recherche apparemment effectuée), alors que son tableau transversal final et sa section handoff indiquent toutes deux « Non recherché en détail » / « recherche non complétée dans cette session ». Ces deux affirmations sont contradictoires. Conformément à la consigne de ne pas inventer ni trancher au-delà des preuves disponibles, ce document **ne retient aucune des deux lectures comme confirmée** : la poignée reste à rechercher explicitement (ou à re-rechercher, si la mention « 0 résultat » s'avère être la bonne) lors d'une prochaine passe OpenLCA — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

#### Produit métier

Poignée de meuble métallique.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié au Lot 2D. `section bar extrusion, aluminium` constitue une brique potentiellement intéressante, **uniquement si** une poignée réelle est confirmée comme profilé aluminium. Le statut de la recherche du 2026-09-16 pour ce produit est incohérent dans le rapport source (voir encadré ci-dessus) et n'est donc pas intégré comme confirmation supplémentaire.

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

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Pied niveleur / niveleur — P1

> **Non couvert par l'interrogation OpenLCA du 2026-09-16.** Le [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) le confirme explicitement : reste à rechercher — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

#### Produit métier

Pied de nivellement, composant actuellement en plastique.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié (les résultats `foot` étaient des faux positifs). Une piste `polypropylene + injection moulding` peut représenter une partie plastique **si cette composition est confirmée**, mais elle ne couvre pas un éventuel insert métallique.

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

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Ferrure métallique de suspension pour meuble mural — P1/P2

> **Non couvert par l'interrogation OpenLCA du 2026-09-16.** Le [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) le confirme explicitement : reste à rechercher — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

#### Produit métier

Ferrure métallique de suspension, type clé française / French cleat.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce composant. Par analogie méthodologique avec les autres quincailleries du Lot 2D, l'absence de produit fonctionnel direct est plausible, mais cela reste à vérifier et ne doit pas être présumé.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer le matériau, la masse, les dimensions et le procédé de fabrication.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

## 8. Emballage

Les emballages sont suivis séparément des matériaux constitutifs du meuble.

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Carton d'emballage / carton ondulé | Dataset historique QC (Lot 2A) non reconfirmé 2026-09-16 ; variante Global trouvée | Bonne (Lot 2A) / Partielle (2026-09-16) | variante QC non reconfirmée ; boîte vs plaque | 🟡 À valider |
| P1 | Film à bulles / papier bulle | Absence confirmée (2026-09-16, 0 résultat) | Aucune | absent de cette base, avec ces requêtes | 🔴 Lacune majeure |
| P1/P2 | Matériau d'emballage blanc fin en rouleau (identification à confirmer) | Identification toujours requise ; candidat LDPE non confirmé (2026-09-16) | Non établie | identification préalable requise | 🟡 À valider |

### Lecture rapide

Le carton ondulé est, d'après le Lot 2A, le cas le plus favorablement régionalisé identifié dans l'ensemble des diagnostics : le marché québécois s'appuyait sur un procédé de fabrication et sur un intrant majeur (le fluting medium) réellement documentés à partir d'une usine québécoise. **Mise à jour (2026-09-16) :** une interrogation OpenLCA directe n'a retrouvé qu'une variante Global de ce marché, décrite comme une boîte formée (pas une plaque) — la variante québécoise n'a été ni reconfirmée ni infirmée, ce point reste `À VÉRIFIER`. Le film à bulles a été recherché le 2026-09-16 (`bubble film`, `foam`, `polyethylene foam`) : absence confirmée dans cette base, avec ces requêtes. **Ajout (validation métier Nicolas, 2026-09-15) :** un matériau d'emballage blanc, très fin, vendu en gros rouleau et utilisé pour envelopper/protéger les meubles, a été identifié comme utilisé en atelier ; son identification exacte (nom commercial, composition) n'est toujours pas certaine et ne doit pas être devinée — un candidat non confirmé (`packaging film, LDPE`) a été relevé le 2026-09-16 par cohérence de facteur de forme uniquement.

### Carton d'emballage / carton ondulé — P1

> **Point de vigilance important (interrogation OpenLCA directe, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** cette session a retrouvé un dataset `market for corrugated board box` sous un **UUID différent** (`b8c827da-42b1-3a3a-a6b5-c5d2f1792e33`), localisé **Global** (pas Canada/Québec), décrit comme **une boîte formée**, pas une plaque plate de carton ondulé. Ni la variante Canada/Québec, ni les briques amont québécoises (production, fluting medium) ci-dessous n'ont été retrouvées ou infirmées le 2026-09-16 — cette session n'a pas cherché spécifiquement à confirmer la géographie Québec de ce produit. **`À VÉRIFIER`** avant de considérer la régionalisation québécoise ci-dessous comme toujours d'actualité dans la base interrogée le 2026-09-16 ; voir la note sur l'anomalie `database_family` en fin de document. Les deux jeux de résultats sont conservés ici sans qu'aucun n'efface l'autre.

#### Produit métier

Carton d'emballage / carton ondulé.

#### Équivalent Ecoinvent identifié

**Candidat historique (Lot 2A, régionalisation québécoise) :**

- **Dataset (marché) :** `market for corrugated board box`
- **UUID :** `2424352b-3df3-3415-9fbf-a6b1eff0ce60`
- **Location :** Canada, Québec
- **Unité / base de comparaison :** kg
- **Briques en amont :** `corrugated board box production` (`17317a18-28b4-335a-a96d-68789b9bfb70`, Canada, Quebec, collecte documentée sur une usine réelle, mix de production daté de 2008) ; `containerboard production, fluting medium, semichemical, 40% recycled content` (`27a2145c-86e5-3f1e-8219-5d1720d12cab`, Canada, Québec, décrit comme issu d'une usine québécoise réelle).

**Candidat vérifié par interrogation OpenLCA directe (2026-09-16) :**

- **Dataset (marché) :** `market for corrugated board box`
- **UUID :** `b8c827da-42b1-3a3a-a6b5-c5d2f1792e33`
- **Location :** Global
- **Unité / base de comparaison :** kg
- **Réserve documentée :** c'est une **boîte formée**, pas une plaque plate de carton ondulé — à vérifier selon l'usage réel en atelier (emballage en plaque découpée vs boîte préformée).

#### Correspondance

*(Ci-dessous : évaluation héritée du Lot 2A pour le candidat québécois `2424352b-…` ; non revalidée ni infirmée le 2026-09-16.)*

- **Produit / fonction :** Bonne pour le candidat Lot 2A ; **partielle** pour le candidat Global du 2026-09-16 (boîte formée, réserve de forme).
- **Composition / matière :** Moyenne — le fluting medium est confirmé québécois (candidat Lot 2A) ; le linerboard, plus gros intrant en masse (0,7434 kg), n'a pas été vérifié dans ce lot ; des intrants chimiques mineurs (amidon de maïs, encre offset) restent génériques.
- **Technologie / procédé :** Forte pour le candidat Lot 2A — procédé de fabrication des boîtes documenté sur une usine réelle.
- **Géographie :** Forte à plusieurs niveaux pour le candidat Lot 2A (marché, production, fluting medium) — **mais non reconfirmée** le 2026-09-16, qui n'a trouvé qu'une variante Global.
- **Données primaires québécoises :** Forte mais partiellement ancienne pour le candidat Lot 2A (données de fabrication datées de 2008) ; électricité non résolue comme CA-QC.

#### Lacune Ecoinvent

La régionalisation décrite au Lot 2A descend jusqu'au procédé de production et à un intrant majeur (fluting medium), ce qui distingue nettement ce cas des autres datasets `CA-QC` examinés. La lacune résiduelle documentée au Lot 2A porte sur les **données primaires québécoises absentes ou non vérifiées** pour le linerboard (le plus gros intrant en masse) et pour l'électricité, ainsi que sur l'ancienneté (2008) des données de fabrication des boîtes. **Nouvelle réserve (2026-09-16)** : l'existence continue de la variante québécoise n'a pas été reconfirmée ; le candidat retrouvé cette session (Global) porte en outre une réserve de forme (boîte vs plaque).

#### Données nécessaires

Vérification de la géographie et de la composition du linerboard, résolution géographique de l'électricité, actualisation éventuelle des données de fabrication ; **re-vérification de l'existence de la variante `Canada, Québec`** dans la base interrogée le 2026-09-16 ; confirmation si le produit réellement utilisé en atelier est une plaque de carton ondulé ou une boîte préformée.

#### Recommandation

**Valider avant utilisation.** Conserver le candidat québécois du Lot 2A comme référence documentée et prometteuse, sans le qualifier sans réserve de représentatif avant vérification du linerboard, de l'énergie, de la fraîcheur des données, **et de sa présence toujours confirmée dans la base** (voir point de vigilance 2026-09-16). Confirmer par ailleurs si le produit réel est une boîte ou une plaque avant d'arrêter un choix de dataset.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md) ; [Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (candidat Global, non reconfirmation de la variante québécoise).

---

### Film à bulles / papier bulle — P1

> **Recherché par interrogation OpenLCA directe (2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** requête `bubble film`, 0 résultat.

#### Produit métier

Film à bulles / papier bulle d'emballage.

#### Équivalent Ecoinvent identifié

**Absence confirmée dans cette base, avec cette requête** (`bubble film`, 0 résultat). Aucun terme synonyme supplémentaire n'a été testé le 2026-09-16 (`air cushion film`, `plastic bubble packaging` restent à essayer, voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md)).

#### Correspondance

Non établie — niveau **ABSENT**, sous réserve des synonymes non encore testés.

#### Lacune Ecoinvent

Absence confirmée pour le terme testé ; ne pas généraliser à « Ecoinvent ne contient pas de film à bulles » sans avoir testé les synonymes anglais usuels. Sa composition exacte reste elle-même à confirmer avant tout mapping.

#### Données nécessaires

Composition exacte du film (à confirmer auprès du fournisseur), en plus de la vérification des synonymes de recherche restants.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur** ; compléter la recherche Ecoinvent avec les synonymes restants avant de conclure définitivement à l'absence.

#### Source du diagnostic

[Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md).

---

### Matériau d'emballage blanc fin en rouleau (identification à confirmer) — P1/P2

> **Nouvel objet (validation métier Nicolas, 2026-09-15).** Matériau blanc, très fin, vendu en gros rouleau, utilisé pour envelopper/protéger les meubles à l'expédition. **Son identification exacte (nom commercial, composition) n'est pas certaine et n'est volontairement pas devinée ici** — ne pas confondre avec le film à bulles (ci-dessus), qui est un produit distinct déjà identifié dans la taxonomie.
>
> **Mise à jour (interrogation OpenLCA directe, 2026-09-16 — [rapport source](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md)) :** malgré l'absence d'identification physique confirmée, une recherche exploratoire a été menée (`bubble film` 0 résultat, `polystyrene foam slab`, `polyethylene foam` 0 résultat, `foam`, `packaging film`, `shrink film` 0 résultat) et a fait remonter un candidat **non confirmé**, présenté ici strictement comme piste et non comme identification.

#### Produit métier

Matériau d'emballage blanc fin, en gros rouleau, pour l'enveloppement/protection des meubles ; nature exacte (papier, non-tissé, film plastique ou autre) non encore confirmée.

#### Équivalent Ecoinvent identifié

**Action préalable toujours requise :** `Identifier précisément le matériau d'emballage avant recherche Ecoinvent`. Aucune recherche Ecoinvent ne peut être menée de façon concluante tant que la nature exacte du matériau n'est pas confirmée — **le candidat ci-dessous ne lève pas cette exigence**, il ne fait que documenter ce qu'une recherche exploratoire a trouvé.

**Candidat non confirmé (2026-09-16) :**

| Dataset | Géographie | Unité | UUID | Statut |
|---|---|---|---|---|
| `market for packaging film, low density polyethylene` | Global | kg | `0c925f5b-401c-330c-9247-04bd41395645` | **NON CONFIRMÉ.** Facteur de forme (rouleau, fin) cohérent avec la description, mais aucune fonction de protection/calage documentée dans le dataset et aucune confirmation que le matériau réel est ce film. Ne pas retenir comme identification. |

Candidat écarté pour mauvais facteur de forme : `market for polystyrene foam slab`, UUID `8b420467-04f4-3461-b3aa-0b9570560486` (mousse rigide EPS, destinée à l'isolation en panneaux rigides — incompatible avec un « gros rouleau »). Absents de la base (0 résultat) : mousse PE (« polyethylene foam »), papier bulle.

#### Correspondance

Non établie — **niveau ABSENT/À VÉRIFIER**, aucune confirmation physique du matériau réel.

#### Lacune Ecoinvent

La lacune actuelle porte toujours sur l'**identification métier du matériau lui-même**, pas sur une lacune Ecoinvent confirmée. Ne pas identifier arbitrairement ce matériau comme étant `packaging film, LDPE` sur la seule base d'une cohérence de facteur de forme.

#### Données nécessaires

Nom commercial ou technique du matériau, composition (papier, non-tissé, film plastique ou autre), grammage, largeur de rouleau, fournisseur — obtenus via une fiche technique ou un échantillon, avant tout choix de dataset.

#### Recommandation

**Identifier précisément le matériau d'emballage avant toute recherche Ecoinvent supplémentaire.** Obtenir d'abord la fiche produit ou l'emballage du rouleau auprès de l'atelier/fournisseur ; ne pas trancher arbitrairement en faveur du candidat `packaging film, LDPE` non confirmé.

#### Source du diagnostic

[Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) (candidat non confirmé, identification physique toujours requise).

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
- [Diagnostic OpenLCA vérifié — 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) — interrogation réelle de la base via le connecteur MCP OpenLCA (contreplaqué merisier/Baltic, papier mélaminé atelier, bande de chant PE, colles PVAc/colle contact, quincaillerie, emballages) ; voir la note sur l'anomalie `database_family` en fin de document.

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
11. Un dataset trouvé indépendamment par deux sessions différentes (Lot 2A–2G via MCP vs interrogation OpenLCA directe du 2026-09-16) peut porter un **UUID différent pour un nom de produit identique** (constaté pour `plywood`, `particleboard, uncoated`, `coating service, melamine impregnated paper`, `adhesive, for metal`, `acrylonitrile-butadiene-styrene copolymer`, `polyvinylchloride`, `wire drawing, steel`, `zinc coating, pieces`) — voir la note sur l'anomalie `database_family` ci-dessous. Ce constat récurrent renforce la prudence méthodologique du point 1 : ne jamais présumer qu'un UUID cité dans un lot antérieur reste valide sans le revérifier.

## Anomalie observée — `database_family: "flcac"`

> **Statut : `À VÉRIFIER`. Ne pas présumer que la base interrogée est définitivement Ecoinvent du seul fait de sa nomenclature.**

Le [diagnostic OpenLCA du 2026-09-16](diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md) rapporte que l'appel `database_info` du connecteur MCP retourne `database_family: "flcac"`, alors que la nomenclature de tous les process interrogés (suffixe `Cutoff, U`, arborescence de catégories NACE à 4 niveaux, vocabulaire des descriptions) correspond à **Ecoinvent 3, système modèle Cutoff**.

**Vérification effectuée dans ce dépôt (2026-09-16, session de réconciliation) :** recherche de `flcac` et `database_family` dans l'ensemble du dépôt Git, dans `mcp/README.md`, `config/README.md` et `.env.example`. **Aucune trace locale de `flcac` n'existe en dehors du rapport lui-même.** Le connecteur MCP n'est pas implémenté dans ce dépôt (`mcp/` ne contient qu'un README de principe ; le README racine confirme explicitement que « la connexion IPC » et « le MCP » ne sont « pas encore implémentés »). Il n'existe donc **aucune configuration locale permettant de trancher** si `flcac` est : un identifiant interne du connecteur, le nom/famille réel de la base interrogée, ou une erreur de détection.

**Élément indirect à considérer, sans le présenter comme une preuve :** la reconfirmation du 2026-09-16 a systématiquement retrouvé des **UUID différents** de ceux documentés aux Lots 2A–2G pour des produits au nom identique (voir point méthodologique 11 ci-dessus), ainsi qu'une variante géographique `Canada, Québec` pour le carton ondulé (Lot 2A) qui n'a pas été retrouvée le 2026-09-16 (variante Global uniquement). Ce schéma est **cohérent avec**, sans le démontrer, l'hypothèse que les deux séries de sessions n'ont pas interrogé exactement la même base ou la même version. **Cette hypothèse n'est pas retenue comme conclusion** — elle est mentionnée uniquement pour motiver la priorité de résolution de cette anomalie avant toute intégration ultérieure plus poussée (ex. régionalisation, quantification).

**Action recommandée :** clarifier la configuration du connecteur MCP (fichier de connexion, version de base chargée dans openLCA, nom exact affiché dans l'interface openLCA) avant la prochaine passe d'intégration. Voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

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
