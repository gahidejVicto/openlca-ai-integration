# Gestion des données

## Politique

Les données suivantes sont locales et ne doivent pas être commitées :

- fichiers `*.zolca` et autres bases openLCA ;
- bases ecoinvent ;
- archives LCIA volumineuses ;
- données propriétaires ou confidentielles.

Cette règle protège les licences, la confidentialité et la taille du dépôt public.

## Répertoires locaux

- `data/test/` : petites bases d'apprentissage non sensibles ;
- `data/methods/` : archives et méthodes LCIA locales ;
- `data/production/` : bases réelles, propriétaires ou sensibles.

Exemples de fichiers qui pourront exister **uniquement en local** :

- `trial_case_sweater.zolca` ;
- `cups.zolca` ;
- `agribalyse 3.2.zolca` ;
- `ecoinvent 3.11 Cutoff Unit-Processes....`.

Ces fichiers ne sont pas fournis par le dépôt. Les fichiers `.gitkeep` existent uniquement pour conserver l'arborescence vide dans Git ; ils ne constituent pas des données.
