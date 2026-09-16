# RECQ36 — Diagnostic des écarts Ecoinvent / OpenLCA
**Matériaux et composants en ébénisterie québécoise**

Rapport produit par interrogation réelle de la base via le connecteur MCP OpenLCA. Aucune modification n'a été apportée au dépôt Git (pas d'accès à ce dépôt dans cette session). Ce document est destiné à être transmis à une instance Claude Code pour intégration au référentiel.

## Note préalable — identification de la base

`database_info` retourne `database_family: "flcac"` et non `ecoinvent`. Cependant, la nomenclature de tous les process interrogés (suffixe `Cutoff, U`, arborescence de catégories NACE à 4 niveaux, vocabulaire des descriptions) correspond à **Ecoinvent 3, système modèle Cutoff**. Cette contradiction n'a pas été résolue dans cette session — à vérifier côté configuration du connecteur avant intégration. Les résultats ci-dessous sont présentés tels qu'obtenus, sans supposer laquelle des deux étiquettes est correcte.

Statistiques de la base : 14 912 process, 23 142 flows, 45 méthodes d'impact, 8 systèmes de produits.

---

## PRIORITÉ 1 — Contreplaqué merisier / Baltic birch plywood

### Produit métier
Contreplaqué de bouleau (merisier / yellow birch / Baltic birch plywood) utilisé en ébénisterie.

### Requêtes effectuées
`plywood`, `birch plywood`, `birch`, `veneer`, `laminated veneer`, `Baltic`, `veneer sheet` (implicite via `veneer`).

### Candidats Ecoinvent trouvés

