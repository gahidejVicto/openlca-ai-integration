# Diagnostic Ecoinvent — Lot 2B
## Panneaux de particules, MDF et TFL

Projet ACV mobilier québécois — Ecoinvent 3.11, Cutoff, via openLCA/MCP.

Portée stricte : panneau de particules brut, MDF brut, panneau de particules TFL fini et MDF TFL fini. Aucun dataset openLCA modifié et aucun proxy construit.

## Objectif

Le Lot 2B applique la grille stabilisée au Lot 2A à quatre produits métier centraux. L'objectif n'est pas seulement de vérifier l'existence d'un dataset, mais de distinguer correspondance physique, origine des données, technologie, intrants, énergie, profondeur de régionalisation et données fabricant nécessaires à une éventuelle adaptation québécoise.

La localisation ou l'étiquette `RoW` n'est jamais considérée comme une preuve de représentativité. Pour les produits finis TFL, la recherche suit une logique product-first : rechercher d'abord un produit fini, puis seulement en son absence évaluer une reconstruction.

---

## 1. Panneau de particules brut

### Identification

| Champ | Marché | Production EPF | Production virgin wood |
|---|---|---|---|
| Dataset | `market for particleboard, uncoated` | `particleboard production, uncoated, average glue mix` | `particleboard production, uncoated, from virgin wood` |
| UUID | `7690ac93-cf92-32dd-b2cf-68e6c7fcf673` (RoW) / `f0e6d7f3-…` (RER) | `1bb7e5df-a7f8-39c2-9a2b-2c5416358f75` | `7e506572-66ec-3f0d-b73d-4e1343a8e64d` |
| Unité | m³ | m³ | m³ |
| Location | RoW / Europe | Europe | RoW |

Le produit correspond fonctionnellement au panneau de particules brut utilisé en mobilier. La description mentionne l'EN 312 et l'usage mobilier. Le marché RoW n'est toutefois pas homogène : son inspection montre environ 78,6 % de production européenne EPF `average glue mix` et 21,4 % de production `from virgin wood`, extrapolée d'un dataset brésilien à base d'eucalyptus.

### Intrants déterminants — production EPF

| Exchange | Quantité | Observation |
|---|---:|---|
| wood chips, post-consumer | 180,67 kg | bois récupéré/post-consommation |
| wood chips, dry | 199,04 kg | origine exacte non précisée |
| slab and siding, softwood | 124,22 kg | résidus de scierie |
| sawdust, wet | 24,11 kg | résidu |
| wood chips, wet | 20,43 kg | résidu |
| pulpwood, softwood | 0,258 m³ | bois rond vierge minoritaire |
| urea formaldehyde resin | 44,45 kg | liant principal |
| melamine formaldehyde resin | 9,78 kg | liant interne, distinct du revêtement TFL |
| phenolic resin | 1,20 kg | liant secondaire |
| MDI | 3,19 kg | liant secondaire |
| paraffin | 3,00 kg | hydrofugation |
| electricity, medium voltage | ~103,1 kWh | linking hétérogène |
| heat, natural gas | 197,20 MJ | énergie procédé |
| heat, fuel oils | 47,06 MJ | énergie procédé |
| tap water | 174,52 kg | marché régional large |
| Formaldehyde, direct | 0,0916 kg | émission de procédé |

La composante `from virgin wood` est technologiquement différente : eucalyptus vierge, environ 71,7 kg d'UF, fuel lourd et émissions directes de CO₂ fossile. Elle ne constitue pas une alternative québécoise.

### Représentativité québécoise

| Critère | Niveau |
|---|---|
| Géographie | Faible |
| Technologie | Moyenne |
| Intrants | Faible |
| Énergie | Faible |
| Transport | Moyenne |
| Données primaires QC | Aucune |
| Correspondance métier | Moyenne |

**Verdict : dataset étranger potentiellement adaptable.** Le principe industriel du pressage à chaud constitue un socle générique raisonnable, mais le mix de bois, les liants, l'énergie, les transports et les fournisseurs doivent être confrontés au contexte réel québécois.

**A — potentiellement transférable :** principe du pressage à chaud et structure générale bois + liant + énergie.

**B — à régionaliser :** électricité, chaleur/combustibles, transport et fournisseurs de bois.

**C — données fabricant :** essences et part vierge/recyclée, système de liant et dosage, densité, consommation énergétique mesurée et taux de matière récupérée.

Lacunes résiduelles : origine exacte de `wood chips, dry`, année de collecte EPF et résolution géographique de certains providers génériques.

---

## 2. MDF brut

### Identification

| Champ | Marché | Production RoW | Production Europe |
|---|---|---|---|
| Dataset | `market for medium density fibreboard` | `medium density fibreboard production, uncoated` | idem |
| UUID | `eef398de-7420-330d-b894-1440a0afa155` | `daa9fa1a-d57f-38d6-a172-3243464ba2b5` | `ff6070a5-a826-3cde-a4b7-6c4c95d36423` |
| Location | RoW | RoW | Europe |
| Unité | m³ | m³ | m³ |

