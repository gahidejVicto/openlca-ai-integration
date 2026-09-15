# Diagnostic Ecoinvent — Lot 2E
## Surfaces : stratifié HPL, placage bois, panneau plaqué bois acheté fini

Projet ACV mobilier québécois — Base Ecoinvent 3.11, système Cutoff, via openLCA/MCP.

Portée stricte : 3 produits métier (HPL, placage bois, panneau plaqué bois fini). Aucun dataset modifié, aucune modification Git, aucun proxy construit. Le TFL (Lot 2B) n'est pas réanalysé, seulement utilisé comme point de comparaison.

---

## FICHE 1 — STRATIFIÉ HPL

### 1. Identification métier
Nom : stratifié HPL (High Pressure Laminate). Fonction : feuille décorative de surface, appliquée sur un panneau support. Forme achetée : feuille rigide, épaisseur typique 0,6-1,5 mm. Unité métier : feuille/m².

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| high pressure laminate / HPL / high-pressure laminate | search_processes | 0 (toutes) | — |
| laminate | search_flows | **15 résultats — massivement des faux positifs** : panneaux photovoltaïques ("photovoltaic laminate"), verre feuilleté ("laminated safety glass"), bois lamellé-collé structurel ("glued laminated timber"), et **"three layered laminated board"** (le seul candidat bois plausible) | **Faux positifs confirmés pour 14/15 résultats ; le 15ᵉ inspecté et rejeté (voir ci-dessous)** |
| decorative laminate / decorative high pressure laminate / decorative sheet | search_processes | 0 (toutes) | — |
| phenolic laminate / melamine laminate / laminated plastic | search_processes | 0 (toutes) | — |
| impregnated paper | search_flows | 1 résultat : `coating, with melamine impregnated paper` (déjà connu, Lot 2B — un service de revêtement mince, pas un HPL) | Non pertinent comme produit HPL |
| resin impregnated paper / decorative paper | search_flows | 0 | — |
| kraft paper | search_flows | 2 résultats : `kraft paper, bleached` et `kraft paper, unbleached` — papier de base **non imprégné** | Brique amont potentielle uniquement, plusieurs étapes en dessous du produit fini |

**Inspection du candidat "three layered laminated board" (par prudence, conformément à la consigne de ne pas conclure sur le seul nom) :**

| Champ | Valeur |
|---|---|
| Dataset | `three layered laminated board production \| three layered laminated board \| Cutoff, U` |
| UUID | `233c8e26-b01d-3b04-80b0-99cab77f2516` |
| Location | Rest-of-World |
| Fait Ecoinvent | <cite>"This dataset represents the production of one m3 three-layered laminated boards. The input of wood is assumed to be sawn timber spruce, i.e. a softwood."</cite> et <cite>"the data reflects a German production site from 1995"</cite> |

**Conclusion de l'inspection : ce n'est PAS du HPL.** C'est un panneau structurel massif 3 plis en épicéa (softwood), collé au PVAc, unité m³ — un produit de construction/structure, pas une feuille décorative stratifiée. **Faux positif confirmé et rejeté**, avec justification factuelle, comme demandé.

### 3. Meilleur candidat
Aucun produit fonctionnel ni proche. Seules briques chimiques amont partiellement pertinentes : `phenolic resin` (Lot 1, chimique brut) et `kraft paper` (papier de base non imprégné) — mais **aucune brique de "papier imprégné de résine phénolique"** (le composant réel des couches core du HPL) n'a été trouvée, et **aucun procédé d'imprégnation ni de pressage à haute pression** n'existe dans la base.

### 4. Niveau auquel Ecoinvent s'arrête
**Matériau seul, et encore partiellement** — seuls des précurseurs chimiques très en amont (résine phénolique brute, papier kraft non imprégné) sont disponibles, sans aucun brique intermédiaire (imprégnation, empilage, pressage à haute pression).

### 5. Ce que dit Ecoinvent
Rien de spécifique au HPL. Le seul résultat structurellement proche ("laminate" + bois) est un produit différent (panneau structurel massif), confirmé par inspection.

