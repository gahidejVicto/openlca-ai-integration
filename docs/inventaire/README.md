# Fiches d'inventaire détaillé

Les fiches répondent à la question : **« Que contient réellement un dataset candidat et dans quelle mesure représente-t-il le Québec ? »** Elles complètent l'[index métier](../materiaux-ebenisterie.md), sans constituer une implémentation openLCA.

Une fiche correspond normalement à :

- un matériau métier ;
- un ou plusieurs datasets ecoinvent candidats ;
- une analyse des paramètres et fournisseurs importants ;
- une évaluation de leur représentativité pour le Québec.

Le [template réutilisable](../../research/templates/dataset-analysis.md) sert de point de départ. La première fiche pilote porte sur le [contreplaqué CA-QC](panneaux/plywood-ca-qc.md).

## Registre des fabricants et fournisseurs

Le [registre transversal des fabricants et fournisseurs](registre-fabricants-fournisseurs.md) est la **source canonique** des entreprises citées dans la feuille de route de collecte étudiant(e) : statuts normalisés (rôle, statut documentaire, validation métier), provenance de chaque information et lien vers les fiches ci-dessous. Aucune entreprise n'y est validée métier ; la validation de la liste est attendue avec Vincent.

## Passes de collecte documentaire

- [Collecte de données fabricants — RECQ36 (2026-09-22)](donnees-fabricants-recq36-2026-09-22.md) — coulisses, adhésifs, bande de chant, film mousse PE.
- [Candidats bois massif (réunion Nicolas 2026-09-28)](bois/candidats-fournisseurs-bois-massif.md) — pistes de Nicolas et TODO « AMB » ; statuts tenus dans le registre transversal.

## Répertoires de fiches fabricant

- [Panneaux à base de bois et stratifiés](panneaux/README.md)
- [Bois massif](bois/README.md)
- [Adhésifs](adhesifs/README.md)
- [Plastiques](plastiques/README.md)
- [Bandes de chant (fonction métier, toutes matières)](bandes-de-chant/README.md)
- [Quincaillerie de meuble](quincaillerie/README.md)
- [Emballages](emballages/README.md)

## Catégories d'évaluation

| Symbole | Catégorie | Usage |
|---|---|---|
| ✓ | Représentatif / acceptable | L'information disponible permet de considérer l'élément acceptable dans le périmètre étudié. |
| ⚠ | À vérifier ou régionaliser | Un écart potentiel est identifié ; une vérification ou une adaptation peut être nécessaire. |
| ? | Information manquante | Les informations disponibles ne permettent pas encore de conclure. |

> **Principe :** ne pas reconstruire un dataset simplement parce qu'il n'est pas parfait. Identifier d'abord précisément ses maillons faibles.

## Dimensions à distinguer

1. **Géographie du procédé** — lieu auquel l'activité de production est rattachée.
2. **Géographie des fournisseurs / intrants** — régions des providers, notamment pour les intrants critiques.
3. **Valeurs quantitatives utilisées** — consommations, rendements, pertes et autres paramètres.
4. **Origine documentaire de ces valeurs** — échantillon, littérature, statistique, hypothèse ou donnée primaire.
5. **Données primaires québécoises à valider** — mesures ou informations requises pour confirmer la représentativité.

Une géographie de procédé `CA-QC` ne valide donc ni les providers, ni les paramètres, ni leurs sources. Chaque conclusion importante doit être traçable conformément aux [règles relatives aux sources](../sources/README.md).
