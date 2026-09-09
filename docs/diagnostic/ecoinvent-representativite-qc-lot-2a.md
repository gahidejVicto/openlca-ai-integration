# Diagnostic Ecoinvent — Lot 2A

## Inspection approfondie de trois cas CA-QC

Projet ACV — représentativité Ecoinvent pour le mobilier québécois  
Base : Ecoinvent 3.11, système Cutoff, via openLCA/MCP

Portée : trois cas uniquement — contreplaqué, carton ondulé et électricité d'atelier. Aucun dataset openLCA n'a été modifié.

## Objectif méthodologique

Ce lot teste une règle centrale du diagnostic : **la géographie `CA-QC` d'un dataset Ecoinvent ne suffit pas à démontrer sa représentativité québécoise**. Il faut distinguer la localisation administrative, l'origine des données primaires, la technologie, les intrants, l'énergie, le transport et la profondeur réelle de la régionalisation dans la chaîne.

---

## Cas 1 — Contreplaqué CA-QC

### Identification

- Dataset : `plywood production | plywood | Cutoff, U`
- UUID : `5538194d-92b2-3020-bb3e-fbc59cb71248`
- Produit de référence : `plywood`
- Unité : m³
- Location : Canada, Quebec
- Type : production
- Comparatif RER : UUID `0f52041a-b664-357b-ab50-e48613bff63d`

### Constat Ecoinvent

La description du dataset CA-QC indique qu'il représente la production de contreplaqué au Québec, mais précise aussi qu'il a été créé comme copie du dataset européen correspondant et que les données reposent sur un échantillon de production allemande. Le produit est générique et n'est pas spécifique à une essence ni à une configuration de plis.

La description technique du procédé est identique entre les versions CA-QC et RER. Les quantités technologiques centrales sont également identiques ou se recomposent exactement à la même somme :

| Exchange déterminant | CA-QC | RER | Observation |
|---|---:|---:|---|
| sawlog and veneer log, hardwood | 2,2057 m³ | 2,0452 + 0,1605 m³ | Somme identique ; aucune différence technologique observée |
| urea formaldehyde resin | 87,0726 kg | 87,0726 kg | Quantité identique |
| electricity, medium voltage | 519,338 kWh | 519,338 kWh | Quantité identique ; type de lien `market for` vs `market group for` |
| tap water | 120,688 kg | 120,688 kg | Quantité identique ; type de lien différent |
| municipal solid waste | 0,4814 kg | 0,4814 kg | Quantité identique ; type de lien différent |
| heat, light fuel oil | 53,26 MJ | 53,26 MJ | Quantité identique |
| diesel | 3,497 MJ | 3,497 MJ | Quantité identique |
| steel, low-alloyed | 0,1128 kg | 0,1128 kg | Quantité identique |

Les émissions directes de procédé sont également identiques entre les versions comparées.

### Prudence sur les providers

L'interface MCP utilisée retourne, pour plusieurs exchanges, **le nom textuel du provider mais pas son UUID ni sa localisation résolue**. Lorsque le nom du provider est identique entre CA-QC et RER, cela ne suffit donc pas à démontrer que l'instance géographique sous-jacente est identique. Cette limite n'affecte pas le constat principal : la recette technologique, les consommations et les émissions centrales sont transférées depuis le modèle européen/allemand.

### Représentativité québécoise

| Critère | Évaluation |
|---|---|
| Location administrative | Forte nominalement, mais trompeuse en substance |
| Technologie | Faible |
| Intrants | Faible |
| Énergie | Faible à moyenne : demande technologique allemande, fournisseur potentiel à vérifier |
| Données primaires QC | Aucune identifiée |
| Spécificité métier | Faible : contreplaqué générique, pas bouleau russe |

**Verdict provisoire : localisation QC trompeuse.**

### Décision méthodologique