### 6. Composition observée
Non disponible / donnée fournisseur nécessaire.

### 7. Procédés observés
Aucun. Recherches "lamination" et "hot pressing" : 0 résultat chacune.

### 8. Correspondance métier

| Dimension | Niveau |
|---|---|
| Fonction | Aucune |
| Forme | Aucune |
| Composition/matière | Très faible (chimie de base seulement : résine phénolique, papier kraft non imprégné) |
| Transformation | Aucune |
| Unité | Sans objet |
| Géographie | Sans objet |

### 9. Représentativité
Produit fonctionnel absent ; composition inconnue au-delà de deux précurseurs chimiques isolés ; technologie absente ; géographie sans objet ; aucune donnée primaire ; bien inspectable (recherches concluantes).

### 10. VERDICT : **produit absent**

### 11. Briques disponibles

| Brique | Dataset | UUID | Location | Rôle | Limite |
|---|---|---|---|---|---|
| Résine phénolique | market for phenolic resin (Lot 1) | (voir Lot 1) | (à vérifier) | Précurseur chimique plausible des couches core | Aucun lien établi avec un papier imprégné ou un HPL fini |
| Papier kraft | kraft paper, bleached / unbleached | 71833dc2-6443-43d7-a992-4773f52f9afe / c4f00122-eccc-4c3c-8068-0022aa7bf13b | (à vérifier) | Papier de base plausible des couches core | Non imprégné ; aucun procédé d'imprégnation disponible pour le combiner à la résine |

### 12. Variables fabricant nécessaires
Épaisseur/grammage du HPL ; nombre de couches ; grammage du papier décor et des couches core ; formulation résine (mélamine en surface, phénolique en core — non confirmé par Ecoinvent, à valider) ; procédé réel du fournisseur.

### 13. Décision méthodologique provisoire
**Données insuffisantes pour décider.** Contrairement au TFL (Lot 2B), qui disposait d'un service de revêtement complet et documenté, le HPL ne dispose d'aucune brique intermédiaire crédible — seuls des précurseurs chimiques isolés existent, sans procédé pour les relier.

---

## FICHE 2 — PLACAGE BOIS

### 1. Identification métier
Nom : placage bois décoratif. Fonction : matériau mince de surface destiné à recouvrir un panneau. Forme achetée : feuille mince (généralement 0,5-3 mm). Unité métier : feuille/m².

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| veneer / wood veneer | search_flows | 0 (déjà confirmé Lot 1/2B) | — |
| veneer sheet | search_flows | 0 (déjà confirmé Lot 1) | — |
| sliced veneer / rotary veneer | search_processes | 0 (toutes) | — |
| decorative veneer / wood veneer sheet | search_processes | 0 (toutes) | — |
| veneer production / veneer manufacturing / veneer market | search_processes | 0 (toutes) | — |
| veneered | search_processes + search_flows | 0 / 0 | — |

**Confirmation totale et convergente, à tous les niveaux testés (process et flow), avec toutes les variantes terminologiques demandées.**

### 3. Meilleur candidat
Aucun produit placage fini. Seule brique en amont : les flows de grume "sawlog and veneer log, [essence]" identifiés dès le Lot 1 et approfondis au Lot 2C (foresterie uniquement, essences européennes limitées : oak/Allemagne, birch/Suède, beech).

### 4. Niveau auquel Ecoinvent s'arrête
**Aucune brique utile au niveau du produit recherché** — la chaîne s'arrête à la grume forestière, plusieurs étapes en amont de la feuille de placage elle-même (il manque le tranchage/déroulage, le séchage du placage, et la découpe aux dimensions).

### 5. Ce que dit Ecoinvent
Rien de spécifique au placage fini. Les datasets de grume mentionnent "veneer log" dans leur nom de flow ("sawlog and **veneer log**, hardwood") — signalant que ce bois est *destiné à*, ou *apte pour*, la production de placage ou de sciage, mais **le produit placage lui-même n'est jamais représenté en aval**.

