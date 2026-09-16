# RECQ36 — Diagnostic des écarts Ecoinvent / OpenLCA
**Matériaux et composants en ébénisterie québécoise**

Rapport de réconciliation fondé sur une interrogation réelle et complète de la base via le connecteur MCP OpenLCA. **Cette version remplace intégralement la précédente (intégrée par erreur dans le commit `aaabecd`), dont la totalité des résultats est invalidée** : cette session-là avait été produite alors que la mauvaise base OpenLCA (`cups`) était ouverte dans le logiciel après un changement de poste de travail, et non Ecoinvent. Aucun UUID, géographie, résultat nul ou conclusion de cette ancienne session n'est réutilisé ici, sauf reconfirmation indépendante dans la présente interrogation ou dans un diagnostic antérieur correctement sourcé (Lots 2A–2G).

Les deux comptes rendus bruts de la session courante sont conservés pour traçabilité :
- [`mcp-ecoinvent-3.11-partie-1.md`](mcp-ecoinvent-3.11-partie-1.md) — PRIORITÉS 1 à 3, début de la PRIORITÉ 4.
- [`mcp-ecoinvent-3.11-partie-2.md`](mcp-ecoinvent-3.11-partie-2.md) — fin de la PRIORITÉ 4, PRIORITÉS 5 et 6, tableau transversal, HANDOFF.

## Résolution de l'anomalie `database_family`

La session invalidée avait retourné `database_family: "flcac"`, avec 14 912 process / 23 142 flows / 45 méthodes d'impact / 8 systèmes de produits. **Cause identifiée :** après un changement de poste de travail, c'est la base OpenLCA `cups` qui était restée ouverte dans le logiciel, pas Ecoinvent — `flcac` n'est pas une anomalie intrinsèque d'Ecoinvent, seulement le nom de la mauvaise base chargée à ce moment-là. Ce statut « à vérifier » est désormais obsolète et ne doit plus être présenté comme une anomalie ouverte.

Après ouverture manuelle de **ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31** et forçage explicite de `database_family` à `ecoinvent`, `database_info` retourne : **25 412 processus, 14 051 flux, 0 méthode d'impact chargée**. C'est la base effectivement interrogée pour l'ensemble des résultats ci-dessous.

---

## PRIORITÉ 1 — Contreplaqué merisier / Baltic birch plywood

### Requêtes effectuées
`plywood`, `birch`, `yellow birch`, `veneer`, `veneer sheet`, `laminated wood`, `Baltic`, `laminated`, plus exploration complète de la catégorie ISIC 1621 (136 process).

### Candidats Ecoinvent trouvés

| Dataset | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| `market for plywood` | plywood | Europe | m³ | `e0fc51ba-b92d-3f5a-909a-6143109d0356` | Générique, non spécifique à l'essence |
| `market for plywood` | plywood | Rest of World | m³ | `b21f0829-ca70-3f94-864b-5fe4c57923f6` | Idem |
| `plywood production` | plywood | Europe | m³ | `0f52041a-b664-357b-ab50-e48613bff63d` | Basé sur un échantillon **allemand**, bois de sciage/déroulage « hardwood » non spécifié, colle urée-formaldéhyde |
| `plywood production` | plywood | Rest of World | m³ | `0b187a5a-6067-3f0f-8fa8-39f3d6ac6721` | **Copie du dataset RER** (« created as copy of the corresponding local dataset for Europe ») |
| `plywood production` | plywood | **Canada, Quebec** | m³ | `5538194d-92b2-3020-bb3e-fbc59cb71248` | **Copie du dataset RER**, même échantillon allemand — la description du dataset le dit explicitement |
| `three and five layered board` (production + marché) | three and five layered board | Rest of World | m³ | `b878e1de-ef8c-300b-ae44-bcfd95de07ee` | **Rejeté** : lamelles de bois massif sciées, aboutées et collées PVAc — un panneau structurel massif, pas du contreplaqué de placages. Faux-ami explicite, à ne jamais confondre avec du contreplaqué dans le référentiel |
| `hardwood forestry, birch` (sawlog and veneer log) | sawlog and veneer log, hardwood | Sweden | m³ | `885df1ec-96c0-32a2-a869-70779dc48420` | Bois rond en forêt, pas un produit fini |

