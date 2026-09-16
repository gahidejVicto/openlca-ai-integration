# Liste structurée — prochaine passe OpenLCA

Préparée le **2026-09-15**, mise à jour le **2026-09-16** après réconciliation avec le [diagnostic OpenLCA vérifié du 2026-09-16](RECQ36_diagnostic_ecoinvent_openLCA.md) (interrogation réelle du connecteur MCP OpenLCA). **Les recherches réellement terminées par cette interrogation ont été retirées de la liste active** (section 1) ; seules les questions encore ouvertes restent structurées en détail (section 2).

**Consignes pour l'instance qui exécutera les recherches encore ouvertes** (rappel des règles déjà appliquées) :
- Utiliser `search_processes` et `search_flows` avec les termes ci-dessous, en documentant le nombre de résultats pour chaque terme (y compris zéro).
- Inspecter (`process_details`) tout candidat trouvé avant de conclure — un nom proche n'est pas une preuve de correspondance.
- Ne jamais déduire une géographie du seul nom d'un process.
- Si aucun résultat n'est trouvé, écrire *« Aucun candidat pertinent identifié avec les méthodes d'interrogation disponibles »*, pas *« Ecoinvent ne contient pas X »*.
- Documenter les UUID réellement retournés par l'outil ; n'en inventer aucun.
- **Documenter explicitement `database_info` (nom, famille, version)** avant toute recherche — voir la priorité 0 ci-dessous.
- Reporter les résultats dans le référentiel (`docs/materiaux-ebenisterie.md`) et le [tableau transversal des lacunes](tableau-transversal-lacunes-ecoinvent.md).

---

## 1. Recherches désormais terminées (retirées de cette liste)

Ces recherches ont été effectuées par interrogation OpenLCA directe le 2026-09-16 et ne nécessitent pas d'être relancées, sauf si l'anomalie `database_family` (priorité 0) s'avère indiquer une base réellement différente :

| Objet | Résultat obtenu | Voir |
|---|---|---|
| Contreplaqué merisier / yellow birch / Baltic plywood | Aucun dataset spécifique trouvé ; proxy `plywood, for indoor use` (RoW) retenu, écart d'essence documenté (hêtre/hardwood) | [Référentiel](../materiaux-ebenisterie.md), [rapport source](RECQ36_diagnostic_ecoinvent_openLCA.md) |
| Papier mélaminé appliqué en atelier | Papier, marché et service d'application vérifiés ; meilleure correspondance du diagnostic à ce jour | idem |
| Bande de chant PE | Absence de produit fonctionnel confirmée (0 résultat) ; matières génériques identifiées comme briques de reconstruction seulement | idem |
| Colle PVAc/PVA (au-delà du monomère) | Absence reconfirmée indépendamment (2F + 2026-09-16) | idem |
| Colle contact à base d'eau | Absence reconfirmée indépendamment, y compris pour les formulations aqueuses explicitement recherchées | idem |
| Charnière invisible / coulisse de tiroir (produit fonctionnel) | Absence reconfirmée indépendamment ; briques génériques de reconstruction bottom-up (acier/inox, mise en forme, revêtement zinc) désormais inventoriées | idem |
| Film à bulles / papier bulle | Terme `bubble film` : 0 résultat (synonymes restants listés en section 2 par prudence) | idem |

---

## 2. Recherches encore ouvertes

### Priorité 0 — Anomalie `database_family: "flcac"` (bloquante pour l'interprétation des résultats)

