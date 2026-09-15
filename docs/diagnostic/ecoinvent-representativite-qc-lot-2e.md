# Diagnostic Ecoinvent — Lot 2E
## Surfaces : stratifié HPL, placage bois, panneau plaqué bois acheté fini

Projet ACV mobilier québécois — Base Ecoinvent 3.11, système Cutoff, via openLCA/MCP.

Portée stricte : 3 produits métier (HPL, placage bois, panneau plaqué bois fini). Aucun dataset modifié, aucune modification Git, aucun proxy construit. Le TFL (Lot 2B) n'est pas réanalysé, seulement utilisé comme point de comparaison.

---

## FICHE 1 — STRATIFIÉ HPL

### 1. Identification métier
Nom : stratifié HPL (High Pressure Laminate). Fonction : feuille décorative de surface, appliquée sur un panneau support. Forme achetée : feuille rigide. Unité métier : feuille/m².

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
Aucun produit fonctionnel ni proche identifié. Des datasets de résine phénolique (`phenolic resin`, Lot 1, chimique brut) et de papier kraft (`kraft paper`, non imprégné) ont été identifiés lors des recherches, mais aucun lien n'a été établi entre ces produits et le HPL métier étudié — ni brique de "papier imprégné de résine" ni procédé d'imprégnation ou de pressage à haute pression n'a été identifié avec les méthodes de recherche disponibles.

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
| Résine phénolique | market for phenolic resin (Lot 1) | (voir Lot 1) | (à vérifier) | Brique amont potentielle, pertinence non établie | Aucun lien établi avec un papier imprégné ou un HPL fini |
| Papier kraft | kraft paper, bleached / unbleached | 71833dc2-6443-43d7-a992-4773f52f9afe / c4f00122-eccc-4c3c-8068-0022aa7bf13b | (à vérifier) | Brique amont potentielle, pertinence non établie | Non imprégné ; aucun procédé d'imprégnation identifié pour le combiner à la résine |

### 12. Variables fabricant nécessaires
Composition/formulation réelle du HPL ; structure du produit (nombre de couches) ; masse surfacique/épaisseur du HPL et de ses couches ; procédé de fabrication réel du fournisseur — sans présupposer la réponse.

### 13. Décision méthodologique provisoire
**Données insuffisantes pour décider.** Contrairement au TFL (Lot 2B), qui disposait d'un service de revêtement complet et documenté, le HPL ne dispose d'aucune brique intermédiaire crédible — seuls des précurseurs chimiques isolés existent, sans procédé pour les relier.

---

## FICHE 2 — PLACAGE BOIS

### 1. Identification métier
Nom : placage bois décoratif. Fonction : matériau mince de surface destiné à recouvrir un panneau. Forme achetée : feuille mince. Unité métier : feuille/m².

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| veneer / wood veneer | search_flows | 0 (déjà confirmé Lot 1/2B) | — |
| veneer sheet | search_flows | 0 (déjà confirmé Lot 1) | — |
| sliced veneer / rotary veneer | search_processes | 0 (toutes) | — |
| decorative veneer / wood veneer sheet | search_processes | 0 (toutes) | — |
| veneer production / veneer manufacturing / veneer market | search_processes | 0 (toutes) | — |
| veneered | search_processes + search_flows | 0 / 0 | — |

**Aucun résultat pertinent n'a été identifié avec les méthodes d'interrogation disponibles (process et flow), pour toutes les variantes terminologiques testées, sous réserve des limites de l'outil.**

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
- **L'essence reste-t-elle identifiable après transformation ?** Sans objet ici — aucune "transformation" n'a été identifiée entre la grume et un produit placage, puisque ce dernier n'a pas été identifié avec les recherches disponibles.
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

**Aucun résultat pertinent n'a été identifié avec les méthodes d'interrogation disponibles, à tous les niveaux testés, sous réserve des limites de l'outil.**

### 3. Meilleur candidat
Aucun. Substrats bruts déjà validés au Lot 2B (MDF, particules) restent disponibles comme briques de base. Aucune brique de "placage fini" ni de "procédé de collage/pressage de placage" n'a été identifiée avec les recherches disponibles pour compléter l'assemblage (cf. Fiche 2 ci-dessus et section 9 ci-dessous). L'adhésif réel du panneau métier n'est pas connu, et sa correspondance Ecoinvent n'a pas été établie dans ce lot.