La description EPF cite directement des usages mobilier : plateaux, façades de portes et tiroirs, surfaces profilées, ainsi que l'emploi comme substrat pour peinture, films décoratifs ou placages.

### Comparaison quantitative RoW / Europe

La grille du Lot 2A révèle que les deux productions sont technologiquement identiques :

| Exchange | RoW | Europe |
|---|---:|---:|
| wood chips, dry | 365,70 kg | 365,70 kg |
| post-consumer wood chips | 110,45 kg | 110,45 kg |
| sawdust, wet | 29,87 kg | 29,87 kg |
| slab and siding, softwood | 10,15 kg | 10,15 kg |
| pulpwood, softwood | 0,6213 m³ | 0,6213 m³ |
| pulpwood, hardwood | 0,00741 m³ | 0,00741 m³ |
| UF resin | 46,371 kg | 46,371 kg |
| MF resin | 41,793 kg | 41,793 kg |
| paraffin | 4,697 kg | 4,697 kg |
| heat, natural gas | 1068,05 MJ | 1068,05 MJ |
| other heat | 40,56 MJ | 40,56 MJ |
| diesel | 35,42 MJ | 35,42 MJ |
| direct emissions | identiques | identiques |

**Conclusion factuelle : le MDF `Rest of World` est une copie technologique du MDF `Europe`.** L'étiquette RoW n'apporte donc pas une technologie nord-américaine ou québécoise distincte.

### Représentativité québécoise

| Critère | Niveau |
|---|---|
| Géographie | Faible |
| Technologie | Moyenne |
| Intrants | Faible |
| Énergie | Faible |
| Transport | Inconnu dans cette inspection |
| Données primaires QC | Aucune |
| Correspondance métier | Forte |

**Verdict : dataset étranger potentiellement adaptable.** La correspondance métier est forte, mais la composition et le profil énergétique proviennent de données EPF européennes.

**A — potentiellement transférable :** principe défibrage + liant + pressage à chaud.

**B — à régionaliser :** énergie, transport et fournisseurs de bois. La forte consommation de gaz naturel du dataset européen doit être confrontée aux consommations réelles du fabricant québécois, sans présumer du profil énergétique local.

**C — données fabricant :** mix de résines et dosage, essences et part recyclée, densité et consommation énergétique mesurée par vecteur.

Lacunes résiduelles : étape de fibration non détaillée comme flow distinct, année de collecte non trouvée et marché/transport non inspecté en profondeur dans ce lot.

---

## 3. Panneau de particules TFL fini

### Recherche product-first

Les recherches `melamine faced particleboard`, `thermally fused laminate`, `decorative particleboard`, `laminated particleboard`, `coated particleboard` et variantes n'ont retourné aucun processus fini pertinent. Une recherche de flows `particleboard` retourne seulement `particleboard, uncoated`, `particleboard, cement bonded` et `tubular particleboard`.

**Conclusion : absence fortement confirmée dans Ecoinvent 3.11 via les méthodes d'interrogation disponibles.** La convergence recherche de processus + recherche de flows rend l'absence très probable, tout en conservant la réserve liée aux limites de l'outil.

### Service de revêtement disponible

Dataset : `coating service, melamine impregnated paper, double-sided`, UUID `4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78`, Europe.

| Élément | Valeur observée |
|---|---|
| Produit de référence | coating, with melamine impregnated paper |
| Unité | m² |
| Nombre de faces | deux |
| Papier mélaminé | 0,604 kg/m² |
| Grammage | 302 g/m²/face |
| Chaleur | 0,36 MJ/m² |
| Électricité | 0,196 kWh/m² |
| Substrat | explicitement exclu |
| Émissions atmosphériques | explicitement exclues faute de données spécifiques |
| Origine | plusieurs usines européennes |
| Applicabilité | déclarée par Ecoinvent pour différents panneaux à base de bois |

Le rapport masse/surface est cohérent : 0,604 kg/m² = 2 × 0,302 kg/m²/face.

### Faisabilité du proxy

`particleboard brut + coating service` est physiquement cohérent comme **proxy de modélisation** d'un TFL acheté fini. Il représente le papier décor, son grammage, la double face et une énergie de thermofusion. Il ne transforme pas pour autant la réalité métier : l'atelier achète un panneau fini, il ne réalise pas le laminage.

Lacunes propres au service : émissions atmosphériques non quantifiées, infrastructure de laminage non vérifiée, pertes non documentées et nécessité d'une hypothèse d'épaisseur pour convertir le substrat en m³ vers le revêtement en m². Ces émissions ne peuvent donc pas être quantifiées par ce service et devront être documentées ou complétées si elles sont jugées significatives.

Le MF présent dans le panneau brut EPF est un liant interne et ne doit pas être confondu avec la mélamine du papier décor : il ne s'agit pas d'un double comptage direct, mais la distinction doit rester explicite.

**Verdict : proxy seulement.** Données fabricant minimales : épaisseur, nombre de faces, grammage réel du papier décor et, si disponibles, données d'émissions de la presse.

---

## 4. MDF TFL fini