**Aucun** dataset « veneer sheet », « Baltic », « yellow birch » ou spécifique au bouleau/merisier appliqué au contreplaqué n'existe dans cette base, avec ces requêtes.

> **Cohérence avec un diagnostic antérieur (Lot 2A) :** le dataset `plywood production | Canada, Quebec` (`5538194d-…`) et son comparatif Europe (`0f52041a-…`) avaient déjà été identifiés au Lot 2A, avant la contamination `cups`. Ils sont ici **reconfirmés indépendamment** par cette nouvelle interrogation Ecoinvent 3.11 — ce ne sont pas de nouveaux résultats, mais une confirmation croisée du même constat.

### Meilleure correspondance actuelle
`plywood production | plywood | Cutoff, U` — Canada, Quebec (`5538194d-…`) reste le meilleur candidat *disponible*, mais **ce n'est pas une correspondance représentative** : c'est une copie administrative du dataset européen.

### Niveau de correspondance
**Proxy / ÉCART** — essence non spécifiée (« hardwood » générique), technologie européenne copiée-collée sur l'étiquette géographique CA-QC.

### Lacunes
- **Représentativité Québec :** le dataset « Canada, Quebec » est une copie administrative du dataset européen — aucune donnée réelle québécoise (essence, procédé, mix électrique) n'y est intégrée. **La localisation CA-QC ne signifie pas représentativité québécoise.**
- **Composition :** essence « hardwood » générique, pas de bouleau jaune/merisier ni de contreplaqué « Baltic birch » (nombreux plis minces, résine phénolique typique).
- **Technologie :** colle urée-formaldéhyde générique, potentiellement différente des colles typiques du Baltic birch (phénol-formaldéhyde).

### Action recommandée
Rechercher des données fabricant (fournisseurs de Baltic birch plywood). Envisager une reconstruction à partir de `sawlog and veneer log, hardwood` + procédé de contreplaqué générique en ajustant les paramètres si besoin. Ne pas chercher davantage dans Ecoinvent : la base ne contient rien de plus spécifique.

---

## PRIORITÉ 2 — Papier mélaminé appliqué en atelier

### Candidats trouvés

| Dataset | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| `market for paper, melamine impregnated` | paper, melamine impregnated | Rest of World | kg | `0a2370fe-1a4c-3401-abae-9143beb78198` | Le papier imprégné lui-même |
| `melamine impregnated paper production` | paper, melamine impregnated | Europe | kg | `8d5fa368-3900-3ebb-9760-9b6d5939bcc7` | Composition détaillée : 0,344 kg kraft paper + 0,377 kg résine mélamine-formaldéhyde + 0,218 kg résine urée-formaldéhyde pour 1 kg de papier fini ; grammage 302 g/m² (dont 104 g/m² de papier de base) |
| `market for coating, with melamine impregnated paper` | coating, with melamine impregnated paper | Global | m² | `24ceb336-520a-3e11-bcd1-9c13efd69c6f` | **Service d'application** — exclut explicitement le panneau support (« input of wood-based board is excluded and should be added manually ») |
| `coating service, melamine impregnated paper, double-sided` | coating, with melamine impregnated paper | Europe | m² | `4bce9bba-0bf8-3f27-aaaf-ed89e3fd2a78` | Application **double face** industrielle (0,604 kg papier/m²) |

> **Cohérence avec un diagnostic antérieur (Lot 2B) :** le service `coating service, melamine impregnated paper, double-sided` (`4bce9bba-…`) avait déjà été documenté au Lot 2B, avant la contamination `cups`. Il est ici **reconfirmé indépendamment** par cette interrogation Ecoinvent 3.11.

