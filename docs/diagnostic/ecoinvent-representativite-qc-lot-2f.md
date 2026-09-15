# Diagnostic Ecoinvent — Lot 2F
## Adhésifs : PVA/PVAc, EVA hot-melt, colle contact, polyuréthane

Projet ACV mobilier québécois — Base Ecoinvent 3.11, système Cutoff, via openLCA/MCP.

Portée stricte : 4 usages métier d'adhésifs. Aucun dataset modifié, aucun proxy construit, `docs/materiaux-ebenisterie.md` non modifié, aucune modification Git au-delà des deux livrables demandés.

**Point méthodologique préalable à ce lot** : les recherches effectuées durant ce tour n'ont pas permis de retrouver le dataset `market for polychloroprene` (UUID `d1147a50-260c-353a-93c0-def3ebd131d0`) cité au Lot 1 pour la colle contact — cet UUID ne résout plus vers aucun process dans la base interrogée ce tour, et aucune recherche par nom ("polychloroprene", "chloroprene", "neoprene") ne retourne de produit correspondant, seulement des flux élémentaires d'émission de chloroprène (substance, pas produit). **Le dataset de polychloroprène cité antérieurement n'a pas pu être reconfirmé avec les méthodes d'interrogation disponibles pendant le Lot 2F. Il n'est donc pas retenu ici comme brique validée.** Cet écart peut provenir des limites de l'outil MCP, d'une différence d'accès ou de recherche, d'une différence de base/version, ou d'une erreur antérieure — le Lot 2F ne permet pas de trancher entre ces explications.

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
**Fait Ecoinvent** : <cite>"This product is generally considered to be used at the production site. Therefore, the market does not contain any transport."</cite> Les exchanges montrent uniquement le monomère vinyl acetate lui-même (deux lots de production agrégés), sans aucune mention de polymérisation, d'émulsion aqueuse, ni de formulation adhésive. **Interprétation (la nôtre)** : le dataset identifié représente le vinyl acetate et non un adhésif PVAc formulé. Le Lot 2F n'a pas identifié les étapes et constituants permettant de relier ce produit au produit métier.

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
Aucun adhésif PVAc formulé correspondant n'a été identifié avec les méthodes d'interrogation disponibles dans ce lot — seul `market for vinyl acetate` a été identifié, et aucune chaîne reliant ce monomère au produit métier n'a été établie.

### 10. Données fournisseur nécessaires
Formulation/composition réelle du produit ; teneur en solides si pertinente et disponible ; densité si nécessaire à une conversion ; consommation réelle ; masse achetée ou unité d'achat.

### 11. Action recommandée
**Données fournisseur nécessaires** — aucune reconstruction sérieuse n'est possible à partir du seul monomère.

---

## FICHE 2 — EVA HOT-MELT (encolleuse de chants)

### 1. Identification métier
Produit : adhésif thermofusible utilisé dans l'encolleuse de chants. Fonction : collage de bande de chant par encolleuse mécanisée. Forme : non précisée par le contexte métier. Usage : application industrielle/mécanisée.

### 2. Recherche product-first

| Terme | Type | Résultat | Pertinence |
|---|---|---|---|
| hot melt adhesive / hot-melt adhesive / hot melt glue | search_processes | 0 (toutes) | — |
| EVA adhesive / EVA hot melt / ethylene vinyl acetate adhesive / ethylene-vinyl acetate adhesive | search_processes | 0 (toutes) | — |
| thermoplastic adhesive | search_processes | 0 | — |
| edge banding adhesive / edgebanding adhesive / adhesive for edge banding | search_processes | 0 (toutes) | — |
| adhesive (générique, déjà couvert Fiche 1) | search_flows | Mêmes 5 résultats, aucun EVA/hot-melt | — |

Aucun adhésif hot-melt formulé correspondant n'a été identifié par les recherches process + flow effectuées dans ce lot, ni aucun produit spécifique à l'encollage de chants.

### 3. Meilleur candidat
Aucun adhésif formulé. Seule brique : `market for ethylene vinyl acetate copolymer`, UUID `fe0fb6f7-fd33-3303-a767-fc1464446ce1`, location **Global**, unité kg.

### 4. Ce que représente réellement le dataset
**Fait Ecoinvent** : <cite>"In this market, expert judgement was used to develop product specific transport distance estimations."</cite> Les exchanges montrent le copolymère EVA lui-même (deux lots de production agrégés) plus le transport (train, camion, mer transocéanique) — aucun autre constituant n'est documenté dans ce dataset. **Interprétation (la nôtre)** : le copolymère EVA constitue une brique matière intermédiaire. Le Lot 2F n'a pas établi la composition de l'adhésif hot-melt formulé ni la chaîne permettant de passer du copolymère au produit métier.

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
Aucun adhésif EVA hot-melt formulé correspondant n'a été identifié par les recherches disponibles ; aucun procédé spécifique d'encollage de chants n'a été identifié ; la formulation réelle du produit métier reste à obtenir.

