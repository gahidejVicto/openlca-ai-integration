# Collecte de données fabricants — RECQ36 (2026-09-22)

> [!IMPORTANT]
> Ce document est le **point d'entrée** d'une passe de collecte documentaire
> sourcée sur des produits fabricants réels, réalisée le 2026-09-22 sur la
> branche `recq36/emballage-pe-foam-et-cloture-recherches`. **Aucune
> recherche OpenLCA/Ecoinvent n'a été effectuée dans cette passe**
> (consigne explicite de la mission) — cette collecte prépare de futures
> reconstructions ACV, elle ne les réalise pas.

> [!NOTE]
> **Passe corrective et complémentaire (même jour, 2026-09-22) :** deux
> sujets ont été repris après la collecte initiale — (1) remplacement de la
> recherche exploratoire de bande de chant par **quatre produits de
> référence explicitement choisis par Jérôme** (voir
> [`bandes-de-chant/README.md`](../inventaire/bandes-de-chant/README.md)),
> et (2) une nouvelle tentative, réussie, pour trouver la masse du **Blum
> MOVENTO** (voir CAS 2 mis à jour ci-dessous, avec un écart de numérotation
> découvert entre deux documents Blum). Le reste de la collecte initiale
> (CAS 1, 3, 6) est inchangé.

> [!CAUTION]
> **Relecture humaine (même jour, 2026-09-22) — deux corrections
> supplémentaires apportées suite à de nouvelles preuves apportées par
> Jérôme :**
> 1. **CAS 5d (bande de chant PE) — conclusion négative réfutée.** Un
>    produit commercial « bande de chant en polyéthylène » existe bien
>    (Naber, réf. 1112007), mais sa fonction déclarée (espacement/
>    insonorisation de plan de travail) diffère de la fonction décorative
>    des trois autres références bande de chant. Voir
>    [`bandes-de-chant/pe-recherche-negative-2026-09-22.md`](../inventaire/bandes-de-chant/pe-recherche-negative-2026-09-22.md)
>    (conclusion corrigée, historique conservé).
> 2. **CAS 4 (Royale 404) — documentation primaire obtenue.** La FDS et la
>    fiche technique papier du Royale 404 (fournies par Jérôme, sans URL
>    numérique) confirment la chimie PVAc et donnent les propriétés
>    physiques nécessaires à une première reconstruction. Voir
>    [`adhesifs/royale-404-abradhesif.md`](../inventaire/adhesifs/royale-404-abradhesif.md).
>
> **Aucune recherche OpenLCA/Ecoinvent n'a été relancée dans cette
> relecture ; aucune reconstruction ACV quantitative n'a été entamée.**

## Objectif et méthode

Six cas ont été traités : deux coulisses de tiroir, deux adhésifs, une
recherche exploratoire de bande de chant (2-4 candidats, sans choix imposé),
et un complément de recherche sur le matériau d'emballage blanc en rouleau
(hypothèse « film mousse PE » posée dans la passe Ecoinvent précédente).

**Règles de preuve appliquées** (voir aussi
[`docs/sources/README.md`](../sources/README.md)) :

- conserver l'URL, le titre, l'organisme et la date de consultation de
  chaque source ;
- distinguer explicitement donnée **fabricant**, donnée **distributeur** et
  **inférence/calcul** ;
- ne jamais déduire une composition ou une masse non publiée ;
- indiquer `non trouvé` plutôt que d'inventer une valeur ;
- privilégier fabricant > documentation technique fabricant > FDS/SDS
  fabricant > distributeur spécialisé.

## Fiches produites

