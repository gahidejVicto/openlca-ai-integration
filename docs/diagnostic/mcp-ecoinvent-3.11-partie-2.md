PRIORITÉ 4 close (résultat : absence confirmée). Je passe à la PRIORITÉ 5 (quincaillerie).PRIORITÉ 5 confirmée : aucun produit fonctionnel quincaillerie n'existe (charnières, coulisses, poignées, patins, taquets, vis — tous à zéro), seulement des matières premières métalliques génériques + services d'usinage. Je passe à la PRIORITÉ 6 (emballages).# Diagnostic RECQ36 — Suite et clôture des recherches OpenLCA

Base : ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31 (confirmée). Suite du travail entamé — PRIORITÉ 4 complétée, PRIORITÉS 5 et 6 traitées.

---

## PRIORITÉ 4 — Adhésifs (complétée)

### Requêtes effectuées

`polyvinylacetate`, `polyvinyl acetate`, `vinyl acetate`, `wood glue`, `dispersion adhesive`, `contact adhesive`, `emulsion` (101 résultats — tous liés aux peintures/déchets, aucun adhésif bois), `adhesive` (recherche exhaustive, 19 résultats).

### Candidats Ecoinvent trouvés

| Dataset Produit de référence Géographie Unité UUID Commentaire  |                                     |        |    |                                      |                                                                                             |
| --------------------------------------------------------------- | ----------------------------------- | ------ | -- | ------------------------------------ | ------------------------------------------------------------------------------------------- |
| market for vinyl acetate                                        | vinyl acetate                       | —      | kg | a4bd8120-5784-3dd9-bee6-a8473d385b7f | **Monomère précurseur**, pas le polymère PVAc                                               |
| market for ethylene vinyl acetate copolymer                     | ethylene vinyl acetate copolymer    | —      | kg | c773d766-c8ff-3493-88ea-09492fbc0048 | Copolymère EVA — chimie différente (hot-melt/mousses), pas la colle blanche PVAc classique  |
| market for polyurethane adhesive                                | polyurethane adhesive               | Global | kg | ad1da3c6-5cb8-364d-8fb5-e96e9dca9e93 | Colle PUR pour bois lamellé (CLT) — isocyanate, sans formaldéhyde. Chimie distincte de PVAc |
| market for melamine urea formaldehyde adhesive                  | melamine urea formaldehyde adhesive | Global | kg | e7001c37-5a60-335b-bf15-ad7395226509 | Colle MUF pour bois lamellé-collé — chimie distincte                                        |
| adhesive, for metal                                             | adhesive, for metal                 | —      | kg | 4a5da11b-2019-326b-990e-254d96e9acb3 | Hors sujet (métal)                                                                          |
| adhesive mortar / bitumen adhesive compound                     | —                                   | —      | —  | —                                    | Hors sujet (construction/étanchéité)                                                        |

### Meilleure correspondance actuelle

**Aucune.** Ni le polymère PVAc, ni une formulation de colle blanche/colle contact à l'eau ne sont présents.

### Niveau de correspondance

**Aucune correspondance satisfaisante** — ni pour PVAc/PVA, ni pour la colle contact à base d'eau.

### Lacunes