### 10. Données fournisseur nécessaires
Composition/formulation réelle du produit ; fractions massiques des constituants si disponibles ; consommation réelle par unité métier pertinente (ex. grammage par mètre linéaire de chant, si disponible) ; densité ou masse si nécessaire ; paramètres d'application uniquement s'ils sont nécessaires à la modélisation et disponibles.

### 11. Action recommandée
**Données fournisseur nécessaires**, avec une reconstruction documentée envisageable si la formulation réelle (fractions massiques des constituants) est obtenue — meilleure base de départ que la Fiche 1 (résine vs monomère).

---

## FICHE 3 — COLLE CONTACT (stratifié)

### 1. Identification métier
Produit : colle contact en pot utilisée pour le collage de stratifié. Fonction : collage de stratifié sur un substrat.

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

Aucun adhésif contact formulé correspondant n'a été identifié par les recherches disponibles. Le dataset de polychloroprène cité antérieurement au Lot 1 n'a pas pu être reconfirmé avec les méthodes d'interrogation disponibles pendant ce lot.

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
Aucun adhésif formulé, aucun polymère PU formé. Seules briques : **briques chimiques amont potentielles identifiées** — `polyol` et `methylene diphenyldiisocyanate` (MDI), non combinés, non formulés, non catalysés, sans chaîne établie vers l'adhésif métier.

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
Aucun adhésif PU formulé correspondant n'a été identifié avec les recherches disponibles ; les produits PU finis rencontrés (mousses) étaient fonctionnellement différents et ont été écartés ; aucun lien quantitatif ou formulation reliant les briques chimiques identifiées (polyol, MDI) à l'adhésif métier n'a été établi.

### 10. Données fournisseur nécessaires
Type et technologie réelle du produit ; composition/formulation fabricant ; fractions massiques pertinentes si disponibles ; densité si nécessaire ; consommation réelle.

### 11. Action recommandée
**Données fournisseur nécessaires** — situation comparable à la Fiche 1 (PVA), avec deux précurseurs identifiés au lieu d'un seul monomère, mais sans formulation ni produit fini pertinent.

---

## CLASSIFICATION RÉCAPITULATIVE A/B/C/D/E

| Adhésif | Niveau | Justification |
|---|---|---|
| PVA/PVAc | **D** | Seul le monomère vinyl acetate existe |
| EVA hot-melt | **C** | Le copolymère EVA (résine) existe, plus proche du produit fini qu'un simple monomère, mais non formulé |
| Colle contact | **E** | Aucune brique chimique confirmée avec les moyens disponibles ce tour |
| Polyuréthane | **D** | Briques chimiques amont potentielles (polyol, MDI) identifiées séparément, sans chaîne démontrée vers l'adhésif métier |

**Réponse directe à la question de Nicolas** : avec les recherches process + flow disponibles dans le Lot 2F, aucun des quatre adhésifs métier n'a été identifié sous la forme d'un adhésif formulé directement correspondant. Le cas EVA est le plus proche, avec un copolymère intermédiaire identifié.

---

## QUESTIONS TRANSVERSALES

**1. Ecoinvent possède-t-il une colle PVAc formulée utilisable ?** Aucun adhésif PVAc formulé correspondant n'a été identifié avec les méthodes d'interrogation disponibles dans ce lot — seul le monomère vinyl acetate a été identifié.

**2. Si oui, correspond-elle réellement à une colle blanche à bois ?** Sans objet (aucun adhésif formulé identifié à la question précédente).

**3. Ecoinvent possède-t-il un adhésif EVA hot-melt formulé ?** Aucun adhésif EVA hot-melt formulé correspondant n'a été identifié avec les méthodes d'interrogation disponibles dans ce lot — seul le copolymère EVA a été identifié.

**4. Existe-t-il quelque chose de spécifique à l'encollage de chants ?** Aucun résultat pertinent identifié pour les termes spécifiques recherchés ("edge banding adhesive" et variantes).

**5. Ecoinvent possède-t-il une colle contact formulée pertinente ?** Aucun adhésif contact formulé correspondant n'a été identifié avec les méthodes d'interrogation disponibles dans ce lot.

**6. Peut-on établir qu'elle correspond au produit métier utilisé pour le stratifié ?** Sans objet — aucun candidat à évaluer.

**7. Ecoinvent possède-t-il un adhésif PU formulé pertinent ?** Aucun adhésif PU formulé correspondant n'a été identifié avec les méthodes d'interrogation disponibles dans ce lot — seuls des mousses PU (fonction différente, écartées) et deux briques chimiques amont potentielles (polyol, MDI) ont été identifiées.

