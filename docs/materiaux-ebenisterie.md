# Référentiel des matériaux et composants — Ébénisterie

> **Statut : V2 — vue consolidée du diagnostic Ecoinvent**
> Ce document reste l'inventaire métier des produits et composants réellement achetés ou utilisés en atelier. Il intègre désormais, pour les matériaux déjà approfondis, les conclusions des diagnostics de représentativité Ecoinvent (Lots 2A à 2D). Les matériaux non encore approfondis conservent leur statut prudent d'origine.

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
| P1 | Contreplaqué de bouleau russe | Dataset identifié (générique) | Faible | essence | 🔴 Lacune majeure |
| P1 | Panneau de particules mélaminé / TFL | Matière + procédé | Partielle | produit fini absent | 🟣 À reconstruire |
| P1 | MDF mélaminé / TFL | Matière + procédé | Partielle | produit fini absent | 🟣 À reconstruire |
| P1 | MDF plaqué bois acheté fini | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Panneau de particules plaqué bois acheté fini | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | HDF brut | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | OSB | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | Autre contreplaqué | Dataset identifié | Partielle | technologie étrangère | 🟠 À adapter |
| P2 | Panneau plaqué en atelier | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Les panneaux bruts (particules, MDF) ont un dataset Ecoinvent dont la fonction correspond bien au produit métier, mais dont la recette, l'énergie et les intrants sont d'origine européenne (EPF) et doivent être adaptés avec des données de fabricant québécois. Les panneaux finis mélaminés/TFL n'existent pas comme produit direct dans Ecoinvent : le meilleur modèle plausible combine le panneau brut et un service générique de revêtement mélaminé, ce qui reste une reconstruction non validée. Le contreplaqué constitue un cas particulier : le seul dataset disponible est un contreplaqué générique dont la géographie `CA-QC` est trompeuse (recette et données allemandes), et il ne représente pas l'essence bouleau russe visée. Les panneaux achetés déjà plaqués (bois), le HDF, l'OSB et le placage en atelier n'ont pas encore fait l'objet d'une analyse Ecoinvent approfondie.

> **Règle métier :** les panneaux sont achetés déjà plaqués autant que possible. Le placage en atelier est secondaire. Un dataset localisé `CA-QC` n'est pas représentatif du Québec du seul fait de sa géographie : ses intrants, paramètres et hypothèses technologiques doivent être analysés.

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

### Contreplaqué de bouleau russe — P1

#### Produit métier

Contreplaqué de bouleau russe, produit distinct dans la taxonomie métier, non substituable d'emblée par un contreplaqué générique.

#### Équivalent Ecoinvent identifié

- **Dataset :** `plywood production | plywood | Cutoff, U` (générique, non spécifique à une essence ni à une configuration de plis)
- **UUID :** `5538194d-92b2-3020-bb3e-fbc59cb71248` (comparatif RER `0f52041a-b664-357b-ab50-e48613bff63d`)
- **Location :** Canada, Quebec (déclaré comme copie du dataset européen ; données reposant sur un échantillon de production allemande)
- **Unité / base de comparaison :** m³

#### Correspondance

- **Produit / fonction :** Partielle — c'est un contreplaqué générique, pas du bouleau russe.
- **Composition / matière :** Faible — sawlog/veneer log hardwood générique, aucune trace de l'essence bouleau russe.
- **Technologie / procédé :** Faible — les quantités technologiques centrales inspectées (bois, résine, énergie, eau) sont identiques ou se recomposent à la même somme entre CA-QC et RER, et les émissions directes de procédé inspectées sont elles aussi identiques.
- **Géographie :** Trompeuse — la mention `Canada, Quebec` ne reflète pas une donnée primaire québécoise ; le dataset est décrit comme une copie du modèle européen basée sur un échantillon allemand.
- **Données primaires québécoises :** Aucune identifiée.

#### Lacune Ecoinvent

