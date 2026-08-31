# openlca-ai-integration

Ce projet vise à expérimenter une interface en langage naturel pour openLCA, tout en conservant openLCA comme moteur de calcul d'analyse du cycle de vie (ACV).

## Architecture cible

```text
Utilisateur
    ↓
Claude Desktop
    ↓
MCP local
    ↓
Python / olca-ipc
    ↓
openLCA
    ↓
Base ACV
```

Claude orchestrera les appels, tandis qu'openLCA réalisera les calculs. L'IA ne remplace pas le moteur ACV : chaque résultat devra rester vérifiable manuellement. Les bases propriétaires, confidentielles ou soumises à licence ne sont pas stockées dans Git.

## État du projet

**Phase actuelle : initialisation du dépôt et apprentissage openLCA.**

Ne sont pas encore implémentés :

- la connexion IPC ;
- le MCP ;
- la connexion à Claude Desktop ;
- le calcul conversationnel.

## Principes du projet

1. Apprendre openLCA avant d'automatiser.
2. Valider l'IPC indépendamment du MCP.
3. Utiliser une petite base de test.
4. Ne pas utiliser ecoinvent pendant les premiers tests.
5. Auditer le MCP avant toute utilisation de données sensibles.
6. Comparer tout premier calcul automatisé avec le calcul manuel.

## Documentation

- [Roadmap](docs/roadmap.md)
- [Sécurité](docs/security.md)
- [Architecture cible](docs/architecture.md)
- [Gestion des données](docs/data-management.md)
- [Checklist d'apprentissage openLCA](docs/openlca-learning.md)
