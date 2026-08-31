# Roadmap

Les jalons sont séquentiels : chaque couche doit être comprise et validée avant d'ajouter la suivante.

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