### 6. Composition observée
Non disponible / donnée fournisseur nécessaire.

### 7. Procédés observés
Aucun procédé de tranchage (slicing) ou déroulage (peeling) de placage trouvé dans la base.

### 8. Correspondance métier

| Dimension | Niveau |
|---|---|
| Fonction | Aucune |
| Forme | Aucune |
| Composition/matière | Faible (grume générique hardwood, essence limitée aux cas déjà documentés au Lot 2C) |
| Transformation | Aucune (tranchage absent) |
| Unité | Grume en m³, placage métier en m²/feuille — écart majeur, sans donnée de rendement de tranchage disponible pour convertir |
| Géographie | Européenne pour la grume, sans rapport avec le Québec |

### 9. Représentativité
Produit fonctionnel absent ; composition inconnue ; technologie de tranchage absente ; géographie sans objet pour le produit recherché ; aucune donnée primaire ; bien inspectable.

### 10. VERDICT : **produit absent**

### 11. Briques disponibles

| Brique | Dataset | UUID | Location | Rôle | Limite |
|---|---|---|---|---|---|
| Grume forestière (générique hardwood, cf. Lot 2C) | hardwood forestry, oak/birch, sustainable forest management | (voir Lot 2C) | Allemagne / Suède | Matière première plusieurs étapes en amont | Aucun procédé de tranchage disponible pour la transformer en feuille de placage ; essence et géographie déjà documentées comme non pertinentes au Lot 2C |

### 12. Variables fabricant nécessaires
Essence réelle du placage ; épaisseur/grammage ; méthode de production (tranché/déroulé) ; dimensions de feuille ; rendement de production (grume→placage) ; pertes.

### 13. Décision méthodologique provisoire
**Données insuffisantes pour décider.** Même conclusion que pour le placage évoqué au Lot 2B (absence de brique de placage fini) — ce résultat est cohérent et non contradictoire avec les lots précédents.

### Réponses aux questions spécifiques (essence et traçabilité)
- **L'essence reste-t-elle identifiable après transformation ?** Sans objet ici — il n'y a pas de "transformation" représentée du tout entre la grume et un produit placage, puisque ce dernier n'existe pas dans la base.
- **Existe-t-il une perte de traçabilité de l'essence dans la chaîne ?** Le phénomène de perte de traçabilité déjà documenté au Lot 2C (l'essence disparaît au passage du nom de process vers le flow générique "hardwood") reste valable ici pour la grume elle-même, mais devient secondaire puisque la chaîne ne va pas plus loin que la grume.

---

## FICHE 3 — PANNEAU PLAQUÉ BOIS ACHETÉ FINI

### 1. Identification métier
Nom : panneau MDF ou particules plaqué bois fini. Fonction : panneau support avec placage bois déjà collé industriellement, acheté comme produit fini. Forme achetée : panneau. Unité métier : panneau/m²/m³.

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| veneered panel / wood veneered panel / veneered MDF / veneered fibreboard / veneered fiberboard | search_processes | 0 (toutes) | — |
| veneered particleboard / veneered particle board / veneer faced board / veneer faced panel | search_processes | 0 (toutes) | — |
| wood faced panel / decorative wood panel / furniture board / veneered board | search_processes + search_flows (furniture board testé en flow) | 0 (toutes) | — |

**Confirmation totale et convergente, à tous les niveaux testés.**

### 3. Meilleur candidat
Aucun. Substrats bruts déjà validés au Lot 2B (MDF, particules) restent disponibles comme briques de base, mais aucune brique de "placage" ni de "procédé de collage/pressage de placage" n'existe pour compléter l'assemblage (cf. Fiche 2 ci-dessus et section 9 ci-dessous).

### 4. Niveau auquel Ecoinvent s'arrête
**Matériau + procédé pour le seul substrat** (MDF ou particules brut, cf. Lot 2B) ; **aucune brique** pour le placage lui-même ni pour l'opération de collage/pressage.

### 5. Ce que dit Ecoinvent
Rien de spécifique au panneau plaqué fini.

