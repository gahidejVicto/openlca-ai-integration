# Diagnostic Ecoinvent — Lot 2G
## Données transversales de fabrication (10 objets)

Projet ACV mobilier québécois — Base Ecoinvent 3.11, système Cutoff, via openLCA/MCP.

Portée stricte : 10 objets (6 P1 + 4 P2). Aucun dataset modifié, aucun proxy construit, `docs/materiaux-ebenisterie.md` non modifié, aucune modification Git.

---

## OBJET 1 — ÉLECTRICITÉ D'ATELIER (P1) — réinspection prioritaire

### 1. Objet métier
Électricité consommée par l'atelier (machines, éclairage, séchage, etc.).

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| market for electricity, medium voltage | search_processes | **218 résultats** (nombre légèrement différent des 223 relevés au Lot 1 — variation normale selon la formulation exacte de la requête, sans incidence sur la conclusion) | Tous identiques par nom, aucune géographie retournée par la recherche |
| electricity medium voltage Quebec / electricity Quebec | search_processes | 0 | Confirme que la géographie n'est jamais dans le nom |
| Québec (avec accent) | search_processes | 0 | Idem, testé pour éliminer une hypothèse d'encodage |
| electricity, medium voltage (flow) | search_flows | 4 résultats, tous génériques (`electricity, medium voltage`, `…label-certified`, `…aluminium industry`, `transmission network, …`) — **aucune géographie au niveau flow non plus** | Confirme la limite structurelle au niveau flow |

**Tentative de méthode alternative (nouvelle ce tour)** : vérification de l'hypothèse qu'un tri stable (p.ex. alphabétique par géographie) permettrait de repérer le Québec parmi un petit échantillon, comme cela avait semblé fonctionner par hasard au Lot 2A/2C (où "Prince Edward Island" avait été trouvé dans un premier lot de résultats). **Cette hypothèse est infirmée ce tour** : une nouvelle recherche du même nom exact retourne un ensemble différent de 20 identifiants sur un total désormais compté à 218 (vs 223 précédemment), sans chevauchement avec l'échantillon où "Prince Edward Island" avait été repéré — l'ordre de retour n'est donc pas stable ni alphabétique, et la découverte précédente relevait du hasard, pas d'une méthode reproductible.

**Autres outils MCP disponibles considérés et écartés** :
- `extract_model` sur le dossier catégorie complet (« Electric power generation, transmission and distribution ») — a échoué par timeout au Lot 2A ; non retenté ce tour car le dossier n'a pas changé de taille et l'échec serait identique.
- `get_system_links` / `contribution_analysis` / `calculate` — nécessitent un système de produits ; `database_info` confirme `product_systems: 0` dans la base actuelle.

### Réponse aux 10 questions posées

1. **Peut-on maintenant isoler un dataset CA-QC ?** Non.
2. **UUID ?** Non déterminé.
3. **Unité ?** Non déterminée pour l'instance CA-QC spécifiquement (le flow générique `electricity, medium voltage` est en MJ ; les exchanges observés dans d'autres process utilisent kWh comme unité d'affichage — cohérence à vérifier si le dataset est un jour isolé).
4. **S'agit-il d'un market de moyenne tension pertinent pour un atelier ?** Par construction du nom ("medium voltage"), ce type de dataset est en général celui utilisé pour une consommation industrielle/commerciale de taille PME — **pertinent en principe**, mais ceci reste une inférence sur le type de dataset, pas une confirmation pour l'instance CA-QC.
5-7. **Mix, structure, part réellement québécoise ?** Non déterminable sans isoler le dataset.
8. **Données primaires québécoises ?** Non vérifiable.
9. **Date/source ?** Non vérifiable.
10. **Directement utilisable pour un atelier québécois ?** **Aucune conclusion possible** — ni positive ni négative. Le résultat démontré est uniquement que l'instance CA-QC n'a pas pu être isolée avec les méthodes d'interrogation MCP disponibles ; ceci n'est ni une lacune Ecoinvent démontrée, ni une confirmation de l'existence du dataset, mais une **limite de l'outil d'interrogation MCP disponible**, à documenter comme telle, pas comme absence de contenu dans Ecoinvent.

### Verdict : **Non évalué — limitation d'accès MCP**

### Statut référentiel proposé
🟡 À valider

### Action
Obtenir un moyen d'accès permettant de filtrer/inspecter directement les processus par géographie avant de conclure.

### Lacune_Ecoinvent
Aucune lacune de contenu démontrée — limite de l'outil de recherche MCP (recherche par nom uniquement, aucun filtre géographique, aucune extraction de masse possible pour ce dossier sans timeout).

### Donnee_entreprise_manquante
Consommation électrique réelle (kWh) de l'atelier, par période si disponible ; à ce stade sans objet tant que le dataset lui-même n'est pas isolé.

---

## OBJET 2 — TRANSPORT ENTRANT (P1)

### 1. Objet métier
Transport des matériaux/composants depuis les fournisseurs jusqu'à l'atelier.

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| transport, freight, lorry | search_processes | **146 résultats** — grande famille par classe EURO (3 à 6), classe de poids (3.5-7.5t, 7.5-16t, 16-32t), et variantes réfrigérées (non pertinentes) | Confirmé riche |
| market for transport, freight, lorry, unspecified | search_processes | 9 résultats (1 market + 8 process sources par classe EURO) | **Candidat retenu** |

### 3. Meilleur candidat

| Champ | Valeur |
|---|---|
| Dataset | `market for transport, freight, lorry, unspecified` |
| UUID | `49eb6ae0-86d7-3674-89b9-566267648ba9` |
| Flow | transport, freight, lorry, unspecified |
| Unité | **t·km** (tonne-kilomètre) |
| Location | **Global** |

