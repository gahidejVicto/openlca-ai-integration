# Collecte de données fabricants — RECQ36 (2026-09-22)

> [!IMPORTANT]
> Ce document est le **point d'entrée** d'une passe de collecte documentaire
> sourcée sur des produits fabricants réels, réalisée le 2026-09-22 sur la
> branche `recq36/emballage-pe-foam-et-cloture-recherches`. **Aucune
> recherche OpenLCA/Ecoinvent n'a été effectuée dans cette passe**
> (consigne explicite de la mission) — cette collecte prépare de futures
> reconstructions ACV, elle ne les réalise pas.

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
| 4 | Colle blanche à bois — Royale 404 (Abradhésif) | [`adhesifs/royale-404-abradhesif.md`](../inventaire/adhesifs/royale-404-abradhesif.md) |
| 5 | Bande de chant — 4 candidats exploratoires | [`plastiques/bande-de-chant-candidats.md`](../inventaire/plastiques/bande-de-chant-candidats.md) |
| 6 | Film mousse PE d'emballage (hypothèse) | [`emballages/film-mousse-pe.md`](../inventaire/emballages/film-mousse-pe.md) |

## Tableau de synthèse

| Famille | Produit | Référence | Source principale | Masse | Matière/composition | Données de fabrication | Données manquantes | Qualité documentaire |
|---|---|---|---|---|---|---|---|---|
| Quincaillerie | Coulisse latérale std. | `706-2605400` (16″) | Langevin Forest (distributeur) | ❓ Non trouvée | ❓ Non précisée (fabricant/OEM non identifié) | Capacité 75 lb @18″ ; mécanisme soft-close breveté non détaillé | Masse, matériaux, revêtement, pays de fabrication, fabricant réel | ❌ Faible |
| Quincaillerie | Coulisse invisible Blum MOVENTO | `760H4000S` (400 mm, 40 kg) | Blum / Richelieu Hardware (fabricant + distributeur QC) | ❓ Non trouvée (fiche PDF officielle trop volumineuse pour extraction) | ✅ Acier zingué ; rouleaux synthétiques (nature exacte non précisée) | Longueur, classe de charge, finition confirmées ; mécanisme BLUMOTION confirmé, composition interne non détaillée | Masse par référence, usine de fabrication, EPD | ⚠️ Moyenne-élevée |
| Adhésifs | Colle contact à l'eau — 3M Fastbond 30-NF | Produit unique, plusieurs formats | 3M Canada — FDS canadienne (fabricant) | Non applicable (produit liquide) | ✅ Néoprène (20-40 %) + eau (40-60 %) + résines (5-10 % chacune) + fractions mineures partiellement secrètes | ✅ Densité 1,1 g/cm³ ; solides ≈50 % ; COV ≤80 g/L ; rendement 3,0-3,5 g/pi²/surface | Fractions exactes de 3 composants (secret commercial), site de fabrication précis, EPD | ✅ Élevée |
| Adhésifs | Colle blanche — Royale 404 | Royale 404 | Abradhésif inc. (fabricant, site web — pas de FDS dédiée) | Non applicable (produit liquide) | ⚠️ « Résine synthétique de type PVA » déclarée par le fabricant ; PVAc non confirmé par FDS pour cette référence | ❓ Taux de solides, densité, COV non trouvés pour cette référence précise | FDS/fiche technique dédiée, confirmation PVAc | ⚠️ Faible-moyenne |
| Plastiques | Bande de chant — 4 candidats | Doellken (PVC), Rehau (PVC/ABS/PP/PMMA), Cedan/Richelieu (ABS), PCM (PVC, non-nommé) | Fabricants + catalogue Richelieu (cross-référence) | ⚠️ Doellken : masse de rouleau connue, densité **inférée** ≈1,82 g/cm³ | ✅ Matériaux confirmés par candidat ; propriétés mécaniques complètes pour Rehau | Fiches techniques variables selon candidat ; aucune densité officiellement publiée | Densité officielle (tous), fabricant amont pour PCM | ⚠️ Variable selon candidat (voir fiche) |
| Emballage | Film mousse PE (hypothèse) | Comparaison : rouleau S.E.D Emballage (France) | S.E.D Emballage (distributeur français, hors QC/Canada) | ❓ Non publiée | ❓ Type de PE non précisé ; densité non publiée | Épaisseurs 1-8 mm, largeurs/longueurs confirmées ; procédé non documenté | Type de PE, densité, grammage, procédé, fournisseur réel des entreprises RECQ36 | ❌ Faible (produit de comparaison) ; ⚠️ moyenne pour les pistes québécoises complémentaires (Protac, Colorel) |

## 1. Résultats par cas

### CAS 1 — Coulisse latérale standard (Langevin Forest)
Produit **sans marque identifiable**. Aucune donnée physique (masse,
matériaux, revêtement) trouvée publiquement. Blocage complet : identité du
fabricant/OEM inconnue.

### CAS 2 — Coulisse invisible (Blum MOVENTO)
Référence `760H4000S` retenue (400 mm, 40 kg), disponible directement chez
Richelieu Hardware. Matériau (acier zingué), mécanisme BLUMOTION et classe
de charge bien confirmés par le fabricant. **Masse par référence non
trouvée** — la fiche technique officielle Blum existe mais son volume a
empêché une extraction complète dans cette session.

