# Roadmap

Les jalons sont séquentiels : chaque couche doit être comprise et validée avant d'ajouter la suivante.

## Workflow de documentation et de régionalisation

Ce workflow sépare l'analyse documentaire de la future implémentation. Le projet se situe actuellement dans les phases **V0 à V2**, avec le [contreplaqué CA-QC](inventaire/panneaux/plywood-ca-qc.md) comme premier cas pilote.

| Phase | Étape | Question directrice | Livrable / condition de passage |
|---|---|---|---|
| **V0** | Inventaire métier | Quels matériaux l'industrie québécoise utilise-t-elle ? | Matériaux, familles, priorités et statuts dans l'[index métier](materiaux-ebenisterie.md) |
| **V1** | Mapping ecoinvent | Quels datasets ecoinvent peuvent servir de point de départ ? | Candidats identifiés, sans présumer de leur validation |
| **V2** | Inventaire détaillé | Quels sont les Inputs/Outputs, paramètres, providers et hypothèses importants du dataset ? | Fiche structurée et maillons faibles identifiés |
| **V3** | Analyse Québec | Quels éléments sont déjà représentatifs du Québec et lesquels nécessitent des données supplémentaires ou une régionalisation ? | Sources, écarts et données primaires documentés |
| **V4** | Implémentation | Quelles adaptations l'analyse justifie-t-elle ? | Création ou adaptation dans openLCA uniquement lorsque l'analyse est suffisante |
| **V5** | Validation | Le dataset québécois obtenu est-il vérifiable et adéquat ? | Comparaison, vérification et décision documentées |

Une géographie `CA-QC` ne suffit jamais à franchir ces étapes : géographie du procédé, providers, valeurs quantitatives et origine documentaire sont évalués séparément. La décision de conserver, documenter, adapter ou reconstruire précède toute implémentation.

## Jalon 1 — Comprendre openLCA

Objectifs :

- installer openLCA ;
- comprendre les notions de process, flow, exchange, product system, functional unit et impact method ;
- réaliser une première ACV manuelle ;
- interpréter l'inventory (LCI), la LCIA et le contribution tree.

Bases recommandées pour les essais : `trial_case_sweater.zolca` ou `cups.zolca`. Ne pas commencer avec ecoinvent.

## Jalon 2 — Python / IPC

Objectifs :

- démarrer **Tools → Developer tools → IPC Server** dans openLCA ;
- installer Python ;
- installer `olca-ipc` ;
- créer un script minimal ;
- récupérer la liste de quelques processus ;
- confirmer que Python communique réellement avec openLCA.

## Jalon 3 — Claude / MCP

Objectifs :

- installer Claude Desktop ;
- évaluer ou récupérer le MCP Below280 ;
- auditer son code ;
- réduire ses permissions ;
- connecter MCP → `olca-ipc` → openLCA ;
- effectuer une interrogation simple ;
- lancer un premier calcul ;
- reproduire manuellement le même calcul ;
- comparer les résultats.

## Gate final — Accès à ecoinvent

Conditions minimales avant tout accès :

- maîtrise du calcul manuel ;
- IPC stable ;
- MCP audité ;
- permissions minimales ;
- validation manuelle réussie.