| Dataset/process | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| market for plywood, for indoor use | plywood, for indoor use | Rest-of-World | m³ | a263faad-eca2-3956-a706-7e9a7b30364f | Générique, usage intérieur |
| plywood production, for indoor use | plywood, for indoor use | Europe | m³ | 365758ba-1bb5-32e9-836b-0d45247fa93d | Intrant bois rond = **hêtre (beech)**, résine urée-formaldéhyde, données site suisse 1996 jugées représentatives de l'Europe |
| plywood production, for indoor use | plywood, for indoor use | Rest-of-World | m³ | a37de0e5-9ea2-3c17-b652-be171d206f5c | Même structure, sourcé via marché générique « sawlog and veneer log, hardwood » (mélange d'essences non spécifié), dataset hérité d'ecoinvent v2 |
| market for plywood, for outdoor use | plywood, for outdoor use | Rest-of-World | m³ | b37a4e46-b1f2-3e0c-a961-90411e492df8 | Usage extérieur, hors périmètre probable |
| hardwood forestry, birch, sustainable forest management (plusieurs flux : sawlog/veneer log, pulpwood, wood chips…) | bois rond de bouleau | (géographies multiples, non détaillées) | m³ / kg | ex. f04b0987-f44e-3f49-871f-253a8c4df77f | Matière première brute (bouleau en forêt) — **existe**, mais n'est PAS reliée à un process de contreplaqué dans la base ; c'est une bûche, pas un panneau |
| — | — | — | — | — | Aucun dataset « birch plywood », « Baltic birch plywood » ou « veneer sheet » spécifique trouvé (0 résultat) |

### Meilleure correspondance actuelle
`market for plywood, for indoor use` (RoW, UUID a263faad-…), qui s'approvisionne lui-même auprès des deux process de production ci-dessus.

### Niveau de correspondance
**Proxy** (aucune correspondance directe ni partielle spécifique à l'espèce).

### Lacunes
- **Matière/composition** : l'hypothèse documentée dans le dataset européen est le **hêtre**, pas le bouleau. Le dataset RoW utilise un marché « hardwood » non spécifié à l'espèce. C'est un écart de composition explicite, pas une supposition de notre part.
- **Technologie** : type de contreplaqué (nombre de plis, épaisseur, type de collage) non spécifié dans la description.
- **Géographie/représentativité Québec** : données européennes (Suisse 1996 pour la version « Europe ») ; aucune donnée nord-américaine ou québécoise.
- **Données fournisseur** : nécessaires pour documenter l'écart réel entre du contreplaqué de bouleau balte importé et ce proxy générique hêtre/hardwood.

### Action recommandée
Conserver le proxy générique existant (déjà identifié précédemment) en documentant explicitement l'écart d'essence (hêtre/hardwood non spécifié vs bouleau). Ne pas chercher davantage dans Ecoinvent : la base ne contient rien de plus spécifique. Prioriser l'obtention de données fabricant si la précision devient nécessaire pour la quantification.

---

## PRIORITÉ 2 — Papier mélaminé appliqué en atelier

### Produit métier
Papier décoratif/mélaminé appliqué sur panneau en atelier.

### Requêtes effectuées
`melamine`.

### Candidats Ecoinvent trouvés

| Dataset/process | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| melamine impregnated paper production | paper, melamine impregnated | Rest-of-World | kg | b2e9c4ee-c34a-3ad7-9662-0ef0b050cda8 | **Le papier imprégné lui-même** : 0,344 kg kraft brut + 0,377 kg résine mélamine-formaldéhyde + 0,218 kg résine urée-formaldéhyde + 0,388 kg formaldéhyde pour 1 kg de papier fini. Grammage documenté : 302 g/m² (dont 104 g/m² de papier support) |
| market for paper, melamine impregnated | paper, melamine impregnated | Global | kg | 55d422f8-6b1d-358e-9691-8de4be164462 | Marché mondial du papier ci-dessus |
| coating service, melamine impregnated paper, double-sided | coating, with melamine impregnated paper | Rest-of-World | m² | 57d226d1-43bb-37cc-81a2-0b4cda274608 (doublon 6c179811-5e5b-3527-bc52-9b5d679bb29a) | **Le procédé d'application** : consomme 0,604 kg de papier mélaminé (marché) par m² de panneau enrobé double face. **Exclut explicitement le panneau support.** Correspond bien au produit métier « application en atelier » |
| particle board production/market, uncoated, average glue mix | particleboard, uncoated | (RoW/marché) | m³ | 87141283-b718-30d4-84b0-39c6c71cc8cf / ff40ec39-1d3e-3168-bebc-e5ac10e28ad2 | Panneau support **non enrobé** — confirme qu'Ecoinvent modélise ce cas de façon découplée (substrat nu + service de placage), pas comme un panneau déjà fini |

### Meilleure correspondance actuelle
Combinaison `coating service, melamine impregnated paper, double-sided` (procédé d'application, m²) + `market for paper, melamine impregnated` (matière, kg) déjà imbriqués l'un dans l'autre dans la base.

### Niveau de correspondance
**Partielle à directe** — c'est le meilleur résultat de tout ce diagnostic : Ecoinvent distingue bel et bien le papier, la résine et le service d'application, et ne confond pas cela avec un panneau déjà mélaminé acheté fini (aucun tel dataset n'existe, ce qui évite le risque de double comptage signalé dans la consigne).

### Lacunes
- **Représentativité Québec** : données européennes multi-usines, aucune donnée nord-américaine.
- **Technologie** : le procédé documenté est une presse industrielle continue, pas nécessairement représentatif d'une application en atelier d'ébénisterie à plus petite échelle.
- **Géographie** : RoW/Global, pas de résolution CA-QC.

### Action recommandée
Utiliser ce couple paper + coating service comme correspondance documentée « partielle à directe ». Vérifier que le grammage (302 g/m²) correspond à ce qui est réellement utilisé en atelier avant de l'intégrer tel quel.

---

## PRIORITÉ 3 — Bande de chant PE

### Produit métier
Bande de chant en polyéthylène utilisée en ébénisterie.

### Requêtes effectuées
`edge band`, `edge banding` (process ET flows — 0 résultat dans les deux cas), puis recherche des matières génériques : `polyethylene, low density`, `polypropylene, granulate`, `acrylonitrile-butadiene-styrene copolymer`, `polyvinylchloride`, `extrusion, plastic`.

### Candidats Ecoinvent trouvés

| Dataset/process | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| — | bande de chant (produit fonctionnel) | — | — | — | **0 résultat, confirmé sur process ET sur flows** |
| market for polyethylene, low density, granulate | polyethylene, low density, granulate | Global | kg | f73b01f9-8ddb-30d0-9f82-2a30a6f689a0 | Matière première seule, aucune forme de profilé/bande |
| market for polypropylene, granulate | polypropylene, granulate | Global | kg | 9c11da4a-05b2-3f03-878d-34c133548b5c | Idem, PP |
| market for acrylonitrile-butadiene-styrene copolymer | acrylonitrile-butadiene-styrene copolymer | Global | kg | 1367e2a2-b284-3325-a907-6183bf2d126e | Idem, ABS |
| market for polyvinylchloride, bulk polymerised | polyvinylchloride, bulk polymerised | Global | kg | 17671bec-6cbf-361f-9318-081db8c739ac | Idem, PVC (polymérisation en masse — il existe possiblement une variante « suspension polymerised » non vérifiée ici) |
| market/production for extrusion, plastic film | extrusion, plastic film | (marché : non vérifié individuellement, production existe) | kg | 06fcff5d-7113-327d-ab1b-8ceae6c2b17e (marché) | Procédé de transformation générique — pourrait approximer la mise en forme d'une bande extrudée, mais conçu pour du film, pas un profilé de chant |

### Meilleure correspondance actuelle
Aucune. Les quatre polymères existent comme matière première générique ; aucun procédé de mise en forme spécifique à une bande de chant n'existe.

### Niveau de correspondance
**Aucune correspondance satisfaisante.**

### Lacunes
- **Fonction** : produit fonctionnel totalement absent.
- **Technologie** : aucun procédé d'extrusion de profilé mince/bande n'a été trouvé (seulement film et tuyau).
- **Données fournisseur nécessaires** : masse linéique (g/m), épaisseur, largeur, et composition exacte (PE pur ou compound avec charges/pigments) pour bâtir un proxy par la masse.

### Action recommandée
Ne pas conclure qu'un des quatre polymères est LE bon proxy sans données fabricant. Documenter comme lacune ouverte nécessitant reconstruction bottom-up (masse de matière + procédé de transformation le plus proche disponible, à défaut d'un procédé de profilé dédié).

---

## PRIORITÉ 4 — Adhésifs

### PVAc/PVA (colle blanche à bois)

### Requêtes effectuées
`polyvinylacetate` (0 résultat), `vinyl acetate`, `adhesive`, `dispersion`.

### Candidats Ecoinvent trouvés

| Dataset/process | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| — | colle PVAc / colle à bois (produit fonctionnel) | — | — | — | **0 résultat** |
| market for adhesive, for metal | adhesive, for metal | Global (non revérifié) | kg | e1e8f512-fa21-320c-92f8-e3f345cda6b8 | Hors sujet fonctionnel (colle métal) |
| bitumen adhesive compound production, hot/cold | bitumen adhesive compound | — | kg | fa09b096-…, 1aed51f6-… | Hors sujet (bitume, construction) |
| adhesive mortar production | adhesive mortar | — | kg | 3f5bd6a3-cd8c-3161-b48e-9b193858e30d | Hors sujet (mortier-colle, construction) |
| market for ethylene vinyl acetate copolymer | ethylene vinyl acetate copolymer | Global | kg | fe0fb6f7-fd33-3303-a767-fc1464446ce1 | Polymère apparenté (EVA) mais chimiquement distinct du PVAc homopolymère utilisé en colle blanche |
| market for acrylic dispersion, without water, in 65% solution state | acrylic dispersion | Global | kg | 44da54f3-7ab8-308d-9c33-6efa0f247130 | Famille chimique différente (acrylique, pas acétate de vinyle) — utilisé plutôt en peinture/revêtement |
| market for vinyl acetate | vinyl acetate | Global | kg | 9381f4dc-deda-3e02-9cf8-4ef4321b137e | **Monomère**, pas le polymère PVAc ni une formulation de colle. La description précise que ce produit est « généralement utilisé sur le site de production même » (pas vraiment un bien de marché transportable) |

### Colle contact à base d'eau

### Requêtes effectuées
Mêmes recherches (`adhesive`, `dispersion`) — aucun terme supplémentaire n'a fait apparaître de résultat distinct.

### Candidats Ecoinvent trouvés
Aucun candidat spécifique trouvé au-delà de la liste ci-dessus.

### Meilleure correspondance actuelle
Aucune.

### Niveau de correspondance
**Aucune correspondance satisfaisante** — ni pour le PVAc, ni pour la colle contact à base d'eau.

### Lacunes
- **Fonction** : aucun produit fonctionnel « colle à bois » ou « colle contact » dans la base.
- **Matière/composition** : les candidats disponibles (EVA, dispersion acrylique, acétate de vinyle monomère) appartiennent à des familles chimiques différentes de celle du PVAc réel ; aucun n'est un proxy défendable sans le documenter comme approximatif.
- **Procédé** : aucun procédé de formulation d'adhésif en émulsion/dispersion aqueuse n'existe.
- **Données fournisseur nécessaires** : teneur en solides, nature exacte du polymère, additifs.

### Action recommandée
Documenter comme lacune ouverte. Si un proxy doit être construit malgré tout pour avancer la quantification, le signaler explicitement comme approximation de dernier recours (ex. dispersion acrylique 65 % comme ordre de grandeur pour une colle en émulsion aqueuse), jamais comme une correspondance.

---

## PRIORITÉ 5 — Quincaillerie

### Produits métier et résultat par famille

| Famille | Produit fonctionnel dans Ecoinvent ? | Procédé proche ? | Matériaux génériques disponibles pour reconstruction |
|---|---|---|---|
| Charnière (hinge/furniture hinge/cabinet hinge) | **Non — 0 résultat sur process ET flows** | Non | Voir ci-dessous |
| Coulisse de tiroir (drawer slide/runner/rail) | **Non — 0 résultat** | Non | Voir ci-dessous |
| Poignée (furniture handle) | **Non — 0 résultat** | Non | Voir ci-dessous |
| Pied réglable / French cleat | Non recherché explicitement cette session (à faire) | — | — |
| Vis à bois (screw) | **Non** — seuls des « air compressor, screw-type » apparaissent (hors sujet) | Non | — (conforme à la consigne : ne pas insister) |

### Matériaux génériques trouvés (briques pour reconstruction bottom-up, charnières/coulisses)

| Dataset/process | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| market for steel, low-alloyed, hot rolled | steel, low-alloyed, hot rolled | — | kg | eba0e6ba-5f96-3ac9-a0c0-2f0d4fc74b8a | Acier standard, matière de base plausible pour charnière/coulisse d'entrée de gamme |
| market for steel, chromium steel 18/8, hot rolled | steel, chromium steel 18/8, hot rolled | — | kg | 288bd21b-b97b-32b7-8383-cc0d2126fe72 | Acier inoxydable — pertinent pour quincaillerie de qualité supérieure |
| sheet rolling, steel (market) | sheet rolling, steel | — | kg | 72416073-2dc0-3d01-a3e4-91c7b0f0dfe3 | Procédé de mise en forme (laminage) |
| wire drawing, steel (market) | wire drawing, steel | — | kg | 641bc156-ed49-3cfa-a712-c27b40902d93 | Pertinent pour ressorts/tiges de coulisses |
| zinc coating, pieces (market) | zinc coat, pieces | — | m² (par µm) | ada0a646-2258-3a16-8223-a31f812325aa | Revêtement anticorrosion typique des charnières/coulisses |
| market for metal working, average for steel/chromium steel/aluminium product manufacturing | metal working, average for … product manufacturing | — | kg | b76ed063-3770-3e6a-b065-c09d9d1891ee (acier) / 00dd895a-1607-35dc-8226-2ba0f5cd9f64 (acier chromé) / e41d54f1-64cf-3ba3-87c9-1d481bc79d76 (aluminium) | Service générique de mise en forme/usinage, unité de reconstruction la plus utile pour approximer la fabrication d'une pièce quincaillerie par sa masse |

### Meilleure correspondance actuelle
Aucun produit fonctionnel. Les matériaux et procédés génériques ci-dessus permettent une reconstruction bottom-up par masse (acier ou acier chromé + mise en forme + revêtement zinc), mais ce n'est pas une correspondance — c'est un chemin de reconstruction.

### Niveau de correspondance
**Absent** (produit fonctionnel) — reconstruction possible pour charnières/coulisses, non prioritaire pour les vis.

### Lacunes
- Fonction complètement absente pour toutes les familles de quincaillerie recherchées.
- Données fournisseur nécessaires : masse par pièce, matériau exact (acier zingué, inox, laiton, nylon pour certaines coulisses), procédé de fabrication (moulage, estampage, extrusion d'aluminium).

### Action recommandée
Pour charnières et coulisses : engager une reconstruction bottom-up (masse + matière + mise en forme + revêtement) dès que les données fabricant (fiches techniques, masses) seront disponibles — approfondissement jugé justifié compte tenu de leur masse/complexité potentiellement significative. Pour les vis : lacune confirmée rapidement, ne pas investir davantage de temps de recherche dans Ecoinvent, conformément à la consigne. Poignées, pieds réglables et French cleat : recherche à compléter dans une prochaine session (non couverte ici pour les pieds/French cleat).

---

## PRIORITÉ 6 — Emballages

### Produit métier
Matériaux d'emballage/protection pour meubles, incluant un matériau non identifié (fin, blanc, en gros rouleau, utilisé pour envelopper/protéger les meubles).

### Requêtes effectuées
`corrugated board`, `bubble film` (0 résultat), `polystyrene foam slab`, `polyethylene foam` (0 résultat), `foam` (recherche large), `packaging film`, `shrink film` (0 résultat).

### Candidats Ecoinvent trouvés

| Dataset/process | Produit de référence | Géographie | Unité | UUID | Commentaire |
|---|---|---|---|---|---|
| market for corrugated board box | corrugated board box | Global | kg | b8c827da-42b1-3a3a-a6b5-c5d2f1792e33 | Produit fonctionnel existant, **mais c'est une boîte formée**, pas une plaque plate de carton ondulé — à vérifier si c'est bien ce qui est utilisé |
| market for packaging film, low density polyethylene | packaging film, low density polyethylene | Global | kg | 0c925f5b-401c-330c-9247-04bd41395645 | Film PE mince — facteur de forme (rouleau, fin) cohérent avec la description du matériau mystère, mais aucune confirmation qu'il s'agit bien de ce matériau (pas de fonction de protection/calage documentée) |
| market for polystyrene foam slab | polystyrene foam slab | — (non revérifié pour le marché) | kg / m³ selon flux | 8b420467-04f4-3461-b3aa-0b9570560486 | Mousse rigide EPS — **mauvais facteur de forme** pour un matériau en « gros rouleau », plutôt destiné à l'isolation en panneaux rigides |
| market for polyethylene, low density, granulate | polyethylene, low density, granulate | Global | kg | f73b01f9-8ddb-30d0-9f82-2a30a6f689a0 | Matière première seule, si le matériau réel s'avère être une mousse ou un film PE non catalogué tel quel |
| — | mousse PE (« polyethylene foam »), papier bulle | — | — | — | **0 résultat** — absents de la base |

### Meilleure correspondance actuelle
- Carton : `market for corrugated board box` — correspondance partielle (boîte, pas plaque).
- Matériau mystère : **aucune décision prise**, deux candidats présentés (film PE mince vs mousse rigide EPS), les deux avec des réserves importantes.

### Niveau de correspondance
Carton : **partielle**. Matériau mystère : **aucune correspondance satisfaisante** — identification physique requise avant tout choix.

### Lacunes
- Carton : représentativité de la forme (boîte vs plaque plate) à vérifier selon l'usage réel en atelier.
- Matériau mystère : aucune caractéristique physique confirmée (épaisseur, densité, présence de bulles/mousse, composition). Ni le film PE ni la mousse EPS ne sont validés comme la bonne réponse.

### Action recommandée
Ne pas trancher arbitrairement pour le matériau mystère. Obtenir une fiche technique ou un échantillon pour déterminer s'il s'agit d'un film plein (candidat : packaging film LDPE), d'un non-tissé, ou d'une mousse mince (aucun candidat trouvé dans Ecoinvent pour ce dernier cas — nécessiterait des données fabricant). Pour le carton, confirmer si le produit réel est une boîte assemblée ou une plaque, et ajuster le choix de dataset en conséquence.

---

## TABLEAU TRANSVERSAL FINAL

| Produit métier | Dataset candidat | Géographie | Correspondance | Composition | Technologie | Représentativité QC | Proxy/reconstruction | Données fabricant nécessaires | Statut |
|---|---|---|---|---|---|---|---|---|---|
| Contreplaqué bouleau/Baltic | market for plywood, for indoor use (a263faad-…) | RoW | Proxy | Hêtre/hardwood non spécifié (≠ bouleau) | Non spécifiée | Aucune | Oui | Oui, si précision requise | ÉCART |
| Papier mélaminé appliqué en atelier | coating service, melamine impregnated paper, double-sided (57d226d1-…) + market paper (55d422f8-…) | RoW / Global | Partielle à directe | Kraft + résine mélamine-formaldéhyde + urée-formaldéhyde, 302 g/m² | Presse industrielle continue (échelle ≠ atelier) | Aucune | Non (utilisable tel quel) | Non, sauf vérification grammage | OK (avec réserve d'échelle) |
| Bande de chant PE | Aucun | — | Aucune | — | — | — | Oui, à partir de granulé PE | Oui (masse linéique, composition) | ABSENT |
| Colle PVAc/PVA | Aucun | — | Aucune | Candidats chimiquement distincts (EVA, acrylique) | — | — | Oui, en dernier recours | Oui (formulation, % solides) | ABSENT |
| Colle contact à base d'eau | Aucun | — | Aucune | — | — | — | Oui, en dernier recours | Oui | ABSENT |
| Charnière | Aucun (matériaux génériques acier/inox + mise en forme + zinc disponibles) | — | Aucune | — | — | — | Oui, bottom-up par masse | Oui (masse, matériau exact) | À VÉRIFIER |
| Coulisse de tiroir | Idem charnière | — | Aucune | — | — | — | Oui, bottom-up par masse | Oui | À VÉRIFIER |
| Poignée | Non recherché en détail | — | — | — | — | — | — | — | À VÉRIFIER |
| Vis à bois | Aucun | — | Aucune | — | — | — | Non prioritaire | Non prioritaire | ABSENT |
| Carton ondulé (emballage) | market for corrugated board box (b8c827da-…) | Global | Partielle | — | — | Aucune | Non | À confirmer forme (boîte vs plaque) | À VÉRIFIER |
| Matériau mystère (film/enveloppe meubles) | packaging film, LDPE (0c925f5b-…) — candidat non confirmé | Global | Aucune (identification physique requise) | PE | Film mince | Aucune | Possible | Oui (identification du matériau réel) | À VÉRIFIER |

Statuts utilisés : OK, ÉCART, À VÉRIFIER, ABSENT, N/A — conformément à la légende demandée.

---

# HANDOFF CLAUDE CODE

## 1. Corrections factuelles à apporter
- Le dataset de contreplaqué « for indoor use » (Europe, UUID 365758ba-…) repose explicitement sur du **hêtre (beech)**, pas sur un mélange incluant le bouleau — si le référentiel actuel décrit ce proxy comme « générique hardwood » sans préciser cette hypothèse de hêtre, corriger la documentation.
- Confirmer que le référentiel ne présente pas le procédé `coating service, melamine impregnated paper, double-sided` comme incluant le panneau support — il ne l'inclut pas (vérifié dans les exchanges : le panneau n'apparaît pas comme intrant).

## 2. Nouveaux datasets identifiés
- `melamine impregnated paper production` (b2e9c4ee-c34a-3ad7-9662-0ef0b050cda8) — papier seul, kg, RoW.
- `market for paper, melamine impregnated` (55d422f8-6b1d-358e-9691-8de4be164462) — kg, Global.
- `coating service, melamine impregnated paper, double-sided` (57d226d1-43bb-37cc-81a2-0b4cda274608, doublon 6c179811-5e5b-3527-bc52-9b5d679bb29a) — m², RoW, exclut le panneau.
- `particleboard, uncoated` (production 87141283-b718-30d4-84b0-39c6c71cc8cf ; marché ff40ec39-1d3e-3168-bebc-e5ac10e28ad2) — substrat nu, utile pour modéliser un panneau mélaminé en atelier par composition (substrat + service de placage).
- Matériaux/procédés génériques pour reconstruction quincaillerie : `steel, low-alloyed, hot rolled` (marché eba0e6ba-5f96-3ac9-a0c0-2f0d4fc74b8a), `steel, chromium steel 18/8, hot rolled` (marché 288bd21b-b97b-32b7-8383-cc0d2126fe72), `wire drawing, steel` (marché 641bc156-ed49-3cfa-a712-c27b40902d93), `zinc coating, pieces` (ada0a646-2258-3a16-8223-a31f812325aa), `metal working, average for steel/chromium steel/aluminium product manufacturing` (b76ed063-…, 00dd895a-…, e41d54f1-…).
- `market for packaging film, low density polyethylene` (0c925f5b-401c-330c-9247-04bd41395645) — candidat non confirmé pour le matériau d'enveloppe mystère.

## 3. UUID et géographies vérifiés
Tous les UUID cités dans le tableau transversal ci-dessus ont été obtenus par requête directe (`search_processes` puis `process_details`) et non reconstruits de mémoire. Géographies confirmées via le champ `location` retourné par `process_details` (voir tableau).

## 4. Anciennes hypothèses invalidées
- Si une hypothèse antérieure supposait qu'un dataset « contreplaqué de bouleau russe » plus spécifique existait dans Ecoinvent au-delà du proxy générique déjà connu : **invalidée**, confirmation qu'aucun dataset plus spécifique n'existe (recherche exhaustive sur bouleau, Baltic, veneer, laminated veneer — tous à 0 ou hors sujet).
- Si une hypothèse antérieure supposait qu'un panneau « déjà mélaminé fini » existait et risquait d'être confondu avec le papier appliqué en atelier : **confirmée comme non-risque** — un tel panneau fini n'existe pas dans la base ; seul le substrat nu + service de placage existent, ce qui structure correctement la distinction demandée.

## 5. Correspondances toujours non résolues
- Bande de chant PE (aucun produit fonctionnel).
- Colle PVAc/PVA et colle contact à base d'eau (aucun produit fonctionnel, candidats chimiques non satisfaisants).
- Charnières, coulisses, poignées, vis (aucun produit fonctionnel — reconstruction bottom-up envisageable pour charnières/coulisses uniquement).
- Matériau d'enveloppe mystère en emballage (identification physique du produit réel requise avant tout choix de dataset).
- Pied réglable/French cleat : non couvert dans cette session.

## 6. Données fabricant nécessaires
- Contreplaqué : composition exacte en essence si une précision au-delà du proxy hêtre/hardwood est requise.
- Bande de chant PE : masse linéique, épaisseur, composition exacte du polymère.
- Colles : nature exacte du polymère, teneur en solides, formulation.
- Quincaillerie (charnières/coulisses) : masse par pièce, matériau exact, procédé de fabrication.
- Emballage : identification physique du matériau mystère (échantillon ou fiche technique fournisseur).

## 7. Recherches supplémentaires éventuellement nécessaires
- Poignées, pieds réglables/French cleat (Priorité 5) : recherche non complétée dans cette session.
- Vérifier la variante « polyvinylchloride, suspension polymerised » (en plus de « bulk polymerised ») pour la Priorité 3, non explorée.
- Clarifier la contradiction `database_family: "flcac"` vs nomenclature Ecoinvent 3 Cutoff observée dans `database_info`, avant toute intégration au référentiel Git.