### 4. Niveau auquel Ecoinvent s'arrête
**Matériau + procédé pour le seul substrat** (MDF ou particules brut, cf. Lot 2B) ; aucune brique identifiée pour le placage fini ni pour un procédé spécifique de collage/pressage. Le statut Ecoinvent de l'adhésif réel n'a pas été établi.

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

**Aucun procédé spécifique de collage/pressage de placage n'a été identifié avec les recherches disponibles**, contrairement au TFL qui bénéficiait du `coating service, melamine impregnated paper`. L'adhésif réel utilisé pour ce type de panneau n'est pas connu et sa correspondance Ecoinvent n'a pas été recherchée en tant que telle dans ce lot.

### 8. Correspondance métier

| Dimension | Niveau |
|---|---|
| Fonction | Aucune pour le produit fini recherché |
| Forme | Aucune |
| Composition/matière | Le substrat seul est connu (MDF/particules, Lot 2B) ; le placage fini n'a pas été identifié ; l'adhésif de collage réel reste à déterminer et sa correspondance Ecoinvent n'a pas été établie |
| Transformation | Aucun procédé spécifique d'assemblage substrat+placage identifié |
| Unité | m³ pour le substrat (Lot 2B) ; le placage fini n'a pas d'unité disponible puisqu'aucun produit fini n'a été identifié |
| Géographie | Celle du substrat seul (Lot 2B — non-QC, cf. rapport correspondant) |

### 9. Représentativité
Produit fonctionnel absent ; composition partiellement connue (substrat seulement, adhésif non caractérisé) ; procédé de collage/pressage non identifié ; géographie limitée au substrat ; aucune donnée primaire identifiée ; bien inspectable.

### 10. VERDICT : **produit absent**

### 11. Briques disponibles

| Brique | Dataset | UUID | Location | Rôle | Limite |
|---|---|---|---|---|---|
| Substrat MDF brut | market for medium density fibreboard (Lot 2B) | eef398de-7420-330d-b894-1440a0afa155 | RoW (copie Europe) | Panneau support plausible | Ne couvre que le substrat ; aucun placage ni collage disponible pour compléter |
| Substrat particules brut | market for particleboard, uncoated (Lot 2B) | 7690ac93-cf92-32dd-b2cf-68e6c7fcf673 | RoW (mélange Europe+Brésil) | idem | idem |

Aucun placage fini ni procédé spécifique de collage/pressage n'a été identifié pour compléter cet assemblage avec les recherches disponibles. L'adhésif réel n'a pas été recherché en tant que produit distinct dans ce lot : sa correspondance Ecoinvent n'a donc pas été établie, ni positivement ni négativement. Contrairement au TFL, cette reconstruction ne peut pas être évaluée dans son ensemble en l'état de ce lot.

### 12. Variables fabricant nécessaires
Essence et grammage du placage ; type d'adhésif de collage réellement utilisé (aucune hypothèse de départ n'est disponible) ; procédé de fabrication (température/pression de pressage) ; substrat réel utilisé (MDF ou particules) ; pertes de production.

### 13. Décision méthodologique provisoire
**Données insuffisantes pour décider.** La reconstruction conceptuelle A/B proposée par le mandat (substrat + placage + adhésif + pressage) ne peut être évaluée que sur sa première brique (le substrat, déjà validé au Lot 2B). Le placage fini et un procédé spécifique de collage/pressage n'ont pas été identifiés avec les recherches disponibles. L'adhésif réel reste à déterminer et sa correspondance Ecoinvent n'a pas été établie dans ce lot — ce point nécessite une donnée fournisseur avant toute recherche Ecoinvent ciblée, non couverte par ce lot.

---

## COMPARAISON AVEC LE TFL (LOT 2B)