### Meilleure correspondance actuelle
Le couple `paper, melamine impregnated` (matière) + `coating, with melamine impregnated paper` (procédé d'application) — matière + application + panneau support restant séparés, conformément à la structure attendue. Le service d'application **exclut explicitement le panneau support**.

### Niveau de correspondance
**Partielle forte / À vérifier** — Ecoinvent distingue bien matière et procédé, et exclut le panneau, ce qui correspond structurellement au besoin métier (application en atelier sur panneau). Ce n'est toutefois pas une correspondance directe : le service documenté est calibré pour une ligne industrielle double face, dont la représentativité pour une application simple face en atelier de PME reste à trancher.

### Lacunes
- Le service d'application est calibré pour une **ligne industrielle double face**, pas pour une application artisanale/atelier (probablement simple face, échelle différente) — **à vérifier avant intégration**.
- Géographie Europe pour le procédé de fabrication du papier — aucune variante CA-QC identifiée.
- Aucun produit « panneau déjà mélaminé fini » n'existe comme dataset unique — ce qui évite la confusion signalée dans le mandat (pas de risque de double comptage panneau + application).

### Action recommandée
Vérifier si une application simple face est modélisable en ne prenant qu'une partie du flux « coating » (p. ex. la moitié du flux double-face, sous réserve de validation méthodologique). Chercher des données fournisseur pour la quantité réelle de papier utilisée en atelier québécois avant d'intégrer ce couple sans réserve.

---

## PRIORITÉ 3 — Bande de chant PE

### Résultat
**Aucune correspondance** — aucun dataset « edge band », « edge banding », « edging » n'existe dans la base, avec ces requêtes.

### Matières génériques disponibles comme briques potentielles

| Matière | Dataset | Géographie | UUID |
|---|---|---|---|
| PE-LD | `market for polyethylene, low density, granulate` | Global | `08d7cf9a-4301-321f-947c-06849afd126c` |
| PP | `market for polypropylene, granulate` | à vérifier | `881eed86-35c6-3cc2-a352-263e9c4c34ee` |
| ABS | `market for acrylonitrile-butadiene-styrene copolymer` | à vérifier | `ca074112-8461-32ac-b814-2d7749b7b862` |
| PVC | `market for polyvinyl chloride, suspension polymerised` | à vérifier | `fa6532b7-7f96-3bbb-8f42-c300d800d5ff` / `68a7d84c-01f2-3731-9d49-67a4054f6c90` |

> **Cohérence avec un diagnostic antérieur (Lot 2D) :** les UUID ABS (`ca074112-…`) et PVC suspension polymérisée (`fa6532b7-…`) avaient déjà été documentés au Lot 2D, avant la contamination `cups`. Ils sont ici **reconfirmés indépendamment**. La variante « bulk polymerised » trouvée par la session invalidée (`17671bec-…`) n'est pas reconfirmée par cette interrogation ; seule la variante « suspension polymerised » l'est.

Procédés de transformation disponibles : `extrusion, plastic pipes` (profil rond) et `extrusion, plastic film` (film mince) — **aucun ne correspond** à une extrusion de profilé plat de type bande de chant. PE-LD, PP, ABS et PVC sont uniquement des briques matière potentielles ; aucun procédé d'extrusion trouvé ne correspond directement à une bande de chant plate.

### Niveau de correspondance
**Absent / Reconstruction** — produit fonctionnel absent ; briques matière disponibles mais non validées fonctionnellement.

### Lacunes
Fonction (produit fini absent), technologie (procédé d'extrusion de profilé plat absent), représentativité Québec (non testée), données fabricant nécessaires pour trancher entre PE/PP/ABS/PVC selon le vrai produit utilisé en ébénisterie.

### Action recommandée
Ne pas conclure qu'un des quatre polymères est LE bon proxy sans données fabricant (masse linéique, épaisseur, largeur, composition exacte).

---

## PRIORITÉ 4 — Adhésifs

### Requêtes effectuées
`polyvinylacetate`, `polyvinyl acetate`, `vinyl acetate`, `wood glue`, `dispersion adhesive`, `contact adhesive`, `emulsion` (101 résultats — tous liés aux peintures/déchets, aucun adhésif bois), `adhesive` (recherche exhaustive, 19 résultats).

### Candidats Ecoinvent trouvés

| Dataset | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| `market for vinyl acetate` | vinyl acetate | — | kg | `a4bd8120-5784-3dd9-bee6-a8473d385b7f` | **Monomère précurseur**, pas le polymère PVAc |
| `market for ethylene vinyl acetate copolymer` | ethylene vinyl acetate copolymer | — | kg | `c773d766-c8ff-3493-88ea-09492fbc0048` | Copolymère EVA — chimie différente (hot-melt/mousses), pas la colle blanche PVAc classique |
| `market for polyurethane adhesive` | polyurethane adhesive | Global | kg | `ad1da3c6-5cb8-364d-8fb5-e96e9dca9e93` | Colle PUR **formulée**, mais destinée au bois lamellé structural (CLT) — isocyanate, sans formaldéhyde. Chimie et usage distincts d'une colle blanche PVAc ou d'une colle multimatériaux d'atelier |
| `market for melamine urea formaldehyde adhesive` | melamine urea formaldehyde adhesive | Global | kg | `e7001c37-5a60-335b-bf15-ad7395226509` | Colle MUF pour bois lamellé-collé (glulam) — chimie et usage industriel distincts ; les adhésifs UF/MUF ne sont pas utilisés directement en atelier (intrants industriels de panneaux) |
| `adhesive, for metal` | adhesive, for metal | — | kg | `4a5da11b-2019-326b-990e-254d96e9acb3` | Hors sujet (colle métal) |
| `adhesive mortar` / `bitumen adhesive compound` | — | — | — | — | Hors sujet (construction/étanchéité) |

**Ne jamais présenter comme équivalents directs d'une colle blanche PVAc ou d'une colle contact d'atelier :** vinyl acetate (monomère, pas le polymère), EVA (copolymère différent), PUR (`ad1da3c6-…`, formulé mais pour CLT structural), MUF (`e7001c37-…`, formulé mais pour glulam industriel), adhesive for metal. Ils ont une chimie et/ou une fonction différentes.

### Meilleure correspondance actuelle
**Aucune.** Ni le polymère PVAc, ni une formulation de colle blanche/colle contact à l'eau ne sont présents dans la base.

### Niveau de correspondance
**Absent** — pour la colle PVAc/PVA comme pour la colle contact à base d'eau.

### Lacunes
- **Fonction :** aucun produit fonctionnel « colle blanche bois » ni « colle contact à l'eau ».
- **Matière/composition :** le polymère PVAc lui-même est absent (seul son monomère, l'acétate de vinyle, existe).
- Les colles bois formulées disponibles (PUR, MUF) sont chimiquement et fonctionnellement non substituables à une colle PVAc en émulsion aqueuse ou à une colle contact — proxy jugé non pertinent sans hypothèse forte, à documenter uniquement comme dernier recours si nécessaire.

### Action recommandée
Reconstruction envisageable à partir du monomère vinyl acetate + un procédé générique de polymérisation en émulsion (existence non vérifiée ailleurs dans la base, hors périmètre de cette recherche — reste une piste ouverte). Sinon, recours à des données fabricant/fiche technique (EPD fournisseur) pour la colle PVAc et la colle contact réellement utilisées en atelier.

---

## PRIORITÉ 5 — Quincaillerie

### Requêtes effectuées
`hinge`, `drawer slide`, `furniture handle`, `levelling foot`, `French cleat`, `wood screw`, `screw`, `furniture fitting`, `metal fastener`, plus exploration de la catégorie ISIC 259 (Manufacture of other fabricated metal products — 473 process, échantillon de 30 examiné).

### Résultat par famille

| Famille | Produit fonctionnel ? | Procédé proche ? | Matériaux/procédés génériques disponibles pour reconstruction |
|---|---|---|---|
| Charnière (hinge/cabinet hinge) | **Absent** | Non | Acier/laiton + services d'emboutissage (`deep drawing, steel`), usinage (`turning`, `milling`), revêtement (`zinc coating, pieces`) |
| Coulisse de tiroir (drawer slide/runner) | **Absent** | Non | Acier (tôle/profilé) + services de formage à froid, extrusion d'aluminium (`impact extrusion of aluminium`) |
| Poignée (furniture handle) | **Absent** | Non | Zinc/laiton/acier + moulage/usinage |
| Patin de nivellement (levelling foot) | **Absent** | Non | Plastique (PP/POM non trouvé spécifiquement) + acier fileté |
| Taquet français / suspension fitting | **Absent** | Non | Acier plié/percé |
| Vis à bois (wood screw) | **Absent** | Non | Non exploré en détail — conforme à la consigne de ne pas surinvestir |

### Constat transversal
La catégorie ISIC 259 ne contient **que des services de transformation métallique génériques** (fraisage, tournage, perçage, emboutissage, extrusion à froid, revêtement zinc, traitement thermique) et des matières premières (acier, laiton, aluminium, fonte) — **aucun produit fini de quincaillerie meuble** (charnière, coulisse, poignée, patin, taquet, vis) n'existe comme dataset autonome dans Ecoinvent. Aucun UUID de brique n'a été relevé nommément dans cette session pour ces services génériques (noms de process seulement) ; ne pas leur substituer les UUID de briques génériques cités dans d'autres lots (Lot 2D, vis) sans nouvelle vérification.

### Niveau de correspondance
**Absent** pour toutes les familles, sans exception.

### Lacunes
Fonction (produit fini totalement absent) pour toutes les familles. Une reconstruction complète (masse de métal + suite d'opérations d'usinage/formage) serait nécessaire pour chaque famille, avec un effort disproportionné par rapport à la précision atteignable sans données fabricant réelles (masses, alliages, procédés exacts).

### Action recommandée
Pour les charnières et coulisses (masse/complexité plus importantes, à prioriser) : obtenir des fiches techniques fabricant (masse par pièce, matière — acier zingué le plus souvent) et construire un proxy manuel : masse d'acier (`market for steel, low-alloyed`) + revêtement zinc + une combinaison raisonnable d'opérations de formage (emboutissage + perçage). Pour poignées/patins/taquets/vis : proxy simplifié matière seule (acier ou zinc selon le produit), sans tenter de reconstruire le procédé complet — ne pas surinvestir sur les petites vis.

---

## PRIORITÉ 6 — Emballages

### Requêtes effectuées
`corrugated board` (8 résultats), `bubble wrap` (0), `polyethylene foam` (0), `expanded polystyrene` (16, tous déchets/traitement), `polystyrene foam` (14, tous isolation périmétrique rigide), `stretch film` (0), `packaging film` (3), `foam sheet` (0).

### Candidats Ecoinvent trouvés

| Dataset | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| `market for corrugated board box` | corrugated board box | **Canada, Québec** | kg | `2424352b-3df3-3415-9fbf-a6b1eff0ce60` | **Marché explicitement régional** — la documentation Ecoinvent précise elle-même que ce type de produit se négocie localement, pas globalement. **Contrairement au contreplaqué CA-QC (copie du dataset RER), ce dataset a une base méthodologique qui justifie sa représentativité québécoise.** |
| `corrugated board box production` | corrugated board box | plusieurs géographies | kg | `17317a18-28b4-335a-a96d-68789b9bfb70` et autres | Production sous-jacente |
| `market for packaging film, low density polyethylene` | packaging film, low density polyethylene | Global | kg | `1b3c1341-0769-32dc-92d7-00fb8891e3d5` | Film LDPE plat générique (usages variés : alimentaire, construction, électroménager). Pas de mousse, pas de bulles |
| `polystyrene foam slab` (for perimeter insulation) | polystyrene foam slab for perimeter insulation | — | m²/kg | `5be8986d-89e3-387f-ba00-fa6e12b6fc7f` et variantes | **Hors sujet** : mousse rigide XPS destinée à l'isolation de fondation, pas un matériau d'emballage souple |

> **Cohérence avec un diagnostic antérieur (Lot 2A) :** le dataset `market for corrugated board box` CA-QC (`2424352b-…`) avait déjà été documenté au Lot 2A, avant la contamination `cups`. Il est ici **reconfirmé indépendamment** par cette interrogation Ecoinvent 3.11 — contrairement au contreplaqué CA-QC, ce dataset résiste à la vérification.

### Sur le matériau non identifié (« matériau blanc très fin, en gros rouleau, pour envelopper les meubles »)
Deux familles de candidats existent dans la base, avec des natures très différentes, et aucune n'est retenue comme identification :
1. **Film LDPE plat** (`packaging film, low density polyethylene`) — mince, souple, mais **non alvéolé/non mousseux**. Correspondrait à un usage de type film étirable ou pellicule de protection simple.
2. **Mousse de polystyrène rigide** (`polystyrene foam slab`) — épaisse, rigide, destinée au bâtiment. **Ne correspond pas** à la description (pas souple, pas en rouleau fin, pas destinée à l'emballage meuble).

Aucun candidat ne représente une **mousse PE/PP fine et souple en rouleau** ni du bubble wrap. Pour identifier le bon candidat (ou confirmer l'absence), il faudrait savoir si le matériau réel est :
- un film plastique plat non alvéolé (→ `packaging film, LDPE` proxy potentiel) ;
- une mousse PE ou PP alvéolée (→ **aucun candidat Ecoinvent**, proxy à construire à partir de résine PE/PP + un procédé de moussage, non trouvé dans cette recherche) ;
- un non-tissé synthétique (→ non recherché dans cette session, piste à explorer si les deux hypothèses précédentes sont écartées).

### Niveau de correspondance
- Carton ondulé : **OK** (correspondance directe et représentativité Québec crédible et documentée).
- Film LDPE : **Proxy potentiel** seulement, si le matériau réel s'avère être un film plat.
- Mousse de protection meuble : **Absent** — aucune correspondance satisfaisante, décision à prendre après identification physique du produit réel.

### Action recommandée
Obtenir un échantillon ou une fiche technique du matériau réel (grammage, composition — PE vs PP vs non-tissé, alvéolé ou non) avant de choisir entre proxy film LDPE ou reconstruction mousse. Ne pas trancher arbitrairement.

---

## TABLEAU TRANSVERSAL FINAL

| Produit métier | Dataset candidat | Géographie | Correspondance | Composition | Technologie | Représentativité QC | Proxy/reconstruction | Données fabricant nécessaires | Statut |
|---|---|---|---|---|---|---|---|---|---|
| Contreplaqué merisier/Baltic | `plywood production` (`5538194d-…`) | Canada, Quebec | Proxy | Hardwood générique, non spécifié | Copie du procédé RER (échantillon allemand) | **Non** — copie administrative, pas de donnée réelle QC | Oui | Oui | ÉCART |
| Papier mélaminé — matière | `paper, melamine impregnated` (`0a2370fe-…`) | RoW | Partielle | Kraft + résine mélamine-formaldéhyde + urée-formaldéhyde | Conforme | Non testée | Non nécessairement | Souhaitable (grammage réel) | À VÉRIFIER |
| Papier mélaminé — application | `coating, with melamine impregnated paper` (`24ceb336-…`) | Global | Partielle | — | Application double face industrielle, panneau exclu | N/A | Ajustement simple/double face | Oui (grammage réel, mode d'application) | À VÉRIFIER |
| Bande de chant PE | Aucun | — | Absent | — | — | N/A | Oui (PE/PP/ABS/PVC générique, à trancher) | Oui (matière exacte + procédé) | ABSENT |
| Colle PVAc/PVA | Aucun | — | Absent | Seul le monomère (vinyl acetate) existe | — | N/A | Oui (reconstruction chimique incertaine) | Oui | ABSENT |
| Colle contact à l'eau | Aucun | — | Absent | — | — | N/A | Oui | Oui | ABSENT |
| Charnière | Aucun | — | Absent | — | Services d'usinage/formage génériques disponibles (sans UUID retenu) | N/A | Oui (acier/laiton + procédés) | Oui (masse, alliage) | ABSENT |
| Coulisse de tiroir | Aucun | — | Absent | — | Idem | N/A | Oui | Oui | ABSENT |
| Poignée de meuble | Aucun | — | Absent | — | Idem | N/A | Oui (simplifié) | Oui | ABSENT |
| Patin de nivellement | Aucun | — | Absent | — | Idem | N/A | Oui (simplifié) | Oui | ABSENT |
| Taquet français | Aucun | — | Absent | — | Idem | N/A | Oui (simplifié) | Oui | ABSENT |
| Vis à bois | Aucun | — | Absent (non approfondi, conforme consigne) | — | — | N/A | Oui (simplifié) | Non prioritaire | ABSENT |
| Carton ondulé (boîte) | `market for corrugated board box` (`2424352b-…`) | **Canada, Québec** | **OK** | Kraftliner/testliner + fluting medium | Conforme, marché régional documenté | **Oui** — représentativité justifiée par la méthodologie même du dataset | Non | Non | OK |
| Film/mousse d'emballage meuble | `packaging film, LDPE` (`1b3c1341-…`) *ou* aucun | Global / — | Proxy incertain / Absent | LDPE plat, non alvéolé | — | Non testée | Oui, selon nature réelle du matériau | Oui (composition réelle : film plat vs mousse) | À VÉRIFIER |

Statuts utilisés : OK, ÉCART, À VÉRIFIER, ABSENT, RECONSTRUCTION, N/A — conformément à la légende demandée. Ces statuts ne sont ni un score carbone ni une métrique quantitative.

---

# HANDOFF CLAUDE CODE

## 1. Corrections factuelles à apporter
- Le dataset `plywood production | plywood | Cutoff, U` localisé **Canada, Quebec** (UUID `5538194d-92b2-3020-bb3e-fbc59cb71248`) est une copie administrative du dataset Europe (même échantillon de données allemand, même colle urée-formaldéhyde, même essence « hardwood » générique). **Toute mention traitant ce dataset comme « représentatif du Québec » doit être corrigée.**
- À l'inverse, le dataset `corrugated board box` localisé **Canada, Québec** (UUID `2424352b-3df3-3415-9fbf-a6b1eff0ce60`) a une représentativité régionale **crédible et documentée par Ecoinvent lui-même** (marché local, pas d'échange global pour ce type de produit) — distinction importante à conserver dans le référentiel entre les deux cas « CA-QC » : localisation ≠ représentativité, mais ce n'est pas vrai de façon uniforme pour tous les datasets CA-QC.
- L'anomalie `database_family: "flcac"` de la session précédente est résolue : cause = mauvaise base (`cups`) restée ouverte après changement de poste. Ne plus la présenter comme une anomalie Ecoinvent ouverte.

## 2. Nouveaux datasets identifiés
- `paper, melamine impregnated` (matière, kg, `0a2370fe-…`) + `coating, with melamine impregnated paper` (service d'application, m², panneau exclu, `24ceb336-…`) — structure en deux datasets bien adaptée pour représenter séparément matière et procédé d'application en atelier ; `coating service, melamine impregnated paper, double-sided` (`4bce9bba-…`, Europe) reconfirme le Lot 2B.
- `three and five layered board` (`b878e1de-…`) — identifié et **explicitement écarté** comme faux-ami pour le contreplaqué (bois massif aboutis-collé, pas du placage).
- Datasets de matières génériques utilisables comme briques de proxy pour la bande de chant : PE-LD (`08d7cf9a-…`), PP (`881eed86-…`), ABS (`ca074112-…`, reconfirme Lot 2D), PVC suspension polymérisée (`fa6532b7-…` / `68a7d84c-…`, reconfirme Lot 2D).
- Adhésifs formulés existants mais non équivalents : `market for polyurethane adhesive` (`ad1da3c6-…`, CLT) et `market for melamine urea formaldehyde adhesive` (`e7001c37-…`, glulam) — chimie et usage industriels distincts d'une colle blanche PVAc ou d'une colle contact d'atelier.
- Services de métallurgie génériques (emboutissage, extrusion d'aluminium, revêtement zinc, tournage, fraisage) disponibles en ISIC 259 pour une future reconstruction quincaillerie — noms de process identifiés, aucun UUID de brique retenu cette session.

## 3. UUID et géographies vérifiés
Tous les UUID cités ci-dessus ont été obtenus par requête directe (`search_processes`/`search_flows` puis `process_details`) dans la base `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` confirmée (`database_family: ecoinvent`, 25 412 processus / 14 051 flux / 0 méthode). Aucun n'est reconstruit de mémoire.

## 4. Anciennes hypothèses invalidées
- L'hypothèse qu'un contreplaqué CA-QC serait plus représentatif qu'un dataset RER est **invalidée** — c'est la même donnée sous une étiquette géographique différente.
- Tous les résultats de la session `cups` (UUID, géographies, résultats nuls, conclusions, anomalie `database_family: "flcac"`) sont **invalidés en tant que preuves Ecoinvent** ; seuls les éléments reconfirmés ci-dessus ou déjà sourcés dans les Lots 2A–2G restent valides.

## 5. Correspondances toujours non résolues
- Contreplaqué merisier/Baltic birch : aucune correspondance directe, proxy générique seulement.
- Papier mélaminé : application simple face vs double face non tranchée ; échelle atelier vs industrielle non confirmée.
- Bande de chant PE : matière proxy non tranchée (PE/PP/ABS/PVC), aucun procédé d'extrusion de profilé plat trouvé.
- Colle PVAc et colle contact à l'eau : absence totale, reconstruction incertaine.
- Toute la quincaillerie (charnières, coulisses, poignées, patins, taquets, vis) : absence totale, reconstruction à construire au cas par cas après données fabricant.
- Matériau d'emballage meuble (film fin blanc en rouleau) : nature physique du matériau réel inconnue, deux hypothèses non départagées (film plat LDPE vs mousse alvéolée absente de la base) ; non-tissé non exploré.

## 6. Données fabricant désormais nécessaires
- Contreplaqué : essence réelle, type de colle, origine géographique réelle du bois.
- Papier mélaminé : grammage réel, application simple/double face.
- Bande de chant : matière exacte (PE/PP/ABS/PVC), procédé (extrusion profilée).
- Colles : formulation exacte (teneur en eau, % PVAc, additifs) pour colle blanche et colle contact.
- Quincaillerie : masse par pièce et alliage pour charnières et coulisses en priorité ; ne pas surinvestir sur les vis.
- Emballage meuble : composition et structure (film plat vs mousse vs non-tissé) du matériau en rouleau.

## 7. Recherches supplémentaires encore ouvertes
- Vérifier l'existence d'un procédé générique de polymérisation en émulsion (pour une éventuelle reconstruction PVAc) ailleurs dans la base — non cherché explicitement dans cette session.
- Vérifier l'existence de mousses PE/PP souples alvéolées sous d'autres termes non testés (ex. « foil », « wrap », « interleaving »), et d'un non-tissé, uniquement si utile après identification physique du matériau réel d'emballage.
- Approfondir les procédés de formage métallique disponibles (emboutissage, extrusion d'aluminium) pour construire un proxy chiffré charnière/coulisse — **seulement après obtention des données fabricant**, pas avant.
- Éviter de multiplier les recherches Ecoinvent supplémentaires : pour la plupart des lacunes ouvertes ci-dessus, le véritable blocage est désormais une donnée fabricant, pas une recherche Ecoinvent restante.
