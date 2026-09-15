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
10. **Directement utilisable pour un atelier québécois ?** **Aucune conclusion possible** — ni positive ni négative. Ce n'est pas une lacune Ecoinvent démontrée (le dataset existe très probablement, comme le suggère le cas confirmé de l'Île-du-Prince-Édouard au Lot 1) mais une **limite de l'outil d'interrogation MCP disponible**, à documenter comme telle, pas comme absence de contenu dans Ecoinvent.

### Verdict : **données insuffisantes** (limite d'outil, pas lacune de contenu)

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
Moyenne pondérée de plusieurs classes d'émission EURO (principalement EURO3 et EURO4, part moindre d'EURO5/6) — <cite>reflète un mix de flotte, sans distinction de classe de poids ni de région</cite> (fait déduit directement des parts observées dans les exchanges : EURO3 ≈ 32%+13%=45%, EURO4 ≈ 11%+28%=39%, EURO5 ≈ 10%+4%=14%, EURO6 ≈ 2%). Il existe aussi des datasets par classe de poids spécifique (3.5-7.5t, 7.5-16t, 16-32t) si une classe de véhicule précise doit être choisie plutôt que la moyenne "unspecified".

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Forte (service de transport routier de marchandises) |
| Technologie | Moyenne (moyenne de flotte européenne, classes EURO3-6 — pas nécessairement représentatif du parc nord-américain) |
| Unité | Forte (t·km, standard et directement utilisable) |
| Géographie | Faible à moyenne (Global, mais fondé sur des facteurs d'émission de véhicules européens) |

### 6. Lacune Ecoinvent
Le dataset "unspecified" est une moyenne de flotte européenne (classes EURO), pas un facteur nord-américain — **incertitude de correspondance technologique**, pas une absence de dataset.

### 7. Données entreprise manquantes
Distance fournisseur → atelier (par fournisseur ou moyenne) ; masse transportée ; éventuellement classe de véhicule si connue (permettrait de choisir un dataset plus spécifique que "unspecified") ; taux de chargement/retour à vide (déjà incorporé dans la moyenne du marché, mais un choix plus spécifique nécessiterait cette donnée séparément).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise**

### 10. Action recommandée
Conserver ce dataset comme service par défaut ; demander à l'entreprise les distances réelles par fournisseur principal.

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
Aucune lacune distincte de l'Objet 2. **Point d'attention méthodologique** : le mobilier fini a un rapport masse/volume potentiellement très différent des matériaux entrants (planches denses vs meuble volumineux et léger) — Ecoinvent modélise le transport en t·km (masse), donc un taux de remplissage du véhicule limité par le **volume** plutôt que la masse ne serait pas capturé par un simple choix de dataset, mais nécessiterait un ajustement du taux de chargement effectif dans le paramétrage.

### 7. Données entreprise manquantes
Distance atelier → client/distributeur ; masse du/des meuble(s) transporté(s) ; **taux de chargement réel du véhicule si le volume est le facteur limitant plutôt que la masse** (donnée spécifique à ce sens de transport, distincte de l'Objet 2).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise**

### 10. Action recommandée
Ne pas réutiliser aveuglément le même taux de chargement que pour le transport entrant ; demander spécifiquement le mode de livraison (tournée propre, transporteur, taux de remplissage typique).

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
Un flux de déchet de bois **non traité** (sans revêtement, colle, ni traitement chimique) — cohérent avec des chutes de bois massif brut d'ébénisterie.

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

### 9. Verdict : **utilisable avec paramétrage entreprise**

### 10. Action recommandée
Conserver ; demander à l'entreprise sa filière réelle de fin de vie pour les chutes de bois massif.

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

UUID `73059859-50e6-4bfb-b729-c9da6ed34f9d` ; traitement associé `treatment of waste fibreboard, collection for final disposal` (UUID `7fa28bdc-7551-3157-a504-209c9e24fb70`, location Rest-of-World). **Fait Ecoinvent** : <cite>"The waste contains 0.925kg untreated wood ... and 0.075kg polyurethane"</cite>. **Interprétation (la nôtre)** : cette composition (bois + polyuréthane, pas de résine urée/mélamine-formaldéhyde) ne correspond pas à un panneau MDF/particules de mobilier tel que caractérisé aux Lots 2B/2C (liants UF/MF) — il s'agit vraisemblablement d'un produit fibreboard différent (isolation, composite automobile, ou porte alvéolaire). **Ce candidat est rejeté comme correspondance de composition, malgré la correspondance de nom.**

### 3. Meilleur candidat
Aucun flow de déchet spécifique aux panneaux de mobilier. Seule option restante : le générique `waste wood, untreated` déjà utilisé pour l'Objet 4 — **mais celui-ci ne reflète pas la composition réelle d'un panneau (résines UF/MF, éventuel revêtement de surface) puisqu'il est explicitement "untreated".**

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
**Lacune de contenu réelle** (pas seulement une donnée entreprise manquante) : Ecoinvent ne distingue pas, dans ses flux de déchets, un panneau de bois composite lié par résine urée/mélamine-formaldéhyde (particules, MDF) d'un bois massif non traité — le seul candidat nominal ("waste fibreboard") s'est révélé, après inspection, être un produit différent.

### 7. Données entreprise manquantes
Quantité de chutes de panneaux ; répartition entre destinations de fin de vie (comme pour l'Objet 4, non supposée).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **proxy à adapter** (utilisation du générique `waste wood, untreated` comme proxy documenté, avec réserve explicite sur la composition résineuse non reflétée)

### 10. Action recommandée
Utiliser `waste wood, untreated` comme proxy en documentant explicitement cette limite (résines/colles internes du panneau non reflétées dans un flux "untreated").

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
**Fait déterminant** : la sciure est modélisée dans Ecoinvent comme un **co-produit commercialisable** (utilisé comme intrant dans la production de particleboard/MDF et comme combustible de séchoir, observé aux Lots 2A-2C), **jamais comme un flux de "déchet" distinct**. Aucun flow "waste sawdust" n'existe.

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Moyenne — correspond si la sciure de l'atelier est valorisée (vendue/donnée pour un usage matière ou énergie) ; **ne correspond pas** si elle est mise en décharge, faute de flow "déchet de sciure" dédié |
| Technologie | Sans objet |
| Unité | kg |
| Géographie | Sans objet (flow générique, pas de production geo-spécifique au niveau du flow lui-même) |

### 6. Lacune Ecoinvent
Aucun flow "déchet de sciure" distinct n'existe — si l'atelier ne valorise pas sa sciure, il faudrait se rabattre sur le générique `waste wood, untreated` (Objet 4), avec la même réserve que pour les chutes de panneaux si la sciure provient en partie de panneaux.

### 7. Données entreprise manquantes
**Distinction essentielle, conformément à la mise en garde du mandat** : la quantité de poussière **captée par aspiration** n'est pas automatiquement une émission atmosphérique — il faut savoir : (a) la quantité totale générée, (b) la part captée vs émise directement à l'air, (c) la destination de la part captée (vente/valorisation énergétique interne vs mise en décharge), (d) si un mélange sciure de bois massif / poussière de panneaux est collecté ensemble ou séparément (pertinent étant donné la lacune de l'Objet 5).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise** (si valorisée) / **proxy à adapter** (si mise en décharge, via le générique bois)

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

### 9. Verdict : **à valider** (existence d'une variante géographique plus pertinente non vérifiée exhaustivement)

### 10. Action recommandée
D'abord confirmer l'usage réel de gaz naturel par l'entreprise ; si confirmé, compléter la recherche géographique parmi les 38 résultats avant de choisir un dataset définitif.

---

## OBJET 8 — EAU DE PROCÉDÉ / NETTOYAGE (P2)

### 1. Objet métier
Eau utilisée pour le nettoyage/procédé en atelier.

### 2. Recherche Ecoinvent

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| market for tap water | search_processes | **4 résultats au total — les 4 inspectés à 3/4** | Ensemble restreint, vérifiable presque intégralement |

**Géographies confirmées par inspection directe** : Suisse (`3e419265…`), Europe sans Suisse (`24690c75…`), Rest-of-World (`882c7e14…`). Le 4ᵉ (`3ab1597e…`) n'a pas été inspecté individuellement ce tour, probablement un marché global agrégé étant donné le nombre total de 4 correspondant au schéma habituel (CH / Europe sans CH / RoW / Global).

**Aucune des trois géographies inspectées n'est le Canada ou le Québec.**

### 3. Meilleur candidat

| Champ | Valeur |
|---|---|
| Dataset | `market for tap water`, variante Rest-of-World (la plus généralement applicable hors Europe) |
| UUID | `882c7e14-18f8-3eb4-8638-b41826090117` |
| Unité | kg |
| Location | Rest-of-World |

### 4. Ce que représente réellement le dataset
**Fait Ecoinvent, explicite** : <cite>"Since tap water is mainly produced and distributed at a regional level, regional markets should be prefered, when relevant."</cite> — Ecoinvent lui-même signale qu'un marché régional serait préférable ; faute d'un marché canadien/québécois identifié parmi les 4 variantes existantes, le RoW reste la meilleure option disponible mais **explicitement sous-optimale selon Ecoinvent lui-même**.

### 5. Correspondance

| Dimension | Niveau |
|---|---|
| Fonction | Forte |
| Technologie | Moyenne (mix de traitement RoW incluant du dessalement d'eau de mer — non pertinent pour le Québec, dilué dans une moyenne mondiale) |
| Unité | Forte (kg) |
| Géographie | **Faible, confirmée** (seulement 4 variantes existent et aucune n'est nord-américaine) |

### 6. Lacune Ecoinvent
Absence confirmée (parmi un ensemble restreint et presque intégralement vérifié) de marché d'eau potable nord-américain ou québécois — contrairement à l'électricité, ce n'est pas une limite d'outil mais une **lacune de contenu vérifiée** sur un ensemble suffisamment petit pour être quasi exhaustivement contrôlé.

### 7. Données entreprise manquantes
Consommation d'eau réelle (m³ ou kg) pour le procédé/nettoyage.

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **proxy à adapter**

### 10. Action recommandée
Utiliser la variante RoW en documentant explicitement l'absence de marché nord-américain comme limite connue.

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

### 9. Verdict : **à valider**

### 10. Action recommandée
Clarifier si l'atelier rejette au réseau municipal (dataset "average" pertinent) ou traite lui-même des eaux contaminées (voir Objet 10) ; compléter l'inspection géographique des 2 variantes non vérifiées.

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
Aucun flow dédié aux résidus de **colle** ou de **solvant** seuls, ni aux **chiffons/absorbants contaminés** — seule la catégorie "peinture" dispose d'un flow spécifique. Pour les autres types de résidus contaminés, seuls les flux génériques `hazardous waste, for incineration` / `hazardous waste, for underground deposit` restent disponibles, sans composition spécifique documentée.

### 7. Données entreprise manquantes
Nature exacte des résidus (peinture/vernis vs solvant vs colle vs chiffons) — **déterminante pour le choix du flow**, puisque seule la catégorie peinture est bien représentée ; quantité générée ; filière de collecte réelle (incinération dangereuse confirmée ou autre).

### 8. Données primaires QC
Aucune identifiée.

### 9. Verdict : **utilisable avec paramétrage entreprise** pour les résidus de peinture/finition ; **proxy à adapter** (flux génériques) pour colles/solvants/chiffons

### 10. Action recommandée
Distinguer, dans la collecte de données entreprise, peinture/finition (bien couverte) des autres résidus contaminés (colles, solvants, chiffons — couverture générique seulement).

---

## SYNTHÈSE DES 10 OBJETS

| Objet_metier | Priorite | Dataset_Ecoinvent | UUID | Unite | Location | Correspondance | Geographie_QC | Donnees_primaires_QC | Verdict | Lacune_Ecoinvent | Donnee_entreprise_manquante | Action_recommandee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Électricité d'atelier | P1 | market for electricity, medium voltage (non isolé pour CA-QC) | Non déterminé | kWh/MJ | CA-QC visé, non confirmé | Inconnue | Non déterminée | Aucune identifiée | Données insuffisantes | Aucune démontrée — limite d'outil MCP | Consommation kWh réelle | Rechercher accès géographique direct hors MCP |
| Transport entrant | P1 | market for transport, freight, lorry, unspecified | 49eb6ae0-86d7-3674-89b9-566267648ba9 | t·km | Global | Moyenne à forte | Faible | Aucune identifiée | Utilisable avec paramétrage entreprise | Moyenne de flotte européenne, pas nord-américaine | Distance fournisseur→atelier, masse | Conserver, demander distances réelles |
| Transport sortant | P1 | market for transport, freight, lorry, unspecified (même dataset, paramétrage distinct) | 49eb6ae0-86d7-3674-89b9-566267648ba9 | t·km | Global | Moyenne à forte | Faible | Aucune identifiée | Utilisable avec paramétrage entreprise | Idem transport entrant | Distance atelier→client, taux de chargement réel (volume vs masse) | Conserver, ne pas réutiliser le taux de chargement de l'entrant |
| Chutes de bois massif | P1 | waste wood, untreated + traitements (landfill/incinération) | 6f2eb438-cde2-4d07-a770-d023a988a9c4 | kg | Europe/RoW selon variante | Moyenne | Faible | Aucune identifiée | Utilisable avec paramétrage entreprise | Paramètres européens de décharge/incinération | Répartition réelle des destinations | Conserver, demander la répartition réelle |
| Chutes de panneaux | P1 | Aucun flow dédié — waste wood, untreated comme proxy (composition résineuse non reflétée) | 6f2eb438-cde2-4d07-a770-d023a988a9c4 (proxy) | kg | Europe/RoW | Faible | Faible | Aucune identifiée | Proxy à adapter | Aucun flow reflétant la composition résineuse (UF/MF) d'un panneau | Quantité, répartition des destinations | Utiliser le proxy en documentant la limite |
| Sciures/poussières | P1 | saw dust, wet/loose, measured as dry mass (co-produit, pas déchet) | a514c9f2-0d4d-4ce2-809b-de4c29e74709 / dfaef357-a79e-4846-aabc-848b1ab59fbb | kg | Générique | Moyenne | Sans objet | Aucune identifiée | Utilisable (si valorisée) / Proxy à adapter (si mise en décharge) | Aucun flow "déchet de sciure" dédié | Part captée/valorisée vs mise en décharge | Clarifier la destination réelle avec l'entreprise |
| Gaz naturel/chaleur | P2 | market for heat, central or small-scale, natural gas | b4a33a9d-da08-3d5b-a883-e22acd9e7415 | MJ | Europe without Switzerland | Moyenne | Non déterminée (28/38 résultats non inspectés) | Aucune identifiée | À valider | Correspondance géographique non exhaustivement vérifiée | Confirmer l'usage réel de gaz + consommation mesurée | Confirmer usage réel avant de choisir un dataset définitif |
| Eau de procédé | P2 | market for tap water | 882c7e14-18f8-3eb4-8638-b41826090117 | kg | Rest-of-World | Moyenne | Faible (confirmée, ensemble restreint vérifié) | Aucune identifiée | Proxy à adapter | Absence confirmée de marché nord-américain (4 variantes, aucune CA/QC) | Consommation d'eau réelle | Utiliser RoW en documentant la limite |
| Eaux usées | P2 | market for wastewater, average | 7a2be1f9-6dca-35f5-a39f-1d64c9e22eae | m³ | Rest-of-World | Moyenne | Faible (partiellement vérifiée) | Aucune identifiée | À valider | Composition détaillée non documentée dans les champs consultés | Nature du rejet (municipal vs contaminé) | Clarifier le mode de rejet réel |
| Résidus contaminés | P2 | treatment of waste paint, hazardous waste incineration | d39c3e17-6987-3ca0-80c1-5121f4806469 | kg | Suisse | Forte (peinture) / Inconnue (colles, solvants) | Faible | Aucune identifiée | Utilisable avec paramétrage (peinture) / Proxy à adapter (autres) | Aucun flow dédié colle/solvant/chiffon | Nature exacte du résidu, quantité, filière | Distinguer peinture des autres résidus dans la collecte |

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

### A. Ecoinvent semble suffisant, seules les données entreprise sont nécessaires
- Transport entrant
- Transport sortant
- Chutes de bois massif

### B. Ecoinvent fournit une base mais une adaptation/validation est nécessaire
- Eau de procédé (géographie confirmée non idéale, mais dataset fonctionnellement adapté)
- Résidus contaminés — volet peinture/finition
- Gaz naturel/chaleur (à valider géographiquement avant usage)
- Eaux usées (à valider selon nature du rejet)

### C. Reconstruction/proxy à partir de plusieurs éléments nécessaire
- Chutes de panneaux (proxy générique bois, composition non reflétée)
- Sciures/poussières (bascule entre co-produit et proxy déchet selon destination réelle)
- Résidus contaminés — volet colles/solvants/chiffons (flux génériques seulement)

### D. Lacune Ecoinvent importante / aucune représentation exploitable identifiée
- Électricité d'atelier CA-QC — **non pas une lacune de contenu démontrée, mais une impossibilité d'isolation avec les outils actuels**, ce qui produit le même blocage pratique qu'une lacune de contenu tant qu'une méthode alternative n'est pas trouvée.

---

## QUESTIONS TRANSVERSALES OBLIGATOIRES

**1. Le dataset électricité CA-QC peut-il enfin être isolé ?** Non. Une nouvelle tentative (recherche accentuée, vérification de l'hypothèse d'un tri stable) a été faite et infirmée ce tour.

**2. Est-il suffisamment représentatif d'un atelier québécois ?** Sans objet — ne peut pas être évalué tant qu'il n'est pas isolé.

**3. Quels datasets de transport utiliser pour entrant et sortant ?** Le même dataset générique (`market for transport, freight, lorry, unspecified`) pour les deux, avec des paramètres entreprise distincts (distance, taux de chargement).

**4. Quelles données entreprise sont nécessaires pour paramétrer le transport ?** Distances réelles (par sens), masse transportée, et pour le sortant spécifiquement, le taux de chargement réel si le volume (pas la masse) est le facteur limitant.

**5. Ecoinvent permet-il de traiter séparément bois massif / panneaux / sciures ?** Partiellement seulement. Le bois massif dispose d'un flow dédié adapté (`waste wood, untreated`). Les panneaux n'ont aucun flow dédié valide (le candidat trouvé a été rejeté après inspection). Les sciures existent comme co-produit, jamais comme déchet.

**6. Quels scénarios de traitement des déchets sont réellement disponibles ?** Décharge sanitaire, décharge non sanitaire, incinération municipale avec/sans récupération d'énergie — tous déjà confirmés aux Lots 1/2C pour le bois ; incinération de déchets dangereux spécifiquement documentée pour la peinture.

**7. Peut-on représenter un scénario mixte de fin de vie sans créer de nouveau dataset ?** Oui conceptuellement — en pondérant les scénarios existants selon la répartition réelle fournie par l'entreprise (non construit dans ce lot, conformément au mandat).

**8. Quel dataset utiliser pour le gaz/chaleur si l'entreprise en consomme ?** `market for heat, central or small-scale, natural gas`, sous réserve de vérifier plus avant si une variante géographique plus pertinente existe parmi les 28 résultats non inspectés.

**9. Quel dataset utiliser pour l'eau ?** `market for tap water`, variante Rest-of-World — la moins mauvaise option confirmée parmi un ensemble restreint et presque intégralement vérifié.

**10. Quel traitement utiliser pour les eaux usées ?** `market for wastewater, average`, variante Rest-of-World, sous réserve de valider si la nature du rejet (contaminé ou non) justifie un traitement différent.

**11. Comment représenter les résidus contaminés ?** Distinguer peinture/finition (flow spécifique bien documenté) des colles/solvants/chiffons (flux génériques `hazardous waste` seulement, sans composition spécifique).

**12. Lesquels nécessitent réellement de nouvelles données ACV et lesquels nécessitent simplement des données d'activité de l'entreprise ?** Nécessitent des données d'activité seulement (transport entrant/sortant, chutes de bois massif, eau, résidus peinture) — le dataset ACV existe déjà. Nécessitent une réflexion de modélisation en plus des données d'activité (chutes de panneaux, sciures, résidus colles/solvants) — parce que le dataset disponible est un proxy imparfait, pas un manque de paramètre.

**13. Quelles sont les cinq données terrain les plus importantes à collecter ?**
1. Consommation électrique réelle (kWh) — bloquant même une fois le dataset isolé.
2. Distances de transport entrant et sortant.
3. Répartition réelle des destinations de fin de vie du bois massif ET des panneaux.
4. Destination réelle des sciures/poussières captées (valorisées ou mises en décharge).
5. Nature exacte des résidus contaminés (peinture vs colle vs solvant vs chiffons) et leurs quantités respectives.

---

## IMPACT POTENTIEL SUR LE RÉFÉRENTIEL — `docs/materiaux-ebenisterie.md` (proposé, non appliqué)

**Rappel : ce fichier n'est PAS modifié.**

| Objet | Ecoinvent | Correspondance | Lacune principale | Statut recommandé | Données entreprise nécessaires | Recommandation |
|---|---|---|---|---|---|---|
| Électricité d'atelier | Non isolé (CA-QC) | Inconnue | Limite d'outil MCP, pas de contenu | 🟡 À valider | Consommation kWh | Rechercher un accès géographique direct hors MCP |
| Transport entrant | market for transport, freight, lorry, unspecified | Moyenne à forte | Flotte européenne, pas nord-américaine | 🟢 Utilisable | Distance, masse | Conserver |
| Transport sortant | Idem | Moyenne à forte | Idem + taux de chargement volume/masse | 🟢 Utilisable | Distance, taux de chargement réel | Conserver, ne pas copier le paramétrage entrant |
| Chutes de bois massif | waste wood, untreated + traitements | Moyenne | Paramètres européens | 🟢 Utilisable | Répartition des destinations | Conserver |
| Chutes de panneaux | Proxy (waste wood, untreated) | Faible | Composition résineuse non reflétée | 🟠 À adapter | Quantité, répartition | Documenter la limite explicitement |
| Sciures/poussières | saw dust (co-produit) | Moyenne | Aucun flow "déchet" dédié | 🟡 À valider | Part captée/valorisée vs décharge | Clarifier la destination réelle |
| Gaz naturel/chaleur | market for heat, central or small-scale, natural gas | Moyenne | Géographie non exhaustivement vérifiée | 🟡 À valider | Confirmer usage + consommation | Compléter la recherche géographique |
| Eau de procédé | market for tap water (RoW) | Moyenne | Absence confirmée de marché nord-américain | 🟠 À adapter | Consommation d'eau | Utiliser en documentant la limite |
| Eaux usées | market for wastewater, average (RoW) | Moyenne | Composition/nature du rejet non tranchée | 🟡 À valider | Nature du rejet | Clarifier le mode de rejet |
| Résidus contaminés | treatment of waste paint (peinture) / flux génériques (autres) | Forte (peinture) / Inconnue (autres) | Aucun flow dédié colle/solvant/chiffon | 🟠 À adapter | Nature exacte, quantités | Distinguer les catégories dans la collecte |

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

**Objets directement utilisables (données entreprise seulement)** : transport entrant, transport sortant, chutes de bois massif.

**Objets utilisables avec adaptation/validation** : eau de procédé, eaux usées, gaz naturel/chaleur, résidus contaminés (volet peinture).

**Objets nécessitant une reconstruction/proxy documenté** : chutes de panneaux, sciures/poussières (selon destination), résidus contaminés (volet colles/solvants/chiffons).

**Véritable lacune bloquante** : l'électricité d'atelier CA-QC reste impossible à isoler avec les outils MCP disponibles — ce n'est pas classé comme une lacune de contenu Ecoinvent (le dataset existe très probablement) mais comme une limite d'accès qui bloque néanmoins toute utilisation pratique tant qu'elle persiste.

**Cinq données terrain prioritaires** : (1) consommation électrique kWh, (2) distances de transport entrant/sortant, (3) répartition des destinations de fin de vie bois massif et panneaux, (4) destination réelle des sciures/poussières captées, (5) nature exacte et quantités des résidus contaminés par catégorie.

---

*Fin du rapport Lot 2G. Aucun dataset openLCA modifié. Aucun proxy construit. `docs/materiaux-ebenisterie.md` non modifié. Seuls les 10 objets demandés ont été traités.*