| Cas | Produit | Fiche |
|---|---|---|
| 1 | Coulisse latérale standard — Langevin Forest (sans marque) | [`quincaillerie/coulisse-langevin-forest.md`](../inventaire/quincaillerie/coulisse-langevin-forest.md) |
| 2 | Coulisse invisible — Blum MOVENTO (`760H4000S`) | [`quincaillerie/coulisse-blum-movento.md`](../inventaire/quincaillerie/coulisse-blum-movento.md) |
| 3 | Colle contact à l'eau — 3M Fastbond 30-NF | [`adhesifs/3m-fastbond-30nf.md`](../inventaire/adhesifs/3m-fastbond-30nf.md) |
| 4 | Colle blanche à bois — Royale 404 (Abradhésif) — **chimie PVAc confirmée à la relecture** | [`adhesifs/royale-404-abradhesif.md`](../inventaire/adhesifs/royale-404-abradhesif.md) |
| 5a | Bande de chant bois véritable — Merisier blanc (Cedan/Richelieu) | [`bandes-de-chant/merisier-blanc-cedan.md`](../inventaire/bandes-de-chant/merisier-blanc-cedan.md) |
| 5b | Bande de chant polyester — Érable Hardrock #992 (Richelieu) | [`bandes-de-chant/erable-hardrock-992-polyester.md`](../inventaire/bandes-de-chant/erable-hardrock-992-polyester.md) |
| 5c | Bande de chant PVC — Gris foncé #100 (Richelieu) | [`bandes-de-chant/gris-fonce-100-pvc.md`](../inventaire/bandes-de-chant/gris-fonce-100-pvc.md) |
| 5d | Bande de chant PE — un produit commercial existe (Naber), fonction non confirmée pour RECQ36 | [`bandes-de-chant/pe-recherche-negative-2026-09-22.md`](../inventaire/bandes-de-chant/pe-recherche-negative-2026-09-22.md) |
| *(historique)* | Recherche exploratoire initiale (4 candidats OEM, supersédée) | [`plastiques/bande-de-chant-candidats.md`](../inventaire/plastiques/bande-de-chant-candidats.md) |
| 6 | Film mousse PE d'emballage (hypothèse) | [`emballages/film-mousse-pe.md`](../inventaire/emballages/film-mousse-pe.md) |

## Tableau de synthèse

