# Référentiel des matériaux et composants — Ébénisterie

> **Statut : V3 — vue consolidée du diagnostic Ecoinvent + validation métier Nicolas (2026-09-15)**
> Ce document reste l'inventaire métier des produits et composants réellement achetés ou utilisés en atelier. Il intègre, pour les matériaux déjà approfondis, les conclusions des diagnostics de représentativité Ecoinvent (Lots 2A à 2G) ainsi que les décisions de validation métier prises en réunion avec Nicolas le 2026-09-15. Cette réunion a confirmé l'approche générale du diagnostic : l'objectif actuel **n'est pas** de calculer quantitativement les impacts ni de régionaliser les datasets, mais d'identifier et de qualifier les écarts entre les données Ecoinvent disponibles et la réalité de l'ébénisterie québécoise. Un rapport final plus synthétique sera produit ultérieurement ; ce document reste volontairement détaillé et traçable. Les matériaux non encore approfondis conservent leur statut prudent d'origine.
>
> **Session sans accès OpenLCA (2026-09-16)** : les ajouts de cette passe (renommage du contreplaqué merisier/bouleau jaune, papier mélaminé en atelier, bande de chant PE, précisions adhésifs, quincaillerie, emballages) sont des décisions de **taxonomie et de priorisation métier**, pas des résultats de recherche Ecoinvent. Toute correspondance Ecoinvent nouvelle est explicitement marquée `À vérifier dans OpenLCA` — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md). Le [tableau transversal des lacunes](diagnostic/tableau-transversal-lacunes-ecoinvent.md) et la [synthèse des spécificités québécoises](specificites-quebecoises.md) complètent ce document.

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
| P1 | Contreplaqué merisier / bouleau jaune (yellow birch) / Baltic plywood | Appellation métier reprécisée (2026-09-15) ; candidat générique existant à revérifier | Faible / à revérifier | essence + appellation à reconfirmer dans OpenLCA | 🔴 Lacune majeure |
| P1 | Panneau de particules mélaminé / TFL | Matière + procédé | Partielle | produit fini absent | 🟣 À reconstruire |
| P1 | MDF mélaminé / TFL | Matière + procédé | Partielle | produit fini absent | 🟣 À reconstruire |
| P1 | MDF plaqué bois acheté fini | Lot 2E : substrat seul disponible | Faible | placage + procédé de collage absents | 🔴 Lacune majeure |
| P1 | Panneau de particules plaqué bois acheté fini | Lot 2E : substrat seul disponible | Faible | placage + procédé de collage absents | 🔴 Lacune majeure |
| P2 | HDF brut | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | OSB | Analyse approfondie non réalisée — **déprioritisé (décision Nicolas, 2026-09-15)** | Non établie | hors périmètre actuel | 🟡 À valider *(hors priorité)* |
| P2 | Autre contreplaqué | Dataset identifié — **déprioritisé (décision Nicolas, 2026-09-15)** | Partielle | hors périmètre actuel | 🟠 À adapter *(hors priorité)* |
| P2 | Panneau plaqué en atelier | Pertinent métier confirmé (2026-09-15) ; analyse Ecoinvent non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Les panneaux bruts (particules, MDF) ont un dataset Ecoinvent dont la fonction correspond bien au produit métier, mais dont la recette, l'énergie et les intrants sont d'origine européenne (EPF) et doivent être adaptés avec des données de fabricant québécois. Les panneaux finis mélaminés/TFL n'existent pas comme produit direct dans Ecoinvent : le meilleur modèle plausible combine le panneau brut et un service générique de revêtement mélaminé, ce qui reste une reconstruction non validée. Le contreplaqué constitue un cas particulier, **reprécisé en réunion de validation métier le 2026-09-15** : le produit métier visé n'est pas un « bouleau russe » générique mais un **contreplaqué merisier / yellow birch / Baltic plywood (contreplaqué baltique)** — voir la fiche ci-dessous pour le détail de ce changement d'appellation. Le seul dataset auparavant associé à cette entrée reste un contreplaqué générique dont la géographie `CA-QC` est trompeuse (recette et données allemandes) ; sa pertinence pour le produit reprécisé n'est **pas** établie et doit être revérifiée dans OpenLCA. Les panneaux achetés déjà plaqués (bois) disposent désormais d'un diagnostic (Lot 2E) : le substrat brut est connu, mais ni le placage fini ni un procédé de collage/pressage spécifique n'ont été identifiés. Le HDF et le placage en atelier n'ont pas encore fait l'objet d'une analyse Ecoinvent approfondie. L'OSB et l'« autre contreplaqué » sont déprioritisés pour l'instant (décision Nicolas, 2026-09-15) : ils ne sont pas retirés de la taxonomie, mais ne constituent plus une cible active du diagnostic.

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