**8. Pour quels produits n'avons-nous que le polymère/résine ?** EVA hot-melt (résine EVA seule).

**9. Pour quels produits avons-nous réellement un adhésif formulé ?** Aucun des quatre n'a été identifié sous forme d'adhésif formulé avec les recherches disponibles. Un adhésif formulé a néanmoins été rencontré ailleurs dans la base (`adhesive, for metal`, époxy pour cadres de fenêtres aluminium) — inspecté et rejeté pour la Fiche 1, mentionné ici pour transparence : Ecoinvent contient donc bien, dans d'autres familles, des adhésifs réellement formulés, ce qui confirme que l'absence observée pour nos 4 cas est spécifique à ces technologies, pas une limite générale de la base sur les adhésifs.

**10. Quels adhésifs nécessiteraient une reconstruction ?** Les quatre, à des degrés différents — EVA hot-melt étant le plus proche d'une reconstruction crédible (résine + additifs à documenter), la colle contact étant la plus éloignée (aucune brique de départ).

**11. Quels adhésifs nécessitent prioritairement des données fournisseur ?** La colle contact en priorité absolue (aucune brique) ; puis PVA et PU (précurseurs seulement) ; EVA hot-melt en dernier (déjà une résine, formulation à préciser).

**12. Existe-t-il des données primaires québécoises identifiées ?** Aucune identifiée, pour les quatre adhésifs.

**13. Le Lot 2F permet-il d'améliorer les conclusions des Lots 2D ou 2E ?** Voir section dédiée ci-dessous.

---

## IMPACT POTENTIEL SUR LES DIAGNOSTICS PRÉCÉDENTS

### Lot 2D — bandes de chant

**Chant bois préencollé** : le Lot 2F identifie un copolymère EVA comme brique matière intermédiaire, mais aucun adhésif hot-melt formulé correspondant n'a été identifié. Cette brique ne suffit donc pas, à elle seule, à représenter le chant préencollé (la lacune sur le bois mince, établie au Lot 2D, demeure également non comblée).

**EVA pour encolleuse de chants** : *mise à jour ultérieure recommandée* — le Lot 2D n'avait pas étudié l'adhésif d'encollage de chants en détail (hors périmètre). Ce lot précise que la résine EVA brute existe (classification C), ce qui est une information légèrement plus favorable que "aucune brique" — à noter si le Lot 2D est révisé pour intégrer explicitement la brique adhésive dans son évaluation de la bande de chant bois préencollée.

### Lot 2E — surfaces

**Panneau plaqué bois** : *mise à jour ultérieure recommandée* — le Lot 2E notait `adhésif réel et correspondance Ecoinvent à établir` comme point ouvert pour le collage placage/substrat. Ce lot ne doit pas être utilisé pour conclure sur le collage industriel d'un panneau plaqué acheté fini — le contexte métier n'établit pas quel adhésif est utilisé par le fabricant de ce panneau. Le résultat PVA/PVAc obtenu dans ce lot concerne la colle d'assemblage bois utilisée en atelier, un usage distinct. Le point ouvert du Lot 2E reste donc non résolu par ce lot.

**Collage HPL/stratifié** : *mise à jour ultérieure recommandée* — le Lot 2E n'avait identifié aucun procédé de pressage/collage pour le HPL. Le Lot 2F apporte une information supplémentaire : aucun adhésif contact formulé correspondant n'a été identifié avec les recherches disponibles. La représentation du collage du stratifié reste donc un point ouvert.

---

## SYNTHÈSE DU LOT 2F