| Famille | Produit | Référence | Source principale | Masse | Matière/composition | Données de fabrication | Données manquantes | Qualité documentaire |
|---|---|---|---|---|---|---|---|---|
| Quincaillerie | Coulisse latérale std. | `706-2605400` (16″) | Langevin Forest (distributeur) | ❓ Non trouvée | ❓ Non précisée (fabricant/OEM non identifié) | Capacité 75 lb @18″ ; mécanisme soft-close breveté non détaillé | Masse, matériaux, revêtement, pays de fabrication, fabricant réel | ❌ Faible |
| Quincaillerie | Coulisse invisible Blum MOVENTO | `760H4000S` (400 mm, 40 kg) — **écart de numérotation avec `760H4001S` non résolu** | Blum (2 documents officiels distincts) / Richelieu Hardware | ✅ **2,08045 kg/paire** (FAIT SOURCÉ + CALCUL) ; ≈1,04 kg/coulisse (INFÉRENCE) | ✅ Acier zingué ; rouleaux synthétiques (nature exacte non précisée) | Longueur, classe de charge, finition confirmées ; mécanisme BLUMOTION confirmé, composition interne non détaillée | Résolution de l'écart de numérotation ; confirmation « Set = paire » ; usine de fabrication ; EPD | ✅ Élevée (masse trouvée), ⚠️ écart de référence à clarifier |
| Adhésifs | Colle contact à l'eau — 3M Fastbond 30-NF | Produit unique, plusieurs formats | 3M Canada — FDS canadienne (fabricant) | Non applicable (produit liquide) | ✅ Néoprène (20-40 %) + eau (40-60 %) + résines (5-10 % chacune) + fractions mineures partiellement secrètes | ✅ Densité 1,1 g/cm³ ; solides ≈50 % ; COV ≤80 g/L ; rendement 3,0-3,5 g/pi²/surface | Fractions exactes de 3 composants (secret commercial), site de fabrication précis, EPD | ✅ Élevée |
| Adhésifs | Colle blanche — Royale 404 | Royale 404 | Abradhésif inc. — **FDS + fiche technique papier fournies par Jérôme (2026-09-22)** | Non applicable (produit liquide) ; densité **1,06 (FDS) / 1,1 kg/L (fiche technique)**, non fusionnées | ✅ **PVAc confirmé** (« acétate polyvinylique en émulsion » / « acétate de polyvinyle ») ; taux de solides 51 %±1 % ; formulation détaillée confidentielle | ✅ pH 4,75±0,25 ; COV 1,4 g/L ; viscosité 5500±500 (unité non précisée) ; bilan massique calculé (≈0,51 kg solides/kg, ≈0,561 kg solides/L) | Composition détaillée de la fraction solide, additifs, répartition exacte eau/non-solide, procédé de fabrication | ✅ Élevée (documents primaires obtenus) |
| Bande de chant | Bois véritable — Merisier blanc | Cedan/Richelieu, SKU `MS03SM078VSA0`, 1 mm × 7/8 po | Richelieu (fabricant Cedan nommé) | ❓ Non trouvée (volontairement non calculée à partir d'une densité générique) | ✅ Essence clarifiée : « White Birch » (bouleau), pas cerisier, malgré le nom commercial « merisier » | Épaisseur, largeur, longueur de rouleau (492 pi), assemblage (microjoint), support (non préencollé) confirmés | Masse, densité, origine, fiche technique | ⚠️ Moyenne (dimensions confirmées, masse absente) |
| Bande de chant | Polyester — Érable Hardrock #992 | Richelieu, SKU `P992234250` | Richelieu (fabricant réel non nommé) | ❓ Non trouvée | ⚠️ « Polyester », construction « 2 plis » confirmée mais nature exacte de chaque pli non détaillée | Largeur, fini, support (préencollé), format d'emballage confirmés ; **épaisseur absente de la fiche technique elle-même** | Épaisseur, masse, construction exacte des 2 plis, fabricant réel | ❌ Faible (le moins documenté des 3 candidats plastiques/composites) |
| Bande de chant | PVC — Gris foncé #100 | Richelieu, SKU `T1001822` | Richelieu (fabricant réel/OEM non nommé) | ❓ Non trouvée | ✅ PVC confirmé ; plastifiants/additifs non documentés | Épaisseur (0,018 po), largeur, longueur de rouleau (1200 pi) confirmées — le mieux documenté des 3 pour les dimensions de base | Fabricant réel, masse, densité, plastifiants | ⚠️ Moyenne (dimensions confirmées, composition/masse absentes) |
| Bande de chant | PE — **existence commerciale confirmée, fonction non confirmée pour RECQ36** | Naber, réf. `1112007` (fabricant réel déclaré : Stauffer Schallschutz + Akustik) | Naber (page produit + fiche PDF officielle) | Non publiée (densité volumique 33 kg/m³ publiée) | ✅ Mousse de polyéthylène à cellules fermées, 33 kg/m³ | Dimensions (4×50 mm, rouleau 20 m), autocollante, fonction déclarée : espacement/insonorisation de plan de travail — **pas une fonction décorative de panneau** | Correspondance fonctionnelle avec l'usage métier RECQ36 (clarification Nicolas nécessaire) | ✅ Élevée pour le produit Naber lui-même ; ⚠️ correspondance métier non établie |
| Emballage | Film mousse PE (hypothèse) | Comparaison : rouleau S.E.D Emballage (France) | S.E.D Emballage (distributeur français, hors QC/Canada) | ❓ Non publiée | ❓ Type de PE non précisé ; densité non publiée | Épaisseurs 1-8 mm, largeurs/longueurs confirmées ; procédé non documenté | Type de PE, densité, grammage, procédé, fournisseur réel des entreprises RECQ36 | ❌ Faible (produit de comparaison) ; ⚠️ moyenne pour les pistes québécoises complémentaires (Protac, Colorel) |

## 1. Résultats par cas

### CAS 1 — Coulisse latérale standard (Langevin Forest)
Produit **sans marque identifiable**. Aucune donnée physique (masse,
matériaux, revêtement) trouvée publiquement. Blocage complet : identité du
fabricant/OEM inconnue.

### CAS 2 — Coulisse invisible (Blum MOVENTO) — mis à jour, passe corrective
Référence `760H4000S` retenue (400 mm, 40 kg), disponible directement chez
Richelieu Hardware. Matériau (acier zingué), mécanisme BLUMOTION et classe
de charge bien confirmés par le fabricant. **Masse désormais trouvée** :
une fiche « Product details » Blum officielle distincte du catalogue
technique (datée du 02/01/2019) donne « Weight per 1,000 Pcs : 2 080,45 kg »
pour un « Item package: Set » — recoupé avec une confirmation indépendante
(« Eenheid: Paar », distributeur néerlandais) pour établir **2,08045 kg par
paire** (FAIT SOURCÉ + CALCUL), soit **≈1,04 kg par coulisse** (INFÉRENCE
par division par 2). **Découverte importante :** le catalogue technique
officiel Blum (TD-132/1 EN/06.22, lu intégralement cette fois) utilise en
réalité la référence **`760H4001S`** pour la même configuration apparente
(NL 400 mm, 40 kg, BLUMOTION S) — un écart de numérotation entre deux
documents Blum authentiques, non résolu, à signaler avant tout usage
définitif. Voir [`quincaillerie/coulisse-blum-movento.md`](../inventaire/quincaillerie/coulisse-blum-movento.md)
pour le détail complet.

### CAS 3 — Colle contact à l'eau (3M Fastbond 30-NF)
**Cas le mieux documenté de cette passe.** FDS canadienne complète obtenue :
composition détaillée (base néoprène/chloroprène, pas PVAc), densité,
teneur en solides, COV, rendement d'application. Trois composants mineurs
(méthanol, rosinate de potassium, toluène) ont une fraction exacte retenue
comme secret commercial — documenté explicitement, non reconstitué.

### CAS 4 — Colle blanche à bois (Royale 404) — mis à jour, relecture 2026-09-22
Fabricant réel identifié (Abradhésif, St-Bruno-de-Montarville, QC — marque
fondatrice de l'entreprise depuis 1976). **La chimie PVAc est désormais
confirmée par des documents primaires** : Jérôme a fourni, lors de la
relecture, la FDS (« Acétate polyvinylique en émulsion », densité relative
1,06, section 3 = mélange à formulation confidentielle) et la fiche
technique papier (« acétate de polyvinyle », taux de solides 51 %±1 %,
densité relative 1,1 kg/L, pH 4,75±0,25, COV 1,4 g/L) du Royale 404
lui-même — pas d'un produit voisin. **Ces deux documents sont des sources
papier fournies directement par Jérôme, sans URL ni PDF numérique.** Un
écart de densité entre les deux documents (1,06 vs 1,1 kg/L) est documenté
sans être fusionné. Un bilan massique simplifié (≈0,51 kg solides / ≈0,49 kg
fraction non solide par kg, ≈0,561 kg solides/L) est calculé et explicitement
identifié comme tel. Voir [`adhesifs/royale-404-abradhesif.md`](../inventaire/adhesifs/royale-404-abradhesif.md)
pour le détail complet.

### CAS 5 — Bande de chant — mis à jour, passe corrective : 4 produits de référence choisis par Jérôme
La recherche exploratoire à 4 candidats OEM (Doellken, Rehau, Cedan/Richelieu,
PCM — conservée comme contexte historique dans
[`plastiques/bande-de-chant-candidats.md`](../inventaire/plastiques/bande-de-chant-candidats.md))
est **remplacée** par quatre produits Richelieu explicitement choisis :

- **5a — Merisier blanc** (bois véritable, Cedan/Richelieu, SKU
  `MS03SM078VSA0`, 1 mm × 7/8 po) : fabricant, essence (bouleau — le nom
  anglais officiel est « White Birch », pas cerisier), dimensions et
  assemblage confirmés ; masse et densité non trouvées.
- **5b — Érable Hardrock #992** (polyester, Richelieu, SKU `P992234250`) :
  matériau et construction « 2 plis » confirmés, mais épaisseur, masse et
  nature exacte des plis non documentées — le cas le moins documenté.
- **5c — Gris foncé #100** (PVC, Richelieu, SKU `T1001822`) : épaisseur
  (0,018 po), largeur et longueur de rouleau confirmées — le mieux
  documenté pour les dimensions de base — mais fabricant réel, masse et
  densité non trouvés.
- **5d — PE** : **conclusion négative corrigée à la relecture (2026-09-22).**
  Un produit commercial existe bel et bien : **Naber, réf. `1112007`**,
  « Bande de chant en polyéthylène, blanc », mousse PE à cellules fermées
  (33 kg/m³), fabriquée par Stauffer Schallschutz + Akustik (Allemagne).
  Sa fonction déclarée par le fabricant/distributeur est un **ruban
  d'espacement/insonorisation entre les faces d'un plan de travail de
  cuisine** — pas un revêtement décoratif de chant de panneau comme les
  trois autres références. La question posée à Nicolas est reformulée :
  elle porte désormais sur la nature/fonction exacte de la bande PE
  utilisée en atelier, pas sur son existence commerciale. **Aucun
  changement de taxonomie (PE → PP).** La recherche négative initiale
  (6 sources) reste documentée comme historique, avec le retrait explicite
  de Wikipédia comme élément de preuve.

Voir [`bandes-de-chant/README.md`](../inventaire/bandes-de-chant/README.md)
pour le détail complet des quatre fiches.

### CAS 6 — Film mousse PE d'emballage (complément)
Le produit de comparaison fourni (S.E.D Emballage) s'est révélé être une
entreprise **française**, peu documentée techniquement (pas de densité, pas
de type de PE précisé, pas de fiche technique). Une recherche complémentaire
a identifié un **fabricant québécois réel de mousse PE** (Les Industries
Protac inc., Saint-Célestin, QC) et un usage meuble documenté par un
distributeur québécois (Colorel, épaisseur 1/8″ pour meubles). Une fiche
technique réelle d'une mousse PE canadienne (Jacobs & Thompson, Ontario)
donne un ordre de grandeur de densité (28,8-35,2 kg/m³) — **non attribuable
au produit RECQ36 sans confirmation**.

## 2. Sources utilisées (vue d'ensemble)

Voir la section « Sources documentaires » de chaque fiche pour le détail
complet (URL, organisme, date de consultation 2026-09-22, page le cas
échéant). Types de sources mobilisées dans cette passe :

- pages produit fabricant (Blum, 3M, Abradhésif, Protac, Rehau, Doellken,
  Naber) ;
- FDS/SDS fabricant (3M Canada et Royale 404, complètes et lues
  intégralement — celle du Royale 404 étant un document papier fourni par
  Jérôme, sans URL) ;
- fiches techniques fabricant (Rehau, Royale 933MAX puis Royale 404 lui-même
  à la relecture — document papier —, Jacobs & Thompson, Naber) ;
- catalogues distributeur (Richelieu Hardware, PCM, Colorel, Groupe Gilco) ;
- une source distributeur hors Québec/Canada, explicitement signalée comme
  telle (S.E.D Emballage, France).

> [!NOTE]
> **Wikipédia a été retiré comme élément de preuve** (relecture 2026-09-22)
> partout où il était cité — voir
> [`bandes-de-chant/pe-recherche-negative-2026-09-22.md`](../inventaire/bandes-de-chant/pe-recherche-negative-2026-09-22.md#7-sources-documentaires).

## 3. Données non trouvées (blocages principaux)

| Cas | Donnée manquante bloquante |
|---|---|
| 1 | Identité du fabricant/OEM ; masse ; matériaux |
| 2 | ~~Masse par référence~~ **trouvée (passe corrective)** ; reste : résolution de l'écart `760H4000S`/`760H4001S` ; confirmation « Set = paire » |
| 3 | Fractions exactes de 3 composants à secret commercial (mineur, non bloquant) |
| 4 | ~~FDS/fiche technique dédiée au Royale 404~~ **obtenues (relecture, documents papier)** ; reste : composition détaillée de la fraction solide, additifs, procédé de fabrication |
| 5a | Masse, densité, origine du Merisier blanc (Cedan) |
| 5b | Épaisseur, masse, construction exacte des 2 plis, fabricant réel de l'Érable Hardrock #992 |
| 5c | Fabricant réel, masse, densité, plastifiants du Gris foncé #100 |
| 5d | ~~Existence commerciale d'une bande PE~~ **confirmée (Naber 1112007, relecture)** ; reste : correspondance fonctionnelle avec l'usage métier RECQ36 — clarification Nicolas nécessaire |
| 6 | Fournisseur réel des entreprises RECQ36 concernées ; densité et type de PE du produit réellement utilisé |

## 4. Produits de référence choisis pour la bande de chant (CAS 5, passe corrective)

**A — Merisier blanc** (bois véritable, Cedan/Richelieu), **B — Érable
Hardrock #992** (polyester, Richelieu), **C — Gris foncé #100** (PVC,
Richelieu), **D — PE** (existence commerciale confirmée — Naber réf.
`1112007` — correspondance fonctionnelle avec l'usage métier RECQ36 encore
à clarifier avec Nicolas ; conclusion négative initiale corrigée à la
relecture du 2026-09-22). Détail complet dans
[`bandes-de-chant/README.md`](../inventaire/bandes-de-chant/README.md).
La recherche exploratoire initiale à 4 candidats OEM reste disponible comme
contexte historique dans
[`plastiques/bande-de-chant-candidats.md`](../inventaire/plastiques/bande-de-chant-candidats.md).

## 5. Produits pour lesquels les données sont désormais suffisantes pour envisager une reconstruction ACV

- **CAS 3 — Colle contact 3M Fastbond 30-NF** : composition, densité,
  teneur en solides et rendement documentés par une FDS fabricant complète.
  C'est le cas le plus mûr de cette passe.
- **CAS 2 — Blum MOVENTO** *(mis à jour, passe corrective)* : matériau,
  finition, paramètres fonctionnels **et désormais la masse** (2,08 kg/paire)
  sont documentés — sous réserve de la résolution de l'écart de
  numérotation `760H4000S`/`760H4001S` avant un usage définitif.
- **CAS 4 — Royale 404** *(mis à jour, relecture)* : chimie PVAc, taux de
  solides, densité (deux valeurs distinctes documentées), pH, COV et un
  bilan massique simplifié sont désormais disponibles via des documents
  primaires fabricant. Inconnues restantes : composition détaillée de la
  fraction solide, additifs, répartition exacte eau/non-solide, procédé de
  fabrication (voir la fiche pour le détail).

## 6. Produits pour lesquels un contact fabricant (ou une clarification métier) est nécessaire

- **CAS 1 — Coulisse Langevin Forest** : blocage total, identité du
  fabricant inconnue — contact avec le distributeur ou pesée physique
  recommandés en priorité.
- **CAS 2 — Blum MOVENTO** : contact Blum/Richelieu pour résoudre l'écart
  de numérotation et confirmer l'interprétation « Set = paire ».
- **CAS 4 — Royale 404** *(réduit, relecture)* : chimie et propriétés
  physiques principales obtenues. Reste à demander à Abradhésif : composition
  détaillée de la fraction solide et des éventuels additifs (probablement
  non communicable, formulation déclarée confidentielle), confirmation que
  la fraction non solide est bien exclusivement de l'eau, explication de
  l'écart de densité entre FDS et fiche technique.
- **CAS 5a/5b/5c — Bande de chant (Merisier blanc, Érable Hardrock #992,
  Gris foncé #100)** : demander à Richelieu/Cedan la masse, la densité et
  (pour 5b/5c) le fabricant réel et la composition exacte.
- **CAS 5d — Bande de chant PE** *(reformulé, relecture)* : **clarification
  métier avec Nicolas** sur la nature et la fonction exacte de la bande PE
  utilisée en atelier (correspond-elle à un produit d'espacement/
  insonorisation type Naber, ou à un revêtement décoratif de chant ?) — pas
  une question d'existence commerciale, désormais tranchée.
- **CAS 6 — Film mousse PE** : contact avec les entreprises RECQ36
  concernées pour confirmer le fournisseur réel et obtenir une fiche
  technique ou un échantillon.

## Journal de travail

| Date | Action | Résultat |
|---|---|---|
| 2026-09-22 | Collecte documentaire pour les 6 cas | 6 fiches produites, synthèse rédigée, structure `docs/inventaire/{quincaillerie,adhesifs,plastiques,emballages}/` complétée |
| 2026-09-22 (passe corrective) | Remplacement de la recherche exploratoire de bande de chant par 4 produits de référence choisis | 4 nouvelles fiches dans `docs/inventaire/bandes-de-chant/`, ancienne fiche conservée comme contexte historique |
| 2026-09-22 (passe corrective) | Nouvelle tentative de recherche de masse pour le Blum MOVENTO | Masse trouvée (2,08 kg/paire) ; écart de numérotation `760H4000S`/`760H4001S` découvert et documenté sans être résolu |
| 2026-09-22 (relecture) | Vérification de la référence Naber (bande de chant PE) fournie par Jérôme | Existence commerciale confirmée ; conclusion négative du CAS 5d corrigée ; fonction du produit identifiée comme distincte de l'usage décoratif de panneau |
| 2026-09-22 (relecture) | Intégration de la FDS et de la fiche technique papier du Royale 404 fournies par Jérôme | Chimie PVAc confirmée ; propriétés physiques complètes obtenues ; écart de densité entre les deux documents documenté ; bilan massique calculé |
| 2026-09-22 (relecture) | Retrait de Wikipédia comme élément de preuve | Appliqué dans la fiche PE ; note ajoutée dans cette synthèse |

---

## Statut du document

**Collecte initiale, passe corrective et relecture terminées.** Prêt pour
revue. Aucune reconstruction ACV quantitative n'a été entamée dans cette
relecture.
