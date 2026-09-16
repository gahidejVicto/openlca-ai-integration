La bascule est confirmée : `database_family` retourne maintenant `ecoinvent`, avec les mêmes compteurs que tu as observés (25 412 processus / 14 051 flux / 0 méthode), cohérents avec ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31 sans méthodes d'impact chargées.

Je charge maintenant les outils de recherche nécessaires et lance la PRIORITÉ 1 (contreplaqué merisier / Baltic plywood) depuis zéro, sans réutiliser aucun résultat de la session précédente.PRIORITÉ 1 est traitée en profondeur. Je passe maintenant à la PRIORITÉ 2 (papier mélaminé).PRIORITÉ 3 est également couverte de façon exhaustive. Je passe à la PRIORITÉ 4 (adhésifs PVAc/PVA et colle contact à l'eau).# Diagnostic RECQ36 — Rapport intermédiaire (session en cours)

**Base interrogée réellement via OpenLCA :** ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31 (confirmé par toi, `database_family` forcé à `ecoinvent`, 25 412 processus / 14 051 flux / 0 méthode chargée).

J'ai atteint la limite d'appels d'outils pour cette réponse. Voici l'état complet et honnête du diagnostic à ce stade — PRIORITÉS 1 à 3 traitées de façon exhaustive, PRIORITÉ 4 entamée, PRIORITÉS 5 et 6 non commencées.

---

## PRIORITÉ 1 — Contreplaqué merisier / Baltic plywood

### Requêtes effectuées

`plywood`, `birch`, `yellow birch`, `veneer`, `veneer sheet`, `laminated wood`, `Baltic`, `laminated`, exploration complète de la catégorie ISIC 1621 (136 processus).

### Candidats Ecoinvent trouvés

| Dataset Produit de référence Géographie Unité UUID Commentaire  |                                 |                    |    |                                      |                                                                                                           |
| --------------------------------------------------------------- | ------------------------------- | ------------------ | -- | ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| market for plywood                                              | plywood                         | Europe             | m³ | e0fc51ba-b92d-3f5a-909a-6143109d0356 | Générique, non spécifique à l'essence                                                                     |
| market for plywood                                              | plywood                         | Rest of World      | m³ | b21f0829-ca70-3f94-864b-5fe4c57923f6 | Idem                                                                                                      |
| plywood production                                              | plywood                         | Europe             | m³ | 0f52041a-b664-357b-ab50-e48613bff63d | Basé sur échantillon allemand, bois de sciage/déroulage "hardwood" non spécifié, colle urée-formaldéhyde  |
| plywood production                                              | plywood                         | Rest of World      | m³ | 0b187a5a-6067-3f0f-8fa8-39f3d6ac6721 | **Copie du dataset RER** ("created as copy of the corresponding local dataset for Europe")                |
| plywood production                                              | plywood                         | **Canada, Quebec** | m³ | 5538194d-92b2-3020-bb3e-fbc59cb71248 | **Copie du dataset RER**, même échantillon allemand — la description le dit explicitement                 |
| three and five layered board (production + market)              | three and five layered board    | RoW                | m³ | b878e1de-ef8c-300b-ae44-bcfd95de07ee | **Rejeté** : lamelles sciées massives, aboutées et collées PVAc — solide, pas du contreplaqué de placages |
| hardwood forestry, birch (sawlog and veneer log)                | sawlog and veneer log, hardwood | **Sweden**         | m³ | 885df1ec-96c0-32a2-a869-70779dc48420 | Bois brut en forêt, pas un produit fini                                                                   |

**Aucun** dataset "veneer sheet", "Baltic", "yellow birch" ou spécifique au bouleau/merisier appliqué au contreplaqué n'existe.

### Meilleure correspondance actuelle

`plywood production | plywood | Cutoff, U` — Canada, Quebec (5538194d…) reste le meilleur candidat *disponible*, mais ce n'est **pas** une correspondance représentative.

### Niveau de correspondance

**Proxy** (générique, essence non spécifiée, technologie européenne copiée-collée sur l'étiquette géographique CA-QC).

### Lacunes

- **Représentativité Québec** : le dataset "Canada, Quebec" est une copie administrative du dataset européen — aucune donnée réelle québécoise (essence, procédé, mix électrique) n'y est intégrée. C'est exactement le piège que tu signales : localisation ≠ représentativité.
- **Composition** : essence "hardwood" générique, pas de bouleau jaune/merisier ni de contreplaqué "Baltic birch" (nombreux plis minces, résine phénolique typique).
- **Technologie** : colle urée-formaldéhyde générique vs. les colles typiques du Baltic birch (phénol-formaldéhyde) potentiellement différentes.

### Action recommandée

Rechercher des données fabricant (fournisseurs de Baltic birch plywood) ; envisager une reconstruction à partir de `sawlog and veneer log, hardwood` + procédé de contreplaqué générique en ajustant les paramètres si besoin.

---

## PRIORITÉ 2 — Papier mélaminé appliqué en atelier

### Candidats trouvés

| Dataset Produit de référence Géographie Unité UUID Commentaire  |                                          |        |    |                                      |                                                                                                                                                                                 |
| --------------------------------------------------------------- | ---------------------------------------- | ------ | -- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market for paper, melamine impregnated                          | paper, melamine impregnated              | RoW    | kg | 0a2370fe-1a4c-3401-abae-9143beb78198 | Le papier imprégné lui-même                                                                                                                                                     |
| melamine impregnated paper production                           | paper, melamine impregnated              | Europe | kg | 8d5fa368-3900-3ebb-9760-9b6d5939bcc7 | Détail composition : kraft paper 0,344 kg + résine mélamine-formaldéhyde 0,377 kg + urée-formaldéhyde 0,218 kg pour 1 kg de papier (grammage 302 g/m², papier de base 104 g/m²) |
| market for coating, with melamine impregnated paper             | coating, with melamine impregnated paper | Global | m² | 24ceb336-520a-3e11-bcd1-9c13efd69c6f | **Service d'application** — exclut explicitement le panneau ("input of wood-based board is excluded and should be added manually")                                              |
| coating service, melamine impregnated paper, double-sided       | coating, with melamine impregnated paper | Europe | m² | 4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78 | Application **double face** industrielle (0,604 kg papier/m²)                                                                                                                   |

### Meilleure correspondance actuelle

Le couple `paper, melamine impregnated` (matière) + `coating, with melamine impregnated paper` (procédé d'application) est une **correspondance partielle forte** : Ecoinvent distingue bien matière/procédé et exclut le panneau, ce qui correspond structurellement à ton besoin (application en atelier sur panneau).

### Niveau de correspondance

**Partielle**

### Lacunes

- Le service d'application est calibré pour une **ligne industrielle double face**, pas pour une application artisanale/atelier (probablement simple face, échelle différente).
- Géographie Europe pour le procédé de fabrication du papier — aucune variante CA-QC identifiée.
- Aucun produit "panneau déjà mélaminé fini" n'existe comme dataset unique — bon signe pour éviter la confusion signalée dans le mandat.

### Action recommandée

Vérifier si une application simple-face est modélisable en ne prenant que la moitié du flux "coating" ; chercher des données fournisseur pour la quantité réelle de papier utilisée en atelier québécois.

---

## PRIORITÉ 3 — Bande de chant PE

### Résultat

**Aucune correspondance** — aucun dataset "edge band", "edge banding", "edging" n'existe dans la base.

### Matières génériques disponibles comme proxys potentiels

| Matière Dataset Géographie UUID  |                                                       |                         |                                                                             |
| -------------------------------- | ----------------------------------------------------- | ----------------------- | --------------------------------------------------------------------------- |
| PE-LD                            | market for polyethylene, low density, granulate       | Global                  | 08d7cf9a-4301-321f-947c-06849afd126c                                        |
| PP                               | market for polypropylene, granulate                   | (à vérifier géographie) | 881eed86-35c6-3cc2-a352-263e9c4c34ee                                        |
| ABS                              | market for acrylonitrile-butadiene-styrene copolymer  | (à vérifier)            | ca074112-8461-32ac-b814-2d7749b7b862                                        |
| PVC                              | market for polyvinyl chloride, suspension polymerised | (à vérifier)            | fa6532b7-7f96-3bbb-8f42-c300d800d5ff / 68a7d84c-01f2-3731-9d49-67a4054f6c90 |

Procédés de transformation disponibles : `extrusion, plastic pipes` (profil rond) et `extrusion, plastic film` (film mince) — **aucun ne correspond** à une extrusion de profilé plat de type bande de chant.

### Niveau de correspondance

**Aucune correspondance satisfaisante** pour le produit fonctionnel ; proxys matière disponibles mais non validés fonctionnellement.

### Lacunes

Fonction (produit fini absent), technologie (procédé d'extrusion profilé absent), représentativité Québec (non testée), données fabricant nécessaires pour trancher entre PE/PP/ABS/PVC selon le vrai produit utilisé en ébénisterie.

---

## PRIORITÉ 4 — Adhésifs (entamée, incomplète)

### PVAc/PVA

- **Aucun** dataset "polyvinyl acetate" (le polymère) n'existe dans la base.
- Seuls présents : `vinyl acetate` (le monomère précurseur) et `ethylene vinyl acetate copolymer` (EVA — copolymère différent, utilisé en hot-melt/mousses, pas en colle blanche PVAc classique).
- **Aucun** dataset "wood glue" ni "dispersion adhesive" (recherche exacte vide).
- Recherches encore à faire : "emulsion adhesive", "contact adhesive", "adhesive" générique, catégorie ISIC adhésifs (2029 probablement).

### Conclusion provisoire

**Absence probable** de correspondance directe ou même de proxy polymère pour la colle PVAc — à confirmer par une recherche plus large sur le terme générique "adhesive" avant de conclure définitivement.

### Colle contact à base d'eau

**Non commencé.**

---

## PRIORITÉ 5 — Quincaillerie

**Non commencé.**

## PRIORITÉ 6 — Emballages

**Non commencé.**

---

## Points de traçabilité déjà exploitables (HANDOFF partiel)

1. **Confirmation critique** : les trois datasets "plywood production" (RER / RoW / CA-QC) partagent le même échantillon de données allemand — le dataset CA-QC est une copie géographique, pas une donnée régionale réelle. Ancienne hypothèse d'une éventuelle "représentativité Québec" du dataset CA-QC est **invalidée**.
2. **Nouveau** : dataset "three and five layered board" identifié et explicitement écarté (solide massif abouté, pas du placage) — à ne pas confondre avec du contreplaqué dans le référentiel.
3. **Nouveau** : couple papier mélaminé (matière, kg) / service de couchage (m², double face, panneau exclu) constitue la meilleure structure disponible pour représenter l'application en atelier — nécessite validation simple-face vs double-face.
4. **Confirmé ABSENT** : bande de chant (toute matière), PVAc/PVA polymère, colle blanche fonctionnelle, contreplaqué Baltic/bouleau jaune spécifique.
5. **Recherches supplémentaires nécessaires** : adhésifs (emulsion/contact/générique), PRIORITÉ 5 et 6 en entier, vérification géographies exactes des marchés PP/ABS/PVC.

Je peux poursuivre l'analyse (PRIORITÉ 4 complète, 5, 6, et le tableau transversal final) dans une prochaine réponse dès que tu me le confirmes.