# Diagnostic Ecoinvent — Lot 2F
## Adhésifs : PVA/PVAc, EVA hot-melt, colle contact, polyuréthane

Projet ACV mobilier québécois — Base Ecoinvent 3.11, système Cutoff, via openLCA/MCP.

Portée stricte : 4 usages métier d'adhésifs. Aucun dataset modifié, aucun proxy construit, `docs/materiaux-ebenisterie.md` non modifié, aucune modification Git au-delà des deux livrables demandés.

**Correction préalable à ce lot** : la recherche approfondie de ce tour n'a pas permis de retrouver le dataset `market for polychloroprene` (UUID `d1147a50-260c-353a-93c0-def3ebd131d0`) cité au Lot 1 pour la colle contact — cet UUID ne résout plus vers aucun process dans la base interrogée ce tour, et aucune recherche par nom ("polychloroprene", "chloroprene", "neoprene") ne retourne de produit correspondant, seulement des flux élémentaires d'émission de chloroprène (substance, pas produit). **Cette citation du Lot 1 doit être considérée comme non confirmée et est corrigée dans ce rapport** — elle n'est pas réutilisée ici comme brique valide. Il ne s'agit pas d'une affirmation qu'aucun dataset de ce type n'existe jamais dans Ecoinvent (limite MCP, cf. discipline de recherche), mais l'accès dont nous disposons ce tour ne permet pas de le retrouver.

---

## FICHE 1 — COLLE PVA/PVAc BLANCHE (assemblage bois)

### 1. Identification métier
Produit : colle blanche liquide pour assemblage bois. Fonction : collage bois-bois. Forme : liquide en contenant. Usage : application manuelle ou mécanisée en atelier d'ébénisterie.

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| polyvinyl acetate adhesive / PVAc adhesive / PVA adhesive / PVA glue | search_processes | 0 (toutes) | — |
| wood adhesive / wood glue / white glue | search_flows | 0 (toutes) | — |
| dispersion adhesive / water based adhesive / water-based adhesive | search_processes | 0 (toutes) | — |
| adhesive (générique) | search_flows | **5 résultats** : `adhesive, for metal`, `adhesive mortar`, `bitumen adhesive compound` (cold/hot), `fibreboard, soft, without adhesives` | **Aucun pertinent pour le bois — voir inspection ci-dessous** |
| adhesive for wood | search_processes | 0 | — |

**Inspection du candidat le plus proche trouvé ("adhesive, for metal")**, par prudence méthodologique : UUID `3bd4e097-7f01-3790-b602-33a7cac44444`, location Rest-of-World. Composition documentée : <cite>"Basic materials applied in the production are organic chemicals, liquid epoxy resin, hydrated lime and silica sand."</cite> et <cite>"The dataset describes the production of a metal adhesive compound used e.g. in the aluminium window frame production."</cite> — **c'est un adhésif époxy formulé pour cadres de fenêtres en aluminium, sans rapport chimique ni applicatif avec une colle PVAc à bois. Rejeté.**

### 3. Meilleur candidat
Aucun adhésif formulé. Seule brique identifiée : `market for vinyl acetate` (monomère), UUID `9381f4dc-deda-3e02-9cf8-4ef4321b137e`, location **Global**, unité kg.

### 4. Ce que représente réellement le dataset
**Fait Ecoinvent** : <cite>"This product is generally considered to be used at the production site. Therefore, the market does not contain any transport."</cite> Les exchanges montrent uniquement le monomère vinyl acetate lui-même (deux lots de production agrégés), sans aucune mention de polymérisation, d'émulsion aqueuse, ni de formulation adhésive. **Interprétation (la nôtre)** : c'est le monomère chimique de base utilisé pour fabriquer le polymère polyvinyle d'acétate — plusieurs étapes chimiques et industrielles avant une colle blanche formulée (polymérisation en émulsion, ajout de plastifiants, charges, conservateurs, ajustement de la teneur en solides).

### 5. Composition observée
Composition non suffisamment documentée pour établir la correspondance avec le produit métier — le dataset ne contient que le monomère lui-même, pas une formulation.

### 6. Correspondance métier

