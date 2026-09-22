# Liste structurée — prochaine passe OpenLCA

Préparée le **2026-09-15**, mise à jour le **2026-09-16** après une interrogation complète et vérifiée du connecteur MCP OpenLCA sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` ([rapport source](RECQ36_diagnostic_ecoinvent_openLCA.md)), puis mise à jour de nouveau le **2026-09-22** après une passe complémentaire ciblée (voir [section dédiée du rapport source](RECQ36_diagnostic_ecoinvent_openLCA.md#passe-complémentaire--2026-09-22)). **Une première mise à jour du 2026-09-16, faite le même jour alors que la mauvaise base OpenLCA (`cups`) était ouverte après un changement de poste de travail, est invalidée en totalité** — voir le [diagnostic corrigé](RECQ36_diagnostic_ecoinvent_openLCA.md) et la note sur l'anomalie `database_family` résolue dans le [référentiel](../materiaux-ebenisterie.md#anomalie-résolue--database_family-flcac). L'interrogation du 2026-09-16 a couvert l'intégralité des six priorités du diagnostic RECQ36, y compris plusieurs objets auparavant non couverts (pied réglable, French cleat, poignée). La passe du 2026-09-22 a posé une hypothèse d'identification pour le matériau d'emballage blanc en rouleau (film mousse PE) et fermé deux pistes Ecoinvent laissées ouvertes le 2026-09-16 (polymérisation en émulsion générique ; mousses PE/PP sous synonymes non testés). **Les recherches désormais terminées ont été retirées de cette liste** ; ne restent que les points encore réellement ouverts.

**Consignes pour l'instance qui exécutera les recherches encore ouvertes** (rappel des règles déjà appliquées) :
- Utiliser `search_processes` et `search_flows` avec les termes ci-dessous, en documentant le nombre de résultats pour chaque terme (y compris zéro).
- Inspecter (`process_details`) tout candidat trouvé avant de conclure — un nom proche n'est pas une preuve de correspondance.
- Ne jamais déduire une géographie du seul nom d'un process.
- Si aucun résultat n'est trouvé, écrire *« Aucun candidat pertinent identifié avec les méthodes d'interrogation disponibles »*, pas *« Ecoinvent ne contient pas X »*.
- Documenter les UUID réellement retournés par l'outil ; n'en inventer aucun.
- **Confirmer `database_info` (nom, famille, version) avant toute recherche** et vérifier manuellement dans l'interface openLCA elle-même que la base ouverte est bien celle attendue — l'anomalie `database_family: "flcac"` résolue en 2026-09-16 provenait d'une mauvaise base laissée ouverte après un changement de poste, pas d'un bug du connecteur.
- Reporter les résultats dans le référentiel (`docs/materiaux-ebenisterie.md`) et le [tableau transversal des lacunes](tableau-transversal-lacunes-ecoinvent.md).
- **Éviter de multiplier les recherches Ecoinvent** lorsque le véritable blocage est désormais une donnée fabricant (formulation, masse par pièce, composition d'un matériau) plutôt qu'une recherche Ecoinvent restante — c'est le cas pour la majorité des lacunes ouvertes ci-dessous.

---

## 1. Recherches désormais terminées (retirées de cette liste)

Ces recherches ont été effectuées par interrogation vérifiée du connecteur MCP OpenLCA sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31` le 2026-09-16, et ne nécessitent pas d'être relancées :