### 4. Ce que représente réellement le dataset
Moyenne pondérée de plusieurs classes d'émission EURO (principalement EURO3 et EURO4, part moindre d'EURO5/6) — <cite>reflète un mix de flotte, sans distinction de classe de poids ni de région</cite> (fait déduit directement des parts observées dans les exchanges : EURO3 ≈ 32%+13%=45%, EURO4 ≈ 11%+28%=39%, EURO5 ≈ 10%+4%=14%, EURO6 ≈ 2%). Le dataset combine plusieurs classes d'émission EURO ; sa représentativité du parc routier québécois/nord-américain n'a pas été établie dans ce lot — la documentation inspectée ne précise pas explicitement une géographie de flotte. Il existe aussi des datasets par classe de poids spécifique (3.5-7.5t, 7.5-16t, 16-32t) si une classe de véhicule précise doit être choisie plutôt que la moyenne "unspecified".

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Forte (service de transport routier de marchandises) |
| Technologie | Moyenne (combine plusieurs classes d'émission EURO3-6 ; représentativité du parc nord-américain non établie dans ce lot) |
| Unité | Forte (t·km, standard et directement utilisable) |
| Géographie | Faible à moyenne (Location Global ; représentativité géographique québécoise/nord-américaine non établie dans ce lot) |

### 6. Lacune Ecoinvent
Le dataset "unspecified" combine plusieurs classes d'émission EURO ; sa représentativité technologique/géographique nord-américaine n'a pas été établie dans ce lot — **incertitude de correspondance technologique/géographique**, pas une absence de dataset.

### 7. Données entreprise manquantes
Distance fournisseur → atelier (par fournisseur ou moyenne) ; masse transportée ; éventuellement classe de véhicule si connue (permettrait de choisir un dataset plus spécifique que "unspecified") ; taux de chargement/retour à vide (déjà incorporé dans la moyenne du marché, mais un choix plus spécifique nécessiterait cette donnée séparément).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise, sous réserve de validation de la représentativité technologique/géographique**

### Statut référentiel proposé
🟡 À valider

### 10. Action recommandée
Conserver ce dataset comme candidat par défaut ; demander à l'entreprise les distances réelles par fournisseur principal ; valider la représentativité technologique/géographique avant adoption définitive.

---

## OBJET 3 — TRANSPORT SORTANT DU MEUBLE (P1)

### 1. Objet métier
Transport du meuble fini de l'atelier vers le client/distributeur.

### 2. Recherche Ecoinvent
Même famille que l'Objet 2 — aucune recherche distincte n'a révélé de dataset spécifique à la "livraison de meuble fini" par opposition à un "transport de matériaux" : Ecoinvent modélise le transport par **service générique de fret**, indépendamment de la nature de la marchandise transportée (le t·km ne distingue pas mobilier vs matière première).

### 3. Meilleur candidat
Identique à l'Objet 2 : `market for transport, freight, lorry, unspecified`, UUID `49eb6ae0-86d7-3674-89b9-566267648ba9`, ou l'une des classes de poids spécifiques si la taille du véhicule de livraison est connue et distincte de celle du transport entrant.

### 4. Ce que représente réellement le dataset
Identique à l'Objet 2 — **aucune différence structurelle Ecoinvent entre transport entrant et sortant** ; la distinction métier (véhicule dédié, tournée de livraison, taux de chargement différent pour du mobilier volumineux mais léger) est **entièrement une question de paramétrage**, pas de choix de dataset différent.

### 5. Correspondance
Identique à l'Objet 2.

### 6. Lacune Ecoinvent
Aucune lacune distincte de l'Objet 2. **Point d'attention méthodologique** : le mobilier fini peut présenter des contraintes de chargement différentes des matériaux entrants (rapport masse/volume potentiellement différent — planches denses vs meuble volumineux et léger). L'incidence du volume et du taux de remplissage devra être évaluée lors du choix et du paramétrage du modèle de transport ; aucune méthode de correction n'est prescrite à ce stade.

### 7. Données entreprise manquantes
Distance atelier → client/distributeur ; masse du/des meuble(s) transporté(s) ; **taux de chargement réel du véhicule si le volume est le facteur limitant plutôt que la masse** (donnée spécifique à ce sens de transport, distincte de l'Objet 2).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise, sous réserve de validation de la représentativité technologique/géographique**

### Statut référentiel proposé
🟡 À valider

### 10. Action recommandée
Ne pas réutiliser aveuglément le même taux de chargement que pour le transport entrant ; demander spécifiquement le mode de livraison (tournée propre, transporteur, taux de remplissage typique) ; valider la représentativité technologique/géographique avant adoption définitive.

---

## OBJET 4 — CHUTES DE BOIS MASSIF (P1)

### 1. Objet métier
Chutes de bois massif générées en fabrication (délignures, retailles).

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| waste wood | search_flows | 3 résultats : `waste wood, untreated`, `waste wood, post-consumer`, `waste wood pole, chrome preserved` | `waste wood, untreated` retenu ; les deux autres écartés (post-consommation = contexte différent ; poteau traité au chrome = non pertinent) |
| treatment waste wood | (déjà documenté Lot 1/2C) | Plusieurs scénarios : décharge sanitaire/non sanitaire, incinération avec/sans valorisation énergétique | Confirmé disponible |

### 3. Meilleur candidat

| Champ | Valeur |
|---|---|
| Flow | `waste wood, untreated` |
| UUID | `6f2eb438-cde2-4d07-a770-d023a988a9c4` |
| Unité | kg |
| Traitements disponibles | Décharge sanitaire, décharge non sanitaire, incinération municipale avec/sans récupération d'énergie (déjà documentés au Lot 1) |

### 4. Ce que représente réellement le dataset
Le flow est explicitement nommé `waste wood, untreated`. Il constitue un candidat fonctionnellement pertinent pour des chutes de bois massif brut, mais la portée exacte de « untreated » (revêtement, colle, traitement chimique) ne doit pas être élargie au-delà de la documentation inspectée.

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Forte |
| Technologie | Moyenne (traitements de type européen : décharge/incinération) |
| Unité | Forte (kg) |
| Géographie | Faible (paramètres européens de décharge/incinération, non vérifiés pour le Québec) |

### 6. Lacune Ecoinvent
Aucune lacune majeure identifiée à ce stade pour le flux lui-même ; les traitements disponibles reposent sur des paramètres européens (taux de méthanisation en décharge, technologie d'incinération) potentiellement différents des filières québécoises.

### 7. Données entreprise manquantes
Répartition réelle entre décharge/incinération/valorisation (aucune répartition supposée, conformément au Lot 1) ; quantité de chutes générées.

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise, sous réserve de validation de la représentativité québécoise des traitements de fin de vie (décharge/incinération)**

### Statut référentiel proposé
🟡 À valider (la représentativité québécoise des traitements n'est pas établie)

### 10. Action recommandée
Conserver comme candidat ; demander à l'entreprise sa filière réelle de fin de vie pour les chutes de bois massif ; valider la représentativité des traitements disponibles.

---

## OBJET 5 — CHUTES DE PANNEAUX (P1)

### 1. Objet métier
Chutes de panneaux (particules/MDF) générées en fabrication — contiennent résines et colles internes.

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| waste particle board / waste particleboard | search_flows | 0 (les deux) | Aucun flow dédié aux panneaux de particules |
| waste fibreboard | search_flows | **1 résultat trouvé** : `waste fibreboard` | **Inspecté et rejeté — voir ci-dessous** |
| waste MDF / waste wood composite / waste wood coated | search_flows | 0 (toutes) | — |

**Inspection du candidat "waste fibreboard" (par prudence, conformément au critère #15 — correspondance réelle au-delà du nom) :**

UUID `73059859-50e6-4bfb-b729-c9da6ed34f9d` ; traitement associé `treatment of waste fibreboard, collection for final disposal` (UUID `7fa28bdc-7551-3157-a504-209c9e24fb70`, location Rest-of-World). **Fait Ecoinvent** : <cite>"The waste contains 0.925kg untreated wood ... and 0.075kg polyurethane"</cite>. Le candidat « waste fibreboard » inspecté présente une composition (bois + polyuréthane, pas de résine urée/mélamine-formaldéhyde) qui ne correspond pas aux panneaux métier caractérisés dans les Lots précédents (liants UF/MF observés aux Lots 2B/2C). Il n'est donc pas retenu comme correspondance directe, malgré la correspondance de nom.

### 3. Meilleur candidat
Aucun flow de déchet spécifique aux panneaux de mobilier identifié. `waste wood, untreated` (déjà utilisé pour l'Objet 4) pourrait constituer un proxy candidat à évaluer, mais sa pertinence est limitée car il ne représente pas explicitement la composition résineuse (UF/MF) ni un éventuel revêtement de surface des panneaux métier.

### 4. Ce que représente réellement le dataset
Le seul flow nommé de façon proche ("waste fibreboard") représente un produit à composition différente (bois + PU) du panneau de mobilier réel. Aucun autre candidat n'a été trouvé.

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Faible (aucun flow calibré sur la composition réelle d'un panneau UF/MF) |
| Technologie | Faible |
| Unité | kg (par défaut, via le proxy générique) |
| Géographie | Faible |

### 6. Lacune Ecoinvent
Aucun flow de déchet suffisamment représentatif des panneaux de mobilier étudiés n'a été identifié avec les méthodes d'interrogation disponibles dans le Lot 2G — le seul candidat nominal (`waste fibreboard`) s'est révélé, après inspection, présenter une composition différente de celle des panneaux métier.

### 7. Données entreprise manquantes
Quantité de chutes de panneaux ; répartition entre destinations de fin de vie (comme pour l'Objet 4, non supposée).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **Proxy candidat à évaluer** (`waste wood, untreated` pourrait servir de proxy, mais n'a pas été construit ni validé dans ce lot ; sa pertinence est limitée car il ne reflète pas la composition résineuse des panneaux)

### Statut référentiel proposé
🟠 À adapter

### 10. Action recommandée
Évaluer `waste wood, untreated` comme proxy candidat pour les panneaux, en documentant explicitement la limite (résines/colles internes du panneau non reflétées dans un flux "untreated") ; le proxy n'a pas été construit dans ce lot.

---

## OBJET 6 — SCIURES / POUSSIÈRES D'USINAGE (P1)

### 1. Objet métier
Sciures et poussières de sciage/ponçage/usinage.

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| sawdust (un seul mot) | search_flows | **0** | Absence apparente |
| saw dust (deux mots) | search_flows | **2 résultats** : `saw dust, loose, wet, measured as dry mass` et `saw dust, wet, measured as dry mass` | **Trouvés — nuance lexicale importante (Ecoinvent utilise "saw dust" en deux mots)** |
| waste, wood, sawdust | search_flows | 0 | Aucun flow "déchet de sciure" dédié |

### 3. Meilleur candidat

| Champ | Valeur |
|---|---|
| Flow | `saw dust, wet, measured as dry mass` |
| Catégorie | Manufacture of wood and of products of wood and cork — Sawmilling and planing of wood |
| Type de flow | **PRODUCT_FLOW** (pas un waste flow) |
| Unité | kg |

### 4. Ce que représente réellement le dataset
**Fait déterminant** : les flows `saw dust` identifiés dans ce lot sont de type **PRODUCT_FLOW** (co-produit commercialisable, utilisé comme intrant dans la production de particleboard/MDF et comme combustible de séchoir, observé aux Lots 2A-2C). Les recherches effectuées dans le Lot 2G ont identifié des flows "saw dust" de type PRODUCT_FLOW, mais aucun flow de déchet de sciure suffisamment pertinent n'a été identifié avec les termes recherchés.

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Moyenne — correspond si la sciure de l'atelier est valorisée (vendue/donnée pour un usage matière ou énergie) ; **ne correspond pas** si elle est mise en décharge, faute de flow "déchet de sciure" dédié |
| Technologie | Sans objet |
| Unité | kg |
| Géographie | Sans objet (flow générique, pas de production geo-spécifique au niveau du flow lui-même) |

### 6. Lacune Ecoinvent
Aucun flow de déchet de sciure suffisamment pertinent n'a été identifié avec les recherches effectuées dans le Lot 2G — si l'atelier ne valorise pas sa sciure, un recours au générique `waste wood, untreated` (Objet 4) pourrait être envisagé comme proxy candidat, avec la même réserve que pour les chutes de panneaux si la sciure provient en partie de panneaux.

### 7. Données entreprise manquantes
**Distinction essentielle, conformément à la mise en garde du mandat** : la quantité de poussière **captée par aspiration** n'est pas automatiquement une émission atmosphérique — il faut savoir : (a) la quantité totale générée, (b) la part captée vs émise directement à l'air, (c) la destination de la part captée (vente/valorisation énergétique interne vs mise en décharge), (d) si un mélange sciure de bois massif / poussière de panneaux est collecté ensemble ou séparément (pertinent étant donné la lacune de l'Objet 5).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise** (si valorisée) / **proxy candidat à évaluer** (si mise en décharge, via le générique bois)

### Statut référentiel proposé
🟡 À valider

### 10. Action recommandée
Clarifier avec l'entreprise si la sciure/poussière captée est vendue, valorisée énergétiquement sur place, ou mise en décharge — le choix de brique Ecoinvent en dépend entièrement.

---

## OBJET 7 — GAZ NATUREL / CHALEUR (P2)

### 1. Objet métier
Gaz naturel consommé pour le chauffage/procédé, si l'atelier en utilise.

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| heat, central or small-scale, natural gas | search_processes | 38 résultats au total (10 montrés) — famille riche incluant chaudières <100kW, cogénération, et marchés | Candidat de marché retenu |

### 3. Meilleur candidat

| Champ | Valeur |
|---|---|
| Dataset | `market for heat, central or small-scale, natural gas` |
| UUID | `b4a33a9d-da08-3d5b-a883-e22acd9e7415` |
| Unité | MJ (chaleur livrée) |
| Location | **Europe without Switzerland** |

### 4. Ce que représente réellement le dataset
**Fait Ecoinvent** : <cite>"The shares of heat supplying activities with combined heat and power (CHP) plants and pure heat power plants have been estimated ... The shares are assumed to amount to 25% heat from CHP plants and 75% heat from heat plants."</cite> — mix de chaudières <100kW (échelle pertinente pour un atelier) et de petites installations de cogénération, **mais explicitement européen**. **Cette recherche n'a pas permis de confirmer l'existence ou l'absence d'une variante nord-américaine/canadienne** parmi les 38 résultats totaux (seuls 10 ont été inspectés par nom) — à approfondir si ce flux est réellement utilisé par l'entreprise.

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Forte (chaleur de chaudière à petite échelle, cohérent avec un atelier) |
| Technologie | Moyenne (mix chaudière/cogénération européen) |
| Unité | Forte (MJ, standard) |
| Géographie | Faible pour la variante identifiée (Europe sans Suisse) ; **non déterminé** si une variante nord-américaine existe parmi les résultats non inspectés |

### 6. Lacune Ecoinvent
**Incertitude de correspondance géographique non résolue à ce stade** (pas une absence confirmée) — 28 des 38 résultats n'ont pas été inspectés individuellement par manque de temps dans ce lot.

### 7. Données entreprise manquantes
**Préalable à toute action** : confirmer si l'atelier utilise réellement du gaz naturel (le mandat précise explicitement de ne pas le supposer). Si oui : consommation mesurée (m³ ou kWh/GJ de gaz, ou chaleur livrée si connue directement).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **À valider — recherche géographique incomplète** (dataset européen présenté comme candidat inspecté, non retenu de façon définitive ; 28 des 38 résultats non inspectés)

### Statut référentiel proposé
🟡 À valider

### 10. Action recommandée
D'abord confirmer l'usage réel de gaz naturel par l'entreprise ; si confirmé, compléter ultérieurement l'inspection des variantes géographiques parmi les 38 résultats avec openLCA/MCP avant de choisir un dataset définitif.

---

## OBJET 8 — EAU DE PROCÉDÉ / NETTOYAGE (P2)

### 1. Objet métier
Eau utilisée pour le nettoyage/procédé en atelier.

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| market for tap water | search_processes | **4 résultats au total — 3 des 4 inspectés** | Ensemble restreint, presque intégralement inspecté |

**Géographies confirmées par inspection directe** : Suisse (`3e419265…`), Europe sans Suisse (`24690c75…`), Rest-of-World (`882c7e14…`). Le 4ᵉ (`3ab1597e…`) n'a pas été inspecté individuellement ce tour, probablement un marché global agrégé étant donné le nombre total de 4 correspondant au schéma habituel (CH / Europe sans CH / RoW / Global).

**Aucune des trois géographies inspectées n'est le Canada ou le Québec.**

### 3. Meilleur candidat

| Champ | Valeur |
|---|---|
| Dataset | `market for tap water`, variante Rest-of-World (candidat inspecté) |
| UUID | `882c7e14-18f8-3eb4-8638-b41826090117` |
| Unité | kg |
| Location | Rest-of-World |

### 4. Ce que représente réellement le dataset
**Fait Ecoinvent, explicite** : <cite>"Since tap water is mainly produced and distributed at a regional level, regional markets should be prefered, when relevant."</cite> — Ecoinvent lui-même signale qu'un marché régional serait préférable. Aucune variante nord-américaine n'a été identifiée parmi les 3 variantes inspectées (Suisse, Europe sans Suisse, Rest-of-World) ; une quatrième variante reste non inspectée. Le RoW constitue un **candidat inspecté**, mais **explicitement sous-optimal selon Ecoinvent lui-même** au regard de la préférence pour un marché régional.

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Forte |
| Technologie | Moyenne (mix de traitement RoW incluant du dessalement d'eau de mer — non pertinent pour le Québec, dilué dans une moyenne mondiale) |
| Unité | Forte (kg) |
| Géographie | **Faible parmi les variantes inspectées** (3 des 4 variantes existantes inspectées ; aucune nord-américaine parmi celles-ci ; 1 variante non inspectée) |

### 6. Lacune Ecoinvent
Aucune variante nord-américaine n'a été identifiée parmi les 3 variantes inspectées (Suisse, Europe sans Suisse, Rest-of-World) ; une quatrième variante (`3ab1597e…`) reste non inspectée. Il ne s'agit donc pas d'une absence confirmée de marché nord-américain, mais d'un résultat obtenu sur une recherche géographique incomplète.

### 7. Données entreprise manquantes
Consommation d'eau réelle (m³ ou kg) pour le procédé/nettoyage.

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **À valider — recherche géographique incomplète** (candidat inspecté : `market for tap water`, Rest-of-World ; 1 des 4 variantes existantes non inspectée)

### Statut référentiel proposé
🟡 À valider

### 10. Action recommandée
Retenir la variante RoW comme candidat inspecté ; compléter ultérieurement l'inspection de la 4ᵉ variante avant de choisir le dataset définitif. Aucune recherche supplémentaire n'a été effectuée dans ce lot.

---

## OBJET 9 — EAUX USÉES (P2)

### 1. Objet métier
Eaux usées générées par l'atelier (nettoyage, procédé).

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| market for wastewater, average | search_processes | 3 résultats (1 inspecté : Rest-of-World) | Ensemble restreint |
| treatment of wastewater, average | search_processes | 12 résultats (plusieurs capacités de station, non toutes inspectées) | Confirme une famille technique riche mais sans indice géographique nord-américain repéré |

### 3. Meilleur candidat

| Champ | Valeur |
|---|---|
| Dataset | `market for wastewater, average` |
| UUID | `7a2be1f9-6dca-35f5-a39f-1d64c9e22eae` |
| Unité | **m³** |
| Location | Rest-of-World |

### 4. Ce que représente réellement le dataset
Traitement municipal moyen, composition non spécifiée au-delà de la mention "average" — mix de stations de différentes capacités (1,6E8 à 4,7E10 litres/an).

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Forte (traitement municipal, pertinent si l'atelier rejette au réseau municipal) |
| Technologie | Moyenne (capacités de station européennes) |
| Unité | Forte (m³) |
| Géographie | Faible (seule la variante RoW a été inspectée ; les 2 autres non vérifiées individuellement ce tour, mais aucune ne porte d'indice nominal nord-américain) |

### 6. Lacune Ecoinvent
Aucune variante nord-américaine identifiée parmi les résultats inspectés — à confirmer en vérifiant les 2 variantes non inspectées, mais convergent avec le constat de l'Objet 8 (eau potable).

### 7. Données entreprise manquantes
**Question centrale posée par le mandat** : la présence éventuelle de produits de finition/colles dans les eaux usées change-t-elle le choix du dataset ? **Réponse fondée sur l'observation** : le dataset "average" ne documente pas de composition détaillée accessible dans les champs consultés — Ecoinvent semble demander un **volume/masse** plutôt qu'une composition chimique détaillée pour ce type de traitement générique. Si les eaux usées de l'atelier sont significativement contaminées (résidus de colle/finition), un traitement de type industriel spécifique (plutôt que municipal "average") pourrait être plus approprié — **à valider**, cette distinction n'a pas pu être testée plus finement dans le temps disponible.

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **À valider — recherche géographique/fonctionnelle partielle** (candidat inspecté : `market for wastewater, average`, Rest-of-World ; 1 des 3 variantes existantes inspectée)

### Statut référentiel proposé
🟡 À valider

### 10. Action recommandée
Clarifier si l'atelier rejette au réseau municipal (dataset "average" pertinent) ou traite lui-même des eaux contaminées (voir Objet 10) ; compléter l'inspection géographique des 2 variantes non vérifiées. Aucune recherche supplémentaire n'a été effectuée dans ce lot.

---

## OBJET 10 — RÉSIDUS CONTAMINÉS (P2)

### 1. Objet métier
Résidus solides/liquides contaminés par colles, finitions, solvants, chiffons.

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| hazardous waste | search_flows | 5 résultats : `hazardous waste incineration facility` (infrastructure), `waste paint, collection for hazardous waste incineration`, `process-specific burdens, hazardous waste incineration plant`, `hazardous waste, for underground deposit`, `hazardous waste, for incineration` | **`waste paint`… le plus spécifique et directement pertinent pour les résidus de finition** |
| waste solvent / waste adhesive | search_flows | 0 (les deux) | Aucun flow dédié |
| spent solvent (variante) | search_flows | 1 résultat : `spent solvent mixture`, catégorisé sous "Manufacture of cement, lime and plaster" | **Contexte de valorisation en combustible de four à ciment, pas un traitement générique de solvant — pertinence incertaine, non retenu comme candidat principal** |

### 3. Meilleur candidat

| Champ | Valeur |
|---|---|
| Dataset | `treatment of waste paint, hazardous waste incineration` |
| UUID | `d39c3e17-6987-3ca0-80c1-5121f4806469` |
| Flow | waste paint |
| Unité | kg |
| Location | Suisse |

### 4. Ce que représente réellement le dataset
**Fait Ecoinvent, très détaillé** : composition documentée (<cite>"Inventoried waste contains 100% paint (remains)"</cite>), pouvoir calorifique 10,86 MJ/kg, teneurs en métaux lourds (Pb, Cd, Cr, Zn, Hg, etc.) toutes chiffrées, récupération d'énergie en incinération (17,11 MJ électrique + 1,27 MJ thermique par kg), résidus solidifiés au ciment envoyés en décharge (0,0296 kg/kg). C'est un dataset **riche et spécifique** pour un résidu de peinture/finition pur — mais ne couvre que la "peinture" nommément, pas explicitement les colles ou solvants.

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Forte pour les résidus de finition (peinture/vernis) ; **inconnue** pour colles et solvants isolés (aucun flow dédié trouvé) |
| Technologie | Moyenne (incinération de déchets dangereux, technologie suisse) |
| Unité | Forte (kg) |
| Géographie | Faible (Suisse) |

### 6. Lacune Ecoinvent
Aucun flow suffisamment spécifique aux colles, solvants ou chiffons contaminés n'a été identifié avec les recherches effectuées dans le Lot 2G — seule la catégorie "peinture" dispose d'un flow spécifique identifié. Pour les autres types de résidus contaminés, seuls les flux génériques `hazardous waste, for incineration` / `hazardous waste, for underground deposit` ont été identifiés, sans composition spécifique documentée.

### 7. Données entreprise manquantes
Nature exacte des résidus (peinture/vernis vs solvant vs colle vs chiffons) — **déterminante pour le choix du flow**, puisque seule la catégorie peinture est bien représentée ; quantité générée ; filière de collecte réelle (incinération dangereuse confirmée ou autre).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise** pour les résidus de peinture/finition (candidat spécifique identifié) ; **proxy à adapter** (flux génériques) pour colles/solvants/chiffons (correspondance non établie)

### Statut référentiel proposé
🟠 À adapter — en distinguant explicitement peinture/finition (candidat spécifique identifié) des autres résidus (correspondance non établie)

### 10. Action recommandée
Distinguer, dans la collecte de données entreprise, peinture/finition (bien couverte) des autres résidus contaminés (colles, solvants, chiffons — couverture générique seulement).

---

## SYNTHÈSE DES 10 OBJETS

| Objet_metier | Priorite | Dataset_Ecoinvent | UUID | Unite | Location | Correspondance | Geographie_QC | Donnees_primaires_QC | Verdict | Lacune_Ecoinvent | Donnee_entreprise_manquante | Action_recommandee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Électricité d'atelier | P1 | market for electricity, medium voltage (non isolé pour CA-QC) | Non déterminé | Non déterminée pour l'instance CA-QC | CA-QC visé, non isolé | Inconnue | Non déterminée | Aucune identifiée | Non évalué — limitation d'accès MCP | Aucune démontrée — limite d'outil MCP | Consommation kWh réelle | Rechercher accès géographique direct hors MCP |
| Transport entrant | P1 | market for transport, freight, lorry, unspecified (candidat inspecté) | 49eb6ae0-86d7-3674-89b9-566267648ba9 | t·km | Global | Moyenne à forte | Faible (non établie) | Aucune identifiée | Utilisable avec paramétrage entreprise, sous réserve de validation de la représentativité technologique/géographique | Dataset combine plusieurs classes EURO3-6 ; représentativité nord-américaine non établie dans ce lot | Distance fournisseur→atelier, masse | Conserver comme candidat, demander distances réelles, valider la représentativité |
| Transport sortant | P1 | market for transport, freight, lorry, unspecified (même dataset candidat, paramétrage distinct) | 49eb6ae0-86d7-3674-89b9-566267648ba9 | t·km | Global | Moyenne à forte | Faible (non établie) | Aucune identifiée | Utilisable avec paramétrage entreprise, sous réserve de validation de la représentativité technologique/géographique | Idem transport entrant ; incidence du volume/taux de remplissage à évaluer lors du paramétrage | Distance atelier→client, masse, informations de chargement si disponibles | Conserver comme candidat, ne pas réutiliser le taux de chargement de l'entrant, valider la représentativité |
| Chutes de bois massif | P1 | waste wood, untreated + traitements (landfill/incinération) | 6f2eb438-cde2-4d07-a770-d023a988a9c4 | kg | Europe/RoW selon variante | Moyenne | Faible (traitements non validés pour le Québec) | Aucune identifiée | Utilisable avec paramétrage entreprise, sous réserve de validation de la représentativité québécoise des traitements | Paramètres européens de décharge/incinération, représentativité québécoise non établie | Répartition réelle des destinations | Conserver comme candidat, demander la répartition réelle, valider la représentativité des traitements |
| Chutes de panneaux | P1 | Aucun flow suffisamment représentatif identifié — waste wood, untreated envisagé comme proxy candidat | 6f2eb438-cde2-4d07-a770-d023a988a9c4 (proxy candidat, non construit) | kg | Europe/RoW | Faible | Faible | Aucune identifiée | Proxy candidat à évaluer | Aucun flow suffisamment représentatif de la composition résineuse (UF/MF) d'un panneau identifié avec les recherches du Lot 2G | Quantité, répartition des destinations | Évaluer le proxy candidat en documentant la limite ; proxy non construit dans ce lot |
| Sciures/poussières | P1 | saw dust, wet/loose, measured as dry mass (PRODUCT_FLOW, co-produit) | a514c9f2-0d4d-4ce2-809b-de4c29e74709 / dfaef357-a79e-4846-aabc-848b1ab59fbb | kg | Générique | Moyenne | Sans objet | Aucune identifiée | Utilisable (si valorisée) / Proxy candidat à évaluer (si mise en décharge) | Aucun flow de déchet de sciure suffisamment pertinent identifié avec les recherches du Lot 2G | Part captée/valorisée vs mise en décharge | Clarifier la destination réelle avec l'entreprise |
| Gaz naturel/chaleur | P2 | market for heat, central or small-scale, natural gas (candidat inspecté) | b4a33a9d-da08-3d5b-a883-e22acd9e7415 | MJ | Europe without Switzerland | Moyenne | Non déterminée (28/38 résultats non inspectés) | Aucune identifiée | À valider — recherche géographique incomplète | Correspondance géographique non exhaustivement vérifiée (28/38 résultats non inspectés) | Confirmer l'usage réel de gaz + consommation mesurée | Compléter la recherche géographique avant de choisir un dataset définitif |
| Eau de procédé | P2 | market for tap water (candidat inspecté) | 882c7e14-18f8-3eb4-8638-b41826090117 | kg | Rest-of-World | Moyenne | Faible parmi les variantes inspectées (3/4 inspectées, aucune nord-américaine) | Aucune identifiée | À valider — recherche géographique incomplète | Aucune variante nord-américaine identifiée parmi les 3 variantes inspectées ; 1 variante non inspectée | Consommation d'eau réelle | Retenir RoW comme candidat inspecté, compléter l'inspection de la 4ᵉ variante |
| Eaux usées | P2 | market for wastewater, average (candidat inspecté) | 7a2be1f9-6dca-35f5-a39f-1d64c9e22eae | m³ | Rest-of-World | Moyenne | Faible (1/3 variantes inspectée) | Aucune identifiée | À valider — recherche géographique/fonctionnelle partielle | Composition détaillée non documentée dans les champs consultés ; 2/3 variantes non inspectées | Nature du rejet (municipal vs contaminé) | Clarifier le mode de rejet réel, compléter l'inspection des variantes restantes |
| Résidus contaminés | P2 | treatment of waste paint, hazardous waste incineration (peinture) ; flux génériques hazardous waste (autres, non spécifiques) | d39c3e17-6987-3ca0-80c1-5121f4806469 | kg | Suisse | Forte (peinture) / Inconnue (colles, solvants) | Faible | Aucune identifiée | Utilisable avec paramétrage (peinture) / Proxy à adapter (autres) | Aucun flow suffisamment spécifique aux colles/solvants/chiffons identifié avec les recherches du Lot 2G | Nature exacte du résidu, quantité, filière | Distinguer peinture des autres résidus dans la collecte |

---

## MATRICE DE COLLECTE TERRAIN

| Objet | Donnée à demander | Unité | Pourquoi | Priorité de collecte |
|---|---|---|---|---|
| Électricité | Consommation électrique annuelle (ou mensuelle) | kWh | Nécessaire dès qu'un dataset sera isolé ; aucune donnée Ecoinvent ne peut s'y substituer | **Haute** |
| Transport entrant | Distance moyenne fournisseur → atelier (par fournisseur principal si possible) | km | Paramètre bloquant complet, aucune valeur par défaut acceptable | **Haute** |
| Transport sortant | Distance atelier → client + mode de livraison (tournée propre/transporteur) | km | Idem, avec distinction du taux de chargement | **Haute** |
| Chutes de bois massif | Répartition entre décharge/incinération/valorisation | % ou kg par filière | Déterminant pour choisir entre 3-4 scénarios très différents en impact | **Haute** |
| Chutes de panneaux | Quantité générée + répartition des destinations | kg, % | Même besoin que le bois massif, avec en plus une composition non reflétée par Ecoinvent | Moyenne |
| Sciures/poussières | Part captée par aspiration vs émise ; destination de la part captée (vente, valorisation interne, décharge) | kg, % | Déterminant pour éviter de confondre un co-produit valorisé avec une émission atmosphérique | **Haute** |
| Gaz naturel | Confirmation d'usage réel + consommation si applicable | m³ ou GJ | Le mandat interdit de présumer l'usage ; sans confirmation, l'objet entier est sans objet | Moyenne |
| Eau de procédé | Consommation d'eau (procédé + nettoyage) | m³ ou kg | Aucune estimation par défaut acceptable | Moyenne |
| Eaux usées | Mode de rejet (municipal standard vs contaminé nécessitant un traitement spécifique) | qualitatif | Change potentiellement le type de dataset à utiliser | Moyenne |
| Résidus contaminés | Nature exacte (peinture/solvant/colle/chiffons) + quantités par catégorie | kg, catégorie | Seule la catégorie "peinture" est bien représentée ; les autres nécessitent une décision au cas par cas | **Haute** |

---

## QU'EST-CE QUI EST DÉJÀ RÉSOLU PAR ECOINVENT ?

**Aucune catégorie ci-dessous n'affirme une représentativité québécoise/nord-américaine établie ; toutes reflètent le niveau de validation atteint dans ce lot, pas une conclusion définitive sur le contenu d'Ecoinvent.**

### A. Dataset fonctionnel identifié, représentativité à valider
- Transport entrant
- Transport sortant
- Chutes de bois massif

### B. Recherche complémentaire nécessaire avant choix définitif
- Gaz naturel/chaleur (28/38 résultats non inspectés)
- Eau de procédé (3/4 variantes inspectées)
- Eaux usées (1/3 variantes inspectée)

### C. Proxy/adaptation/reconstruction potentielle
- Chutes de panneaux (proxy candidat générique bois, composition non reflétée)
- Sciures/poussières (bascule entre co-produit et proxy candidat déchet selon destination réelle)
- Résidus contaminés — volet colles/solvants/chiffons (flux génériques seulement)

### D. Candidat spécifique identifié pour une partie du besoin
- Résidus contaminés — volet peinture/finition

### E. Non évalué — limitation d'accès
- Électricité d'atelier CA-QC — le blocage est pratique (limite de l'outil d'interrogation MCP, recherche par nom sans filtre géographique), mais **aucune lacune de contenu Ecoinvent n'est démontrée**. Ceci n'est pas compté parmi les véritables lacunes de contenu Ecoinvent.

---

## QUESTIONS TRANSVERSALES OBLIGATOIRES

**1. Le dataset électricité CA-QC peut-il enfin être isolé ?** Non. Une nouvelle tentative (recherche accentuée, vérification de l'hypothèse d'un tri stable) a été faite et infirmée ce tour.

**2. Est-il suffisamment représentatif d'un atelier québécois ?** Sans objet — ne peut pas être évalué tant qu'il n'est pas isolé.

**3. Quels datasets de transport utiliser pour entrant et sortant ?** Le même dataset générique (`market for transport, freight, lorry, unspecified`) constitue actuellement un candidat pour les deux flux, sous réserve de validation de sa représentativité technologique/géographique et d'un paramétrage entreprise distinct (distance, masse, taux de chargement).

**4. Quelles données entreprise sont nécessaires pour paramétrer le transport ?** Distances réelles (par sens), masse transportée, et pour le sortant spécifiquement, le taux de chargement réel si le volume (pas la masse) est le facteur limitant.

**5. Ecoinvent permet-il de traiter séparément bois massif / panneaux / sciures ?** Partiellement seulement, dans les limites des recherches effectuées dans ce lot. Le bois massif dispose d'un flow candidat identifié (`waste wood, untreated`), sous réserve de validation des traitements. Aucun flow suffisamment représentatif des panneaux étudiés n'a été identifié dans les recherches du Lot 2G (le candidat trouvé a été rejeté après inspection de sa composition). Des flows de sciure de type PRODUCT_FLOW ont été identifiés ; aucun flow de déchet suffisamment pertinent n'a été identifié avec les recherches effectuées.

**6. Quels scénarios de traitement des déchets sont réellement disponibles ?** Décharge sanitaire, décharge non sanitaire, incinération municipale avec/sans récupération d'énergie — tous déjà confirmés aux Lots 1/2C pour le bois ; incinération de déchets dangereux spécifiquement documentée pour la peinture.

**7. Peut-on représenter un scénario mixte de fin de vie sans créer de nouveau dataset ?** Oui conceptuellement — en pondérant les scénarios existants selon la répartition réelle fournie par l'entreprise (non construit dans ce lot, conformément au mandat).

**8. Quel dataset utiliser pour le gaz/chaleur si l'entreprise en consomme ?** `market for heat, central or small-scale, natural gas` constitue un **candidat inspecté**, non retenu de façon définitive — une recherche géographique complémentaire parmi les 28 résultats non inspectés est nécessaire avant de choisir un dataset.

**9. Quel dataset utiliser pour l'eau ?** `market for tap water`, variante Rest-of-World, constitue un **candidat inspecté** ; 3 des 4 variantes existantes ont été inspectées et aucune n'est nord-américaine, mais la 4ᵉ variante reste à vérifier avant un choix définitif.

**10. Quel traitement utiliser pour les eaux usées ?** `market for wastewater, average`, variante Rest-of-World, constitue un **candidat inspecté** (1 des 3 variantes existantes inspectée) — sous réserve de compléter la recherche géographique et de valider si la nature du rejet (contaminé ou non) justifie un traitement différent.

**11. Comment représenter les résidus contaminés ?** Distinguer peinture/finition (flow spécifique bien documenté) des colles/solvants/chiffons (flux génériques `hazardous waste` seulement, sans composition spécifique).

**12. Lesquels nécessitent réellement de nouvelles données ACV et lesquels nécessitent simplement des données d'activité de l'entreprise ?** Nécessitent principalement des données d'activité entreprise, sur la base d'un candidat déjà identifié (transport entrant/sortant, chutes de bois massif, résidus peinture) — sous réserve de validation de la représentativité du dataset. Nécessitent une recherche géographique complémentaire avant tout choix définitif (gaz naturel/chaleur, eau de procédé, eaux usées) — ni l'eau, ni le gaz, ni les eaux usées ne sont classés comme définitivement résolus par Ecoinvent. Nécessitent une réflexion de modélisation en plus des données d'activité (chutes de panneaux, sciures selon destination, résidus colles/solvants) — parce qu'aucun dataset suffisamment représentatif n'a été identifié, pas un simple manque de paramètre.

**13. Quelles sont les cinq données terrain les plus importantes à collecter ?**
1. Consommation électrique réelle (kWh) — bloquant même une fois le dataset isolé.
2. Distances de transport entrant et sortant.
3. Répartition réelle des destinations de fin de vie du bois massif ET des panneaux.
4. Destination réelle des sciures/poussières captées (valorisées ou mises en décharge).
5. Nature exacte des résidus contaminés (peinture vs colle vs solvant vs chiffons) et leurs quantités respectives.

---

## IMPACT POTENTIEL SUR LE RÉFÉRENTIEL — `docs/materiaux-ebenisterie.md` (proposé, non appliqué)

**Rappel : ce fichier n'est PAS modifié.**

**Ces statuts reflètent le niveau de validation actuel, pas une conclusion définitive sur le contenu d'Ecoinvent.**

| Objet | Ecoinvent | Correspondance | Lacune principale | Statut recommandé | Données entreprise nécessaires | Recommandation |
|---|---|---|---|---|---|---|
| Électricité d'atelier | Non isolé (CA-QC) | Inconnue | Limite d'outil MCP — non évalué, pas une lacune de contenu | 🟡 À valider | Consommation kWh | Rechercher un accès géographique direct hors MCP |
| Transport entrant | market for transport, freight, lorry, unspecified (candidat inspecté) | Moyenne à forte | Représentativité nord-américaine non établie dans ce lot | 🟡 À valider | Distance, masse | Conserver comme candidat, valider la représentativité |
| Transport sortant | Idem (candidat inspecté) | Moyenne à forte | Idem + incidence du volume/taux de remplissage à évaluer | 🟡 À valider | Distance, taux de chargement réel | Conserver comme candidat, ne pas copier le paramétrage entrant, valider la représentativité |
| Chutes de bois massif | waste wood, untreated + traitements (candidat inspecté) | Moyenne | Représentativité québécoise des traitements non établie | 🟡 À valider | Répartition des destinations | Conserver comme candidat, valider la représentativité des traitements |
| Chutes de panneaux | Aucun flow suffisamment représentatif identifié ; waste wood, untreated envisagé comme proxy candidat (non construit) | Faible | Composition résineuse non reflétée | 🟠 À adapter | Quantité, répartition | Évaluer le proxy candidat en documentant la limite ; proxy non construit |
| Sciures/poussières | saw dust (PRODUCT_FLOW, co-produit) | Moyenne | Aucun flow de déchet suffisamment pertinent identifié avec les recherches effectuées | 🟡 À valider | Part captée/valorisée vs décharge | Clarifier la destination réelle |
| Gaz naturel/chaleur | market for heat, central or small-scale, natural gas (candidat inspecté) | Moyenne | Géographie non exhaustivement vérifiée (28/38 non inspectés) | 🟡 À valider | Confirmer usage + consommation | Compléter la recherche géographique |
| Eau de procédé | market for tap water, RoW (candidat inspecté) | Moyenne | Aucune variante nord-américaine identifiée parmi 3/4 variantes inspectées ; recherche incomplète | 🟡 À valider | Consommation d'eau | Retenir comme candidat inspecté ; compléter l'inspection de la 4ᵉ variante |
| Eaux usées | market for wastewater, average, RoW (candidat inspecté) | Moyenne | Composition/nature du rejet non tranchée ; recherche géographique partielle (1/3 inspectée) | 🟡 À valider | Nature du rejet | Clarifier le mode de rejet, compléter l'inspection des variantes restantes |
| Résidus contaminés | treatment of waste paint (peinture, candidat spécifique) / flux génériques (autres, non spécifiques) | Forte (peinture) / Inconnue (autres) | Aucun flow suffisamment spécifique colle/solvant/chiffon identifié avec les recherches effectuées | 🟠 À adapter | Nature exacte, quantités | Distinguer les catégories dans la collecte |

---

## CONTRÔLE FINAL

1. Exactement 10 objets étudiés. ✅
2. Exactement 10 lignes CSV (fichier séparé). ✅
3. MD et CSV cohérents. ✅
4. UUID vérifiés par inspection directe (`process_details`) pour chaque candidat retenu, sauf mention explicite contraire (ex. électricité CA-QC, non isolé). ✅
5. Aucune donnée entreprise inventée. ✅
6. Aucune affirmation absolue fondée uniquement sur une recherche MCP — formulations `Aucun dataset pertinent identifié avec les méthodes d'interrogation disponibles` utilisées où pertinent. ✅
7. Distinction systématique Lacune_Ecoinvent / Donnee_entreprise_manquante appliquée à chaque objet. ✅
8. Électricité CA-QC réellement réinspectée (nouvelle recherche accentuée + test de l'hypothèse de tri stable, infirmée). ✅
9. Aucun autre matériau étudié — strictement les 10 objets du périmètre. ✅
10. Aucun dataset openLCA modifié. ✅
11. Aucun proxy construit (seulement évalués conceptuellement). ✅
12. Aucun Web utilisé. ✅

### Synthèse finale

**Objets avec dataset candidat identifié, représentativité à valider** : transport entrant, transport sortant, chutes de bois massif.

**Objets nécessitant une recherche géographique complémentaire avant choix définitif** : eau de procédé (3/4 variantes inspectées), eaux usées (1/3 variante inspectée), gaz naturel/chaleur (28/38 résultats non inspectés).

**Candidat spécifique identifié pour une partie du besoin** : résidus contaminés — volet peinture/finition.

**Objets nécessitant une reconstruction/proxy documenté** : chutes de panneaux, sciures/poussières (selon destination), résidus contaminés (volet colles/solvants/chiffons).

**Non évalué — limitation d'accès** : l'électricité d'atelier CA-QC n'a pas pu être isolée avec les méthodes d'interrogation MCP disponibles. Ce blocage est pratique et ne constitue pas une lacune de contenu Ecoinvent démontrée ; l'existence du dataset n'est ni confirmée ni infirmée par ce lot.

**Cinq données terrain prioritaires** : (1) consommation électrique kWh, (2) distances de transport entrant/sortant, (3) répartition des destinations de fin de vie bois massif et panneaux, (4) destination réelle des sciures/poussières captées, (5) nature exacte et quantités des résidus contaminés par catégorie.

---

*Fin du rapport Lot 2G. Aucun dataset openLCA modifié. Aucun proxy construit. `docs/materiaux-ebenisterie.md` non modifié. Seuls les 10 objets demandés ont été traités.*