C'est un cas de **dataset CA-QC utilisant en réalité des données étrangères** combiné à une **essence générique** : la localisation `Canada, Quebec` sert uniquement au linking vers des marchés régionaux, tandis que les quantités technologiques centrales inspectées (bois, résine, énergie, eau) sont identiques ou se recomposent à la même somme, et les émissions directes de procédé inspectées sont elles aussi identiques à celles de la version allemande/européenne. Le produit ne correspond ni à l'essence ni à la technologie de fabrication du contreplaqué de bouleau russe recherché.

#### Données nécessaires

Essence réelle (bouleau russe), configuration des plis, origine de fabrication, adhésif utilisé, données de fabricant si une reconstruction est un jour envisagée.

#### Recommandation

**Données insuffisantes pour décider.** Ne pas présenter ce dataset comme représentatif du contreplaqué de bouleau russe ; l'utiliser au mieux comme proxy générique documenté, en explicitant sa dépendance aux données allemandes.

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md)

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

Panneau MDF plaqué bois, acheté fini ; le support et le placage ne sont pas séparés d'emblée dans la taxonomie.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.** Aucun dataset candidat n'a encore été recherché pour ce produit fini.

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit précis. Le fichier initial le classait « à rechercher » ; ce statut est conservé.

#### Données nécessaires

À déterminer lors d'une future analyse : essence de placage, épaisseur, adhésif de placage, origine de fabrication.

#### Recommandation

**Données insuffisantes pour décider.** Traiter ce produit dans un futur lot d'approfondissement, en suivant la logique product-first déjà appliquée aux panneaux TFL.

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Panneau de particules plaqué bois acheté fini — P1

#### Produit métier

Panneau de particules plaqué bois, acheté fini ; le support et le placage ne sont pas séparés d'emblée dans la taxonomie.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit précis.

#### Données nécessaires

À déterminer lors d'une future analyse : essence de placage, épaisseur, adhésif de placage, origine de fabrication.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

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

#### Produit métier

Panneau OSB.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit.

#### Données nécessaires

À déterminer.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Autre contreplaqué — P2

#### Produit métier

Contreplaqué générique, catégorie d'usage réel distincte du contreplaqué de bouleau russe ; candidat à vérifier selon le contreplaqué réellement utilisé.

#### Équivalent Ecoinvent identifié

- **Dataset :** `plywood production | plywood | Cutoff, U` — le même dataset générique évalué en détail pour le contreplaqué de bouleau russe.
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

Même lacune technique que pour le contreplaqué de bouleau russe : un **dataset CA-QC utilisant en réalité des données étrangères**. La différence tient au produit métier visé : ici, la catégorie « autre contreplaqué » n'exige pas une essence précise, ce qui rend ce dataset générique plus directement utilisable comme candidat, sous réserve d'adaptation de la technologie et de la géographie déclarée.

#### Données nécessaires

Essence et configuration réelles du contreplaqué visé par cette catégorie, données de fabricant pour confirmer ou corriger la recette technologique (bois, résine, énergie).

#### Recommandation

**Adapter/régionaliser le dataset existant.** Utiliser comme candidat générique documenté, en corrigeant les hypothèses technologiques avant tout usage défendable ; voir aussi la [fiche pilote CA-QC](inventaire/panneaux/plywood-ca-qc.md).

#### Source du diagnostic

[Diagnostic détaillé — Lot 2A](diagnostic/ecoinvent-representativite-qc-lot-2a.md)

---

### Panneau plaqué en atelier — P2

#### Produit métier

Cas secondaire où le panneau fini n'est pas disponible : support, placage et adhésif sont alors comptabilisés séparément.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. Ce cas dépend des fiches « panneau brut », « placage de bois naturel » et « adhésifs », qui doivent elles-mêmes être approfondies.

#### Données nécessaires

À déterminer une fois les composantes (support, placage, adhésif) approfondies individuellement.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