### 6. Composition observée
Non disponible / donnée fournisseur nécessaire.

### 7. Procédés observés (recherche dédiée, section 9 du mandat)

| Terme | Type | Résultat |
|---|---|---|
| wood lamination / laminating / lamination | search_processes | 0 (toutes) |
| wood pressing / hot pressing / panel pressing | search_processes | 0 (toutes) |
| veneer gluing / wood gluing | search_processes | 0 (toutes) |
| adhesive application / surface coating | (couvert conceptuellement par les résultats déjà obtenus au Lot 2B pour le "coating service" — pertinent seulement pour le mélaminé, pas pour un placage bois véritable, cf. Fiche 1 du Lot 2B) | Non applicable au placage bois |

**Aucun procédé de collage/pressage de placage n'existe dans la base**, contrairement au TFL qui bénéficiait du `coating service, melamine impregnated paper`.

### 8. Correspondance métier

| Dimension | Niveau |
|---|---|
| Fonction | Aucune pour le produit fini recherché |
| Forme | Aucune |
| Composition/matière | Le substrat seul est connu (MDF/particules, Lot 2B) ; le placage et l'adhésif de collage restent inconnus |
| Transformation | Aucune pour l'assemblage substrat+placage |
| Unité | m³ pour le substrat (Lot 2B) ; le placage n'a pas d'unité disponible puisqu'absent |
| Géographie | Celle du substrat seul (Lot 2B — non-QC, cf. rapport correspondant) |

### 9. Représentativité
Produit fonctionnel absent ; composition partiellement connue (substrat seulement) ; technologie de collage absente ; géographie limitée au substrat ; aucune donnée primaire ; bien inspectable.

### 10. VERDICT : **produit absent**

### 11. Briques disponibles

| Brique | Dataset | UUID | Location | Rôle | Limite |
|---|---|---|---|---|---|
| Substrat MDF brut | market for medium density fibreboard (Lot 2B) | eef398de-7420-330d-b894-1440a0afa155 | RoW (copie Europe) | Panneau support plausible | Ne couvre que le substrat ; aucun placage ni collage disponible pour compléter |
| Substrat particules brut | market for particleboard, uncoated (Lot 2B) | 7690ac93-cf92-32dd-b2cf-68e6c7fcf673 | RoW (mélange Europe+Brésil) | idem | idem |

**Aucune autre brique** (placage, adhésif de collage bois, procédé de pressage) n'a été trouvée pour compléter cet assemblage — contrairement au TFL, cette reconstruction ne peut même pas être évaluée conceptuellement de façon complète, faute de deuxième et troisième brique.

### 12. Variables fabricant nécessaires
Essence et grammage du placage ; type et grammage d'adhésif de collage (contrairement au TFL, aucune hypothèse de départ n'est même disponible) ; température/pression de pressage ; substrat réel utilisé (MDF ou particules) ; pertes de production.

### 13. Décision méthodologique provisoire
**Données insuffisantes pour décider.** La reconstruction conceptuelle A/B proposée par le mandat (substrat + placage + adhésif + pressage) ne peut être évaluée que sur sa première brique (le substrat, déjà validé au Lot 2B) — les trois autres briques sont absentes de la base, rendant la reconstruction non seulement non construite mais **non évaluable dans son ensemble** à ce stade.

---

## COMPARAISON AVEC LE TFL (LOT 2B)

