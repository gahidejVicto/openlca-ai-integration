# Registre des fabricants et fournisseurs — RECQ36

> [!IMPORTANT]
> **Ce registre est la source canonique des entreprises citées dans la
> feuille de route de collecte étudiant(e).** Toute régénération de la
> feuille de route doit partir de ce fichier et des fiches qu'il relie ;
> une information qui n'existerait que dans le Word doit d'abord être
> rapatriée ici.
>
> **Aucune entreprise n'est validée métier à ce jour.** La liste n'est pas
> figée : elle doit être validée par Vincent (voir [section 6](#6-points-à-soumettre-à-vincent)).

## Chaîne documentaire visée

```text
sources primaires / validations métier
        ↓
documentation Git RECQ36 (ce registre + fiches d'inventaire)
        ↓
feuille de route étudiant(e) (Word généré)
        ↓
collecte terrain
        ↓
nouvelles preuves réinjectées dans Git
```

## 1. Provenance des informations

| Code | Source | Nature |
|---|---|---|
| **FR-V0** | Feuille de route de collecte terrain RECQ36, « Version V0 — 22 septembre 2026 », section 4 (fichier `RECQ36_Feuille_de_route_collecte_etudiant_V1_fiches_fabricants.docx`) | **Synthèse de travail, pas une source primaire.** Ses affirmations restent « information issue de la feuille de route de collecte — à vérifier » tant qu'aucune fiche Git ne les appuie. |
| **N-0928** | Réunion de suivi avec Nicolas, 2026-09-28 | Suggestions et décisions de méthode ; une suggestion n'est pas une validation métier. |
| **Fiche Git** | Fiche d'inventaire liée, avec ses propres sources (S1, S2…) | Prime sur FR-V0 en cas de divergence (voir [section 5](#5-divergences-feuille-de-route--git)). |

Hiérarchie de preuve du projet : fabricant / document primaire > fiche
technique, FDS, EPD > distributeur > déclaration écrite > mesure terrain >
estimation.

## 2. Nomenclature des statuts

Chaque entreprise est qualifiée selon **trois axes indépendants**, pour
qu'un simple candidat ne puisse pas apparaître comme fabricant représentatif
validé.

**Rôle dans la chaîne** (ce que fait l'entreprise pour le produit visé) :

| Rôle | Signification |
|---|---|
| **Fabricant** | Fabrication du produit visé établie par une fiche Git sourcée. |
| **Fabricant (selon FR-V0)** | Fabrication affirmée par la feuille de route, non encore prouvée dans Git. |
| **Fournisseur/distributeur** | Vend ou distribue ; ne prouve pas une fabrication. |
| **Fabricant/OEM à déterminer** | Le fabricant réel du produit acheté n'est pas identifié (typiquement derrière un distributeur). |
| **Entreprise utilisatrice** | Fabrique/livre des meubles ; interrogée sur ses fournisseurs, pas documentée comme fabricant. |

**Statut documentaire** :

| Statut | Signification |
|---|---|
| **Documenté** | Fiche d'inventaire Git avec sources pour le rôle/produit concerné. |
| **Partiellement documenté** | Fiche Git existante, mais le rôle ou le produit cité par FR-V0 n'y est pas couvert. |
| **Candidat identifié** | Entreprise citée par FR-V0, sans fiche Git. |
| **Candidat proposé par Nicolas** | Piste suggérée par Nicolas (N-0928), sans fiche Git. |
| **À identifier** | Identité incertaine ; aucune fiche avant confirmation. |

**Validation métier** :

| Statut | Signification |
|---|---|
| **À valider avec Vincent** | Valeur par défaut de toutes les entrées actuelles. |
| **Validé métier** | Représentativité pour le marché québécois confirmée par Vincent. **Aucune entrée à ce jour.** |

> [!NOTE]
> La colonne « Confiance FR-V0 » reprend telle quelle l'estimation de la
> feuille de route. Elle qualifie l'assurance du rédacteur de la feuille de
> route, **pas** un niveau de preuve ni une validation.

## 3. Vue d'ensemble par famille

Validation métier : **à valider avec Vincent pour toutes les lignes.**

| Famille | Entreprise | Rôle | Statut documentaire | Confiance FR-V0 | Fiche(s) Git | Provenance |
|---|---|---|---|---|---|---|
| Panneaux de particules | Uniboard | Fabricant | Documenté | Élevée | [`uniboard-val-dor.md`](panneaux/uniboard-val-dor.md) | FR-V0 + fiche Git |
| Panneaux de particules | Tafisa Canada | Fabricant | Documenté | Élevée | [`tafisa-lac-megantic.md`](panneaux/tafisa-lac-megantic.md) | FR-V0 + fiche Git |
| MDF | Uniboard | Fabricant | Documenté | Moyen | [`uniboard-mont-laurier.md`](panneaux/uniboard-mont-laurier.md) | FR-V0 + fiche Git |
| MDF | Goodfellow | Fournisseur/distributeur ; MDF : fabricant/OEM à déterminer | Partiellement documenté (fiche bois massif seulement) | Élevé (rôle distributeur) | [`goodfellow.md`](bois/goodfellow.md) | FR-V0 + fiche Git |
| Contreplaqué | Husky Plywood / Commonwealth Plywood | Fabricant | Documenté | Élevé | [`husky-plywood.md`](panneaux/husky-plywood.md), [`husky-plywood-rempli-v1.md`](panneaux/husky-plywood-rempli-v1.md) | FR-V0 + fiche Git |
| Contreplaqué | Ply Supply | Fournisseur/distributeur (rôle exact à confirmer) ; fabricant/OEM à déterminer | Candidat identifié | Moyen | — | FR-V0 |
| Mélaminé / TFL | Tafisa Canada | Fabricant | Partiellement documenté (TFL mentionné, fiche centrée sur le panneau brut) | Élevé | [`tafisa-lac-megantic.md`](panneaux/tafisa-lac-megantic.md) | FR-V0 + fiche Git |
| Mélaminé / TFL | Uniboard | Fabricant (usine TFL à confirmer par référence) | Partiellement documenté | Élevé TFL ; usine à confirmer | [`uniboard-val-dor.md`](panneaux/uniboard-val-dor.md) | FR-V0 + fiche Git |
| Mélaminé / TFL | Distributions Nortra | Fournisseur/distributeur (service de laminage selon FR-V0) | Candidat identifié | Moyen | — | FR-V0 |
| Placage / panneaux plaqués | Les Spécialités MGH / Royflex | Fabricant (selon FR-V0) | Candidat identifié | Élevé | — | FR-V0 |
| Placage / panneaux plaqués | Commonwealth Plywood | Fabricant (division sciage documentée ; division placage selon FR-V0) | Partiellement documenté | Élevé | [`commonwealth-plywood-sciage.md`](bois/commonwealth-plywood-sciage.md) | FR-V0 + fiche Git |
| Placage / panneaux plaqués | Placages X Press | Fournisseur/distributeur (fabrication/lamination à confirmer) | Candidat identifié | Moyen | — | FR-V0 |
| Bandes de chant | Cedan | Fabricant (chant bois véritable ; site non trouvé) | Documenté | Moyen à Élevé | [`merisier-blanc-cedan.md`](bandes-de-chant/merisier-blanc-cedan.md) | FR-V0 + fiche Git |
| Bandes de chant | Richelieu | Fournisseur/distributeur ; polyester et PVC : fabricant/OEM à déterminer | Documenté | Élevé (distribution) | [`erable-hardrock-992-polyester.md`](bandes-de-chant/erable-hardrock-992-polyester.md), [`gris-fonce-100-pvc.md`](bandes-de-chant/gris-fonce-100-pvc.md) | FR-V0 + fiche Git |
| Bandes de chant | Commonwealth Plywood Distribution | Fournisseur/distributeur ; fabricant/OEM à déterminer | Candidat identifié | Élevé (distribution) | — | FR-V0 |
| Adhésifs | Les Adhésifs Marcan | Fabricant (selon FR-V0 ; usine à confirmer par produit) | Candidat identifié | Moyen à Élevé | — | FR-V0 |
| Adhésifs | Abra-Dhésif (Abradhésif inc.) | Fabricant/formulateur (Royale 404) | Documenté | Élevé (distribution) — **dépassé par la fiche Git** | [`royale-404-abradhesif.md`](adhesifs/royale-404-abradhesif.md) | FR-V0 + fiche Git |
| Adhésifs | Canmade Montréal | Fournisseur/distributeur (Jowat et autres marques) ; fabricant/OEM à déterminer | Candidat identifié | Moyen | — | FR-V0 |
| Bois massif feuillu | C.A. Spencer | Fabricant (selon FR-V0) | Candidat identifié | Élevé | — | FR-V0 ; mentionné en N-0928 |
| Bois massif feuillu | Scierie Leclerc et Tremblay | Fabricant (selon FR-V0) | Candidat identifié | Moyen à Élevé | — | FR-V0 ; mentionné en N-0928 |
| Bois massif feuillu | Ressources Lumber | Fabricant (selon FR-V0) | Candidat identifié | Élevé | — | FR-V0 ; mentionné en N-0928 |
| Bois massif feuillu | Commonwealth Plywood — division sciage (Husky Lumber) | Fabricant | Documenté | — (hors FR-V0 §4.8) | [`commonwealth-plywood-sciage.md`](bois/commonwealth-plywood-sciage.md) | Fiche Git (lot 2) |
| Bois massif feuillu | Goodfellow | Fournisseur/distributeur avec transformation ; sciage non établi | Documenté | — (hors FR-V0 §4.8) | [`goodfellow.md`](bois/goodfellow.md) | Fiche Git (lot 2) |
| Bois massif feuillu | Bois Malo | Non établi | Candidat proposé par Nicolas | — | — | N-0928 |
| Bois massif feuillu | BFRANC *(graphie à confirmer)* | Non établi | Candidat proposé par Nicolas | — | — | N-0928 |
| Bois massif feuillu | Bois Poulin | Non établi | Candidat proposé par Nicolas | — | — | N-0928 |
| Bois massif feuillu | « AMB » / « AM B » | Non établi | **À identifier** — ne pas créer de fiche | — | [TODO](bois/candidats-fournisseurs-bois-massif.md#todo-amb) | N-0928 (transcription automatique) |
| Quincaillerie | Richelieu | Fournisseur/distributeur ; fabrication propre à confirmer par produit | Documenté (rôle distributeur) | Élevé (distribution) | [`coulisse-accuride-3832ec.md`](quincaillerie/coulisse-accuride-3832ec.md), [`coulisse-blum-movento.md`](quincaillerie/coulisse-blum-movento.md) | FR-V0 + fiche Git |
| Quincaillerie | Blum | Fabricant (marque autrichienne ; usine non confirmée) | Documenté | Élevé (marque) | [`coulisse-blum-movento.md`](quincaillerie/coulisse-blum-movento.md) | FR-V0 + fiche Git |
| Quincaillerie | Accuride | Fabricant (Accuride International ; usine de la référence non trouvée) | Documenté | Moyen | [`coulisse-accuride-3832ec.md`](quincaillerie/coulisse-accuride-3832ec.md) | FR-V0 + fiche Git |
| Emballages | ACorr | Fabricant (selon FR-V0) — **pas un fournisseur réel établi** | Candidat identifié | Élevé | — | FR-V0 |
| Emballages | OnduCorr | Fabricant (selon FR-V0) — **pas un fournisseur réel établi** | Candidat identifié | Moyen | — | FR-V0 |
| Emballages | Groupe Induspac | Fabricant (selon FR-V0) — **pas un fournisseur réel établi** | Candidat identifié | Élevé | — | FR-V0 |
| Emballages | Mitchel Lincoln | Fabricant (selon FR-V0) — **pas un fournisseur réel établi** | Candidat identifié | Élevé | — | FR-V0 |
| Emballages | Oldwood | Entreprise utilisatrice (à interroger) | Candidat identifié | — | [`film-mousse-pe.md` §5.1](emballages/film-mousse-pe.md#51-méthode-didentification-du-fournisseur-réel-réunion-nicolas-2026-09-28) | N-0928 |

> [!WARNING]
> **Emballages.** ACorr, OnduCorr, Groupe Induspac et Mitchel Lincoln
> apparaissent dans FR-V0 comme contacts prioritaires, mais **aucun n'est
> établi comme fournisseur réel des entreprises étudiées**. Depuis N-0928,
> la méthode est : interroger 2–3 entreprises québécoises qui fabriquent,
> emballent et livrent des meubles → obtenir leurs fournisseurs et
> références réels → seulement ensuite documenter ces fabricants (détail :
> [`film-mousse-pe.md` §5.1](emballages/film-mousse-pe.md#51-méthode-didentification-du-fournisseur-réel-réunion-nicolas-2026-09-28)).
> Les candidats de FR-V0 ne servent que de comparaison si les réponses les
> désignent.

## 4. Fiches courtes — informations rapatriées de FR-V0

Tout le contenu de cette section est **information issue de la feuille de
route de collecte (FR-V0) — à vérifier**, sauf mention d'une fiche Git.
Les « sources » sont celles citées par FR-V0 ; elles n'ont pas été
consultées lors du rapatriement et aucune URL n'était fournie.

### 4.1 Entreprises sans fiche Git

#### Ply Supply — contreplaqué

- **Rôle FR-V0 :** distributeur québécois ; rôle de fournisseur/distributeur à confirmer selon produit. Confiance : moyen.
- **Localisation FR-V0 :** Québec.
- **Produit pertinent :** bouleau baltique, bouleau préfini, plywood cabinet grade.
- **Pourquoi :** remonter au fabricant ou au pays d'origine du Baltic plywood utilisé en atelier.
- **Données à demander :** fabricant/OEM, pays/usine, essence ; colle, densité, masse panneau ; fiche technique, FDS si colle/formaldéhyde.
- **Sources citées par FR-V0 :** site Ply Supply ; rôle exact à confirmer.

#### Distributions Nortra — panneaux mélaminés / TFL

- **Rôle FR-V0 :** distributeur québécois ; service de laminage mentionné. Confiance : moyen.
- **Produit pertinent :** Tafisa, stratifiés, service de laminage.
- **Pourquoi :** obtenir fiches et références réelles ; distinguer TFL acheté et laminage sur mesure.
- **Données à demander :** référence, fabricant, procédé de laminage le cas échéant ; grammage papier, colle/résine, fiche technique.
- **Sources citées par FR-V0 :** page Distributions Nortra — Tafisa.

#### Les Spécialités MGH / Royflex — placage

- **Rôle FR-V0 :** fabricant québécois. Confiance : élevé.
- **Localisation FR-V0 :** Tring-Jonction, Québec.
- **Produit pertinent :** placages flexibles ; placages sur MDF, particules ou contreplaqué.
- **Pourquoi :** peut documenter à la fois le placage, le support et le procédé d'application.
- **Données à demander :** essence, épaisseur placage, support ; colle, endos, procédé ; taux de perte, masse/m², fiches techniques.
- **Sources citées par FR-V0 :** site officiel MGH/Royflex.

#### Placages X Press — placage / panneaux plaqués

- **Rôle FR-V0 :** distributeur québécois ; fabrication/lamination sur mesure mentionnée, à confirmer. Confiance : moyen.
- **Localisation FR-V0 :** Saint-Denis-sur-Richelieu, Québec.
- **Produit pertinent :** placages naturels et reconstitués, panneaux architecturaux, portes plaquées.
- **Pourquoi :** identifier les produits réellement spécifiés en ébénisterie architecturale.
- **Données à demander :** fabricant/OEM du placage, essence, support ; colle, masse surfacique, fiche technique.
- **Sources citées par FR-V0 :** site Placages X Press ; rôle exact à confirmer.

#### Commonwealth Plywood Distribution — bandes de chant

- **Rôle FR-V0 :** distributeur québécois. Confiance : élevé (distribution).
- **Localisation FR-V0 :** centres de distribution au Québec et en Ontario.
- **Produit pertinent :** chants bois véritable, PVC, polyester, mélamine et autres.
- **Pourquoi :** références alternatives utilisées par les ébénistes et fiches de fournisseurs.
- **Données à demander :** référence, OEM, matière ; masse linéique, longueur rouleau, pays de production ; fiche technique.
- **Sources citées par FR-V0 :** catalogue Commonwealth Plywood Distribution.
- **Note :** entité de distribution distincte de la division sciage documentée dans [`commonwealth-plywood-sciage.md`](bois/commonwealth-plywood-sciage.md).

#### Les Adhésifs Marcan — adhésifs

- **Rôle FR-V0 :** fabricant québécois ; formulation/production locale indiquée pour la majorité des colles bois, usine à confirmer par produit. Confiance : moyen à élevé.
- **Produit pertinent :** PVA, colle contact, EVA hot-melt, PUR.
- **Pourquoi :** couvre plusieurs familles d'adhésifs utilisées en ébénisterie.
- **Données à demander :** produit exact, solides, densité ; formulation simplifiée, site de production, dosage ; FDS, fiche technique, données environnementales.
- **Sources citées par FR-V0 :** site Marcan Adhesives.

#### Canmade Montréal — adhésifs

- **Rôle FR-V0 :** distributeur / représentant de marques étrangères (Jowat et autres). Confiance : moyen.
- **Localisation FR-V0 :** Montréal.
- **Produit pertinent :** EVA hot-melt, PUR Jowatherm/Jowat, colles pour bande de chant.
- **Pourquoi :** point d'entrée pour les hot-melt et PUR dont le fabricant n'est pas québécois.
- **Données à demander :** fiche technique, FDS, fabricant/OEM ; pays/usine, dosage, température d'application ; formulation générale.
- **Sources citées par FR-V0 :** catalogue Canmade Montréal.

#### C.A. Spencer — bois massif feuillu

- **Rôle FR-V0 :** fabricant québécois. Confiance : élevé.
- **Localisation FR-V0 :** Laval et scieries/séchoirs du groupe ; sites précis à confirmer par essence.
- **Produit pertinent :** érable, merisier/bouleau jaune, frêne, chêne rouge, autres feuillus.
- **Pourquoi :** contact majeur pour le bois franc et les données de sciage/séchage.
- **Données à demander :** essence, provenance forêt, sciage ; séchage, humidité, rendement ; énergie des séchoirs, transport, certification ; densité.
- **Sources citées par FR-V0 :** site C.A. Spencer ; fiche QWEB.

#### Scierie Leclerc et Tremblay — bois massif feuillu

- **Rôle FR-V0 :** fabricant québécois. Confiance : moyen à élevé.
- **Localisation FR-V0 :** Saint-Georges / Estrie ; livraison au Québec.
- **Produit pertinent :** érable, merisier, frêne, chêne rouge, plaine.
- **Pourquoi :** bois d'ébénisterie vendu en petites ou grandes quantités au Québec.
- **Données à demander :** essence, grade, humidité ; dimensions, séché ou vert, provenance ; énergie de séchage, pertes.
- **Sources citées par FR-V0 :** site Scierie Leclerc et Tremblay.

#### Ressources Lumber — bois massif feuillu

- **Rôle FR-V0 :** fabricant québécois (sciage de feuillus). Confiance : élevé.
- **Localisation FR-V0 :** Québec.
- **Produit pertinent :** bouleau jaune, érable, frêne, chêne rouge, hêtre, noyer ; bois modifié thermiquement.
- **Pourquoi :** feuillus séchés et bois modifié thermiquement.
- **Données à demander :** essence, provenance, sciage ; séchage, énergie, certification FSC ; densité, humidité, rendement.
- **Sources citées par FR-V0 :** fiche QWEB Ressources Lumber.

#### ACorr — emballages (candidat FR-V0, non fournisseur établi)

- **Rôle FR-V0 :** fabricant québécois. Confiance : élevé.
- **Localisation FR-V0 :** Lachine, Québec.
- **Produit pertinent :** boîtes en carton ondulé, emballages de protection sur mesure.
- **Données à demander (si désigné par les entreprises utilisatrices) :** grammage, cannelure, masse par boîte ; contenu recyclé, origine papier, énergie ; encre/colle, fiche technique.
- **Sources citées par FR-V0 :** site officiel ACorr.

#### OnduCorr — emballages (candidat FR-V0, non fournisseur établi)

- **Rôle FR-V0 :** fabricant québécois ; adresse d'usine à confirmer. Confiance : moyen.
- **Localisation FR-V0 :** Québec/Montréal.
- **Produit pertinent :** carton ondulé sur mesure, y compris secteur meubles.
- **Données à demander (si désigné) :** type de carton, masse par emballage, contenu recyclé ; conception, pertes, colle ; impression, fiche technique.
- **Sources citées par FR-V0 :** site OnduCorr.

#### Groupe Induspac — emballages (candidat FR-V0, non fournisseur établi)

- **Rôle FR-V0 :** fabricant québécois. Confiance : élevé.
- **Localisation FR-V0 :** Candiac, Québec.
- **Produit pertinent :** carton, mousse PE/PU/PSE, inserts, protection industrielle.
- **Pertinence :** seul candidat FR-V0 couvrant la mousse PE (voir [`film-mousse-pe.md`](emballages/film-mousse-pe.md)) ; il n'est pas pour autant le fournisseur réel du film/mousse PE observé.
- **Données à demander (si désigné) :** type PE/PU/PSE, densité, contenu recyclé ; procédé, masse par pièce, fiche technique ; FDS, pays/usine.
- **Sources citées par FR-V0 :** site Groupe Induspac.

#### Mitchel Lincoln — emballages (candidat FR-V0, non fournisseur établi)

- **Rôle FR-V0 :** fabricant avec usines au Québec. Confiance : élevé.
- **Localisation FR-V0 :** St-Laurent, Côte-de-Liesse, Cavendish, Vaudreuil-sur-le-Lac, Drummondville.
- **Produit pertinent :** carton ondulé, boîtes, présentoirs, solutions sur mesure.
- **Données à demander (si désigné) :** grammage, cannelure, masse ; contenu recyclé, énergie, encre/colle ; EPD ou données environnementales.
- **Sources citées par FR-V0 :** site Mitchel Lincoln.

### 4.2 Compléments FR-V0 pour les entreprises déjà documentées

Les fiches Git restent la référence ; seuls les éléments **absents** des
fiches sont repris ici, comme informations FR-V0 à vérifier.

| Entreprise | Complément FR-V0 non couvert par la fiche Git | Données à demander (FR-V0) |
|---|---|---|
| Uniboard | Production TFL et HPL complémentaire ; usine TFL par référence à confirmer. Mention « Val-d'Or/Unires pour résines » non vérifiée. | Référence, support, papier décor, couches, résine, usine réelle, énergie, EPD. |
| Tafisa Canada | Procédé TFL sur panneau de particules ; collections décoratives. | Procédé TFL, papier décor, grammage, résine mélamine, densité par grade, contenu recyclé, énergie, EPD. |
| Goodfellow | Rôle de distributeur de MDF de fabricants nord-américains (Arauco, West Fraser « ou autres selon références » — OEM non établi). | Référence exacte, fabricant, usine/pays, fiche technique, densité, certification, contact technique fabricant. |
| Commonwealth Plywood | Division placage (tranchage) ; contreplaqué décoratif. | Essences, origine bois, rendement tranchage, épaisseur placage, colle, énergie, certifications. |
| Husky Plywood | Aucun (Sainte-Thérèse et Princeville déjà confirmés dans la fiche Git). | Essence, âme, plis, colle, densité, origine bois, usine, énergie. |
| Cedan | Bandes multi-plis et placage flexible. | Essence, origine, épaisseur, largeur, masse linéique, endos, préencollage, lieu de production. |
| Richelieu | Chants ABS/acrylique et correspondances TFL ; activité de fabrication de quincaillerie « selon communications publiques », à confirmer par produit. | Référence, masse par mètre/pièce, composition, fabricant/OEM, pays/usine, FDS, BOM simplifiée. |
| Blum | Charnières invisibles, TANDEM, systèmes de tiroirs (au-delà de MOVENTO). | Poids par référence, matières, BOM, pays/usine, finitions, EPD, emballage. |
| Accuride | — | Masse paire, matières, finition, pays/usine, BOM simplifiée. |

### 4.3 Ordre de contact recommandé par FR-V0

Repris pour traçabilité. **Cet ordre est suspendu à la validation de la
liste par Vincent** et ne vaut pas instruction de contact.

| Vague FR-V0 | Entreprises |
|---|---|
| A — débloquer plusieurs données | Uniboard, Tafisa Canada, Husky Plywood / Commonwealth Plywood, Les Spécialités MGH / Royflex, Les Adhésifs Marcan, Richelieu |
| B — produits spécifiques | Cedan, Abra-Dhésif, Canmade Montréal, Blum, Accuride, Groupe Induspac *(emballage : remplacé par la méthode N-0928)* |
| C — pistes secondaires | C.A. Spencer, Ressources Lumber, ACorr et Mitchel Lincoln *(emballage : remplacé par la méthode N-0928)*, Ply Supply ou Commonwealth Plywood Distribution (relais vers les OEM) |

## 5. Divergences feuille de route ↔ Git

| Sujet | FR-V0 | Git (retenu) |
|---|---|---|
| Abra-Dhésif | « Distributeur québécois ; fabrication à confirmer » | **Fabricant/formulateur** : Colle Royale est la marque maison d'Abradhésif inc. (St-Bruno-de-Montarville) — fiche mise à jour avec FDS et fiche technique papier ([`royale-404-abradhesif.md`](adhesifs/royale-404-abradhesif.md)). |
| Uniboard — panneau de particules | Usine citée : Sayabec ; « Val-d'Or/Unires mentionné pour résines » | **Val-d'Or** retenu parce que les sources Uniboard lui attribuent explicitement les panneaux de particules ; Sayabec fabrique aussi des panneaux sans attribution de portefeuille ([`uniboard-val-dor.md`](panneaux/uniboard-val-dor.md)). |
| Cedan | « Fabricant canadien ; site à confirmer » | Compatible : fabricant réel du chant bois, **filiale de Richelieu** ; site toujours non trouvé ([`merisier-blanc-cedan.md`](bandes-de-chant/merisier-blanc-cedan.md)). |
| Accuride, Blum | « Distributeur / représentant d'une marque étrangère » | Fabricants étrangers (Accuride International, É.-U. ; Blum, Autriche) distribués au Québec par Richelieu ; usine de la référence non trouvée. |
| Bois massif — libellés | « Scierie Leclerc et Tremblay » et « Ressources Lumber » : deux entités | Le registre bois du commit `9d1b298` les avait découpées à tort (« Scierie Leclerc » + « Tremblay / Ressources Lumber ») ; **corrigé** selon FR-V0. |
| Bois massif — liste | C.A. Spencer, Scierie Leclerc et Tremblay, Ressources Lumber | Git ajoute Commonwealth Plywood (sciage) et Goodfellow (lot 2), et les pistes N-0928. |
| Emballages | ACorr, OnduCorr, Groupe Induspac, Mitchel Lincoln en contacts prioritaires | Aucun n'est fournisseur réel établi ; méthode N-0928 prioritaire. Git documente en outre Protac, Colorel, Gilco, Jacobs & Thompson pour la mousse PE, sans confirmation de fournisseur réel. |
| Nom du fichier Word | `…_V1_fiches_fabricants.docx` | La page de garde indique « Version V0 — 22 septembre 2026 » ; la provenance retient **V0 du 2026-09-22**. |

## 6. Points à soumettre à Vincent

1. Valider (ou retirer) chacune des entreprises de la [section 3](#3-vue-densemble-par-famille) comme représentative du marché québécois pour sa famille, y compris celles déjà documentées dans Git.
2. Bois massif : arbitrer la liste entre C.A. Spencer, Scierie Leclerc et Tremblay, Ressources Lumber, Commonwealth Plywood (sciage), Goodfellow et les pistes de Nicolas (Bois Malo, BFRANC, Bois Poulin, « AMB » une fois identifié).
3. Contreplaqué : Ply Supply est-il un relais pertinent pour le Baltic / merisier-bouleau réellement acheté ?
4. Mélaminé / TFL : Distributions Nortra est-il pertinent ; le laminage sur mesure est-il une pratique à couvrir ?
5. Placage : pertinence respective de Les Spécialités MGH / Royflex, Commonwealth Plywood (placage) et Placages X Press.
6. Bandes de chant : Commonwealth Plywood Distribution est-il une source utile en plus de Richelieu/Cedan ?
7. Adhésifs : Les Adhésifs Marcan et Canmade Montréal (Jowat) couvrent-ils des produits réellement utilisés (EVA, PUR, contact) ?
8. Emballages : quelles 2–3 entreprises utilisatrices interroger (Oldwood ? client de Saint-Jérôme à identifier ?), avant toute documentation de fabricant d'emballage.
9. Candidats manquants dans l'une ou l'autre famille.

## 7. Consignes pour la feuille de route de collecte (Johan)

1. **La liste n'est pas figée** ; elle sera révisée après la validation de Vincent.
2. Pour les candidats sans fiche Git (candidats identifiés et candidats proposés par Nicolas) : commencer par les informations **publiques** des sites officiels (raison sociale, usines, activité réelle, essences/produits, certifications, fiches techniques, FDS, EPD).
3. **Ne pas encore contacter** les candidats non validés.
4. Le statut reste « à valider avec Vincent » même si les informations publiques sont complètes.
5. « AMB » n'est pas à rechercher avant confirmation de son identité.
6. Emballages : identifier d'abord la chaîne d'approvisionnement réelle auprès de 2–3 entreprises utilisatrices.
7. Toute nouvelle preuve est réinjectée dans Git (fiche d'inventaire + mise à jour de ce registre) avant régénération du Word.

## 8. Journal

| Date | Action | Résultat |
|---|---|---|
| 2026-09-22 | Rédaction de la feuille de route V0 (Word) | Section 4 « Entreprises et fabricants à contacter » produite hors Git. |
| 2026-09-28 | Réunion de suivi avec Nicolas | Pistes bois massif, méthode emballage, validation de la liste confiée à Vincent. |
| 2026-09-30 | Rapatriement FR-V0 §4 dans Git | Registre créé ; 14 entreprises absentes rapatriées ; entreprises documentées reliées à leur fiche ; statuts normalisés ; registre bois (`9d1b298`) fusionné et libellés corrigés. Aucune source FR-V0 consultée ni recherche Web effectuée. |