Les recherches `thermally fused laminate MDF`, `TFL MDF`, `melamine faced MDF`, `melamine coated MDF`, `decorative MDF`, `coated MDF` et `laminated MDF` ne retournent aucun produit fini. La recherche par flow ne révèle qu'un MDF générique non revêtu parmi les flows pertinents.

Le même service de coating peut être appliqué au MDF selon la documentation Ecoinvent, qui le décrit comme utilisable pour différents panneaux à base de bois. Ecoinvent ne modélise toutefois aucune dépendance du service à la porosité, densité ou rugosité du substrat : grammage, énergie, nombre de faces et pertes restent identiques.

Cette transférabilité est donc **une déclaration de généricité du modèle Ecoinvent, et non une validation physique indépendante spécifique au MDF**.

| Critère | Niveau |
|---|---|
| Géographie | Faible |
| Technologie | Moyenne |
| Intrants | Faible |
| Énergie | Faible |
| Transport | Inconnu |
| Données primaires QC | Aucune |
| Correspondance métier | Moyenne |

**Verdict : proxy seulement**, avec une réserve supplémentaire : vérifier, si ce paramètre s'avère sensible, si le comportement de pressage MDF + papier mélaminé diffère significativement de celui du particleboard.

---

## Comparaison particleboard / MDF

| Critère | Particleboard | MDF |
|---|---|---|
| Origine | EPF Europe + composante brésilienne | EPF Europe uniquement |
| Mix bois | recyclé/résidus + variante eucalyptus vierge | résidus + recyclé + bois rond minoritaire |
| Résines | UF + MF + phénolique + MDI pour EPF | UF + MF |
| Énergie | électricité + gaz/fuels | chaleur fortement dominée par gaz naturel dans le dataset |
| Technologie | particules + pressage | défibrage + pressage |
| Géographie | marché RoW mélange plusieurs technologies étrangères | RoW = copie technologique Europe |
| Adaptation QC sensible | mix bois/liants | profil énergétique + mix matière |

Une grille de localisation commune A/B/C est utilisable, mais les paramètres doivent être traités séparément. Il n'est pas méthodologiquement justifié d'appliquer un facteur de correction commun au particleboard et au MDF.

---

## Analyse spécifique TFL

**Réalité métier :** panneau TFL acheté fini.

**Modèle ACV éventuel :** substrat brut + `coating service, melamine impregnated paper, double-sided` + hypothèse d'épaisseur pour relier m³ et m².

Ce proxy est méthodologiquement défendable sous conditions : les paramètres du service sont explicites et Ecoinvent revendique sa généricité vis-à-vis des panneaux à base de bois. Il hérite toutefois des lacunes du substrat et ajoute ses propres limites : émissions de pressage absentes, infrastructure non vérifiée, conversion m³/m² et absence de différenciation MDF/particleboard.

Il ne doit pas être présenté comme équivalent à une donnée réelle de produit TFL fini sans ces réserves.

---

## Synthèse du Lot 2B

| Produit métier | Meilleur candidat | Correspondance | Origine | Verdict | Lacune principale | Action |
|---|---|---|---|---|---|---|
| Particleboard brut | `market for particleboard, uncoated` | A | EPF + Brésil | Dataset étranger potentiellement adaptable | mix bois/liants étrangers | adapter avec données fabricant |
| MDF brut | `market for medium density fibreboard` | A | EPF Europe | Dataset étranger potentiellement adaptable | RoW = copie Europe ; profil énergie/matière | adapter avec données fabricant |
| Particleboard TFL | substrat + coating | B | données européennes | Proxy seulement | produit fini absent ; émissions et conversion d'unité | documenter + données fabricant |
| MDF TFL | substrat + coating | B | données européennes | Proxy seulement | idem + transférabilité substrat non démontrée physiquement | documenter + vérifier hypothèse |

### Variables minimales à obtenir ultérieurement des fabricants québécois

Pour les panneaux bruts : essences/mix bois, part vierge/recyclée, système de liant et dosage, densité, consommation électrique et thermique réelle. Pour le TFL : épaisseur, nombre de faces et grammage réel du papier décor ; données d'émissions de presse si disponibles.

---

## Impact méthodologique

Le Lot 2B confirme la valeur de la comparaison quantitative entre géographies : elle révèle ici que le MDF RoW est une copie technologique de l'Europe. Il confirme aussi l'importance des descriptions narratives et la limite de résolution des providers portant un nom identique.

Trois enseignements complètent la grille du Lot 2A :

1. Un marché mondial peut être un mélange de plusieurs technologies et origines ; il faut le décomposer avant de juger sa représentativité.
2. Pour tester l'existence d'un produit, la recherche des flows complète utilement la recherche des processus et renforce un constat d'absence.
3. Une affirmation de généricité par Ecoinvent doit être distinguée d'une validation physique indépendante : le service TFL en fournit un exemple clair.

La faisabilité d'inspection doit aussi distinguer extraction massive, sujette aux timeouts, et recherches ciblées par nom ou flow, plus efficaces dans ce lot.

---

*Fin du rapport Lot 2B. Aucun dataset openLCA modifié, aucun proxy construit et aucune modification de la base Ecoinvent.*