| Objet | Résultat obtenu | Voir |
|---|---|---|
| Contreplaqué merisier / yellow birch / Baltic plywood | Aucun dataset spécifique trouvé ; le candidat `plywood production`, Canada-Quebec (`5538194d-…`, déjà identifié au Lot 2A) est reconfirmé indépendamment — copie administrative, écart d'essence documenté | [Référentiel](../materiaux-ebenisterie.md), [rapport source](RECQ36_diagnostic_ecoinvent_openLCA.md) |
| Papier mélaminé appliqué en atelier | Papier, marché et service d'application reconfirmés (dont le service déjà documenté au Lot 2B, même UUID) ; correspondance partielle forte, pas directe (simple/double face et échelle atelier à trancher) | idem |
| Bande de chant PE | Absence de produit fonctionnel confirmée (0 résultat) ; matières génériques (PE, PP, ABS, PVC) identifiées comme briques de reconstruction seulement, ABS et PVC reconfirmant le Lot 2D | idem |
| Colle PVAc/PVA (au-delà du monomère) | Absence reconfirmée indépendamment (Lot 2F + Ecoinvent 3.11) ; deux nouveaux hors-sujets écartés (adhésif mortier, bitume) | idem |
| Colle contact à base d'eau | Absence reconfirmée indépendamment, y compris pour les formulations aqueuses explicitement recherchées (recherche `adhesive` exhaustive, 19 résultats, tous hors sujet) | idem |
| Colle polyuréthane / PUR | Un adhésif PUR **formulé** existe (`market for polyurethane adhesive`, CLT) mais chimie/usage distincts d'une colle multimatériaux d'atelier ; une colle MUF formulée pour glulam également trouvée, même réserve | idem |
| Charnière, coulisse, poignée, pied réglable, French cleat, vis à bois | Absence de produit fonctionnel confirmée pour toutes les familles (0 résultat process + flows), plus exploration de la catégorie ISIC 259 (473 process, échantillon de 30) : uniquement des services génériques de transformation métallique et des matières premières | idem |
| Carton d'emballage / carton ondulé — variante Québec | **Reconfirmée** : même UUID qu'au Lot 2A (`2424352b-…`), toujours Canada-Québec, avec justification renforcée (marché explicitement régional documenté par Ecoinvent) | idem |
| Variante PVC `suspension polymerised` | **Reconfirmée** : même UUID qu'au Lot 2D (`fa6532b7-…`), avec un second UUID pour le même produit relevé cette session (`68a7d84c-…`, à vérifier s'il s'agit d'un doublon) | idem |
| Film à bulles / papier bulle | Absence confirmée sur plusieurs synonymes (`bubble wrap`, `stretch film`, `foam sheet` — 0 résultat ; `expanded polystyrene`, `polystyrene foam` — résultats hors sujet) | idem |
| Anomalie `database_family: "flcac"` | **Résolue** : cause = mauvaise base OpenLCA (`cups`) restée ouverte après changement de poste, pas une anomalie Ecoinvent | [Référentiel](../materiaux-ebenisterie.md#anomalie-résolue--database_family-flcac) |
| **(2026-09-22)** Procédé générique de polymérisation en émulsion (reconstruction PVAc) | **Fermée par réponse négative** : un procédé « emulsion polymerisation » existe, mais exclusivement pour le PVC (`1900a736-…` / `49299e8d-…`) ; recherche exhaustive `polymerisation` (8 résultats, tous PVC) confirme qu'aucun procédé générique transposable à la PVAc n'existe dans cette base | [Rapport source, section 2026-09-22](RECQ36_diagnostic_ecoinvent_openLCA.md) |
| **(2026-09-22)** Mousse PE/PP souple pour le matériau d'emballage mystère, sous synonymes non testés le 2026-09-16 (`foil`, `wrap`, `interleaving`, `nonwoven`, etc.) | **Absence reconfirmée de façon exhaustive** : 14 variantes lexicales testées + le terme générique `foam` seul (55 process/15 flux, tous inspectés) — aucune mousse PE/PP dans la base. Une hypothèse d'identification (film mousse PE, par rapprochement avec un produit commercial de référence externe) a été posée, non confirmée pour le Québec ; seule une résine PE-LD vierge (`08d7cf9a-…`) et un procédé de moussage générique calibré polystyrène (`polymer foaming`, pentane) existent comme briques, insuffisantes pour un proxy validé | idem |

---

## 2. Recherches encore ouvertes

### Priorité 1 — Approfondissement des procédés de formage métallique (quincaillerie), après données fabricant uniquement

| Champ | Contenu |
|---|---|
| Ce qu'on cherche à déterminer | Pour charnières et coulisses, une fois la nomenclature fabricant obtenue (masse par pièce, matière, revêtement), approfondir les procédés de formage identifiés (`deep drawing, steel`, `impact extrusion of aluminium`, `turning`, `milling`, `zinc coating, pieces`) pour construire un proxy chiffré. |
| Données déjà connues | Ces noms de process ont été identifiés par exploration de la catégorie ISIC 259 (2026-09-16), sans UUID retenu pour l'instant. |
| Question exacte à résoudre | **Ne pas entreprendre cette recherche avant l'obtention des données fabricant** (masse par pièce, matériau exact, revêtement) — le blocage actuel n'est pas une recherche Ecoinvent, c'est une donnée fabricant manquante. Une fois ces données obtenues, identifier les UUID précis des process ci-dessus et vérifier leur applicabilité par masse. |

### Priorité 2 — Écarts d'UUID résiduels entre sessions authentiquement Ecoinvent (sans lien avec l'anomalie `flcac`)

| Champ | Contenu |
|---|---|
| Ce qu'on cherche à déterminer | Même entre le Lot 2F (MCP, avant la contamination `cups`) et la nouvelle interrogation Ecoinvent 3.11 (2026-09-16), certains produits génériques reviennent sous des UUID différents : `vinyl acetate` (Lot 2F : `9381f4dc-…` vs 2026-09-16 : `a4bd8120-…`), `ethylene vinyl acetate copolymer` (Lot 2F : `fe0fb6f7-…` vs 2026-09-16 : `c773d766-…`), `adhesive, for metal` (Lot 2F : `3bd4e097-…` vs 2026-09-16 : `4a5da11b-…`). |
| Données déjà connues | Ces trois écarts sont **distincts** de l'anomalie `database_family: "flcac"` (résolue — cause : mauvaise base `cups`) : les deux sessions comparées ici ont toutes deux interrogé une base authentiquement Ecoinvent. |
| Question exacte à résoudre | S'agit-il d'un changement de version mineure d'Ecoinvent entre les deux sessions, d'un échantillonnage différent parmi des datasets dupliqués, ou d'une autre cause ? Vérifier dans l'interface openLCA si plusieurs datasets portent ce nom de produit exact. Ne pas présumer qu'un des deux UUID est erroné. |

---

## 3. Données fabricant nécessaires (non-Ecoinvent, mais bloquantes pour les reconstructions identifiées)

- **Contreplaqué merisier/Baltic :** essence réelle, type de colle, origine géographique réelle du bois.
- **Papier mélaminé en atelier :** grammage réellement utilisé (à comparer aux 302 g/m² documentés), confirmation simple face vs double face, paramètres de presse d'atelier.
- **Bande de chant PE/ABS/PVC :** masse linéique (g/m), épaisseur, largeur, composition exacte (compound, charges/pigments).
- **Charnière invisible :** nomenclature complète (masse totale, matériaux constitutifs et leurs parts, revêtement, nombre de pièces) — **bloquante**, aucune reconstruction bottom-up n'est possible sans elle.
- **Coulisse de tiroir :** *(largement résolue, relecture 2026-09-22, voir ci-dessus)* — matériaux, finition et géométrie disponibles pour les deux archétypes retenus ; reste à préciser la masse fiable des rails seuls pour l'Accuride 3832EC et l'écart de numérotation `760H4000S`/`760H4001S` pour le Blum MOVENTO.
- **Coulisse de tiroir :** ~~choix d'un modèle fournisseur de référence unique~~ — **résolu (relecture 2026-09-22)** : deux archétypes fonctionnels retenus, Accuride 3832EC 16 po (coulisse latérale, remplace la coulisse Langevin Forest précédemment explorée) et Blum MOVENTO `760H4000S` (coulisse invisible) — voir `docs/inventaire/quincaillerie/`.
- **Poignée, pied réglable, French cleat :** matériau réel, masse, dimensions, procédé de fabrication.
- **Colle contact, PVAc/PVA, EVA hot-melt, PUR :** formulation/composition réelle, teneur en solides, densité, consommation réelle ; **PVAc désormais confirmé pour la Royale 404** (relecture 2026-09-22, voir `docs/inventaire/adhesifs/royale-404-abradhesif.md`) — reste ouvert pour la colle contact et les autres colles de cette liste.
- **Matériau d'emballage blanc en rouleau :** l'identification (film mousse de polyéthylène) est **confirmée par validation métier de Nicolas (2026-09-22)** — reste bloquant : grammage/épaisseur, densité et procédé de fabrication réel (extrusion, réticulation) du produit effectivement utilisé, auprès des entreprises québécoises concernées.

---

## 4. Hors périmètre (inchangé depuis le 2026-09-15)

Non touchés par la réconciliation du 2026-09-16, restent au statut établi le 2026-09-15 :
- les 10 objets de « Données transversales » (électricité, transport, chutes, gaz, eau, eaux usées, résidus) — déjà diagnostiqués au Lot 2G/2G-bis et mis en phase ultérieure ;
- l'OSB et l'« autre contreplaqué » (Panneaux) — déprioritisés le 2026-09-15 ;
- les finitions (vernis, scellant, teinture, solvants) et le bois massif (tilleul, bois exotique) — restent `🟡 À valider` dans le référentiel sans changement de priorité relative ;
- HDF brut, panneau plaqué en atelier (dépend de la lacune « placage bois fini », Lot 2E, elle-même non touchée le 2026-09-16).

Si une future passe OpenLCA dispose de temps additionnel, ces objets restent des candidats secondaires légitimes, dans l'ordre déjà établi par les priorités P1/P2 du [référentiel](../materiaux-ebenisterie.md) et le [tableau transversal des lacunes](tableau-transversal-lacunes-ecoinvent.md).

---

*Liste préparée le 2026-09-15 sans accès OpenLCA, mise à jour le 2026-09-16 par une réconciliation corrective avec le [diagnostic OpenLCA vérifié](RECQ36_diagnostic_ecoinvent_openLCA.md) sur `ecoinvent 3.11 Cutoff Unit-Processes 2025-01-31`, puis mise à jour de nouveau le 2026-09-22 par une passe complémentaire ciblée sur la même base (reconfirmée avant requête : `database_family: ecoinvent`, 25 412 processus / 14 051 flux). Une première mise à jour du 2026-09-16, faite sur la mauvaise base OpenLCA (`cups`), est invalidée en totalité. Aucun UUID n'est inventé ; tous les UUID cités proviennent des diagnostics déjà sourcés (Lots 2A, 2D, 2F, l'interrogation vérifiée du 2026-09-16, et la passe du 2026-09-22).*