### CAS 3 — Colle contact à l'eau (3M Fastbond 30-NF)
**Cas le mieux documenté de cette passe.** FDS canadienne complète obtenue :
composition détaillée (base néoprène/chloroprène, pas PVAc), densité,
teneur en solides, COV, rendement d'application. Trois composants mineurs
(méthanol, rosinate de potassium, toluène) ont une fraction exacte retenue
comme secret commercial — documenté explicitement, non reconstitué.

### CAS 4 — Colle blanche à bois (Royale 404)
Fabricant réel identifié (Abradhésif, St-Bruno-de-Montarville, QC — marque
fondatrice de l'entreprise depuis 1976). La chimie « PVA » est **déclarée
par le fabricant sur sa page produit**, mais **aucune FDS ou fiche
technique dédiée à cette référence précise n'a été trouvée**. Une fiche
technique existe pour un produit voisin de la même marque (Royale 933MAX,
confirmé PVAc) mais ne peut être attribuée au 404.

### CAS 5 — Bande de chant (4 candidats, aucun choix imposé)
Voir [`plastiques/bande-de-chant-candidats.md`](../inventaire/plastiques/bande-de-chant-candidats.md)
pour le détail complet. Résumé : **Doellken/Surteco** (OEM réel, masse de
rouleau connue permettant une densité inférée) ; **Rehau** (fiche technique
officielle la plus complète, propriétés mécaniques normalisées) ;
**Cedan/Richelieu** (fabricant filiale d'une entreprise à siège social
québécois, avantages environnementaux documentés, GREENGUARD) ; **PCM**
(disponibilité québécoise directe et lien explicite avec les fabricants de
mélamine québécois Tafisa/Uniboard, mais fabricant amont du PVC non nommé).

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

- pages produit fabricant (Blum, 3M, Abradhésif, Protac, Rehau, Doellken) ;
- FDS/SDS fabricant (3M Canada, complète et lue intégralement) ;
- fiches techniques fabricant (Rehau, Royale 933MAX, Jacobs & Thompson) ;
- catalogues distributeur (Richelieu Hardware, PCM, Colorel, Groupe Gilco) ;
- une source distributeur hors Québec/Canada, explicitement signalée comme
  telle (S.E.D Emballage, France).

## 3. Données non trouvées (blocages principaux)

| Cas | Donnée manquante bloquante |
|---|---|
| 1 | Identité du fabricant/OEM ; masse ; matériaux |
| 2 | Masse par référence (fiche PDF officielle existe mais non exploitée entièrement) |
| 3 | Fractions exactes de 3 composants à secret commercial (mineur, non bloquant) |
| 4 | FDS/fiche technique dédiée au Royale 404 (confirmation PVAc) |
| 5 | Densité officielle pour tous les candidats (une valeur inférée existe pour Doellken) |
| 6 | Fournisseur réel des entreprises RECQ36 concernées ; densité et type de PE du produit réellement utilisé |

## 4. Candidats proposés pour la bande de chant (CAS 5)

**A — Doellken Woodtape (Surteco)**, **B — Rehau**, **C — Cedan
(Richelieu Hardware)**, **D — PCM (Anjou, QC)**. Détail complet, avantages
et lacunes documentaires dans la fiche dédiée. **Aucun choix n'a été fait**
— décision en attente de Jérôme.

## 5. Produits pour lesquels les données sont désormais suffisantes pour envisager une reconstruction ACV

- **CAS 3 — Colle contact 3M Fastbond 30-NF** : composition, densité,
  teneur en solides et rendement documentés par une FDS fabricant complète.
  C'est le cas le plus mûr de cette passe.
- **CAS 2 — Blum MOVENTO** : matériau, finition et paramètres fonctionnels
  bien confirmés ; **manque uniquement la masse** pour une reconstruction
  bottom-up complète (matière + procédé de formage/zingage).

## 6. Produits pour lesquels un contact fabricant est nécessaire

- **CAS 1 — Coulisse Langevin Forest** : blocage total, identité du
  fabricant inconnue — contact avec le distributeur ou pesée physique
  recommandés en priorité.
- **CAS 4 — Royale 404** : demander la FDS/fiche technique dédiée à
  Abradhésif pour confirmer la chimie PVAc et obtenir les paramètres
  physiques.
- **CAS 5 — Bande de chant** : une fois un candidat choisi par Jérôme,
  demander la densité officielle (aucun des quatre candidats ne la publie).
- **CAS 6 — Film mousse PE** : contact avec les entreprises RECQ36
  concernées pour confirmer le fournisseur réel et obtenir une fiche
  technique ou un échantillon.

## Journal de travail

| Date | Action | Résultat |
|---|---|---|
| 2026-09-22 | Collecte documentaire pour les 6 cas | 6 fiches produites, synthèse rédigée, structure `docs/inventaire/{quincaillerie,adhesifs,plastiques,emballages}/` complétée |

---

## Statut du document

**Collecte terminée pour les 6 cas demandés.** Prêt pour revue.