| Dimension | Niveau |
|---|---|
| Fonction | Aucune (monomère, pas un adhésif) |
| Technologie | Faible (précurseur chimique de la bonne famille polymère) |
| Formulation | Aucune |
| Forme | Aucune (le métier utilise un liquide prêt à l'emploi ; le dataset est un monomère solide/liquide industriel) |
| Application | Aucune |
| Unité | kg — écart avec l'unité métier probable (pot/litre) |
| Géographie | Global |

### 7. Données primaires QC
Aucune identifiée.

### 8. VERDICT : **proxy matière seulement**

Classification A/B/C/D/E : **D — précurseurs chimiques seulement.**

### 9. Principale lacune
Ecoinvent ne contient aucun adhésif PVAc formulé, ni même le polymère polyvinyle d'acétate lui-même sous forme d'émulsion — seul le monomère vinyl acetate, plusieurs étapes chimiques en amont de toute colle utilisable, a été identifié.

### 10. Données fournisseur nécessaires
Formulation réelle (teneur en solides, plastifiants, charges) ; densité ; masse achetée ; consommation réelle par assemblage ; conditionnement.

### 11. Action recommandée
**Données fournisseur nécessaires** — aucune reconstruction sérieuse n'est possible à partir du seul monomère.

---

## FICHE 2 — EVA HOT-MELT (encolleuse de chants)

### 1. Identification métier
Produit : adhésif thermofusible EVA. Fonction : collage de bande de chant par encolleuse mécanisée. Forme : bâtonnet ou granulé fondu à chaud. Usage : application industrielle/mécanisée.

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| hot melt adhesive / hot-melt adhesive / hot melt glue | search_processes | 0 (toutes) | — |
| EVA adhesive / EVA hot melt / ethylene vinyl acetate adhesive / ethylene-vinyl acetate adhesive | search_processes | 0 (toutes) | — |
| thermoplastic adhesive | search_processes | 0 | — |
| edge banding adhesive / edgebanding adhesive / adhesive for edge banding | search_processes | 0 (toutes) | — |
| adhesive (générique, déjà couvert Fiche 1) | search_flows | Mêmes 5 résultats, aucun EVA/hot-melt | — |

**Confirmation totale : aucun hot-melt formulé, aucun produit spécifique à l'encollage de chants.**

### 3. Meilleur candidat
Aucun adhésif formulé. Seule brique : `market for ethylene vinyl acetate copolymer`, UUID `fe0fb6f7-fd33-3303-a767-fc1464446ce1`, location **Global**, unité kg.

### 4. Ce que représente réellement le dataset
**Fait Ecoinvent** : <cite>"In this market, expert judgement was used to develop product specific transport distance estimations."</cite> Les exchanges montrent le copolymère EVA lui-même (deux lots de production agrégés) plus le transport (train, camion, mer transocéanique) — **aucune mention de cires, résines tackifiantes, antioxydants ou autres additifs de formulation hot-melt**. **Interprétation (la nôtre)** : c'est la résine polymère de base, avant la formulation complète (ajout de cires paraffiniques/microcristallines, résines tackifiantes, antioxydants) qui caractérise un adhésif hot-melt EVA réellement utilisé en encolleuse.

### 5. Composition observée
Composition non suffisamment documentée pour établir la correspondance avec le produit métier — copolymère seul, sans additifs de formulation.

### 6. Correspondance métier

| Dimension | Niveau |
|---|---|
| Fonction | Aucune (résine, pas un adhésif prêt à l'emploi) |
| Technologie | Moyenne (bonne famille polymère de base) |
| Formulation | Aucune |
| Forme | Aucune (métier = bâtonnet/granulé formulé ; dataset = résine industrielle) |
| Application | Aucune (aucun procédé d'encollage de chants trouvé) |
| Unité | kg — cohérent avec une éventuelle conversion future si masse par mètre de chant connue |
| Géographie | Global |

### 7. Données primaires QC
Aucune identifiée.

### 8. VERDICT : **proxy matière seulement**

Classification A/B/C/D/E : **C — résine/polymère intermédiaire seulement** (plus proche du produit final que le cas PVA, puisque c'est déjà le polymère et non un simple monomère, mais toujours pas une formulation).

### 9. Principale lacune
Aucune formulation hot-melt complète (cires, tackifiants, antioxydants) n'est représentée ; aucun procédé d'application par encolleuse n'a été trouvé.

### 10. Données fournisseur nécessaires
Formulation réelle du hot-melt (part EVA vs cires vs résines tackifiantes) ; grammage appliqué par mètre linéaire de chant ; température d'application ; consommation réelle par panneau.

### 11. Action recommandée
**Données fournisseur nécessaires**, avec une reconstruction envisageable à moyen terme si la formulation réelle (répartition massique EVA/cires/tackifiants) est obtenue — meilleure base de départ que la Fiche 1 (résine vs monomère).

---

## FICHE 3 — COLLE CONTACT (stratifié)

### 1. Identification métier
Produit : colle contact liquide en pot. Fonction : collage de stratifié sur un substrat. Forme : liquide, application manuelle (pinceau/rouleau) sur les deux surfaces avant assemblage.

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| contact adhesive / contact glue / contact cement | search_processes | 0 (toutes) | — |
| solvent based adhesive / solvent-based adhesive / adhesive solvent | search_processes | 0 (toutes) | — |
| rubber adhesive | search_processes | 0 | — |
| neoprene adhesive / polychloroprene adhesive | search_processes + search_flows | 0 / 0 | — |
| polychloroprene (seul) | search_processes + search_flows | **0 / 0 — voir correction méthodologique en préambule** | Le dataset cité au Lot 1 n'a pas pu être retrouvé ce tour |
| chloroprene | search_flows | 6 résultats, **tous des flux élémentaires d'émission de la substance chloroprène**, pas un produit | Non pertinent comme brique matière |
| laminate adhesive / adhesive for laminate / adhesive for laminates | search_processes | 0 (toutes) | — |
| synthetic rubber (générique, non demandé explicitement mais recherché par prudence) | search_flows | 1 résultat : `synthetic rubber` (type non spécifié) | Brique très générique, non confirmée comme néoprène |

**Confirmation : aucun adhésif contact formulé, et — contrairement à ce qui avait été avancé au Lot 1 — aucune brique de polychloroprène n'a pu être retrouvée avec les moyens de recherche disponibles ce tour.**

### 3. Meilleur candidat
Aucune brique chimique spécifiquement confirmée. La seule piste générique trouvée, `synthetic rubber` (type non précisé dans le nom), n'a pas été confirmée comme correspondant à une chimie néoprène/polychloroprène — elle n'est donc pas retenue comme candidat sérieux, seulement mentionnée pour traçabilité de recherche.

### 4. Ce que représente réellement le dataset
Sans objet — aucun candidat sérieux à décrire.

### 5. Composition observée
Composition non suffisamment documentée pour établir la correspondance avec le produit métier — aucune brique chimique confirmée n'a été identifiée.

### 6. Correspondance métier

| Dimension | Niveau |
|---|---|
| Fonction | Aucune |
| Technologie | Inconnue (chimie réelle du produit métier non présumée, conformément au mandat) |
| Formulation | Aucune |
| Forme | Aucune |
| Application | Aucune |
| Unité | Sans objet |
| Géographie | Sans objet |

### 7. Données primaires QC
Aucune identifiée.

### 8. VERDICT : **lacune majeure**

Classification A/B/C/D/E : **E — aucune brique pertinente identifiée** (avec les méthodes de recherche disponibles ce tour).

### 9. Principale lacune
Aucun adhésif contact formulé, ni aucune brique chimique confirmée (résine ou polymère) n'a pu être identifiée avec les outils disponibles — situation plus défavorable que les Fiches 1 et 2, qui disposaient au moins d'un précurseur ou d'une résine.

### 10. Données fournisseur nécessaires
Chimie réelle de l'adhésif (aucune hypothèse retenue) ; teneur en solides ; solvant(s) utilisé(s) ; densité ; consommation réelle par m² de stratifié.

### 11. Action recommandée
**Rechercher autre source** — les méthodes de recherche MCP disponibles ce tour n'ont permis d'identifier aucune brique. Une vérification complémentaire (recherche par UUID direct si un identifiant fiable est retrouvé ailleurs, ou accès à une version différente de l'outil) est recommandée avant de conclure définitivement à l'absence totale dans la base.

---

## FICHE 4 — ADHÉSIF POLYURÉTHANE (bois↔métal, bois↔plastique)

### 1. Identification métier
Produit : adhésif polyuréthane. Fonction : collage occasionnel bois-métal ou bois-plastique. Forme : non précisée par le contexte métier (mono ou bi-composant non présumé).

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| polyurethane adhesive / PU adhesive / PUR adhesive / polyurethane glue | search_processes | 0 (toutes) | — |
| structural adhesive / assembly adhesive / wood adhesive polyurethane | search_processes | 0 (toutes) | — |
| polyurethane (générique) | search_flows | **5 résultats : `polyurethane, rigid foam`, `polyurethane, flexible foam`, `waste polyurethane foam`, `waste polyurethane seal`, `waste polyurethane`** | **Tous des mousses/joints/déchets — faux positifs confirmés, aucun adhésif** |
| polyurethane resin | (couvert par la recherche générique ci-dessus, aucun résultat "resin" distinct) | 0 | — |
| polyol | search_flows | 1 résultat : `polyol` (précurseur PU, chimie générique) | Précurseur chimique, pas un adhésif |
| methylene diphenyldiisocyanate (MDI) | search_flows | 1 résultat pertinent (+ 9 flux d'émission) : `methylene diphenyldiisocyanate`, produit chimique | Précurseur chimique, pas un adhésif — déjà rencontré comme liant interne de panneau au Lot 2B |

**Confirmation : aucun adhésif PU formulé. Les seuls produits "polyurethane" existants sont des mousses (isolation/rembourrage) et des joints — fonction radicalement différente d'un adhésif, confirmés comme faux positifs après inspection du nom (aucune inspection de description nécessaire, la fonction "foam"/"seal" est sans ambiguïté dans le nom lui-même).**

### 3. Meilleur candidat
Aucun adhésif formulé, aucun polymère PU formé. Seules briques : **précurseurs chimiques** `polyol` et `methylene diphenyldiisocyanate` (MDI) — les deux réactifs de base d'une polyuréthane, mais non combinés, non formulés, non catalysés.

### 4. Ce que représente réellement le dataset
Deux produits chimiques industriels séparés (polyol ; MDI), chacun utilisé dans de nombreuses applications (mousses, élastomères, adhésifs, revêtements) sans lien établi par Ecoinvent vers une application adhésive spécifique. Le MDI a déjà été rencontré au Lot 2B comme liant interne de panneaux de particules/MDF (usage différent : liant de panneau, pas adhésif d'assemblage bois-métal).

### 5. Composition observée
Composition non suffisamment documentée pour établir la correspondance avec le produit métier — seuls les deux précurseurs séparés existent, sans réaction, catalyseur, ni charge documentés.

### 6. Correspondance métier

| Dimension | Niveau |
|---|---|
| Fonction | Aucune |
| Technologie | Faible (précurseurs de la bonne famille chimique seulement) |
| Formulation | Aucune |
| Forme | Aucune |
| Application | Aucune |
| Unité | kg pour les deux précurseurs |
| Géographie | Non vérifiée ce tour pour polyol/MDI spécifiquement |

### 7. Données primaires QC
Aucune identifiée.

### 8. VERDICT : **proxy matière seulement**

Classification A/B/C/D/E : **D — précurseurs chimiques seulement.**

### 9. Principale lacune
Aucun adhésif PU formulé ; les seuls produits PU finis représentés (mousses) sont fonctionnellement sans rapport avec un adhésif d'assemblage.

### 10. Données fournisseur nécessaires
Type de PU (mono/bi-composant) ; ratio polyol/isocyanate réel ; catalyseurs/additifs ; consommation réelle par assemblage ; densité.

### 11. Action recommandée
**Données fournisseur nécessaires** — situation comparable à la Fiche 1 (PVA), avec deux précurseurs identifiés au lieu d'un seul monomère, mais sans formulation ni produit fini pertinent.

---

## CLASSIFICATION RÉCAPITULATIVE A/B/C/D/E

| Adhésif | Niveau | Justification |
|---|---|---|
| PVA/PVAc | **D** | Seul le monomère vinyl acetate existe |
| EVA hot-melt | **C** | Le copolymère EVA (résine) existe, plus proche du produit fini qu'un simple monomère, mais non formulé |
| Colle contact | **E** | Aucune brique chimique confirmée avec les moyens disponibles ce tour |
| Polyuréthane | **D** | Les deux précurseurs (polyol, MDI) existent séparément, non combinés/formulés |

**Réponse directe à la question de Nicolas** : non, nous n'avons la colle réellement utilisée par l'entreprise dans aucun des quatre cas. Nous avons, au mieux, la matière chimique de base dont une colle *pourrait* être composée (EVA, cas le plus favorable), et au pire, aucune brique du tout (colle contact).

---

## QUESTIONS TRANSVERSALES

**1. Ecoinvent possède-t-il une colle PVAc formulée utilisable ?** Non — seul le monomère vinyl acetate a été identifié.

**2. Si oui, correspond-elle réellement à une colle blanche à bois ?** Sans objet (réponse à la question 1 négative).

**3. Ecoinvent possède-t-il un adhésif EVA hot-melt formulé ?** Non — seul le copolymère EVA brut a été identifié, sans cires ni tackifiants.

**4. Existe-t-il quelque chose de spécifique à l'encollage de chants ?** Non, aucun résultat pour les termes spécifiques ("edge banding adhesive" et variantes).

**5. Ecoinvent possède-t-il une colle contact formulée pertinente ?** Non.

**6. Peut-on établir qu'elle correspond au produit métier utilisé pour le stratifié ?** Sans objet — aucun candidat à évaluer.

**7. Ecoinvent possède-t-il un adhésif PU formulé pertinent ?** Non — seuls des mousses PU (fonction différente) et deux précurseurs chimiques séparés existent.

**8. Pour quels produits n'avons-nous que le polymère/résine ?** EVA hot-melt (résine EVA seule).

**9. Pour quels produits avons-nous réellement un adhésif formulé ?** Aucun des quatre. Un adhésif formulé a néanmoins été rencontré ailleurs dans la base (`adhesive, for metal`, époxy pour cadres de fenêtres aluminium) — inspecté et rejeté pour la Fiche 1, mentionné ici pour transparence : Ecoinvent contient donc bien, dans d'autres familles, des adhésifs réellement formulés, ce qui confirme que l'absence observée pour nos 4 cas est spécifique à ces technologies, pas une limite générale de la base sur les adhésifs.

**10. Quels adhésifs nécessiteraient une reconstruction ?** Les quatre, à des degrés différents — EVA hot-melt étant le plus proche d'une reconstruction crédible (résine + additifs à documenter), la colle contact étant la plus éloignée (aucune brique de départ).

**11. Quels adhésifs nécessitent prioritairement des données fournisseur ?** La colle contact en priorité absolue (aucune brique) ; puis PVA et PU (précurseurs seulement) ; EVA hot-melt en dernier (déjà une résine, formulation à préciser).

**12. Existe-t-il des données primaires québécoises identifiées ?** Aucune identifiée, pour les quatre adhésifs.

**13. Le Lot 2F permet-il d'améliorer les conclusions des Lots 2D ou 2E ?** Voir section dédiée ci-dessous.

---

## IMPACT POTENTIEL SUR LES DIAGNOSTICS PRÉCÉDENTS

### Lot 2D — bandes de chant

**Chant bois préencollé** : aucun changement. Le Lot 2D concluait à l'absence totale de brique de bois mince ; ce lot ne trouve pas non plus de brique adhésive EVA hot-melt formulée qui aurait pu compléter un futur proxy — la lacune reste double (bois ET colle), pas seulement sur le bois.

**EVA pour encolleuse de chants** : *mise à jour ultérieure recommandée* — le Lot 2D n'avait pas étudié l'adhésif d'encollage de chants en détail (hors périmètre). Ce lot précise que la résine EVA brute existe (classification C), ce qui est une information légèrement plus favorable que "aucune brique" — à noter si le Lot 2D est révisé pour intégrer explicitement la brique adhésive dans son évaluation de la bande de chant bois préencollée.

### Lot 2E — surfaces

**Panneau plaqué bois** : *mise à jour ultérieure recommandée* — le Lot 2E notait `adhésif réel et correspondance Ecoinvent à établir` comme point ouvert pour le collage placage/substrat. Ce lot ne trouve aucune brique d'adhésif bois générique pertinente (PVAc = monomère seul) qui pourrait combler cette lacune spécifique — **la conclusion du Lot 2E reste valable et n'est pas améliorée** : le collage placage-panneau demeure une brique manquante, la colle PVA elle-même n'étant représentée qu'à l'état de monomère.

**Collage HPL/stratifié** : *mise à jour ultérieure recommandée* — le Lot 2E n'avait identifié aucun procédé de pressage/collage pour le HPL. Ce lot confirme qu'aucune colle contact formulée n'existe non plus pour recoller un stratifié sur un substrat — **la lacune du Lot 2E est donc confirmée et légèrement aggravée** : non seulement le procédé de pressage HPL est absent, mais l'adhésif de pose (pour un HPL déjà fabriqué, collé ensuite sur un substrat en atelier) est également introuvable.

---

## SYNTHÈSE DU LOT 2F

| Produit_metier | Produit_fonctionnel_Ecoinvent | Meilleur_dataset | UUID | Niveau_A_B_C_D_E | Correspondance_physique | Formulation_connue | Unite | Location | Geographie_QC | Donnees_primaires_QC | Verdict | Principale_lacune | Variables_fournisseur | Action_recommandee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colle PVA/PVAc blanche | Non | market for vinyl acetate | 9381f4dc-deda-3e02-9cf8-4ef4321b137e | D | Faible | Non | kg | Global | Aucune identifiée | Aucune identifiée | Proxy matière seulement | Seul le monomère existe, plusieurs étapes avant une colle formulée | Formulation réelle, densité, masse achetée, consommation | Données fournisseur nécessaires |
| EVA hot-melt (encolleuse chants) | Non | market for ethylene vinyl acetate copolymer | fe0fb6f7-fd33-3303-a767-fc1464446ce1 | C | Faible à moyenne | Non | kg | Global | Aucune identifiée | Aucune identifiée | Proxy matière seulement | Résine brute sans cires/tackifiants/additifs de formulation hot-melt | Formulation réelle, grammage/m linéaire, température d'application | Données fournisseur nécessaires |
| Colle contact (stratifié) | Non | Aucun dataset pertinent identifié avec les méthodes d'interrogation disponibles | Sans objet | E | Aucune | Non | Sans objet | Sans objet | Aucune identifiée | Aucune identifiée | Lacune majeure | Aucune brique chimique confirmée (correction du Lot 1 : polychloroprène non retrouvé) | Chimie réelle, teneur en solides, solvant, densité | Rechercher autre source |
| Adhésif polyuréthane | Non | market for polyol + methylene diphenyldiisocyanate (précurseurs séparés) | Voir flows polyol / MDI ci-dessus | D | Faible | Non | kg | Non vérifiée ce tour | Aucune identifiée | Aucune identifiée | Proxy matière seulement | Précurseurs séparés, non combinés/formulés ; seuls produits PU finis = mousses (fonction différente) | Type PU, ratio polyol/isocyanate, catalyseurs, consommation | Données fournisseur nécessaires |

---

## IMPACT POTENTIEL SUR LE RÉFÉRENTIEL — `docs/materiaux-ebenisterie.md` (proposé, non appliqué)

**Rappel : ce fichier n'est PAS modifié. Éléments proposés pour QC avant intégration.**

### Colle PVA/PVAc blanche
- **Ecoinvent** : seul le monomère vinyl acetate (Global, kg).
- **Correspondance** : aucune avec le produit formulé.
- **Lacune principale** : absence de toute étape entre le monomère et la colle prête à l'emploi.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : recherche exhaustive sans résultat pour tout adhésif bois formulé ; un faux positif plausible (adhesive, for metal) inspecté et rejeté.
- **Recommandation** : données fournisseur indispensables avant toute tentative de proxy.

### EVA hot-melt (encolleuse de chants)
- **Ecoinvent** : copolymère EVA brut (Global, kg), sans additifs.
- **Correspondance** : faible à moyenne (bonne famille chimique, pas de formulation).
- **Lacune principale** : absence des cires/tackifiants qui caractérisent un hot-melt réellement applicable.
- **Statut recommandé** : 🟠 À adapter.
- **Résumé** : c'est la brique la plus proche d'un proxy défendable parmi les quatre adhésifs de ce lot.
- **Recommandation** : envisager une reconstruction documentée si la formulation réelle (parts massiques EVA/cires/résines) est obtenue d'un fournisseur.

### Colle contact (stratifié)
- **Ecoinvent** : aucune brique confirmée cette fois-ci (correction d'une citation erronée du Lot 1).
- **Correspondance** : aucune.
- **Lacune principale** : absence totale, y compris au niveau chimique de base.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : recherche exhaustive convergente vers l'absence ; la piste polychloroprène du Lot 1 n'a pas pu être reconfirmée.
- **Recommandation** : vérifier si l'accès direct à openLCA (hors MCP) permet de retrouver un dataset de type polychloroprène/néoprène avant de conclure définitivement.

### Adhésif polyuréthane
- **Ecoinvent** : deux précurseurs séparés (polyol, MDI) ; aucun produit PU adhésif ; seules des mousses PU existent (fonction différente, faux positifs écartés).
- **Correspondance** : faible.
- **Lacune principale** : précurseurs non combinés, aucune formulation.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : usage occasionnel du métier, cohérent avec une lacune Ecoinvent tout aussi occasionnelle à documenter plutôt qu'à combler dans l'immédiat.
- **Recommandation** : données fournisseur nécessaires si l'usage bois-métal/bois-plastique devient significatif dans l'inventaire.

---

*Fin du rapport Lot 2F. Aucun dataset openLCA modifié. Aucun proxy construit. `docs/materiaux-ebenisterie.md` non modifié. Seuls les 4 adhésifs demandés ont été traités.*
