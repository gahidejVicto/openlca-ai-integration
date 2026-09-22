# Film mousse de polyéthylène en rouleau — matériau d'emballage blanc

> [!IMPORTANT]
> **VALIDATION MÉTIER — Nicolas a confirmé le 2026-09-22 que le matériau
> blanc en rouleau observé pour l'emballage/protection du mobilier
> correspond bien au film/mousse de polyéthylène (PE) identifié pendant le
> diagnostic.** Ceci est une validation métier RECQ36, **pas une donnée
> fabricant** — elle confirme la nature du matériau, pas l'identité d'un
> fournisseur ni les caractéristiques physiques précises du produit
> réellement utilisé. L'identification n'est plus présentée comme une
> hypothèse : voir section 0 pour le nouveau statut et la question
> désormais à résoudre.

## 0. Statut mis à jour (relecture RECQ36, 2026-09-22)

| Type | Affirmation |
|---|---|
| **VALIDATION MÉTIER** | Le matériau d'emballage blanc en rouleau du périmètre RECQ36 est bien un film/mousse de polyéthylène (PE) — confirmé par Nicolas le 2026-09-22. |
| **FAIT SOURCÉ (Ecoinvent, inchangé)** | Aucun dataset fonctionnel satisfaisant représentant directement la mousse PE d'emballage n'a été identifié dans Ecoinvent 3.11 (voir [diagnostic Ecoinvent](../../diagnostic/RECQ36_diagnostic_ecoinvent_openLCA.md#passe-complémentaire--2026-09-22), conclusion **non rouverte** dans cette passe). |
| **NON TROUVÉ** | Épaisseur, densité, masse surfacique/linéique, largeur, type de PE exact (LDPE/autre), structure cellulaire (fermée/ouverte), procédé de moussage, taux d'expansion, contenu recyclé, fabricant/fournisseur réel, origine de fabrication — **du produit réellement utilisé par les entreprises RECQ36**. |

> [!CAUTION]
> **La validation métier ne change pas la conclusion Ecoinvent.** Le
> PE-LD vierge (`market for polyethylene, low density, granulate`) reste
> une brique matière possible ; le procédé générique `polymer foaming`
> examiné précédemment **ne doit pas devenir automatiquement le proxy de
> production de cette mousse** — sa description Ecoinvent elle-même
> l'oriente vers d'autres plastiques expansés, notamment le polystyrène
> (agent gonflant pentane, typique du moussage de perles de polystyrène
> expansible). Cette réserve est conservée telle quelle ; aucune recherche
> Ecoinvent supplémentaire n'a été menée dans cette passe.

**La question a changé.** Il ne s'agit plus de « Quel est ce matériau ? »
(résolu par la validation métier) mais de :

> **Quelles sont les caractéristiques physiques et de production du
> film/mousse PE réellement utilisé par les entreprises RECQ36 ?**

Voir la section 5 mise à jour pour la liste complète des données encore
nécessaires.

## 1. Produit de comparaison fourni par la mission

| Champ | Information | Statut | Source |
|---|---|---|---|
| Produit | Rouleau de film mousse (mousse PE) | ✅ Confirmé (page produit) | S1 |
| Entreprise | S.E.D Emballage (Sauvage Emballage Distribution) | ✅ Confirmé | S1, S2 |
| **Pays** | **France** (Margival, Aisne — à ~1h de Paris) — **pas une entreprise québécoise ni canadienne** | ✅ Confirmé | S2 |
| Fabricant réel du film (vs. S.E.D. distributeur) | **Non identifié** — S.E.D Emballage se décrit comme une entreprise de distribution de produits d'emballage (film étirable, papier bulle, machines, outils, cerclage, carton), fondée en 1993 ; rien n'indique qu'elle fabrique elle-même la mousse | ❓ Non trouvé | S2 |
| Épaisseurs offertes | 1 mm, 2 mm, 3 mm, 5 mm, 8 mm | ✅ Confirmé | S1 |
| Largeurs offertes | 0,45 m, 0,60 m, 1,0 m, 1,20 m, 1,50 m | ✅ Confirmé | S1 |
| Longueurs de rouleau | 25 m, 65 m, 100 m, 180 m, 250 m, 500 m | ✅ Confirmé | S1 |
| Type de PE | **Non précisé** (LDPE/HDPE non spécifié) | ❓ Non trouvé | S1 |
| Densité | **Non publiée** | ❓ Non trouvé | S1 |
| Masse / grammage | **Non publié** | ❓ Non trouvé | S1 |
| Structure cellulaire | Décrite comme « douce, blanche », flexible, légère ; résiste à l'humidité et aux moisissures | ✅ Description qualitative confirmée | S1 |
| Procédé de fabrication | **Non mentionné** (extrusion/moussage/réticulation non précisé) | ❓ Non trouvé | S1 |
| Agent gonflant | **Non mentionné** | ❓ Non trouvé | S1 |
| Fiche technique / FDS | **Aucune trouvée sur la page produit** | ❓ Non trouvé | S1 |

> [!CAUTION]
> **Ce produit reste un produit de comparaison commercial, pas une preuve
> qu'un atelier RECQ36 utilise ce produit français ou un équivalent
> identique.** La nature du matériau (film/mousse PE) est désormais
> confirmée par validation métier (section 0) — ce produit S.E.D Emballage
> reste utile pour situer une plage physique plausible (épaisseurs 1-8 mm)
> mais ne fournit toujours pas de données techniques exploitables
> (densité, grammage et procédé absents de sa fiche produit) pour le
> produit réellement utilisé.

## 2. Fabricants et distributeurs québécois/canadiens identifiés (recherche complémentaire)

Puisque le produit de comparaison fourni est français et peu documenté
techniquement, une recherche complémentaire a identifié des acteurs
réellement présents au Québec/Canada pour ce type de produit.

### 2.1 — Les Industries Protac inc. (fabricant, Québec)

| Champ | Information | Statut | Source |
|---|---|---|---|
| Fabricant | **Les Industries Protac inc.** | ✅ Confirmé | S3 |
| Localisation | Saint-Célestin, Québec (45, rue Jean-Clermont, J0C 1G0) | ✅ Confirmé | S3 |
| Produits | Mousse de polyéthylène **extrudée** (LDPE et HDPE, plusieurs densités) et mousse de polyéthylène **réticulée** (« cross-linked »), en feuilles, rouleaux, pièces découpées | ✅ Confirmé | S3 |
| Densité | Non précisée dans le contenu consulté (« plusieurs options de densité » mentionnées sans valeurs chiffrées publiques) | ❓ Non trouvé (valeurs non publiées, disponibles probablement sur demande) | S3 |
| Applications déclarées | Emballage protecteur, isolation réfléchissante, barrières hydrofuges, calfeutrage, insonorisation | ✅ Confirmé | S3 |
| Fiche technique dédiée à un grade d'emballage précis | Non trouvée dans le temps imparti de cette recherche | ❓ À demander directement (formulaire de demande de données techniques disponible sur le site) | S3 |

> [!NOTE]
> Protac est un **fabricant québécois réel de mousse PE**, ce qui en fait un
> candidat bien plus pertinent que le produit de comparaison français pour
> représenter un éventuel équivalent local — mais aucune fiche technique
> spécifique à un rouleau d'emballage fin (1-8 mm, blanc) n'a été récupérée
> dans cette session.

### 2.2 — Distributeurs québécois de rouleaux de mousse PE d'emballage

| Distributeur | Localisation | Épaisseurs documentées | Fabricant amont nommé ? |
|---|---|---|---|
| **Colorel** | Montréal, QC (3850 rue Jean-Talon Ouest) | 1/32″ (électroménager), 1/16″ (porcelaine/verre), 3/32″ (métal), **1/8″ (meubles et produits alimentaires)** | ❌ Non — Colorel se présente comme distributeur, pas fabricant |
| **Groupe Gilco** | Québec (entreprise active depuis plus de 40 ans) | 1/32″ à 1/2″, largeurs 48″-60″, longueurs jusqu'à 2000 pi | ⚠️ Un exemple de produit consulté (60″×1250′×1/16″) attribue le produit à la marque **Ivex** (fabricant nord-américain de produits d'emballage, non québécois) |
| **Boucard Emballages** | Non vérifié dans cette recherche | Non détaillé | ❓ Non vérifié |
| **Arteau** | Non vérifié dans cette recherche | Non détaillé | ❓ Non vérifié |

> [!IMPORTANT]
> **Fait notable :** Colorel documente explicitement un usage à **1/8″
> (≈3,2 mm) pour les meubles** — une épaisseur cohérente avec la plage
> 1-8 mm rapportée pour le produit de comparaison français, et avec un usage
> meuble explicitement documenté par un distributeur québécois. Ceci
> renforce la plausibilité de l'hypothèse d'identification sans la confirmer
> pour un client RECQ36 précis.

### 2.3 — Fiche technique réelle de mousse PE (fabricant canadien, hors Québec)

Une fiche technique complète et chiffrée a été localisée pour un grade de
mousse PE fabriqué par une entreprise canadienne (Ontario), ce qui fournit
une donnée de référence réelle sur la densité d'une mousse PE à cellules
fermées — **à ne pas attribuer au produit d'emballage RECQ36 sans
confirmation**, mais utile comme ordre de grandeur documenté.

| Champ | Information | Statut | Source |
|---|---|---|---|
| Fabricant | **Jacobs & Thompson Inc.** (marque FoamParts) | ✅ Confirmé | S4 |
| Localisation | Ontario, Canada (89 Kenhar Drive) | ✅ Confirmé | S4 |
| Référence | Mousse | Polyéthylène | 2542 | ✅ Confirmé | S4 |
| **Densité** | **28,8 à 35,2 kg/m³** (1,8-2,2 PCF) | ✅ Confirmé, méthode ASTM D3575-W | S4 |
| Applications déclarées pour ce grade | Toiture, équipement sportif, rembourrage médical (pas explicitement l'emballage meuble) | ✅ Confirmé | S4 |
| Certifications qualité | ISO 9001:2015, ISO/IEC 17025:2017 | ✅ Confirmé | S4 |
| Document | Fiche technique REV. 006, datée 2018-09-30 | ✅ Confirmé | S4 |

> [!CAUTION]
> Ce grade (2542) est destiné à des applications structurelles/de
> rembourrage, pas explicitement à l'emballage de protection en rouleau fin.
> Sa densité (≈29-35 kg/m³) est fournie **comme ordre de grandeur documenté
> pour une mousse PE fermée en général**, pas comme la densité du produit
> réellement utilisé en atelier RECQ36, dont la densité reste inconnue.

## 3. Synthèse — la nature du matériau est confirmée ; la caractérisation physique ne l'est pas

**La question d'identification est résolue (VALIDATION MÉTIER, section 0).**
Ce qui reste à établir n'est plus la nature du matériau mais ses
caractéristiques physiques et de production réelles. Le produit de
comparaison (S.E.D Emballage, France) confirme la plausibilité de la plage
dimensionnelle (épaisseurs 1-8 mm, couleur blanche, souplesse) mais ne
fournit :
- ni densité,
- ni grammage,
- ni type de PE (LDPE/HDPE),
- ni procédé de fabrication,
- ni agent gonflant,
- ni fiche technique.

La recherche complémentaire apporte des éléments utiles mais dispersés, et
**aucun de ces fabricants/distributeurs n'est confirmé comme fournissant le
produit effectivement utilisé par les entreprises RECQ36** :
- **Les Industries Protac inc.** (Saint-Célestin, QC) : fabricant québécois
  réel de mousse PE (extrudée et réticulée), mais aucune fiche technique
  d'un grade d'emballage précis obtenue — **candidat plausible, pas
  confirmé**.
- **Colorel** (Montréal, QC) : distributeur documentant explicitement un
  usage meuble à 1/8″ (≈3,2 mm) — **usage cohérent, pas une preuve de
  fournisseur**.
- **Jacobs & Thompson Inc.** (Ontario) : fournit un ordre de grandeur de
  densité réel pour une mousse PE fermée comparable (28,8-35,2 kg/m³) mais
  pour un grade destiné à la toiture/au rembourrage, **pas à l'emballage —
  non attribuable au produit RECQ36**.

## 4. Conclusion pour la reconstruction ACV

**Données actuellement insuffisantes pour une reconstruction ACV fiable —
mais le blocage a changé de nature.** L'identification du matériau (film
mousse PE) est désormais un fait métier établi, pas une hypothèse à
vérifier. Le blocage restant est entièrement une question de **données
physiques et de fournisseur** pour le produit réellement utilisé (aucune
donnée quantitative — densité, grammage, type de PE exact — n'est confirmée
pour ce produit précis). Rappel du constat Ecoinvent, **non affecté par la
validation métier et non réexaminé dans cette passe** : aucun procédé de
moussage PE n'existe dans Ecoinvent 3.11 ; le seul procédé générique
disponible, `polymer foaming`, est documenté par Ecoinvent lui-même comme
calibré pour le polystyrène et ne doit pas devenir automatiquement le
proxy de production de cette mousse.

## 5. Données prioritaires à demander (aux entreprises RECQ36 concernées)

**La question n'est plus l'identité du matériau, mais ses caractéristiques
physiques et de production.** Données encore nécessaires pour une
reconstruction :

1. Épaisseur réellement utilisée (parmi la plage 1-8 mm observée
   commercialement, ou une valeur précise si connue).
2. Densité du film/mousse.
3. Masse surfacique (g/m²) ou masse par longueur de rouleau.
4. Largeur du rouleau réellement utilisée.
5. Masse et longueur d'un rouleau, si disponibles auprès du fournisseur.
6. Type de PE exact si connu (PE-LD, PE-HD, autre).
7. Structure : mousse à cellules fermées ou ouvertes, si documentée.
8. Procédé de moussage (extrusion, réticulation, autre) si documenté.
9. Taux d'expansion, si documenté.
10. Contenu recyclé éventuel.
11. Fabricant/fournisseur réel du produit utilisé en atelier — **aucun des
    fabricants/distributeurs déjà identifiés (S.E.D Emballage, Protac,
    Colorel, Jacobs & Thompson) n'est confirmé comme étant ce fournisseur** ;
    ils sont conservés uniquement avec leur niveau de preuve réel respectif
    (comparaison commerciale, candidat plausible, usage documenté, ou ordre
    de grandeur non attribuable).
12. Origine de fabrication du produit réellement utilisé.

Un échantillon ou une fiche technique du rouleau réellement utilisé en
atelier reste la voie la plus directe pour obtenir ces données.

## 6. Sources documentaires

### S1 — S.E.D Emballage — Rouleau de film mousse
- Organisme : S.E.D Emballage (Sauvage Emballage Distribution).
- Contenu utilisé : épaisseurs, largeurs, longueurs de rouleau, description
  qualitative (souple, blanc, résistant à l'humidité).
- URL : https://sedemballage.com/produit/rouleau-de-film-mousse/
- Consultation : 2026-09-22.

### S2 — Verif.com / LinkedIn — Identification de S.E.D Emballage
- Contenu utilisé : confirmation que S.E.D Emballage (Sauvage Emballage
  Distribution) est une entreprise française (Margival, Aisne), fondée en
  1993, positionnée comme distributeur de produits d'emballage.
- URL : https://www.verif.com/en/company/SAUVAGE-EMBALLAGE-DISTRIBUTION-68d9c4ca1299230338eeae83/ ;
  https://sedemballage.com/notre-activite/
- Consultation : 2026-09-22.

### S3 — Les Industries Protac inc. — Mousse de polyéthylène
- Organisme : Les Industries Protac inc.
- Contenu utilisé : identification du fabricant québécois, types de mousse
  PE (extrudée, réticulée), localisation (Saint-Célestin, QC), coordonnées.
- URL : https://www.protac.ca/en/products/plastic-products/polyethylene-foams/
- Consultation : 2026-09-22.

### S4 — FoamParts (Jacobs & Thompson Inc.) — Fiche technique Mousse | Polyéthylène | 2542
- Organisme : Jacobs & Thompson Inc. (Ontario, Canada).
- Contenu utilisé : densité (28,8-35,2 kg/m³), propriétés mécaniques,
  méthodes d'essai ASTM D3575, certifications ISO.
- Document : REV. 006, daté 2018-09-30.
- URL : https://www.foamparts.com/specsheets/fr/2542-fr.pdf
- Consultation : 2026-09-22.

### S5 — Groupe Gilco — Rouleau de mousse de polyéthylène 60″×1250′×1/16″
- Organisme : Groupe Gilco (distributeur québécois).
- Contenu utilisé : dimensions disponibles, attribution de marque (Ivex)
  pour cet exemple précis.
- URL : https://groupegilco.com/fr/inventaire/produits-demballage/rouleaux-de-bulle-mousse/60-x-1250-x-1-16-rouleau-de-mousse-de-polyethylene/
- Consultation : 2026-09-22.

### S6 — Colorel — Rouleaux de mousse
- Organisme : Colorel (distributeur, Montréal, QC).
- Contenu utilisé : épaisseurs offertes et usages associés, dont l'usage
  meuble documenté à 1/8″.
- URL : https://colorel.ca/products/rouleaux-mousse
- Consultation : 2026-09-22.

## 7. Journal de travail

| Date | Action | Résultat |
|---|---|---|
| 2026-09-22 | Analyse du produit de comparaison fourni | Confirmé français (S.E.D Emballage), peu documenté techniquement |
| 2026-09-22 | Recherche de fabricants/distributeurs québécois équivalents | Protac (fabricant QC) et plusieurs distributeurs (Colorel, Gilco) identifiés |
| 2026-09-22 | Recherche d'une fiche technique de densité réelle | Fiche Jacobs & Thompson (Ontario) trouvée — ordre de grandeur, pas une preuve pour le produit RECQ36 |
| 2026-09-22 (relecture) | Validation métier reçue de Nicolas | Identification « film/mousse PE » confirmée comme fait métier établi, plus une hypothèse ; question reformulée vers les caractéristiques physiques/production |

---

## Statut de la fiche

**Identification confirmée par validation métier (Nicolas, 2026-09-22).**
Le blocage restant n'est plus l'identité du matériau mais ses
caractéristiques physiques et son fournisseur réel — confirmation
fournisseur et fiche technique/échantillon toujours nécessaires auprès des
entreprises RECQ36 concernées. La conclusion Ecoinvent (aucun dataset
fonctionnel, réserve sur `polymer foaming`) reste inchangée.