| Champ | Contenu |
|---|---|
| Ce qu'on cherche à déterminer | `database_info` du connecteur MCP retourne `database_family: "flcac"`, alors que la nomenclature de tous les process interrogés correspond à Ecoinvent 3, système Cutoff. Ce point n'a pu être résolu ni le 2026-09-16, ni par vérification locale du dépôt (aucune trace de `flcac` en dehors du rapport ; le connecteur MCP n'est pas implémenté dans ce dépôt). |
| Données déjà connues | Statistiques rapportées : 14 912 process, 23 142 flows, 45 méthodes d'impact, 8 systèmes de produits. Plusieurs UUID cités par le 2026-09-16 diffèrent de ceux des Lots 2A–2G pour des produits au nom identique (`plywood`, `particleboard, uncoated`, `coating service, melamine impregnated paper`, `adhesive, for metal`, ABS, PVC, `wire drawing, steel`, `zinc coating, pieces`) ; la variante `Canada, Québec` du carton ondulé (Lot 2A) n'a pas été retrouvée le 2026-09-16 (voir priorité 2 ci-dessous). |
| Question exacte à résoudre | Dans l'interface openLCA elle-même (pas seulement via MCP) : quel est le nom exact et la version de la base actuellement chargée ? `flcac` correspond-il à un identifiant de connecteur, un nom de base réel, ou une erreur de détection ? Si une autre base qu'Ecoinvent 3.11 Cutoff est chargée, laquelle, et les UUID cités dans les Lots 2A–2G restent-ils valides dans cette base ? |

### Priorité 1 — Pied réglable / niveleur (composant complet)

| Champ | Contenu |
|---|---|
| Termes FR | pied de nivellement ; niveleur ; pied réglable |
| Termes EN | leveling foot ; adjustable foot ; furniture leg leveler |
| Ce qu'on cherche à déterminer | Confirmer si `polypropylene + injection moulding` (Lot 2D) couvre le corps plastique ; identifier une brique pour un éventuel insert métallique. Non couvert par l'interrogation du 2026-09-16 (confirmé explicitement dans son rapport). |
| Données déjà connues | Lot 2D : aucun produit fonctionnel (les résultats `foot` étaient des faux positifs) ; piste PP + moulage par injection non confirmée pour la composition complète. |
| Question exacte à résoudre | Un process/flow "leveling foot"/"adjustable foot" existe-t-il ? Une brique pour un insert métallique fileté est-elle disponible en complément du corps plastique ? |

### Priorité 2 — Ferrure métallique de suspension (French cleat)

| Champ | Contenu |
|---|---|
| Termes FR | ferrure de suspension ; clé française ; système d'accrochage mural |
| Termes EN | French cleat ; wall mounting hardware ; hanging bracket ; suspension hardware |
| Ce qu'on cherche à déterminer | Aucune recherche menée à ce jour (ni Lot 2D, ni 2026-09-16, qui le confirme explicitement). Rechercher d'abord un produit fonctionnel, puis des briques matière/procédé plausibles (acier, aluminium, découpe/pliage). |
| Données déjà connues | Aucune — objet non encore diagnostiqué. |
| Question exacte à résoudre | Un process/flow "wall bracket"/"hanging hardware"/"French cleat" existe-t-il ? À défaut, quelles briques matière/procédé génériques (acier plié, aluminium) sont disponibles ? |

### Priorité 3 — Poignée de meuble métallique (statut de recherche incohérent, à clarifier)

| Champ | Contenu |
|---|---|
| Termes FR | poignée de meuble ; poignée métallique |
| Termes EN | cabinet handle ; furniture handle ; pull handle ; aluminium handle |
| Ce qu'on cherche à déterminer | Le rapport du 2026-09-16 est auto-contradictoire : une de ses sections indique « 0 résultat » pour `furniture handle`, une autre indique « non recherché en détail ». **Refaire la recherche explicitement** pour lever cette ambiguïté, plutôt que de présumer laquelle des deux affirmations est correcte. |
| Données déjà connues | Lot 2D : aucun produit fonctionnel ; brique `section bar extrusion, aluminium` potentiellement pertinente mais conditionnelle (matériau réel non confirmé). |
| Question exacte à résoudre | Un process/flow "handle"/"cabinet hardware, handle" existe-t-il (confirmer par une recherche non ambiguë, avec le compte de résultats explicitement noté) ? À défaut, la brique `section bar extrusion, aluminium` est-elle applicable, sous réserve de confirmation fournisseur du matériau ? |

### Priorité 4 — Variante PVC `suspension polymerised` (bande de chant)

| Champ | Contenu |
|---|---|
| Ce qu'on cherche à déterminer | Le Lot 2D avait documenté `market for polyvinyl chloride, suspension polymerised` (UUID `fa6532b7-7f96-3bbb-8f42-c300d800d5ff`). Le 2026-09-16 n'a retrouvé qu'une variante `polyvinylchloride, bulk polymerised` (UUID `17671bec-6cbf-361f-9318-081db8c739ac`), sans reconfirmer la variante « suspension ». |
| Données déjà connues | Deux variantes de polymérisation PVC potentiellement distinctes, chacune vérifiée dans une seule des deux sessions. |
| Question exacte à résoudre | Les deux variantes (`suspension polymerised` et `bulk polymerised`) coexistent-elles dans la base actuellement interrogée, ou une seule est-elle réellement disponible ? Laquelle est la plus représentative d'une bande de chant PVC (procédé de calandrage déjà documenté au Lot 2D) ? |

### Priorité 5 — Carton d'emballage / carton ondulé : reconfirmer la variante Québec

| Champ | Contenu |
|---|---|
| Ce qu'on cherche à déterminer | Le Lot 2A avait documenté `market for corrugated board box` localisé **Canada, Québec** (UUID `2424352b-3df3-3415-9fbf-a6b1eff0ce60`), avec des briques amont québécoises réelles (production, fluting medium). Le 2026-09-16 n'a retrouvé qu'une variante **Global** (UUID `b8c827da-42b1-3a3a-a6b5-c5d2f1792e33`, boîte formée plutôt que plaque) — sans chercher spécifiquement la variante québécoise. |
| Données déjà connues | Voir le [référentiel](../materiaux-ebenisterie.md), fiche « Carton d'emballage / carton ondulé », pour le détail des deux candidats. |
| Question exacte à résoudre | La variante `Canada, Québec` de `market for corrugated board box` (et ses briques amont `corrugated board box production`, `containerboard production, fluting medium, semichemical, 40% recycled content`) existe-t-elle toujours dans la base actuellement interrogée ? Le produit réellement utilisé en atelier est-il une plaque découpée ou une boîte préformée ? |

### Priorité 6 — Matériau d'emballage blanc fin en rouleau (identification physique requise avant toute recherche)

| Champ | Contenu |
|---|---|
| Termes FR | *(à ne pas deviner)* |
| Termes EN | *(à ne pas deviner)* |
| Ce qu'on cherche à déterminer | **Action préalable non-Ecoinvent toujours requise** : `Identifier précisément le matériau d'emballage avant recherche Ecoinvent`. Obtenir la fiche produit / l'étiquette du rouleau auprès de l'atelier ou du fournisseur (nom commercial, composition — papier, non-tissé, film plastique). |
| Données déjà connues | Matériau blanc, très fin, vendu en gros rouleau, utilisé pour envelopper/protéger les meubles (description métier Nicolas, 2026-09-15). Le 2026-09-16 a relevé un candidat **non confirmé** (`market for packaging film, low density polyethylene`, UUID `0c925f5b-401c-330c-9247-04bd41395645`, Global) par simple cohérence de facteur de forme — **ne pas retenir comme identification**. |
| Question exacte à résoudre | *Reste sans objet tant que l'identification physique n'est pas faite.* Une fois l'identification obtenue, vérifier si `packaging film, LDPE` correspond réellement, ou reformuler la recherche avec les termes appropriés. |

### Priorité 7 — Film à bulles / papier bulle : synonymes restants

| Champ | Contenu |
|---|---|
| Ce qu'on cherche à déterminer | Le 2026-09-16 n'a testé que le terme `bubble film` (0 résultat). Par prudence méthodologique, tester les synonymes anglais usuels avant de considérer l'absence comme définitivement établie dans cette base. |
| Termes EN restants à tester | `air cushion film` ; `plastic bubble packaging` ; `protective packaging film` |
| Données déjà connues | `bubble film` : 0 résultat (process et flows). Absents également : mousse PE (« polyethylene foam »). |
| Question exacte à résoudre | Un des synonymes restants retourne-t-il un résultat pertinent ? |

---

## 3. Données fabricant nécessaires (non-Ecoinvent, mais bloquantes pour les reconstructions identifiées)

Ces éléments ne sont **pas** des recherches OpenLCA — ils sont listés ici parce qu'ils conditionnent l'usage des briques de reconstruction déjà identifiées (Lot 2D, 2026-09-16) :

- **Bande de chant PE/ABS/PVC :** masse linéique (g/m), épaisseur, largeur, composition exacte (compound, charges/pigments).
- **Charnière invisible, coulisse de tiroir :** nomenclature complète (masse totale, matériaux constitutifs et leurs parts, revêtement, nombre de pièces) — **bloquante**, aucune reconstruction bottom-up n'est possible sans elle malgré les briques génériques (acier/inox, mise en forme, zinc) désormais disponibles.
- **Coulisse de tiroir :** choix d'un **modèle fournisseur de référence unique** (documentation la plus détaillée disponible), conformément à la consigne de ne pas subdiviser par technologie/dimension.
- **Colle contact, PVAc/PVA, EVA hot-melt, PUR :** formulation/composition réelle, teneur en solides, densité, consommation réelle.
- **Papier mélaminé en atelier :** grammage réellement utilisé (à comparer aux 302 g/m² documentés) et paramètres de presse d'atelier, pour confirmer la représentativité d'échelle.
- **Matériau d'emballage blanc en rouleau :** voir priorité 6 ci-dessus — identification physique, pas une donnée de reconstruction.

---

## 4. Hors périmètre (inchangé depuis le 2026-09-15)

Non touchés par la réconciliation du 2026-09-16, restent au statut établi le 2026-09-15 :
- les 10 objets de « Données transversales » (électricité, transport, chutes, gaz, eau, eaux usées, résidus) — déjà diagnostiqués au Lot 2G/2G-bis et mis en phase ultérieure ;
- l'OSB et l'« autre contreplaqué » (Panneaux) — déprioritisés le 2026-09-15 ;
- les finitions (vernis, scellant, teinture, solvants) et le bois massif (tilleul, bois exotique) — restent `🟡 À valider` dans le référentiel sans changement de priorité relative ;
- HDF brut, panneau plaqué en atelier (dépend de la lacune « placage bois fini », Lot 2E, elle-même non touchée le 2026-09-16).

Si une future passe OpenLCA dispose de temps additionnel, ces objets restent des candidats secondaires légitimes, dans l'ordre déjà établi par les priorités P1/P2 du [référentiel](../materiaux-ebenisterie.md) et le [tableau transversal des lacunes](tableau-transversal-lacunes-ecoinvent.md).

---

*Liste préparée le 2026-09-15 sans accès OpenLCA, mise à jour le 2026-09-16 par réconciliation avec le [diagnostic OpenLCA vérifié](RECQ36_diagnostic_ecoinvent_openLCA.md). Aucun UUID n'est inventé ; tous les UUID cités proviennent des diagnostics déjà sourcés (Lots 2A, 2D, 2F, et l'interrogation du 2026-09-16). La priorité 0 (anomalie `database_family`) doit être résolue avant que les autres résultats de ce document soient considérés comme définitivement fiables.*
