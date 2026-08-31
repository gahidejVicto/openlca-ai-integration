# Sécurité

## Menaces à considérer

Avant de connecter un MCP à une vraie base, l'audit doit couvrir :

- la lecture excessive de fichiers ;
- l'écriture ou la modification de données ;
- la suppression de données ;
- l'exécution arbitraire de commandes ;
- l'accès réseau non nécessaire ;
- l'exfiltration de données ;
- l'accès à des secrets ;
- la manipulation accidentelle de la base openLCA.

## Politique initiale

- privilégier la lecture seule ;
- exposer uniquement les outils nécessaires ;
- n'utiliser aucune donnée ecoinvent avant la fin de l'audit ;
- ne stocker aucun secret dans Git ;
- tester uniquement avec une petite base non sensible ;
- valider manuellement le premier calcul automatisé.

## Checklist d'audit MCP

- [ ] Lire le code source et identifier ses dépendances.
- [ ] Inventorier chaque outil exposé et justifier son besoin.
- [ ] Vérifier les droits de lecture, d'écriture et de suppression.
- [ ] Limiter les chemins accessibles à une liste explicite.
- [ ] Désactiver l'exécution de commandes arbitraires.
- [ ] Recenser et restreindre les accès réseau sortants.
- [ ] Vérifier qu'aucun secret n'est lu, journalisé ou renvoyé.
- [ ] Examiner les journaux pour prévenir l'exfiltration de données.
- [ ] Tester les entrées invalides et les demandes hors périmètre.
- [ ] Tester sur une copie non sensible et prévoir la restauration.
- [ ] Comparer le premier résultat au calcul manuel openLCA.
- [ ] Documenter la version auditée, les limites et les risques résiduels.
