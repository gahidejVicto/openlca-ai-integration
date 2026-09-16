# Liste structurée — prochaine passe OpenLCA

Préparée le **2026-09-16**, dans une session sans accès au connecteur OpenLCA, pour transmission à une instance de Claude disposant de cet accès. Chaque entrée suit le même schéma : produit métier, termes de recherche (français, anglais, synonymes), ce qu'on cherche à déterminer, données déjà connues (sourcées), et la question exacte à résoudre.

**Consignes pour l'instance qui exécutera ces recherches** (rappel des règles déjà appliquées dans les Lots 2A–2G) :
- Utiliser `search_processes` et `search_flows` avec les termes ci-dessous, en documentant le nombre de résultats pour chaque terme (y compris zéro).
- Inspecter (`process_details`) tout candidat trouvé avant de conclure — un nom proche n'est pas une preuve de correspondance.
- Ne jamais déduire une géographie du seul nom d'un process.
- Si aucun résultat n'est trouvé, écrire *« Aucun candidat pertinent identifié avec les méthodes d'interrogation disponibles »*, pas *« Ecoinvent ne contient pas X »*.
- Documenter les UUID réellement retournés par l'outil ; n'en inventer aucun.
- Reporter les résultats dans le référentiel (`docs/materiaux-ebenisterie.md`) et le [tableau transversal des lacunes](tableau-transversal-lacunes-ecoinvent.md) en conservant la distinction `Lacune_Ecoinvent` / `Donnee_entreprise_manquante`.

---

## Priorité 1 — Contreplaqué merisier / yellow birch / Baltic plywood