> **Changement d'appellation (validation métier Nicolas, 2026-09-15) :** cette entrée s'appelait auparavant « Contreplaqué de bouleau russe ». Le produit métier réellement visé est un **contreplaqué de merisier / yellow birch / Baltic plywood (contreplaqué baltique)**, et non un contreplaqué de « bouleau russe » à proprement parler. Ce renommage est une **clarification de taxonomie métier**, pas une nouvelle recherche Ecoinvent : la correspondance ci-dessous reste celle établie au Lot 2A pour l'ancienne appellation et **n'a pas été revalidée** pour les termes merisier/yellow birch/Baltic plywood. Voir aussi l'entrée « Merisier / bouleau jaune massif » de la section [Bois massif](#4-bois-massif), qui documente une chaîne forestière `birch` distincte (Lot 2C, Suède) pour le bois massif — cette chaîne concerne le bois massif, pas le contreplaqué, et ne doit pas être confondue avec la présente entrée.

#### Produit métier

Contreplaqué de merisier / bouleau jaune (yellow birch) / Baltic plywood (contreplaqué baltique), produit distinct dans la taxonomie métier, non substituable d'emblée par un contreplaqué générique.

#### Équivalent Ecoinvent identifié

**Candidat précédemment évalué (Lot 2A, pour l'ancienne appellation « bouleau russe ») — à revérifier pour les nouveaux termes :**

- **Dataset :** `plywood production | plywood | Cutoff, U` (générique, non spécifique à une essence ni à une configuration de plis)
- **UUID :** `5538194d-92b2-3020-bb3e-fbc59cb71248` (comparatif RER `0f52041a-b664-357b-ab50-e48613bff63d`)
- **Location :** Canada, Quebec (déclaré comme copie du dataset européen ; données reposant sur un échantillon de production allemande)
- **Unité / base de comparaison :** m³

> **Action requise — `À vérifier dans OpenLCA`** : rechercher explicitement les appellations *merisier*, *yellow birch*, *Baltic plywood* et *contreplaqué baltique* (termes français et anglais, y compris variantes de search_processes/search_flows) avant de conclure sur une correspondance. Ne pas présumer que le dataset générique `plywood production` ci-dessus représente ce produit reprécisé — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

#### Correspondance

*(Correspondance ci-dessous héritée du Lot 2A pour l'ancienne appellation « bouleau russe » ; à revalider pour merisier/yellow birch/Baltic plywood.)*

- **Produit / fonction :** Partielle — c'est un contreplaqué générique, dont la correspondance à un contreplaqué merisier/yellow birch/Baltic plywood n'a pas été vérifiée.
- **Composition / matière :** Faible — sawlog/veneer log hardwood générique, aucune trace d'essence spécifique confirmée pour ce produit.
- **Technologie / procédé :** Faible — les quantités technologiques centrales inspectées (bois, résine, énergie, eau) sont identiques ou se recomposent à la même somme entre CA-QC et RER, et les émissions directes de procédé inspectées sont elles aussi identiques.
- **Géographie :** Trompeuse — la mention `Canada, Quebec` ne reflète pas une donnée primaire québécoise ; le dataset est décrit comme une copie du modèle européen basée sur un échantillon allemand.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

C'est un cas de **dataset CA-QC utilisant en réalité des données étrangères** combiné à une **essence non confirmée pour le produit reprécisé** : la localisation `Canada, Quebec` sert uniquement au linking vers des marchés régionaux, tandis que les quantités technologiques centrales inspectées (bois, résine, énergie, eau) sont identiques ou se recomposent à la même somme, et les émissions directes de procédé inspectées sont elles aussi identiques à celles de la version allemande/européenne. **Aucune conclusion n'est tirée ici sur l'existence ou l'absence d'un dataset merisier/yellow birch/Baltic plywood dans Ecoinvent** : cette question reste `À vérifier dans OpenLCA`.

#### Données nécessaires

Confirmation de l'essence et de la configuration réelles (merisier / yellow birch / Baltic plywood), configuration des plis, origine de fabrication, adhésif utilisé, données de fabricant si une reconstruction est un jour envisagée.

#### Recommandation

**Données insuffisantes pour décider.** Ne pas présenter le dataset générique comme représentatif du contreplaqué merisier/yellow birch/Baltic plywood avant recherche dédiée dans OpenLCA ; l'utiliser au mieux comme proxy générique documenté dans l'attente de cette vérification, en explicitant sa dépendance aux données allemandes.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md) (pour l'ancienne appellation « bouleau russe » ; correspondance non revalidée pour l'appellation reprécisée le 2026-09-15).

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
| P1/P2 | Papier mélaminé appliqué en atelier | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Le Lot 2E a diagnostiqué le stratifié HPL et le placage de bois naturel : dans les deux cas, aucun produit fini n'a été identifié avec les méthodes d'interrogation disponibles, et la chaîne de reconstruction s'arrête plus tôt que pour le TFL (Lot 2B) — le HPL ne dispose que de deux précurseurs chimiques isolés (résine phénolique, papier kraft non imprégné) sans procédé de liaison identifié, et le placage bois s'arrête à la grume forestière générique, plusieurs étapes avant la feuille de placage elle-même. Le placage de bois naturel partage donc, en amont, certaines des lacunes déjà documentées pour le bois massif (essence, traçabilité — voir Lot 2C), mais la lacune principale du placage lui-même est plus fondamentale : aucune transformation (tranchage/déroulage) n'a été identifiée. **Nouveauté (validation métier Nicolas, 2026-09-15) :** le papier mélaminé n'arrive pas toujours déjà appliqué sur le panneau — certaines entreprises réalisent cette opération en atelier, ce qui leur permet de proposer leurs propres collections/couleurs. Ce cas d'usage n'a pas encore fait l'objet d'un diagnostic Ecoinvent dédié et est ajouté ci-dessous.

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

#### Produit métier

Papier décor mélaminé appliqué sur panneau support (particules ou MDF) directement en atelier, plutôt qu'acheté déjà revêtu.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.** Le Lot 2B a documenté un service `coating service, melamine impregnated paper, double-sided` (UUID `4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78`, Europe) dans le contexte du panneau TFL **acheté fini** ; sa pertinence pour une opération réalisée **en atelier** (plutôt qu'en usine de panneaux) n'a pas été évaluée et doit être vérifiée séparément — le procédé industriel documenté peut ne pas correspondre à une presse d'atelier.