## 2. Surfaces

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Stratifié HPL | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Placage de bois naturel | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Aucun des deux revêtements de surface n'a encore fait l'objet d'un diagnostic Ecoinvent approfondi dans les Lots 2A–2D. Le placage de bois naturel partage vraisemblablement certaines des lacunes déjà documentées pour le bois massif (essence, traçabilité), mais cela reste à vérifier spécifiquement plutôt qu'à présumer.

### Stratifié HPL — P1

#### Produit métier

Revêtement stratifié haute pression, utilisé notamment avec une colle contact.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce matériau.

#### Données nécessaires

À déterminer.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Placage de bois naturel — P1

#### Produit métier

Placage de bois naturel utilisé pour le cas secondaire du placage en atelier.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce matériau. Le Lot 2D a constaté, pour la bande de chant bois véritable, l'absence de toute brique de placage/bois mince exploitable dans Ecoinvent ; ce constat concerne une recherche distincte mais pourrait annoncer une difficulté similaire pour le placage de surface — à vérifier, sans le présumer.

#### Données nécessaires

À déterminer : essence, épaisseur, procédé de tranchage.

#### Recommandation

**Données insuffisantes pour décider.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

## 3. Bandes de chant

### Vue d'ensemble

| Priorité | Produit métier | Ecoinvent | Correspondance | Lacune principale | Statut |
|---|---|---|---|---|---|
| P1 | Bande de chant en bois véritable préencollée | Produit direct absent | Faible | produit fini absent | 🔴 Lacune majeure |
| P1 | Bande de chant en bois véritable non encollée | Produit direct absent | Faible | produit fini absent | 🔴 Lacune majeure |
| P1 | Bande de chant ABS | Matière + procédé | Faible | procédé absent | 🟣 À reconstruire |
| P1 | Bande de chant PVC | Matière + procédé | Partielle | procédé absent | 🟣 À reconstruire |

### Lecture rapide

Aucune bande de chant n'existe comme produit fini direct dans Ecoinvent. Pour le bois véritable (préencollé ou non), aucune brique de placage ou de bande mince exploitable n'a été trouvée : la lacune commence dès la composante bois elle-même, avant même la question de l'adhésif. Pour l'ABS et le PVC, la matière de base existe et des procédés de transformation plastique proches existent aussi, mais aucun ne reproduit la géométrie exacte d'une bande de chant ; le PVC dispose d'un indice supplémentaire (un flux de déchet de calandrage spécifique au PVC) qui en fait un proxy légèrement mieux étayé que l'ABS, sans que cela constitue une validation.

> **Rappel métier :** l'ABS et le PVC sont décrits ici selon leur usage en bande de chant, et non comme familles de matière autonomes.

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
| P1 | Colle PVAc / PVA blanche | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Adhésif thermofusible EVA / EVA hot-melt | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P1 | Colle contact | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |
| P2 | Colle polyuréthane / PUR | Analyse approfondie non réalisée | Non établie | diagnostic à réaliser | 🟡 À valider |

### Lecture rapide

Aucun adhésif d'atelier n'a encore fait l'objet d'un diagnostic Ecoinvent approfondi. Le Lot 2D a toutefois établi que, pour la bande de chant en bois véritable préencollée, les briques d'adhésif disponibles dans Ecoinvent ne résolvent pas la lacune principale (l'absence de la composante bois elle-même) — ce constat concerne l'usage en bande de chant, pas les adhésifs eux-mêmes en tant que produits.

> **Rappel méthodologique :** les adhésifs UF et MUF ne sont pas utilisés directement en atelier et ne figurent pas dans cette taxonomie ; ils relèvent des intrants industriels des panneaux (voir famille Panneaux). La colle PUR d'assemblage multimatériaux ne doit pas être confondue avec l'adhésif EVA hot-melt de l'encolleuse de chants.

### Colle PVAc / PVA blanche — P1