| Produit | Surface disponible | Substrat disponible | Produit fini disponible | Procédé disponible | Reconstruction plausible | Lacune principale |
|---|---|---|---|---|---|---|
| **TFL sur MDF/particules (Lot 2B, rappel)** | Oui — `coating, with melamine impregnated paper` (papier déjà imprégné, grammage documenté 302 g/m²/face) | Oui (Lot 2B) | Non | **Oui** — service de revêtement complet et documenté | **Oui, avec réserves documentées** (émissions de pressage exclues, hypothèse d'épaisseur nécessaire) | Émissions de pressage non incluses ; hypothèse d'épaisseur requise |
| **HPL** | Non — aucune feuille stratifiée, aucun papier imprégné de résine phénolique | Sans objet (le HPL n'a pas de "substrat" au sens panneau — c'est une feuille autoportante) | Non | **Non** — aucune imprégnation, aucun pressage haute pression | **Non — aucune brique intermédiaire pour relier les précurseurs chimiques au produit** | Absence quasi-totale : ni surface, ni procédé, seulement deux précurseurs chimiques isolés |
| **Placage bois (fini)** | Non — aucune feuille de placage, seule la grume existe | Sans objet pour le placage lui-même | Non | **Non** — aucun tranchage/déroulage | **Non — la chaîne s'arrête à la grume, plusieurs étapes avant le produit recherché** | Absence de toute transformation entre grume et placage fini |
| **Panneau plaqué bois fini** | Non (dépend du placage, absent — voir ligne précédente) | Oui (substrat MDF/particules, Lot 2B) | Non | **Non** — aucun collage/pressage de placage | **Non — seule la première des quatre briques de l'assemblage conceptuel existe** | Trois briques sur quatre absentes (placage, adhésif, procédé) |

**Réponse à la question du Lot 2E** : **non, Ecoinvent ne présente pas le même type de lacune pour ces trois technologies.** Le TFL est nettement mieux représenté que les trois technologies de ce lot — il dispose d'une brique de surface complète, documentée et directement combinable. Le HPL et le placage bois (fini) sont dans une situation strictement plus défavorable : le HPL ne dispose que de précurseurs chimiques isolés sans procédé de liaison, et le placage bois fini ne dispose d'aucune brique du tout entre la grume et la feuille recherchée. Le panneau plaqué bois fini hérite de cette double absence (placage + procédé), ne conservant que le substrat comme brique valide.

---

## PRODUIT ACHETÉ VS OPÉRATION EN ATELIER

**Cas A — panneau acheté déjà plaqué** : Ecoinvent ne permet pas de représenter ce scénario, faute de produit fini (Fiche 3, verdict "produit absent").

**Cas B — panneau plaqué manuellement/localement dans l'entreprise** : Ecoinvent permet de représenter **une partie seulement** de ce scénario — le substrat brut (Fiche 3, brique 1) est disponible et déjà validé au Lot 2B, mais le placage, l'adhésif et l'opération de pressage manquent tous les trois. **Le scénario B n'est donc pas plus représentable que le scénario A dans l'état actuel de la base** — la différence entre les deux cas n'est pas une différence de disponibilité de données Ecoinvent, mais une différence de réalité métier (où acheter le produit fini vs le fabriquer soi-même) qu'aucun des deux ne permet actuellement de documenter complètement.

---

## DONNÉES FOURNISSEUR MINIMALES (établies à partir des résultats réels de ce lot)

### HPL
- **Grammage et nombre de couches** — nécessaire car aucune structure de référence n'existe dans Ecoinvent ; indispensable.
- **Formulation résine (répartition mélamine décor / phénolique core)** — nécessaire car Ecoinvent ne fournit qu'une résine phénolique isolée sans lien vérifié au produit ; indispensable pour toute reconstruction future.
- **Épaisseur du HPL fini** — nécessaire pour toute conversion masse/surface future ; indispensable.
- **Procédé réel du fournisseur** — souhaitable, pour évaluer si un procédé générique de l'industrie du papier/stratifié pourrait un jour être identifié ailleurs dans Ecoinvent ou une autre base.

### Placage
- **Essence réelle** — indispensable, car aucune essence métier (érable, frêne, merisier, chêne rouge — cf. Lot 2C) n'est représentée même à l'état de grume pour trois des quatre essences.
- **Épaisseur/grammage et méthode de production (tranché/déroulé)** — indispensable, car ce sont les seules variables qui pourraient permettre de relier un futur dataset générique (si Ecoinvent en ajoutait un) au produit réel.
- **Rendement grume→placage** — souhaitable, utile seulement si une brique de tranchage devient disponible dans une version future d'Ecoinvent.

### Panneau plaqué fini
- **Substrat réel (MDF ou particules)** — indispensable, car cette information seule reste actuellement exploitable (cf. Lot 2B).
- **Grammage/essence du placage et type d'adhésif** — indispensable, mêmes raisons que pour le placage seul.
- **Température, pression et durée de pressage** — souhaitable seulement si une brique de procédé de pressage devient disponible ; sans objet dans l'état actuel de la base.

---

## RÉPONSES EXPLICITES

**1. Ecoinvent possède-t-il un HPL fini utilisable ?** Non. Recherche exhaustive (process + flow, toutes variantes terminologiques du mandat) : 0 résultat pertinent après élimination des faux positifs (photovoltaïque, verre, panneau structurel massif).

**2. Ecoinvent possède-t-il du placage bois fini ?** Non, confirmé à tous les niveaux (process et flow), pour toutes les variantes terminologiques testées.

**3. Le placage disponible conserve-t-il l'information d'essence ?** Sans objet — aucun placage fini n'existe pour évaluer cette question. Seule la grume en amont conserve nominalement une essence (cf. Lot 2C), déjà démontrée non pertinente pour 3 des 4 essences métier.

**4. Ecoinvent possède-t-il un panneau MDF plaqué bois fini ?** Non, confirmé.

**5. Ecoinvent possède-t-il un panneau de particules plaqué bois fini ?** Non, confirmé — même recherche, même résultat nul pour les deux substrats.

**6. Existe-t-il un procédé de collage/lamination suffisamment pertinent ?** Non pour le placage bois véritable. Le seul procédé de revêtement existant (`coating, with melamine impregnated paper`) est spécifique au papier mélaminé (TFL, Lot 2B) et ne représente pas un collage de placage bois véritable.

**7. Le panneau plaqué fini est-il mieux représenté que le TFL étudié en 2B ?** Non — c'est l'inverse. Le TFL dispose d'une brique de surface complète et documentée ; le panneau plaqué bois fini ne dispose d'aucune brique de surface ni de procédé, seulement du substrat.

**8. HPL et TFL présentent-ils la même lacune ou des lacunes différentes ?** Des lacunes différentes et de sévérité différente. Le TFL manque seulement du produit fini final (mais dispose de toutes les briques pour une reconstruction documentée). Le HPL manque du produit fini ET de toute brique de liaison entre ses deux seuls précurseurs chimiques identifiés — une lacune structurellement plus sévère.

**9. Peut-on représenter proprement le scénario `panneau acheté déjà plaqué` ?** Non, pour aucun des trois produits de ce lot.

**10. Peut-on représenter séparément `panneau plaqué dans l'entreprise` ?** Partiellement seulement pour le substrat (déjà validé Lot 2B) ; non pour le placage, l'adhésif, ou le pressage.

**11. Quelles données fournisseur sont indispensables pour distinguer les deux scénarios (A vs B) ?** Dans l'état actuel de la base, cette distinction est **prématurée** — aucun des deux scénarios n'est représentable au-delà du substrat. La question redevient pertinente seulement si une brique de placage/procédé de pressage devient disponible.

**12. Quelles sont les principales lacunes Ecoinvent révélées par cette famille ?** (a) Absence totale de toute brique de placage bois fini, à tous les niveaux de transformation entre la grume et la feuille. (b) Absence de toute brique de HPL au-delà de deux précurseurs chimiques isolés et non reliés. (c) Absence de tout procédé de collage de placage ou de pressage haute pression, contrastant avec la disponibilité du service de revêtement mélaminé (TFL) — ce contraste montre que la richesse de la base Ecoinvent sur les surfaces de panneaux est **spécifique à la technologie TFL/mélamine**, pas générale aux technologies de surface du mobilier.

---

## IMPACT SUR LE RÉFÉRENTIEL — informations proposées pour `docs/materiaux-ebenisterie.md`

**Rappel : ce fichier n'est PAS modifié dans ce lot. Les éléments ci-dessous sont proposés pour QC avant intégration ultérieure.**

### Stratifié HPL
- **Ecoinvent** : aucun produit fini, aucune surface, aucun procédé de liaison. Seuls deux précurseurs chimiques isolés (résine phénolique, papier kraft non imprégné) existent, sans lien établi entre eux ni avec le produit recherché.
- **Correspondance** : aucune.
- **Lacune principale** : absence quasi-totale — pas de brique de reconstruction évaluable, contrairement au TFL.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : recherche exhaustive (process + flow, ~15 variantes terminologiques) sans résultat pertinent ; un faux positif plausible ("three layered laminated board") inspecté et rejeté (panneau structurel massif, pas un stratifié décoratif).
- **Recommandation** : ne pas tenter de reconstruction avant l'obtention de données fournisseur sur la formulation et la structure en couches ; envisager une recherche future dans une autre base si le projet en dispose.

### Placage bois
- **Ecoinvent** : aucun produit placage fini à aucun niveau ; seule la grume forestière générique (cf. Lot 2C) existe, plusieurs étapes en amont.
- **Correspondance** : aucune.
- **Lacune principale** : absence de toute transformation entre grume et placage fini (tranchage/déroulage absent).
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : confirmation totale et convergente par recherche process + flow, cohérente avec les constats déjà faits aux Lots 1, 2B et 2C.
- **Recommandation** : données fournisseur indispensables sur l'essence, le grammage et la méthode de production avant toute tentative de proxy.

### Panneau plaqué bois acheté fini
- **Ecoinvent** : substrat brut (MDF ou particules) disponible et déjà validé (Lot 2B, non-QC) ; placage, adhésif et procédé de pressage tous absents.
- **Correspondance** : faible (substrat seul sur les quatre composantes conceptuelles de l'assemblage).
- **Lacune principale** : trois briques sur quatre manquantes (placage, adhésif, procédé) — hérite des lacunes des deux fiches précédentes.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : produit fini absent ; reconstruction conceptuelle non évaluable dans son ensemble faute de briques suffisantes.
- **Recommandation** : traiter comme un cas d'attente jusqu'à ce que la Fiche 2 (placage) évolue ; ne pas utiliser le substrat seul comme proxy du panneau fini sans avertissement explicite.

---

## IMPACT SUR LA GRILLE MÉTHODOLOGIQUE

Aucun nouveau critère numéroté n'est ajouté ce tour — les 17 critères stabilisés jusqu'au Lot 2D ont suffi à structurer l'analyse, en particulier :
- **#14 (homonymies)** : confirmée avec force par la pollution du terme "laminate" (photovoltaïque, verre feuilleté, bois structurel) — le cas le plus massif de faux positifs rencontré depuis le début du diagnostic.
- **#15 (correspondance réelle au-delà du nom)** : confirmée par l'inspection et le rejet justifié de "three layered laminated board".
- **#17 (inspection des flux de sortie pour détecter une calibration matière)** : appliquée mais sans révéler de calibration cachée ici (contrairement au calandrage PVC du Lot 2D) — utile de noter que ce critère peut aussi conclure par la négative (absence de calibration détectable), ce qui est en soi une information.

**Un phénomène nouveau, mais qui ne justifie pas un nouveau critère isolé** : ce lot montre que la richesse de représentation d'Ecoinvent pour les technologies de surface de panneaux n'est **pas uniforme entre technologies concurrentes visant la même fonction** (TFL vs HPL vs placage) — alors que les Lots précédents avaient surtout révélé des variations **géographiques** (même technologie, représentativité différente selon la région) ou de **profondeur de chaîne** (même essence, disparaissant à un stade donné). Ce constat est mieux compris comme une **application** du critère #7 (spécificité produit) à un niveau comparatif entre produits concurrents, plutôt que comme un critère nouveau.

---

*Fin du rapport Lot 2E. Aucun dataset openLCA modifié. Aucune modification Git. Aucun proxy construit. `docs/materiaux-ebenisterie.md` n'a pas été modifié. Seuls les 3 produits métier demandés ont été traités.*