Utiliser seulement comme **proxy générique**, avec documentation explicite de la dépendance aux données allemandes. Ne pas présenter ce dataset comme représentatif du contreplaqué de bouleau russe utilisé dans le contexte québécois.

---

## Cas 2 — Carton ondulé CA-QC

### Identification

- Dataset : `market for corrugated board box`
- UUID : `2424352b-3df3-3415-9fbf-a6b1eff0ce60`
- Produit de référence : `corrugated board box`
- Unité : kg
- Location : Canada, Québec
- Type : market

### Remontée de la chaîne

Le marché CA-QC est associé à un processus de production lui-même localisé au Québec :

- `corrugated board box production`, UUID `17317a18-28b4-335a-a96d-68789b9bfb70`, location Canada, Quebec ;
- la description documente une collecte sur une usine réelle et donne un mix de production daté de 2008 ;
- l'intrant `containerboard production, fluting medium, semichemical, 40% recycled content`, UUID `27a2145c-86e5-3f1e-8219-5d1720d12cab`, est lui aussi localisé Canada, Québec et décrit comme issu d'une usine québécoise réelle.

Principaux échanges du processus de fabrication des boîtes :

| Exchange | Quantité | Observation QC |
|---|---:|---|
| containerboard, fluting medium | 0,3727 kg | Provider CA-QC confirmé ; donnée primaire québécoise |
| containerboard, linerboard | 0,7434 kg | Plus gros intrant en masse ; géographie non vérifiée dans ce lot |
| electricity, medium voltage | 0,1012 kWh | Géographie non résolue via MCP |
| tap water | 0,969 kg | Non vérifié |
| maize starch | 0,0319 kg | Intrant générique |
| printing ink, offset | 0,0024 kg | Intrant générique |

### Ce qui est réellement régionalisé

- marché final et distances de transport régionales ;
- procédé de fabrication des boîtes issu d'une usine québécoise ;
- fluting medium issu d'une collecte primaire québécoise ;
- intrants forestiers et eau de rivière documentés au niveau du fluting medium.

### Limites

- le **linerboard**, intrant principal en masse, n'a pas encore été inspecté ;
- l'électricité n'est pas encore résolue comme CA-QC ;
- les données de fabrication des boîtes sont datées de 2008 ;
- plusieurs intrants chimiques mineurs restent génériques.

### Représentativité québécoise

| Critère | Évaluation |
|---|---|
| Géographie | Forte |
| Technologie | Forte |
| Intrants | Moyenne |
| Énergie | Faible à moyenne, non vérifiée |
| Transport | Forte |
| Données primaires QC | Forte mais partiellement ancienne |

**Verdict provisoire : QC plausible mais validation nécessaire.**

### Décision méthodologique

Conserver comme **candidat fortement régionalisé et prometteur pour le Québec**, mais ne pas le qualifier sans réserve de représentatif avant vérification du linerboard, de l'énergie et de la fraîcheur des données.

---

## Cas 3 — Électricité d'atelier CA-QC

### Cible

`market for electricity, medium voltage`, location visée `CA-QC`.

### Limite d'accès constatée

Le dataset CA-QC n'a pas pu être isolé avec l'interface MCP actuelle :

1. la recherche par nom retourne 223 processus portant le même nom sans exposer la géographie ;
2. rechercher `Quebec` dans les noms retourne zéro résultat, la localisation n'étant pas incluse dans le champ recherché ;
3. les providers d'exchanges sont retournés comme texte, sans UUID ni localisation ;
4. une extraction en masse de la catégorie électrique a expiré après plusieurs minutes ;
5. les outils nécessitant un product system ne sont pas applicables dans la base actuelle sans créer d'objet supplémentaire.

Un dataset provincial pour l'Île-du-Prince-Édouard a été observé, ce qui confirme l'existence d'une modélisation provinciale canadienne dans Ecoinvent, mais **ce constat ne permet pas de déduire le contenu ni même l'UUID du dataset québécois**.