#### Produit métier

Colle PVAc/PVA blanche utilisée pour le collage et l'assemblage du bois.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit.

#### Données nécessaires

Formulation exacte, à confirmer à partir de la fiche de données de sécurité (FDS) du produit atelier de référence.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Adhésif thermofusible EVA / EVA hot-melt — P1

#### Produit métier

Adhésif thermofusible EVA utilisé dans l'encolleuse de chants.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée. Le Lot 2D a examiné la composante bois des bandes de chant, mais pas l'adhésif EVA lui-même comme produit distinct.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la formulation et le grammage d'application.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Colle contact — P1

#### Produit métier

Colle contact utilisée pour le collage du stratifié HPL.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit.

#### Données nécessaires

Composition exacte, à confirmer à partir de la FDS du produit en pot utilisé en atelier.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

---

### Colle polyuréthane / PUR — P2

#### Produit métier

Colle PUR utilisée occasionnellement pour le collage métal-bois ou plastique-bois.

#### Équivalent Ecoinvent identifié

**Analyse approfondie : non réalisée à ce stade.**

#### Correspondance

Non établie.

#### Lacune Ecoinvent

Aucune recherche Ecoinvent n'a encore été menée pour ce produit.

#### Données nécessaires

À déterminer lors du diagnostic approfondi ; au minimum confirmer la formulation exacte et l'usage réel.

#### Recommandation

**Obtenir d'abord la nomenclature fournisseur.**

#### Source du diagnostic

**Analyse approfondie : non réalisée à ce stade.**

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

> **Rappel méthodologique :** rechercher d'abord le composant fonctionnel, puis un produit proche ; une reconstruction à partir de matières et de procédés ne vient qu'en dernier recours. L'acier, l'aluminium, le zinc et le plastique ne constituent pas des familles principales autonomes.

### Vis d'assemblage #6 — P1

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

### Lecture rapide

Le carton ondulé est le cas le plus favorablement régionalisé identifié à ce stade dans l'ensemble des diagnostics : le marché québécois s'appuie sur un procédé de fabrication et sur un intrant majeur (le fluting medium) réellement documentés à partir d'une usine québécoise. Certaines briques restent toutefois non vérifiées, notamment le linerboard (le plus gros intrant en masse) et l'électricité. Le film à bulles n'a pas encore été examiné.

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

## 9. Données transversales

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

Ces quatre lots ont établi plusieurs enseignements méthodologiques transversaux, reflétés dans les fiches ci-dessus :

1. Une localisation `CA-QC` ne prouve pas la présence de données primaires québécoises ; elle doit être distinguée de la déclaration narrative, de la comparaison quantitative avec une version étrangère équivalente et de la profondeur réelle de régionalisation.
2. Pour chaque matériau, il faut distinguer **produit métier réel → équivalent Ecoinvent → correspondance physique → représentativité québécoise → lacune → donnée nécessaire pour corriger cette lacune.**
3. Pour les composants manufacturés, il faut distinguer produit fonctionnel absent, nomenclature/composition absente, procédé absent, et reconstruction possible mais non validée.
4. Une matière disponible dans Ecoinvent ne signifie pas que le composant fonctionnel est correctement représenté.
5. Pour les bois massifs, l'existence d'un dataset générique `hardwood` ne représente pas automatiquement l'essence québécoise ciblée ; la transformation détruit généralement la traçabilité de l'essence dans le flow générique.
6. Pour le PVC, un exchange `waste polyvinylchloride` est un indice quantitatif de spécificité matière du procédé de calandrage, pas une preuve que le dataset représente une ligne réelle de chants PVC.
7. Pour les vis #6 et #8, un modèle commun ne peut être envisagé que si le fournisseur confirme composition, procédé et revêtement équivalents.
8. Pour charnières et coulisses, la première donnée manquante est la nomenclature physique/composition du composant acheté.

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