- **Fonction** : aucun produit fonctionnel « colle blanche bois » ni « colle contact à l'eau ».
- **Matière/composition** : le polymère PVAc lui-même est absent (seul son monomère, l'acétate de vinyle, existe).
- Les colles bois disponibles (PUR, MUF) sont chimiquement non substituables à une colle PVAc en émulsion aqueuse — proxy chimique jugé non pertinent sans hypothèse forte.

### Action recommandée

Reconstruction nécessaire à partir du monomère vinyl acetate + un procédé de polymérisation en émulsion générique (à vérifier s'il existe ailleurs dans la base, hors du périmètre de cette recherche) OU recours à des données fabricant/fiche technique (EcoPlatform, EPD fournisseur) pour la colle PVAc et la colle contact utilisées en atelier.

---

## PRIORITÉ 5 — Quincaillerie

### Requêtes effectuées

`hinge`, `drawer slide`, `furniture handle`, `levelling foot`, `French cleat`, `wood screw`, `screw`, `furniture fitting`, `metal fastener`, exploration de la catégorie ISIC 259 (Manufacture of other fabricated metal products — 473 processus, échantillon de 30 examiné).

### Résultat par famille

| Famille Produit fonctionnel ? Procédé proche ? Matériaux génériques disponibles pour reconstruction  |            |     |                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------- | ---------- | --- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Charnière (hinge/cabinet hinge)                                                                      | **Absent** | Non | Acier/laiton + services d'emboutissage (`deep drawing, steel`), usinage (`turning`, `milling`), revêtement (`zinc coating, pieces`) |
| Coulisse de tiroir (drawer slide/runner)                                                             | **Absent** | Non | Acier (tôle/profilé) + services de formage à froid, extrusion d'aluminium (`impact extrusion of aluminium`)                         |
| Poignée (furniture handle)                                                                           | **Absent** | Non | Zinc/laiton/acier + moulage/usinage                                                                                                 |
| Patin de nivellement (levelling foot)                                                                | **Absent** | Non | Plastique (PP/POM non trouvé spécifiquement) + acier fileté                                                                         |
| Taquet français / suspension fitting                                                                 | **Absent** | Non | Acier plié/percé                                                                                                                    |
| Vis à bois (wood screw)                                                                              | **Absent** | Non | Non exploré en détail (conforme à la consigne)                                                                                      |

### Constat transversal

La catégorie ISIC 259 ne contient **que des services de transformation métallique génériques** (fraisage, tournage, perçage, emboutissage, extrusion à froid, revêtement zinc, traitement thermique) et des matières premières (acier, laiton, aluminium, fonte) — **aucun produit fini de quincaillerie meuble** (charnière, coulisse, poignée, patin, taquet, vis) n'existe comme dataset autonome dans Ecoinvent.

### Niveau de correspondance

**Absent** pour toutes les familles, sans exception.

### Lacunes

Fonction (produit fini totalement absent) pour toutes les familles. Une reconstruction complète (masse de métal + suite d'opérations d'usinage/formage) serait nécessaire pour chaque famille, avec un effort disproportionné par rapport à la précision atteignable sans données fabricant réelles (masses, alliages, procédés exacts).

### Action recommandée

Pour les charnières et coulisses (masse/complexité plus importante, comme demandé) : obtenir des fiches techniques fabricant (masse par pièce, matière — acier zingué le plus souvent) et construire un proxy manuel : masse d'acier (`market for steel, low-alloyed`) + zinc coating + une combinaison raisonnable d'opérations de formage (deep drawing + drilling). Pour poignées/patins/taquets/vis : proxy simplifié matière seule (acier ou zinc, selon le produit), sans tenter de reconstruire le procédé complet — cohérent avec la consigne de ne pas sur-investir sur les vis.

---

## PRIORITÉ 6 — Emballages

### Requêtes effectuées

`corrugated board` (8 résultats), `bubble wrap` (0), `polyethylene foam` (0), `expanded polystyrene` (16, tous déchets/traitement), `polystyrene foam` (14, tous isolation périmétrique rigide), `stretch film` (0), `packaging film` (3), `foam sheet` (0).

### Candidats Ecoinvent trouvés

| Dataset Produit de référence Géographie Unité UUID Commentaire  |                                                |                         |          |                                                   |                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------- | ---------------------------------------------- | ----------------------- | -------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market for corrugated board box                                 | corrugated board box                           | **Canada, Québec**      | kg       | 2424352b-3df3-3415-9fbf-a6b1eff0ce60              | **Marché explicitement régional** — la documentation Ecoinvent précise elle-même que ce type de produit se négocie localement, pas globalement. Contrairement au contreplaqué CA-QC (copie de RER), ce dataset a une base méthodologique qui **justifie** sa représentativité québécoise |
| corrugated board box production                                 | corrugated board box                           | (plusieurs géographies) | kg       | 17317a18-28b4-335a-a96d-68789b9bfb70 et autres    | Production sous-jacente                                                                                                                                                                                                                                                                  |
| market for packaging film, low density polyethylene             | packaging film, low density polyethylene       | Global                  | kg       | 1b3c1341-0769-32dc-92d7-00fb8891e3d5              | Film LDPE plat générique (usages variés : alimentaire, construction, électroménager). Pas de mousse, pas de bulles                                                                                                                                                                       |
| polystyrene foam slab (for perimeter insulation)                | polystyrene foam slab for perimeter insulation | —                       | m² ou kg | 5be8986d-89e3-387f-ba00-fa6e12b6fc7f et variantes | **Hors sujet** : mousse rigide XPS destinée à l'isolation de fondation, pas un matériau d'emballage souple                                                                                                                                                                               |

### Sur le matériau non identifié (« matériau blanc très fin, en gros rouleau, pour envelopper les meubles »)

Deux familles de candidats existent dans la base, avec des natures très différentes :

1. **Film LDPE plat** (`packaging film, low density polyethylene`) — mince, souple, mais **non alvéolé/non mousseux**. Correspond à un usage de type film étirable ou pellicule de protection simple.
2. **Mousse de polystyrène rigide** (`polystyrene foam slab`) — épaisse, rigide, destinée au bâtiment. **Ne correspond pas** à la description (pas souple, pas en rouleau fin, pas blanc typiquement destiné à l'emballage meuble).

Aucun candidat ne représente une **mousse PE fine et souple en rouleau** (type « foam wrap » ou intercalaire de protection meuble) ni du bubble wrap. Conformément à la consigne, je ne tranche pas arbitrairement : pour identifier le bon candidat (ou confirmer l'absence), il faudrait savoir si le matériau réel est :

- un film plastique plat non alvéolé (→ `packaging film, low density polyethylene` serait un proxy raisonnable) ;
- une mousse PE ou PP alvéolée (→ **aucun candidat Ecoinvent**, proxy à construire à partir de résine PE/PP + un procédé de moussage, non trouvé dans cette recherche) ;
- un non-tissé synthétique (→ non recherché dans cette session, piste à explorer si les deux hypothèses précédentes sont écartées).

### Niveau de correspondance

- Carton ondulé : **Correspondance directe** (et représentativité Québec crédible).
- Film LDPE : **Proxy** possible si le matériau réel est un film plat.
- Mousse de protection meuble : **Aucune correspondance satisfaisante** — candidats présentés, décision à prendre après clarification du produit réel.

### Action recommandée

Obtenir un échantillon ou une fiche technique du matériau réel (grammage, composition — PE vs PP vs non-tissé, alvéolé ou non) avant de choisir entre proxy film LDPE ou reconstruction mousse.

---

## Tableau transversal final

| Produit métier Dataset candidat Géographie Correspondance Composition Technologie Représentativité QC Proxy/reconstruction Données fabricant nécessaires Statut  |                                                      |                    |                                            |                                                                |                                                         |                                                                          |                                           |                                                |            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------ | ------------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------- | ---------------------------------------------- | ---------- |
| Contreplaqué merisier/Baltic                                                                                                                                     | plywood production \| plywood (5538194d…)            | Canada, Quebec     | Proxy                                      | Hardwood générique, non spécifié                               | Copie du procédé RER (échantillon allemand)             | **Non** — copie administrative, pas de donnée réelle QC                  | Oui                                       | Oui                                            | ÉCART      |
| Papier mélaminé — matière                                                                                                                                        | paper, melamine impregnated (0a2370fe…)              | RoW                | Partielle                                  | Kraft paper + résine mélamine-formaldéhyde + urée-formaldéhyde | Conforme                                                | Non testée                                                               | Non nécessairement                        | Souhaitable (grammage réel)                    | À VÉRIFIER |
| Papier mélaminé — application                                                                                                                                    | coating, with melamine impregnated paper (24ceb336…) | Global             | Partielle                                  | —                                                              | Application **double face industrielle**, panneau exclu | N/A                                                                      | Ajustement simple/double face             | Oui (grammage réel, mode d'application)        | À VÉRIFIER |
| Bande de chant PE                                                                                                                                                | —                                                    | —                  | Absent                                     | —                                                              | —                                                       | N/A                                                                      | Oui (PE/PP/ABS/PVC générique, à trancher) | Oui (matière exacte + procédé)                 | ABSENT     |
| Colle PVAc/PVA                                                                                                                                                   | —                                                    | —                  | Absent                                     | Seul le monomère (vinyl acetate) existe                        | —                                                       | N/A                                                                      | Oui (reconstruction chimique incertaine)  | Oui                                            | ABSENT     |
| Colle contact à l'eau                                                                                                                                            | —                                                    | —                  | Absent                                     | —                                                              | —                                                       | N/A                                                                      | Oui                                       | Oui                                            | ABSENT     |
| Charnière                                                                                                                                                        | —                                                    | —                  | Absent                                     | —                                                              | Services d'usinage/formage génériques disponibles       | N/A                                                                      | Oui (acier/laiton + procédés)             | Oui (masse, alliage)                           | ABSENT     |
| Coulisse de tiroir                                                                                                                                               | —                                                    | —                  | Absent                                     | —                                                              | Idem                                                    | N/A                                                                      | Oui                                       | Oui                                            | ABSENT     |
| Poignée de meuble                                                                                                                                                | —                                                    | —                  | Absent                                     | —                                                              | Idem                                                    | N/A                                                                      | Oui (simplifié)                           | Oui                                            | ABSENT     |
| Patin de nivellement                                                                                                                                             | —                                                    | —                  | Absent                                     | —                                                              | Idem                                                    | N/A                                                                      | Oui (simplifié)                           | Oui                                            | ABSENT     |
| Taquet français                                                                                                                                                  | —                                                    | —                  | Absent                                     | —                                                              | Idem                                                    | N/A                                                                      | Oui (simplifié)                           | Oui                                            | ABSENT     |
| Vis à bois                                                                                                                                                       | —                                                    | —                  | Absent (non approfondi, conforme consigne) | —                                                              | —                                                       | N/A                                                                      | Oui (simplifié)                           | Non prioritaire                                | ABSENT     |
| Carton ondulé (boîte)                                                                                                                                            | corrugated board box (2424352b…)                     | **Canada, Québec** | **OK**                                     | Kraftliner/testliner + fluting medium                          | Conforme, marché régional documenté                     | **Oui** — représentativité justifiée par la méthodologie même du dataset | Non                                       | Non                                            | OK         |
| Film/mousse d'emballage meuble                                                                                                                                   | packaging film, LDPE (1b3c1341…) *ou* aucun          | Global / —         | Proxy incertain / Absent                   | LDPE plat, non alvéolé                                         | —                                                       | Non testée                                                               | Oui, selon nature réelle du matériau      | Oui (composition réelle : film plat vs mousse) | À VÉRIFIER |

---

# HANDOFF CLAUDE CODE

**1. Corrections factuelles à apporter**

- Le dataset `plywood production | plywood | Cutoff, U` localisé **Canada, Quebec** (UUID `5538194d-92b2-3020-bb3e-fbc59cb71248`) est une copie administrative du dataset Europe (même échantillon de données allemand, même colle urée-formaldéhyde, même essence "hardwood" générique). **Toute mention antérieure dans le référentiel traitant ce dataset comme "représentatif du Québec" doit être corrigée.**
- À l'inverse, le dataset `corrugated board box` localisé **Canada, Quebec** (UUID `2424352b-3df3-3415-9fbf-a6b1eff0ce60`) a une représentativité régionale **crédible et documentée par Ecoinvent lui-même** (marché local, pas d'échange global pour ce type de produit) — distinction importante à conserver dans le référentiel entre les deux cas "CA-QC".

**2. Nouveaux datasets identifiés**

- `paper, melamine impregnated` (matière, kg) + `coating, with melamine impregnated paper` (service d'application, m², panneau exclu) — structure en deux datasets bien adaptée pour représenter séparément matière et procédé d'application en atelier.
- `three and five layered board` — identifié et **explicitement écarté** comme faux-ami pour le contreplaqué (bois massif aboutis-collé, pas du placage).
- Datasets de matières génériques utilisables comme briques de proxy : PE-LD (`08d7cf9a…`), PP (`881eed86…`), ABS (`ca074112…`), PVC suspension polymérisée (`fa6532b7…`/`68a7d84c…`).
- Services de métallurgie génériques (deep drawing, impact extrusion, zinc coating, turning, milling) disponibles en ISIC 259 pour reconstruction quincaillerie.

**3. UUID et géographies vérifiés** — voir tableau transversal ci-dessus, colonne "Dataset candidat" (tous vérifiés via `process_details` réel).

**4. Anciennes hypothèses invalidées**

- L'hypothèse (implicite dans un diagnostic antérieur, selon le prompt initial) qu'un contreplaqué CA-QC serait plus représentatif qu'un dataset RER est **invalidée** — c'est la même donnée sous une étiquette géographique différente.

**5. Correspondances toujours non résolues**

- Contreplaqué merisier/Baltic birch : aucune correspondance directe, proxy générique seulement.
- Papier mélaminé : application simple face vs double face non tranchée.
- Bande de chant PE : matière proxy non tranchée (PE/PP/ABS/PVC).
- Colle PVAc et colle contact à l'eau : absence totale, reconstruction incertaine.
- Toute la quincaillerie (charnières, coulisses, poignées, patins, taquets) : absence totale, reconstruction à construire au cas par cas.
- Matériau d'emballage meuble (film fin blanc en rouleau) : nature physique du matériau réel inconnue, deux hypothèses non départagées (film plat LDPE vs mousse alvéolée absente de la base).

**6. Données fabricant nécessaires**

- Contreplaqué : essence réelle, type de colle, origine géographique réelle du bois.
- Papier mélaminé : grammage réel, application simple/double face.
- Bande de chant : matière exacte (PE/PP/ABS/PVC), procédé (extrusion profilée).
- Colles : formulation exacte (teneur en eau, % PVAc, additifs) pour colle blanche et colle contact.
- Quincaillerie : masse par pièce et alliage pour charnières et coulisses en priorité.
- Emballage meuble : composition et structure (film plat vs mousse vs non-tissé) du matériau en rouleau.

**7. Recherches supplémentaires éventuellement nécessaires**

- Vérifier l'existence d'un procédé générique de polymérisation en émulsion (pour reconstruction PVAc) ailleurs dans la base — non cherché explicitement dans cette session.
- Vérifier l'existence de mousses PE/PP souples alvéolées sous d'autres termes non testés (ex. "foil", "wrap", "interleaving").
- Approfondir les procédés de formage métallique disponibles (deep drawing, impact extrusion) pour construire un proxy chiffré charnière/coulisse une fois les données fabricant obtenues.