| Produit_metier | Produit_fonctionnel_Ecoinvent | Meilleur_dataset | UUID | Niveau_A_B_C_D_E | Correspondance_physique | Formulation_connue | Unite | Location | Geographie_QC | Donnees_primaires_QC | Verdict | Principale_lacune | Variables_fournisseur | Action_recommandee |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colle PVA/PVAc blanche | Non | market for vinyl acetate | 9381f4dc-deda-3e02-9cf8-4ef4321b137e | D | Faible | Non | kg | Global | Aucune identifiée | Aucune identifiée | Proxy matière seulement | Aucun adhésif PVAc formulé correspondant identifié ; chaîne vers le produit métier non établie | Formulation/composition réelle, teneur en solides si pertinente, densité si nécessaire, consommation réelle, masse achetée ou unité d'achat | Données fournisseur nécessaires |
| EVA hot-melt (encolleuse chants) | Non | market for ethylene vinyl acetate copolymer | fe0fb6f7-fd33-3303-a767-fc1464446ce1 | C | Faible à moyenne | Non | kg | Global | Aucune identifiée | Aucune identifiée | Proxy matière seulement | Copolymère intermédiaire identifié ; formulation hot-melt et chaîne vers le produit métier non établies | Composition/formulation réelle, fractions massiques si disponibles, consommation réelle par unité métier pertinente, densité/masse si nécessaire, paramètres d'application si nécessaires et disponibles | Données fournisseur nécessaires |
| Colle contact (stratifié) | Non | Aucun dataset pertinent identifié avec les méthodes d'interrogation disponibles | Sans objet | E | Aucune | Non | Sans objet | Sans objet | Aucune identifiée | Aucune identifiée | Lacune majeure | Aucune brique chimique confirmée ; résultat polychloroprène antérieur non reconfirmé pendant le Lot 2F | Chimie réelle, teneur en solides, solvant, densité | Rechercher autre source |
| Adhésif polyuréthane | Non | market for polyol + methylene diphenyldiisocyanate (briques chimiques amont potentielles, non combinées) | Voir flows polyol / MDI ci-dessus | D | Faible | Non | kg | Non vérifiée ce tour | Aucune identifiée | Aucune identifiée | Proxy matière seulement | Briques chimiques amont potentielles (polyol, MDI) identifiées séparément, sans chaîne démontrée vers l'adhésif métier ; produits PU finis rencontrés (mousses) fonctionnellement différents et écartés | Type et technologie réelle, composition/formulation fabricant, fractions massiques si disponibles, densité si nécessaire, consommation réelle | Données fournisseur nécessaires |

---

## IMPACT POTENTIEL SUR LE RÉFÉRENTIEL — `docs/materiaux-ebenisterie.md` (proposé, non appliqué)

**Rappel : ce fichier n'est PAS modifié. Éléments proposés pour QC avant intégration.**

### Colle PVA/PVAc blanche
- **Ecoinvent** : seul le monomère vinyl acetate (Global, kg).
- **Correspondance** : aucune avec le produit formulé.
- **Lacune principale** : absence de toute étape entre le monomère et la colle prête à l'emploi.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : aucun adhésif bois formulé correspondant n'a été identifié avec les méthodes d'interrogation disponibles ; un faux positif plausible (adhesive, for metal) inspecté et rejeté.
- **Recommandation** : données fournisseur indispensables avant toute tentative de proxy.

### EVA hot-melt (encolleuse de chants)
- **Ecoinvent** : copolymère EVA brut (Global, kg), sans additifs.
- **Correspondance** : faible à moyenne (bonne famille chimique, pas de formulation).
- **Lacune principale** : formulation hot-melt complète et chaîne vers le produit métier non établies.
- **Statut recommandé** : 🟣 À reconstruire.
- **Résumé** : le dataset identifié est une matière intermédiaire (copolymère EVA), et non un adhésif formulé directement utilisable ; une représentation du produit métier nécessiterait une reconstruction documentée à partir de données supplémentaires.
- **Recommandation** : reconstruction documentée envisageable si la formulation réelle (fractions massiques des constituants) est obtenue d'un fournisseur.

### Colle contact (stratifié)
- **Ecoinvent** : aucune brique confirmée avec les méthodes d'interrogation disponibles pendant ce lot ; le résultat polychloroprène antérieur n'a pas pu être reconfirmé.
- **Correspondance** : aucune.
- **Lacune principale** : aucune brique chimique identifiée avec les méthodes disponibles, y compris au niveau des précurseurs de base.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : aucun résultat pertinent identifié avec les méthodes disponibles, sous réserve des limites de l'outil ; la piste polychloroprène du Lot 1 n'a pas pu être reconfirmée.
- **Recommandation** : vérifier si l'accès direct à openLCA (hors MCP) permet de retrouver un dataset de type polychloroprène/néoprène avant de conclure définitivement.

### Adhésif polyuréthane
- **Ecoinvent** : deux briques chimiques amont potentielles identifiées (polyol, MDI), non combinées/formulées ; aucun adhésif PU formulé correspondant identifié ; les seuls produits PU finis rencontrés sont des mousses (fonction différente, écartées).
- **Correspondance** : faible.
- **Lacune principale** : briques chimiques amont seulement, sans chaîne démontrée vers l'adhésif métier.
- **Statut recommandé** : 🔴 Lacune majeure.
- **Résumé** : usage occasionnel du métier, cohérent avec une lacune Ecoinvent tout aussi occasionnelle à documenter plutôt qu'à combler dans l'immédiat.
- **Recommandation** : données fournisseur nécessaires si l'usage bois-métal/bois-plastique devient significatif dans l'inventaire.

---

*Fin du rapport Lot 2F. Aucun dataset openLCA modifié. Aucun proxy construit. `docs/materiaux-ebenisterie.md` non modifié. Seuls les 4 adhésifs demandés ont été traités.*