| Produit | Surface disponible | Substrat disponible | Produit fini disponible | Procédé disponible | Reconstruction plausible | Lacune principale |
|---|---|---|---|---|---|---|
| **TFL sur MDF/particules (Lot 2B, rappel)** | Oui — `coating, with melamine impregnated paper` (papier déjà imprégné, grammage documenté 302 g/m²/face) | Oui (Lot 2B) | Non | **Oui** — service de revêtement complet et documenté | **Oui, avec réserves documentées** (émissions de pressage exclues, hypothèse d'épaisseur nécessaire) | Émissions de pressage non incluses ; hypothèse d'épaisseur requise |
| **HPL** | Non — aucune feuille stratifiée ni papier imprégné identifiés | Sans objet (le HPL n'a pas de "substrat" au sens panneau — c'est une feuille autoportante) | Non | **Non** — aucune imprégnation ni pressage haute pression identifiés | **Non — aucune brique intermédiaire identifiée pour relier les précurseurs chimiques potentiels au produit** | Aucune chaîne de représentation exploitable identifiée : ni surface ni procédé identifiés, seuls deux précurseurs chimiques isolés trouvés dont la pertinence reste à établir |
| **Placage bois (fini)** | Non — aucune feuille de placage identifiée, seule la grume existe | Sans objet pour le placage lui-même | Non | **Non** — aucun tranchage/déroulage identifié | **Non — la chaîne s'arrête à la grume, plusieurs étapes avant le produit recherché** | Aucune transformation identifiée entre grume et placage fini |
| **Panneau plaqué bois fini** | Non (dépend du placage, non identifié — voir ligne précédente) | Oui (substrat MDF/particules, Lot 2B) | Non | **Non** — aucun procédé spécifique de collage/pressage de placage identifié | **Non — seul le substrat de l'assemblage conceptuel est disponible** | Placage fini et procédé spécifique de collage/pressage non identifiés ; adhésif réel et sa correspondance Ecoinvent à établir |

**Réponse à la question du Lot 2E** : **non, les recherches disponibles ne montrent pas le même type de lacune pour ces trois technologies.** Le TFL est nettement mieux représenté que les trois technologies de ce lot — il dispose d'une brique de surface complète, documentée et directement combinable. Le HPL et le placage bois (fini) sont, d'après les recherches menées, dans une situation plus défavorable : le HPL ne dispose que de précurseurs chimiques isolés sans procédé de liaison identifié, et le placage bois fini ne dispose d'aucune brique identifiée entre la grume et la feuille recherchée. Le panneau plaqué bois fini hérite de cette double lacune (placage + procédé de collage/pressage non identifiés), le substrat restant la seule brique valide ; le statut Ecoinvent de son adhésif réel n'a pas été établi dans ce lot.

---

## PRODUIT ACHETÉ VS OPÉRATION EN ATELIER

**Cas A — panneau acheté déjà plaqué** : Ecoinvent ne permet pas de représenter ce scénario, faute de produit fini (Fiche 3, verdict "produit absent").

**Cas B — panneau plaqué manuellement/localement dans l'entreprise** : Ecoinvent permet de représenter **une partie seulement** de ce scénario — le substrat brut (Fiche 3, brique 1) est disponible et déjà validé au Lot 2B, mais le placage fini et un procédé spécifique de collage/pressage n'ont pas été identifiés avec les recherches disponibles ; l'adhésif réel reste à déterminer et sa correspondance Ecoinvent n'a pas été établie dans ce lot. **Le scénario B n'est donc pas mieux représentable que le scénario A avec les données actuellement disponibles** — la différence entre les deux cas n'est pas une différence de disponibilité de données Ecoinvent, mais une différence de réalité métier (où acheter le produit fini vs le fabriquer soi-même) qu'aucun des deux ne permet actuellement de documenter complètement.

---

## DONNÉES FOURNISSEUR MINIMALES (établies à partir des résultats réels de ce lot)

### HPL
- **Structure du produit (grammage et nombre de couches)** — nécessaire car aucune structure de référence n'a été identifiée dans Ecoinvent ; indispensable.
- **Composition/formulation réelle du HPL** — nécessaire car les datasets identifiés (résine phénolique, papier kraft) ne sont pas reliés au produit ; indispensable pour toute reconstruction future, sans présupposer de répartition entre types de résine.
- **Masse surfacique/épaisseur du HPL fini** — nécessaire pour toute conversion masse/surface future ; indispensable.
- **Procédé de fabrication réel du fournisseur** — souhaitable, pour évaluer si un procédé pertinent pourrait un jour être identifié ailleurs dans Ecoinvent ou une autre base.

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

**1. Ecoinvent possède-t-il un HPL fini utilisable ?** Aucun produit fonctionnel HPL n'a été identifié dans les recherches disponibles (process + flow, toutes variantes terminologiques du mandat) : aucun résultat pertinent après élimination des faux positifs (photovoltaïque, verre, panneau structurel massif), sous réserve des limites de l'outil.

**2. Ecoinvent possède-t-il du placage bois fini ?** Aucun produit fonctionnel identifié dans les recherches disponibles, à tous les niveaux testés (process et flow), pour toutes les variantes terminologiques testées.

**3. Le placage disponible conserve-t-il l'information d'essence ?** Sans objet — aucun placage fini n'a été identifié pour évaluer cette question. Seule la grume en amont conserve nominalement une essence (cf. Lot 2C), déjà démontrée non pertinente pour 3 des 4 essences métier.

**4. Ecoinvent possède-t-il un panneau MDF plaqué bois fini ?** Aucun produit fonctionnel identifié dans les recherches disponibles.

**5. Ecoinvent possède-t-il un panneau de particules plaqué bois fini ?** Aucun produit fonctionnel identifié dans les recherches disponibles — même recherche, même résultat nul pour les deux substrats.

**6. Existe-t-il un procédé de collage/lamination suffisamment pertinent ?** Aucun procédé suffisamment pertinent identifié pour le placage bois véritable avec les recherches disponibles. Le seul procédé de revêtement identifié (`coating, with melamine impregnated paper`) est spécifique au papier mélaminé (TFL, Lot 2B) et ne représente pas un collage de placage bois véritable.

**7. Le panneau plaqué fini est-il mieux représenté que le TFL étudié en 2B ?** Non — c'est l'inverse d'après les recherches menées. Le TFL dispose d'une brique de surface complète et documentée ; le panneau plaqué bois fini ne dispose d'aucune brique de surface ni de procédé de collage/pressage identifiés, seulement du substrat. Le statut Ecoinvent de son adhésif réel n'a pas été établi dans ce lot.

**8. HPL et TFL présentent-ils la même lacune ou des lacunes différentes ?** Des lacunes différentes et de sévérité différente d'après les recherches menées. Le TFL manque seulement du produit fini final (mais dispose de toutes les briques identifiées pour une reconstruction documentée). Le HPL manque du produit fini ET de toute brique de liaison identifiée entre ses deux seuls précurseurs chimiques potentiels — une lacune structurellement plus sévère.

**9. Peut-on représenter proprement le scénario `panneau acheté déjà plaqué` ?** Aucun produit fini identifié dans les recherches disponibles, pour aucun des trois produits de ce lot.

**10. Peut-on représenter séparément `panneau plaqué dans l'entreprise` ?** Partiellement seulement pour le substrat (déjà validé Lot 2B) ; le placage fini et un procédé spécifique de collage/pressage n'ont pas été identifiés avec les recherches disponibles. Le statut Ecoinvent de l'adhésif réel n'a pas été établi dans ce lot.

**11. Quelles données fournisseur sont indispensables pour distinguer les deux scénarios (A vs B) ?** Dans l'état actuel des recherches, cette distinction est **prématurée** — aucun des deux scénarios n'est représentable au-delà du substrat avec les briques identifiées. La question redevient pertinente si une brique de placage/procédé de pressage est identifiée, ou si le statut Ecoinvent de l'adhésif réel est établi.

**12. Quelles sont les principales lacunes Ecoinvent révélées par cette famille ?** (a) Aucune brique de placage bois fini identifiée, à tous les niveaux de transformation testés entre la grume et la feuille. (b) Aucune brique de HPL identifiée au-delà de deux précurseurs chimiques isolés dont le lien avec le produit métier n'a pas été établi. (c) Aucun procédé de collage de placage ni de pressage haute pression identifié avec les recherches disponibles, contrastant avec la disponibilité du service de revêtement mélaminé (TFL) — ce contraste montre que la richesse de la base Ecoinvent sur les surfaces de panneaux, telle qu'observée par ces recherches, est **spécifique à la technologie TFL/mélamine**, pas générale aux technologies de surface du mobilier.

---

## IMPACT SUR LE RÉFÉRENTIEL — informations proposées pour `docs/materiaux-ebenisterie.md`

**Rappel : ce fichier n'est PAS modifié dans ce lot. Les éléments ci-dessous sont proposés pour QC avant intégration ultérieure.**

### Stratifié HPL
- **Ecoinvent** : aucun produit fini, aucune surface, aucun procédé de liaison identifiés avec les recherches disponibles. Deux datasets de précurseurs chimiques isolés (résine phénolique, papier kraft non imprégné) ont été identifiés, sans lien établi entre eux ni avec le produit recherché — ils ne peuvent être considérés que comme des briques amont potentielles.
- **Correspondance** : aucune identifiée.
- **Lacune principale** : aucune chaîne de représentation exploitable identifiée — pas de brique de reconstruction évaluable, contrairement au TFL.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : recherches menées (process + flow, ~15 variantes terminologiques) sans résultat pertinent ; un faux positif plausible ("three layered laminated board") inspecté et rejeté (panneau structurel massif, pas un stratifié décoratif).
- **Recommandation** : ne pas tenter de reconstruction avant l'obtention de données fournisseur sur la composition/formulation réelle et la structure en couches ; envisager une recherche future dans une autre base si le projet en dispose.

### Placage bois
- **Ecoinvent** : aucun produit placage fini identifié à aucun niveau testé ; seule la grume forestière générique (cf. Lot 2C) existe, plusieurs étapes en amont.
- **Correspondance** : aucune identifiée.
- **Lacune principale** : aucune transformation identifiée entre grume et placage fini (tranchage/déroulage non identifié).
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : aucun résultat pertinent identifié par les recherches process + flow disponibles, convergentes sur toutes les variantes testées, cohérent avec les constats déjà faits aux Lots 1, 2B et 2C.
- **Recommandation** : données fournisseur indispensables sur l'essence, le grammage et la méthode de production avant toute tentative de proxy.

### Panneau plaqué bois acheté fini
- **Ecoinvent** : substrat brut (MDF ou particules) disponible et déjà validé (Lot 2B, non-QC) ; placage fini et procédé spécifique de collage/pressage non identifiés avec les recherches disponibles ; adhésif réel et sa correspondance Ecoinvent à établir.
- **Correspondance** : faible (seul le substrat, parmi les composantes conceptuelles de l'assemblage, est disponible).
- **Lacune principale** : produit fini et placage non identifiés ; procédé spécifique de collage/pressage non identifié ; adhésif réel et correspondance Ecoinvent à établir.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : produit fini non identifié ; reconstruction conceptuelle non évaluable dans son ensemble avec les briques actuellement identifiées.
- **Recommandation** : traiter comme un cas d'attente jusqu'à ce que la Fiche 2 (placage) évolue et que le statut Ecoinvent de l'adhésif réel soit établi ; ne pas utiliser le substrat seul comme proxy du panneau fini sans avertissement explicite.

---

## IMPACT SUR LA GRILLE MÉTHODOLOGIQUE

Aucun nouveau critère numéroté n'est ajouté ce tour — les 17 critères stabilisés jusqu'au Lot 2D ont suffi à structurer l'analyse, en particulier :
- **#14 (homonymies)** : confirmée avec force par la pollution du terme "laminate" (photovoltaïque, verre feuilleté, bois structurel) — le cas le plus massif de faux positifs rencontré depuis le début du diagnostic.
- **#15 (correspondance réelle au-delà du nom)** : confirmée par l'inspection et le rejet justifié de "three layered laminated board".
- **#17 (inspection des flux de sortie pour détecter une calibration matière)** : appliquée mais sans révéler de calibration cachée ici (contrairement au calandrage PVC du Lot 2D) — utile de noter que ce critère peut aussi conclure par la négative (absence de calibration détectable), ce qui est en soi une information.

**Un phénomène nouveau, mais qui ne justifie pas un nouveau critère isolé** : ce lot montre que la richesse de représentation d'Ecoinvent pour les technologies de surface de panneaux n'est **pas uniforme entre technologies concurrentes visant la même fonction** (TFL vs HPL vs placage) — alors que les Lots précédents avaient surtout révélé des variations **géographiques** (même technologie, représentativité différente selon la région) ou de **profondeur de chaîne** (même essence, disparaissant à un stade donné). Ce constat est mieux compris comme une **application** du critère #7 (spécificité produit) à un niveau comparatif entre produits concurrents, plutôt que comme un critère nouveau.

---

*Fin du rapport Lot 2E. Aucun dataset openLCA modifié. Aucune modification Git. Aucun proxy construit. `docs/materiaux-ebenisterie.md` n'a pas été modifié. Seuls les 3 produits métier demandés ont été traités.*