### Représentativité québécoise

Tous les critères restent inconnus tant que le dataset CA-QC n'est pas isolé directement.

**Verdict provisoire : impossible à déterminer.**

### Décision méthodologique

Ne pas attribuer de classification A/B/C/D pour l'instant. Résoudre ce cas avec un accès permettant un filtre direct par `location = CA-QC` dans openLCA ou via une API/requête locale plus adaptée.

---

## Comparaison des trois cas

| Critère | Contreplaqué CA-QC | Carton CA-QC | Électricité CA-QC |
|---|---|---|---|
| Localisation CA-QC confirmée | Oui | Oui, sur plusieurs niveaux | Non isolée |
| Données primaires QC | Non | Oui | Inconnu |
| Technologie QC | Non, copie allemande | Oui, données de site | Inconnu |
| Intrants QC | Faible | Partiel | Inconnu |
| Énergie QC | Non démontrée | Non vérifiée | Inconnu |
| Transport QC | Non observé ici | Oui, régionalisé | N/A |
| Héritage européen/RoW | Massif | Limité à certains intrants | Inconnu |
| Niveau réel de régionalisation | Cosmétique / partiel | Substantiel | Non déterminé |
| Verdict | Localisation QC trompeuse | QC plausible, validation nécessaire | Impossible à déterminer |
| Action | Proxy générique seulement | Conserver comme candidat régionalisé, valider les limites | Obtenir un accès par géographie |

## Enseignements méthodologiques

1. Le champ `location` est une **condition nécessaire mais jamais suffisante** pour juger la représentativité québécoise.
2. La description narrative est un signal très discriminant : elle permet de distinguer une copie déclarée d'une collecte primaire sur site.
3. La comparaison quantitative avec une version RER/GLO/RoW équivalente permet de détecter une régionalisation seulement cosmétique.
4. Il faut vérifier la **profondeur de régionalisation** : marché final, procédé de production, puis principaux intrants.
5. L'âge des données est un axe distinct de la géographie : une donnée peut être réellement québécoise tout en étant devenue ancienne.
6. La correspondance métier reste indépendante de la géographie : un contreplaqué générique CA-QC ne devient pas un contreplaqué de bouleau russe.
7. Les limitations de l'outil doivent être distinguées des lacunes d'Ecoinvent : l'impossibilité de résoudre l'électricité CA-QC via MCP ne prouve pas l'absence du dataset.

## Grille provisoire de contrôle

| # | Critère | Question de contrôle |
|---|---|---|
| 1 | Location administrative | Le champ `location` correspond-il à la géographie visée ? |
| 2 | Déclaration narrative | Le dataset décrit-il une collecte primaire ou une copie/adaptation d'une autre région ? |
| 3 | Comparaison quantitative | Les montants sont-ils identiques à une version étrangère équivalente ? |
| 4 | Providers d'arrière-plan | Les liens sont-ils régionalisés, et leur géographie peut-elle être résolue ? |
| 5 | Profondeur de régionalisation | La régionalisation descend-elle du marché vers la production et les principaux intrants ? |
| 6 | Âge et source | L'année et la source des données primaires sont-elles connues ? |
| 7 | Spécificité produit | Le produit correspond-il réellement au produit métier visé ? |
| 8 | Résolution technique des providers | L'outil expose-t-il UUID et localisation, ou seulement un nom textuel ? |
| 9 | Faisabilité de l'inspection | Le dataset ou la catégorie sont-ils inspectables avec les outils actuels ? |
| 10 | Écart au contexte métier québécois | Technologie, matières, énergie et pratiques correspondent-elles au contexte réel ? |

**Règle de synthèse provisoire : ne jamais conclure sur la seule base de `location = CA-QC`.** La déclaration narrative, la comparaison quantitative avec une version étrangère et la profondeur de régionalisation sont les contrôles les plus discriminants observés dans ce lot.