| Champ | Contenu |
|---|---|
| Produit métier | Contreplaqué merisier / bouleau jaune / Baltic plywood (contreplaqué baltique) — renommé le 2026-09-15, anciennement « contreplaqué de bouleau russe » dans le référentiel |
| Termes FR | contreplaqué merisier ; contreplaqué bouleau jaune ; contreplaqué baltique ; contreplaqué de bouleau |
| Termes EN | birch plywood ; yellow birch plywood ; Baltic birch plywood ; Baltic plywood ; Russian birch plywood *(pour vérifier si l'ancienne appellation métier correspondait réellement à un terme Ecoinvent)* |
| Synonymes / pièges | **Attention à l'ambiguïté linguistique** : « merisier » désigne usuellement le cerisier (*cherry*, *Prunus*) en français standard, mais est employé ici comme synonyme métier régional du bouleau jaune (*yellow birch*, *Betula alleghaniensis*) — ne pas rechercher « cherry plywood » comme si c'était le même produit sans vérifier explicitement laquelle des deux espèces le fournisseur/l'atelier vise réellement. |
| Ce qu'on cherche à déterminer | Un process ou flow Ecoinvent existe-t-il spécifiquement pour un contreplaqué de bouleau (jaune ou autre) ou pour un contreplaqué balte ? Si oui, quelle location, quelle essence documentée, quelle configuration de plis, quelle unité ? |
| Données déjà connues | Lot 2A : `plywood production \| plywood \| Cutoff, U`, UUID `5538194d-92b2-3020-bb3e-fbc59cb71248` (comparatif RER `0f52041a-b664-357b-ab50-e48613bff63d`), location `Canada, Quebec` déclarée copie du modèle allemand — générique, sans essence. Ce dataset reste le seul candidat connu à ce jour et sa pertinence pour l'appellation reprécisée n'a **pas** été revalidée. |
| Question exacte à résoudre | Existe-t-il, dans Ecoinvent 3.11, un process ou un flow distinct portant les termes birch/Baltic/yellow birch appliqués au contreplaqué (pas au bois massif, déjà couvert au Lot 2C) ? Si non, le dataset générique `plywood production` doit-il être conservé comme proxy documenté, ou existe-t-il un candidat plus proche (ex. contreplaqué européen `RER` avec essence feuillue précisée) ? |

## Priorité 2 — Papier mélaminé appliqué en atelier

| Champ | Contenu |
|---|---|
| Produit métier | Papier décor mélaminé appliqué sur panneau support directement en atelier (par opposition au panneau TFL acheté fini, Lot 2B) |
| Termes FR | papier mélaminé ; revêtement mélaminé en atelier ; presse mélamine atelier ; plaquage mélaminé |
| Termes EN | melamine paper ; melamine impregnated paper ; in-house melamine pressing ; small-scale melamine coating ; melamine overlay |
| Synonymes / pièges | Ne pas confondre avec le liant mélamine-formaldéhyde interne au panneau brut (MF), qui est un intrant industriel distinct (voir famille Panneaux, MDF/particules mélaminé). |
| Ce qu'on cherche à déterminer | Le service `coating service, melamine impregnated paper, double-sided` (Lot 2B) est-il applicable, dans sa documentation ou son échelle, à une presse d'atelier de PME plutôt qu'à une ligne industrielle de fabrication de panneaux ? Existe-t-il une alternative dédiée à plus petite échelle ? |
| Données déjà connues | Lot 2B : UUID `4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78`, location Europe (plusieurs usines), grammage 0,604 kg/m² (2 × 0,302 kg/m²/face), documenté pour un contexte industriel de fabrication de panneaux. |
| Question exacte à résoudre | La documentation détaillée de ce service précise-t-elle une échelle de production (industrielle vs atelier) ou des paramètres de presse (température, pression, cycle) permettant de juger sa transférabilité à un usage d'atelier ? Existe-t-il, sinon, un process distinct pour un revêtement mélaminé à plus petite échelle ? |

## Priorité 3 — Bande de chant PE / polyéthylène

| Champ | Contenu |
|---|---|
| Produit métier | Bande de chant en polyéthylène (PE) |
| Termes FR | bande de chant polyéthylène ; chant PE ; bordure de chant polyéthylène |
| Termes EN | PE edge banding ; polyethylene edge band ; edgebanding PE ; LDPE edge band ; HDPE edge band |
| Synonymes / pièges | Vérifier la variante de polyéthylène pertinente (LDPE, HDPE, LLDPE) — Ecoinvent distingue généralement ces variantes comme des marchés matière séparés. |
| Ce qu'on cherche à déterminer | Suivre la même méthode que pour l'ABS et le PVC (Lot 2D) : la matière `polyethylene` (variante à préciser) existe-t-elle comme marché générique ? Un procédé de transformation plausible (extrusion de feuille/profilé, calandrage) existe-t-il, même sans reproduire exactement la géométrie d'une bande de chant ? |
| Données déjà connues | Lot 2D (par analogie, pas encore vérifié pour le PE) : pour l'ABS, matière `market for acrylonitrile-butadiene-styrene copolymer` (UUID `ca074112-8461-32ac-b814-2d7749b7b862`) + procédé `extrusion, plastic pipes` (proxy faible) ; pour le PVC, matière `market for polyvinyl chloride, suspension polymerised` (UUID `fa6532b7-7f96-3bbb-8f42-c300d800d5ff`) + procédé `calendering, rigid sheets` (UUID `d0a9fc16-0991-3ab1-b75e-340dbf4c0506`, proxy avec indice de spécificité PVC). |
| Question exacte à résoudre | Un marché `market for polyethylene, [variante]` existe-t-il, et quel procédé de transformation plastique (extrusion de profilé plat, calandrage) lui est associé dans une location pertinente (Europe/RoW/Global) ? |

## Priorité 4 — Colle contact à base d'eau

| Champ | Contenu |
|---|---|
| Produit métier | Colle contact pour collage de stratifié, formulation à base d'eau prioritaire (précision métier Nicolas, 2026-09-15) |
| Termes FR | colle contact base eau ; adhésif de contact aqueux ; colle contact hydrodispersée |
| Termes EN | water-based contact adhesive ; aqueous contact cement ; water-borne contact adhesive ; dispersion contact adhesive |
| Synonymes / pièges | Ne pas se limiter à la chimie polychloroprène/néoprène (traditionnellement solvantée) — chercher explicitement les familles aqueuses (dispersions acryliques ou SBR utilisées en colle contact). |
| Ce qu'on cherche à déterminer | (a) Un adhésif contact formulé, en particulier à base d'eau, existe-t-il dans Ecoinvent ? (b) Le dataset `market for polychloroprene` cité au Lot 1 est-il accessible via un accès direct OpenLCA (hors limites de l'interrogation MCP rencontrées au Lot 2F) ? |
| Données déjà connues | Lot 2F : aucune brique chimique confirmée avec les méthodes MCP disponibles (`contact adhesive`, `contact glue`, `contact cement`, `solvent based adhesive`, `rubber adhesive`, `neoprene adhesive`, `polychloroprene`, `chloroprene`, `synthetic rubber` — tous testés). UUID antérieur cité (non reconfirmé) : `d1147a50-260c-353a-93c0-def3ebd131d0`. |
| Question exacte à résoudre | Un process ou flow "water-based contact adhesive"/"aqueous adhesive"/"acrylic dispersion adhesive" existe-t-il ? Le dataset `d1147a50-260c-353a-93c0-def3ebd131d0` résout-il vers un process réel via l'accès direct OpenLCA ? |

## Priorité 5 — Colle PVAc/PVA (au-delà du monomère)

| Champ | Contenu |
|---|---|
| Produit métier | Colle PVAc/PVA blanche formulée pour assemblage bois |
| Termes FR | colle PVA formulée ; colle blanche à bois (émulsion) ; dispersion PVAc |
| Termes EN | formulated PVA adhesive ; polyvinyl acetate emulsion adhesive ; PVAc dispersion ; wood glue dispersion ; white wood glue |
| Synonymes / pièges | Distinguer clairement le monomère `vinyl acetate` (déjà identifié, Lot 2F) d'une émulsion/dispersion polymérisée et formulée — chercher des termes de procédé (`emulsion polymerization`, `dispersion`) en plus des termes produit. |
| Ce qu'on cherche à déterminer | Au-delà du monomère, un process de polymérisation en émulsion ou un produit "PVA(c) dispersion/emulsion" formulé existe-t-il ? |
| Données déjà connues | Lot 2F : `market for vinyl acetate`, UUID `9381f4dc-deda-3e02-9cf8-4ef4321b137e`, location Global — monomère seul, aucune polymérisation ni formulation documentée. |
| Question exacte à résoudre | Un process "polyvinyl acetate dispersion/emulsion" ou "adhesive, PVAc/PVA" existe-t-il, distinct du monomère vinyl acetate ? |

## Priorité 6 — Quincaillerie encore non résolue (prioritaire selon Nicolas)

> Ordre de priorité métier confirmé le 2026-09-15 : charnières → coulisses de tiroir → poignées → pieds/niveleurs → ferrures de suspension. Les vis ne sont **pas** prioritaires (modèle simplifié masse+matière jugé probablement suffisant).

### 6.1 Charnière invisible de meuble

| Champ | Contenu |
|---|---|
| Termes FR | charnière invisible ; charnière de meuble ; charnière à cuvette |
| Termes EN | concealed hinge ; cup hinge ; cabinet hinge ; European hinge |
| Ce qu'on cherche à déterminer | Un produit fonctionnel « charnière » existe-t-il ? À défaut, la nomenclature physique (matériaux constitutifs, parts, revêtement) d'un composant proche est-elle documentée quelque part dans la base (ex. quincaillerie générique, ferrures) ? |
| Données déjà connues | Lot 2D : aucun produit fonctionnel identifié ; briques génériques de métal/traitement de surface existent mais sans nomenclature applicable à ce composant. |
| Question exacte | Un process/flow "hinge", "cabinet hardware" ou équivalent existe-t-il, avec une composition documentée (masse, matériaux, revêtement) ? |

### 6.2 Coulisse de tiroir — `À vérifier / choisir modèle fournisseur de référence`

| Champ | Contenu |
|---|---|
| Termes FR | coulisse de tiroir ; glissière de tiroir ; rail télescopique |
| Termes EN | drawer slide ; drawer runner ; telescopic rail ; ball-bearing slide |
| Ce qu'on cherche à déterminer | Un produit fonctionnel existe-t-il ? **Ne pas subdiviser par technologie/dimension** — l'objectif est d'identifier un **modèle standard représentatif unique**, en privilégiant un produit dont la documentation fournisseur (masse, matériaux, longueur) est la plus détaillée disponible, pas d'exhaustivité technologique. |
| Données déjà connues | Lot 2D : aucun produit ni système de roulement caractérisé. |
| Question exacte | Un process/flow "drawer slide"/"telescopic rail"/"ball bearing slide" existe-t-il ? Si plusieurs variantes existent, laquelle dispose de la documentation (masse, matériaux) la plus complète pour servir de modèle de référence unique ? |

### 6.3 Poignée de meuble métallique

| Champ | Contenu |
|---|---|
| Termes FR | poignée de meuble ; poignée métallique |
| Termes EN | cabinet handle ; furniture handle ; pull handle ; aluminium handle |
| Ce qu'on cherche à déterminer | Confirmer si `section bar extrusion, aluminium` (Lot 2D) est un proxy défendable — cela suppose que le matériau réel soit un profilé aluminium, ce qui reste à confirmer côté fournisseur, pas côté Ecoinvent. |
| Données déjà connues | Lot 2D : aucun produit fonctionnel ; brique `section bar extrusion, aluminium` potentiellement pertinente mais conditionnelle. |
| Question exacte | Un process/flow "handle"/"cabinet hardware, handle" existe-t-il ? À défaut, quelle est la documentation exacte de `section bar extrusion, aluminium` (UUID à confirmer) permettant de juger sa transférabilité ? |

### 6.4 Pied niveleur / niveleur

| Champ | Contenu |
|---|---|
| Termes FR | pied de nivellement ; niveleur ; pied réglable |
| Termes EN | leveling foot ; adjustable foot ; furniture leg leveler |
| Ce qu'on cherche à déterminer | Confirmer si `polypropylene + injection moulding` (Lot 2D) couvre le corps plastique ; identifier une brique pour un éventuel insert métallique. |
| Données déjà connues | Lot 2D : aucun produit fonctionnel (les résultats `foot` étaient des faux positifs) ; piste PP + moulage par injection non confirmée pour la composition complète. |
| Question exacte | Un process/flow "leveling foot"/"adjustable foot" existe-t-il ? Une brique pour un insert métallique fileté est-elle disponible en complément du corps plastique ? |

### 6.5 Ferrure métallique de suspension (French cleat) — non encore recherchée

| Champ | Contenu |
|---|---|
| Termes FR | ferrure de suspension ; clé française ; système d'accrochage mural |
| Termes EN | French cleat ; wall mounting hardware ; hanging bracket ; suspension hardware |
| Ce qu'on cherche à déterminer | Aucune recherche menée à ce jour (Lot 2D ne l'a pas couvert). Rechercher d'abord un produit fonctionnel, puis des briques matière/procédé plausibles (acier, aluminium, découpe/pliage). |
| Données déjà connues | Aucune — objet non encore diagnostiqué. |
| Question exacte | Un process/flow "wall bracket"/"hanging hardware"/"French cleat" existe-t-il ? À défaut, quelles briques matière/procédé génériques (acier plié, aluminium) sont disponibles ? |

## Priorité 7 — Emballages non résolus

### 7.1 Film à bulles / papier bulle

| Champ | Contenu |
|---|---|
| Termes FR | film à bulles ; papier bulle ; film de protection à bulles |
| Termes EN | bubble wrap ; bubble film ; air cushion film ; plastic bubble packaging |
| Ce qu'on cherche à déterminer | Un produit fini "bubble wrap" existe-t-il, ou seulement une matière (polyéthylène) + procédé de moulage/extrusion de film ? |
| Données déjà connues | Aucune — objet non encore diagnostiqué. |
| Question exacte | Un process/flow "bubble wrap"/"bubble film"/"packaging film, LDPE" existe-t-il ? |

### 7.2 Matériau d'emballage blanc fin en rouleau (identification à confirmer)

| Champ | Contenu |
|---|---|
| Termes FR | *(à ne pas deviner)* |
| Termes EN | *(à ne pas deviner)* |
| Ce qu'on cherche à déterminer | **Action préalable non-Ecoinvent requise avant toute recherche** : `Identifier précisément le matériau d'emballage avant recherche Ecoinvent`. Obtenir la fiche produit / l'étiquette du rouleau auprès de l'atelier ou du fournisseur (nom commercial, composition — papier, non-tissé, film plastique). |
| Données déjà connues | Matériau blanc, très fin, vendu en gros rouleau, utilisé pour envelopper/protéger les meubles (description métier Nicolas, 2026-09-15) ; composition non confirmée. |
| Question exacte | *Sans objet tant que l'identification n'est pas faite.* Une fois l'identification obtenue, reformuler cette entrée avec les termes de recherche appropriés. |

---

## Rappel de portée

Cette liste couvre les objets explicitement priorisés par Nicolas le 2026-09-15. Elle ne couvre **pas** :
- les 10 objets de « Données transversales » (électricité, transport, chutes, gaz, eau, eaux usées, résidus) — déjà diagnostiqués au Lot 2G/2G-bis et mis en phase ultérieure ;
- l'OSB et l'« autre contreplaqué » (Panneaux) — déprioritisés le 2026-09-15 ;
- les finitions (vernis, scellant, teinture, solvants) et le bois massif (tilleul, bois exotique) — non touchés par les décisions du 2026-09-15, restent `🟡 À valider` dans le référentiel sans changement de priorité relative.

Si une future passe OpenLCA dispose de temps additionnel, ces objets restent des candidats secondaires légitimes, dans l'ordre déjà établi par les priorités P1/P2 du [référentiel](../materiaux-ebenisterie.md) et le [tableau transversal des lacunes](tableau-transversal-lacunes-ecoinvent.md).

---

*Liste préparée sans accès OpenLCA (2026-09-16). Aucun UUID n'est inventé ; tous les UUID cités proviennent des diagnostics déjà sourcés (Lots 2D, 2F). Aucune affirmation d'avoir interrogé la base n'est faite pour les objets listés ici — c'est précisément leur raison d'être dans ce document.*