#### Correspondance

Non établie pour le cas d'application en atelier.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée spécifiquement pour l'application en atelier (par opposition à l'application industrielle déjà documentée pour le TFL acheté fini, Lot 2B). `À vérifier dans OpenLCA` — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

#### Données nécessaires

Grammage réel du papier décor utilisé en atelier, nombre de faces, paramètres de presse d'atelier (température, pression, durée), panneau support réel (particules ou MDF).

#### Recommandation

**Données insuffisantes pour décider.** Vérifier d'abord si le service de revêtement documenté au Lot 2B (contexte industriel) est applicable à une presse d'atelier avant toute reconstruction.

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.** Service de revêtement mélaminé documenté en contexte industriel : [Lot 2B](diagnostic/ecoinvent-representativite-qc-lot-2b.md).

---

## 3. Bandes de chant

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Bande de chant en bois véritable préencollée | Produit direct absent | Faible | produit fini absent | 🔴 Lacune majeure |
| P1 | Bande de chant en bois véritable non encollée | Produit direct absent | Faible | produit fini absent | 🔴 Lacune majeure |
| P1 | Bande de chant ABS | Matière + procédé | Faible | procédé absent | 🟣 À reconstruire |
| P1 | Bande de chant PVC | Matière + procédé | Partielle | procédé absent ; **place relative à revérifier (2026-09-15)** | 🟣 À reconstruire |
| P1 | Bande de chant PE / polyéthylène | Analyse approfondie non réalisée (nouvel objet, 2026-09-15) | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Aucune bande de chant n'existe comme produit fini direct dans Ecoinvent. Pour le bois véritable (préencollé ou non), aucune brique de placage ou de bande mince exploitable n'a été trouvée : la lacune commence dès la composante bois elle-même, avant même la question de l'adhésif. Pour l'ABS et le PVC, la matière de base existe et des procédés de transformation plastique proches existent aussi, mais aucun ne reproduit la géométrie exacte d'une bande de chant ; le PVC dispose d'un indice supplémentaire (un flux de déchet de calandrage spécifique au PVC) qui en fait un proxy légèrement mieux étayé que l'ABS, sans que cela constitue une validation. **Ajout (validation métier Nicolas, 2026-09-15) :** la bande de chant PE/polyéthylène est ajoutée comme objet explicite au périmètre — elle n'a pas encore été recherchée dans Ecoinvent. Le PVC est conservé dans le référentiel, mais sa place relative face au PE et à l'ABS doit être revérifiée plutôt que d'être présumée acquise.

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

> **Nouvel objet (validation métier Nicolas, 2026-09-15).** À ajouter explicitement au périmètre du diagnostic.

#### Produit métier

Bande de chant en PE (polyéthylène), décrite selon son usage plutôt que comme famille de matière autonome.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.** Par analogie méthodologique avec l'ABS et le PVC (Lot 2D), il est plausible qu'une matière `polyethylene` générique existe (marché mondial du polymère) sans procédé de transformation reproduisant la géométrie exacte d'une bande de chant — mais cela reste à vérifier et ne doit pas être présumé. `À vérifier dans OpenLCA` — voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit.

#### Données nécessaires

Masse par mètre, largeur, épaisseur, type de PE (basse/haute densité), formulation/additifs, procédé réel de mise en forme.

#### Recommandation

**Données insuffisantes pour décider.** Rechercher d'abord la matière PE et un procédé de transformation plausible (extrusion, calandrage) dans OpenLCA, en suivant la même méthode que pour l'ABS et le PVC (Lot 2D).

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

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
| P1 | Colle PVAc / PVA blanche | Lot 2F : monomère seul (vinyl acetate) | Aucune | correspondance Ecoinvent non établie | 🔴 Lacune majeure |
| P1 | Adhésif thermofusible EVA / EVA hot-melt | Lot 2F : copolymère seul | Faible à moyenne | formulation hot-melt absente | 🟣 À reconstruire |
| P1 | Colle contact | Lot 2F : aucune brique identifiée | Aucune | aucune brique chimique identifiée | 🔴 Lacune majeure |
| P2 | Colle polyuréthane / PUR | Lot 2F : précurseurs seuls (polyol, MDI) | Faible | correspondance Ecoinvent non établie | 🔴 Lacune majeure |

### Lecture rapide

Les quatre adhésifs d'atelier ont été diagnostiqués au **Lot 2F**. Dans aucun des quatre cas un adhésif *formulé* correspondant n'a été identifié avec les recherches process/flow disponibles : Ecoinvent ne propose, au mieux, que des précurseurs chimiques isolés (monomère vinyl acetate pour la PVA, copolymère EVA pour l'adhésif hot-melt, polyol et MDI séparés pour le PUR), sans formulation ni chaîne établie vers le produit métier. Pour la colle contact, même cette étape de précurseur fait défaut : aucune brique chimique n'a pu être identifiée avec les méthodes disponibles pendant ce lot, y compris pour le polychloroprène cité dans un lot antérieur (dataset non reconfirmé). Le Lot 2D avait par ailleurs déjà établi que, pour la bande de chant en bois véritable préencollée, les briques d'adhésif disponibles ne résolvent pas la lacune principale de cette bande (l'absence de la composante bois elle-même) — ce constat concerne l'usage en bande de chant, distinct des présentes fiches.

> **Rappel méthodologique :** les adhésifs UF et MUF ne sont pas utilisés directement en atelier et ne figurent pas dans cette taxonomie ; ils relèvent des intrants industriels des panneaux (voir famille Panneaux). La colle PUR d'assemblage multimatériaux ne doit pas être confondue avec l'adhésif EVA hot-melt de l'encolleuse de chants.

### Colle PVAc / PVA blanche — P1

#### Produit métier

Colle PVAc/PVA blanche utilisée pour le collage et l'assemblage du bois.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**. Recherches process/flow (`polyvinyl acetate adhesive`, `PVAc adhesive`, `PVA glue`, `wood adhesive`, `wood glue`, `white glue`, `dispersion adhesive`, `water based adhesive`, `adhesive for wood`) : aucun adhésif formulé identifié. Un candidat générique `adhesive, for metal` (UUID `3bd4e097-7f01-3790-b602-33a7cac44444`, Rest-of-World) a été inspecté et rejeté : c'est un adhésif époxy pour cadres de fenêtres en aluminium, sans rapport avec une colle à bois. Seule brique identifiée : `market for vinyl acetate` (monomère, non polymérisé, non formulé), UUID `9381f4dc-deda-3e02-9cf8-4ef4321b137e`, location Global, unité kg.

#### Correspondance

**Analyse Ecoinvent réalisée (Lot 2F) / correspondance non établie.** Aucun adhésif PVAc formulé n'a été identifié ; le seul dataset disponible (vinyl acetate) représente le monomère, pas la colle prête à l'emploi.

- **Produit / fonction :** Aucune (monomère, pas un adhésif).
- **Technologie :** Faible — brique chimique amont potentielle uniquement.
- **Forme / application :** Aucune (le métier utilise un liquide prêt à l'emploi ; le dataset est un monomère industriel).
- **Unité :** kg — écart avec l'unité métier probable (pot/litre).
- **Géographie :** Global.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucune étape entre le monomère vinyl acetate et la colle prête à l'emploi n'a été identifiée avec les méthodes d'interrogation disponibles au Lot 2F.

#### Données nécessaires

Formulation/composition réelle du produit (à confirmer via la FDS du produit atelier de référence), teneur en solides si pertinente, densité si nécessaire à une conversion, consommation réelle, masse achetée ou unité d'achat.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Aucune reconstruction sérieuse n'est possible à partir du seul monomère.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md)

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

> **Précision métier (validation Nicolas, 2026-09-15) :** les formulations à base d'eau sont particulièrement pertinentes aujourd'hui pour ce produit. Cette précision oriente la recherche fournisseur et une future recherche Ecoinvent ciblée ; elle ne modifie pas le constat déjà établi ci-dessous (aucune brique identifiée, quelle que soit la formulation).

#### Produit métier

Colle contact utilisée pour le collage du stratifié HPL, en tenant compte de la pertinence actuelle des formulations à base d'eau.

#### Équivalent Ecoinvent identifié

Diagnostiqué au **Lot 2F**. Recherches process/flow (`contact adhesive`, `contact glue`, `contact cement`, `solvent based adhesive`, `rubber adhesive`, `neoprene adhesive`, `polychloroprene adhesive`, `polychloroprene` seul, `chloroprene`, `laminate adhesive`, `synthetic rubber`) : aucun adhésif contact formulé, ni aucune brique chimique confirmée, n'a été identifié. Le dataset `market for polychloroprene` cité dans un lot antérieur (UUID `d1147a50-260c-353a-93c0-def3ebd131d0`) n'a pas pu être reconfirmé avec les méthodes d'interrogation disponibles au Lot 2F — cet écart n'a pas pu être attribué avec certitude à une limite d'outil, une différence de version de base, ou une erreur antérieure.

#### Correspondance

**Analyse Ecoinvent réalisée (Lot 2F) / correspondance non établie**, y compris à l'étape des précurseurs.

- **Produit / fonction :** Aucune.
- **Technologie :** Inconnue — chimie réelle du produit métier non présumée.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Aucun adhésif contact formulé, ni aucune brique chimique confirmée (résine ou polymère), n'a pu être identifié avec les outils disponibles au Lot 2F — situation plus défavorable que la PVA et l'EVA, qui disposent au moins d'un précurseur ou d'une résine.

#### Données nécessaires

Composition/formulation réelle du produit (à confirmer via la FDS du produit en pot utilisé en atelier, **en priorisant les formulations à base d'eau** selon la précision métier 2026-09-15), teneur en solides si pertinente, présence et nature des solvants si applicable, densité si nécessaire, consommation réelle.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur**, en ciblant les formulations à base d'eau. Une vérification complémentaire dans OpenLCA (accès direct, hors limites de l'interrogation MCP) est recommandée avant de conclure définitivement à l'absence totale dans la base — `À vérifier dans OpenLCA`, voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).

#### Source du diagnostic

[Diagnostic détaillé — Lot 2F](diagnostic/ecoinvent-representativite-qc-lot-2f.md)

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
| P1 | Charnière invisible de meuble | Matière seulement | Faible | composition inconnue | 🔴 Lacune majeure |
| P1 | Coulisse de tiroir | Matière seulement | Faible | composition inconnue | 🔴 Lacune majeure |
| P1 | Poignée de meuble métallique | Matière + procédé | Conditionnelle | composition inconnue | 🟣 À reconstruire |
| P1 | Pied niveleur / niveleur | Matière + procédé | Conditionnelle | composition inconnue | 🟣 À reconstruire |
| P1/P2 | Ferrure métallique de suspension (clé française) | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Aucun composant de quincaillerie ne dispose d'un produit fonctionnel direct dans Ecoinvent. Pour les vis, la poignée et le pied niveleur, une reconstruction matière + procédé est plausible mais reste conditionnelle à la confirmation, par le fournisseur, de la composition, du revêtement et du procédé réels — l'absence de distinction de taille dans Ecoinvent ne démontre pas que la masse est la seule différence réelle entre les produits. Pour la charnière invisible et la coulisse de tiroir, la lacune est plus profonde : même la nomenclature physique du composant (matériaux constitutifs, parts, revêtement) est absente, ce qui bloque toute reconstruction avant d'obtenir cette donnée. La ferrure de suspension n'a pas encore été examinée.

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

#### Produit métier

Charnière invisible de meuble ; Blum est un exemple atelier, pas le nom principal du composant.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié. Des briques génériques de métal, de traitement de surface et de metal working existent, mais aucune nomenclature interne de la charnière n'est disponible et aucun procédé spécifique n'a été établi.

#### Correspondance

- **Produit / fonction :** Non établie.
- **Composition / matière :** Faible — aucune nomenclature disponible.
- **Technologie / procédé :** Non établie.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

C'est le cas le plus bloquant du lot : la **nomenclature physique/composition du composant est elle-même la première donnée manquante**. Sans elle, aucune reconstruction matière + procédé ne peut être envisagée, contrairement aux vis où la matière probable est au moins identifiable.

#### Données nécessaires

Masse totale, matériaux constitutifs et leurs parts, revêtement, nombre de pièces, origine de fabrication.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.** Cette donnée est bloquante avant toute tentative de modélisation.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Coulisse de tiroir — P1

> **Priorisation et méthode (validation Nicolas, 2026-09-15) :** la coulisse de tiroir est l'un des composants de quincaillerie prioritaires (avec charnières, poignées, pieds/niveleurs et ferrures de suspension). Ne pas subdiviser inutilement toutes les technologies et dimensions de coulisses : prévoir plutôt l'utilisation future d'un **modèle standard représentatif**, en privilégiant un produit dont la documentation fournisseur est suffisamment détaillée. **Action : `À vérifier / choisir modèle fournisseur de référence`.**

#### Produit métier

Coulisse de tiroir ; exemple atelier Blum, profondeurs typiques de 10 à 22 pouces.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié (`drawer slide`, `drawer runner`, `telescopic rail` ou équivalent). Aucun système de roulement ou procédé spécifique n'a été caractérisé par les données inspectées.

#### Correspondance

- **Produit / fonction :** Non établie.
- **Composition / matière :** Faible — même le matériau dominant n'est pas établi.
- **Technologie / procédé :** Non établie.
- **Géographie :** Non établie.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

Comme pour la charnière, la **composition et le système fonctionnel du composant sont la première donnée manquante**. Aucune reconstruction n'est possible avant d'obtenir cette information de la part du fabricant.

#### Données nécessaires

Masse, matériaux constitutifs et leurs parts, revêtement, longueur, origine.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

[Diagnostic détaillé — Lot 2D](diagnostic/ecoinvent-representativite-qc-lot-2d.md)

---

### Poignée de meuble métallique — P1

#### Produit métier

Poignée de meuble métallique.

#### Équivalent Ecoinvent identifié

Aucun produit fonctionnel identifié. `section bar extrusion, aluminium` constitue une brique potentiellement intéressante, **uniquement si** une poignée réelle est confirmée comme profilé aluminium.

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
| P1 | Carton d'emballage / carton ondulé | Dataset identifié | Bonne | données primaires QC absentes | 🟡 À valider |
| P1 | Film à bulles / papier bulle | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1/P2 | Matériau d'emballage blanc fin en rouleau (identification à confirmer) | Analyse approfondie non réalisée — **identification du matériau elle-même non confirmée (2026-09-15)** | Non établie | identification préalable requise | 🟡 À valider |

### Lecture rapide

Le carton ondulé est le cas le plus favorablement régionalisé identifié à ce stade dans l'ensemble des diagnostics : le marché québécois s'appuie sur un procédé de fabrication et sur un intrant majeur (le fluting medium) réellement documentés à partir d'une usine québécoise. Certaines briques restent toutefois non vérifiées, notamment le linerboard (le plus gros intrant en masse) et l'électricité. Le film à bulles n'a pas encore été examiné. **Ajout (validation métier Nicolas, 2026-09-15) :** un matériau d'emballage blanc, très fin, vendu en gros rouleau et utilisé pour envelopper/protéger les meubles, a été identifié comme utilisé en atelier ; son identification exacte (nom commercial, composition) n'est pas encore certaine et ne doit pas être devinée.

### Carton d'emballage / carton ondulé — P1

#### Produit métier

Carton d'emballage / carton ondulé.

#### Équivalent Ecoinvent identifié

- **Dataset (marché) :** `market for corrugated board box`
- **UUID :** `2424352b-3df3-3415-9fbf-a6b1eff0ce60`
- **Location :** Canada, Québec
- **Unité / base de comparaison :** kg
- **Briques en amont :** `corrugated board box production` (`17317a18-28b4-335a-a96d-68789b9bfb70`, Canada, Quebec, collecte documentée sur une usine réelle, mix de production daté de 2008) ; `containerboard production, fluting medium, semichemical, 40% recycled content` (`27a2145c-86e5-3f1e-8219-5d1720d12cab`, Canada, Québec, décrit comme issu d'une usine québécoise réelle).

#### Correspondance

- **Produit / fonction :** Bonne.
- **Composition / matière :** Moyenne — le fluting medium est confirmé québécois ; le linerboard, plus gros intrant en masse (0,7434 kg), n'a pas été vérifié dans ce lot ; des intrants chimiques mineurs (amidon de maïs, encre offset) restent génériques.
- **Technologie / procédé :** Forte — procédé de fabrication des boîtes documenté sur une usine réelle.
- **Géographie :** Forte, à plusieurs niveaux (marché, production, fluting medium).
- **Données primaires québécoises :** Forte mais partiellement ancienne (données de fabrication datées de 2008) ; électricité non résolue comme CA-QC dans ce lot.

#### Lacune Ecoinvent

La régionalisation descend ici jusqu'au procédé de production et à un intrant majeur (fluting medium), ce qui distingue nettement ce cas des autres datasets `CA-QC` examinés. La lacune résiduelle porte sur les **données primaires québécoises absentes ou non vérifiées** pour le linerboard (le plus gros intrant en masse) et pour l'électricité, ainsi que sur l'ancienneté (2008) des données de fabrication des boîtes.

#### Données nécessaires

Vérification de la géographie et de la composition du linerboard, résolution géographique de l'électricité, actualisation éventuelle des données de fabrication.

#### Recommandation

**Valider avant utilisation.** Conserver comme candidat fortement régionalisé et prometteur, sans le qualifier sans réserve de représentatif avant vérification du linerboard, de l'énergie et de la fraîcheur des données.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md)

---

### Film à bulles / papier bulle — P1

#### Produit métier

Film à bulles / papier bulle d'emballage.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit. Sa composition exacte reste elle-même à confirmer avant tout mapping.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la composition exacte du film.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Matériau d'emballage blanc fin en rouleau (identification à confirmer) — P1/P2

> **Nouvel objet (validation métier Nicolas, 2026-09-15).** Matériau blanc, très fin, vendu en gros rouleau, utilisé pour envelopper/protéger les meubles à l'expédition. **Son identification exacte (nom commercial, composition) n'est pas certaine et n'est volontairement pas devinée ici** — ne pas confondre avec le film à bulles (ci-dessus), qui est un produit distinct déjà identifié dans la taxonomie.

#### Produit métier

Matériau d'emballage blanc fin, en gros rouleau, pour l'enveloppement/protection des meubles ; nature exacte (papier, non-tissé, film plastique ou autre) non encore confirmée.

#### Équivalent Ecoinvent identifié

**Sans objet à ce stade — action préalable requise :** `Identifier précisément le matériau d'emballage avant recherche Ecoinvent`. Aucune recherche Ecoinvent ne peut être menée de façon fiable tant que la nature exacte du matériau n'est pas confirmée.

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Sans objet — la lacune actuelle porte sur l'identification métier du matériau lui-même, pas encore sur une lacune Ecoinvent.

#### Données nécessaires

Nom commercial ou technique du matériau, composition (papier, non-tissé, film plastique ou autre), grammage, largeur de rouleau, fournisseur.

#### Recommandation

**Identifier précisément le matériau d'emballage avant toute recherche Ecoinvent.** Obtenir d'abord la fiche produit ou l'emballage du rouleau auprès de l'atelier/fournisseur.

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

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
