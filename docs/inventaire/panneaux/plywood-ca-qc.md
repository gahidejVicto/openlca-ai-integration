# Contreplaqué — `plywood production [CA-QC]`

Cette fiche est le premier cas pilote de la méthode. Elle illustre pourquoi la géographie `CA-QC` d'un procédé ne signifie pas automatiquement que l'ensemble du dataset représente le Québec : les intrants, les valeurs de paramètres et leurs sources doivent être évalués séparément.

| Élément | ecoinvent 3.11 | Évaluation |
|---|---|---|
| Production du contreplaqué | CA-QC | ✓ Québec |
| Électricité | CA-QC | ✓ Québec |
| Bois feuillu | RoW | ⚠ À régionaliser / vérifier |
| Quantité de bois | 2,206 m³/m³ plywood | ⚠ Valeur à valider pour le Québec |
| Source de cette quantité | échantillon / littérature Allemagne | ⚠ Faible représentativité géographique |
| Résine UF | À vérifier | ? |
| Chaleur | À vérifier | ? |

## Deux questions distinctes concernant le bois

### Quantité de matière

> **Question :** Est-ce que 2,206 m³ de billes par m³ de contreplaqué est représentatif des procédés québécois ?

Il s'agit d'un problème de paramètre et de rendement matière, indépendamment de la géographie du provider. Une valeur locale doit être recherchée avant de conclure.

### Provenance et empreinte du bois

> **Question :** Est-ce qu'un provider de type `market ... hardwood - RoW` représente correctement l'approvisionnement en billes d'une usine québécoise ?

Il faudra rechercher si un provider CA-QC, CA ou nord-américain pertinent existe, puis vérifier son périmètre et sa représentativité avant toute substitution.

## 1. Identification

| Champ | Valeur |
|---|---|
| Matériau métier | Contreplaqué |
| Base | ecoinvent |
| Version | 3.11 |
| Dataset | `plywood production` |
| Géographie | CA-QC |
| Unité fonctionnelle / unité de référence | À vérifier |
| Statut | Analyse pilote en cours |
| Décision actuelle | À vérifier ; aucune régionalisation implémentée |

## 2. Évaluation générale

| Élément | Valeur / Dataset | Géographie / origine | Évaluation | Notes |
|---|---|---|---|---|
| Procédé de production | `plywood production` | CA-QC | ✓ | Géographie du procédé uniquement |
| Électricité | À vérifier | CA-QC | ✓ | Géographie québécoise établie ; autres caractéristiques à vérifier |
| Bois feuillu | Provider exact à vérifier | RoW | ⚠ | Approvisionnement québécois non démontré |
| Rendement matière bois | 2,206 m³/m³ plywood | Échantillon / littérature Allemagne | ⚠ | Valeur Québec à rechercher |
| Résine UF | À vérifier | À vérifier | ? | Quantité et provider inconnus |
| Chaleur | À vérifier | À vérifier | ? | Quantité et provider inconnus |

## 3. Intrants critiques

| Intrant | Quantité | Unité | Provider | Géographie | Criticité | Action |
|---|---|---|---|---|---|---|
| Bois feuillu | 2,206 | m³/m³ plywood | `market ... hardwood - RoW` (type à confirmer) | RoW | Élevée | Vérifier le rendement et rechercher un provider pertinent |
| Électricité | À vérifier | À vérifier | À vérifier | CA-QC | À évaluer | Documenter le provider et la quantité |
| Résine UF | À vérifier | À vérifier | À vérifier | À vérifier | À évaluer | Relever quantité, provider et géographie |
| Chaleur | À vérifier | À vérifier | À vérifier | À vérifier | À évaluer | Relever quantité, technologie, provider et géographie |

## 4. Paramètres à valider

| Paramètre | Valeur ecoinvent | Origine de la donnée | Valeur Québec | Source Québec | Statut |
|---|---|---|---|---|---|
| Volume de billes par volume de contreplaqué | 2,206 m³/m³ plywood | Échantillon / littérature Allemagne | À rechercher | À rechercher | ⚠ |
| Consommation d'électricité | À vérifier | À vérifier | À rechercher | À rechercher | ? |
| Quantité de résine UF | À vérifier | À vérifier | À rechercher | À rechercher | ? |
| Quantité de chaleur | À vérifier | À vérifier | À rechercher | À rechercher | ? |

## 5. Fournisseurs et géographies

| Intrant | Provider ecoinvent | Géographie actuelle | Alternative CA-QC / CA / Amérique du Nord | Justification |
|---|---|---|---|---|
| Bois feuillu | `market ... hardwood - RoW` (type à confirmer) | RoW | À rechercher | Confirmer d'abord la chaîne d'approvisionnement d'une usine québécoise |
| Électricité | À vérifier | CA-QC | À vérifier | Documenter le provider actuel avant toute décision |
| Résine UF | À vérifier | À vérifier | À rechercher | Information manquante |
| Chaleur | À vérifier | À vérifier | À rechercher | Information manquante |

## 6. Données québécoises à rechercher

- données d'entreprises sur le volume de billes consommé par m³ de contreplaqué ;
- données de fabricants sur les essences, les pertes et le rendement matière ;
- publications décrivant la technologie de production québécoise ;
- données d'associations sectorielles sur l'approvisionnement en bois ;
- statistiques québécoises ou canadiennes sur l'origine des billes ;
- quantités, technologies et providers relatifs à la résine UF, à la chaleur et à l'électricité.

Toutes ces informations sont **à rechercher** ou **à vérifier** ; aucune valeur québécoise n'est encore retenue.

## 7. Sources

| Information | Source | Statut |
|---|---|---|
| Dataset et géographie du procédé | ecoinvent 3.11 | Référence détaillée à documenter |
| Quantité de bois et origine allemande | ecoinvent 3.11 | Référence détaillée à documenter |
| Valeurs québécoises | À rechercher | ? |

Appliquer les [règles de traçabilité](../../sources/README.md) sans reproduire de contenu ecoinvent protégé.

## 8. Analyse des écarts

| Type d'écart | Constat | Action | Statut |
|---|---|---|---|
| Géographique | Procédé et électricité CA-QC, mais bois feuillu RoW | Vérifier l'approvisionnement et les providers possibles | ⚠ |
| Technologique | Technologie de production non analysée | Rechercher les caractéristiques des procédés québécois | ? |
| Énergétique | Électricité CA-QC ; chaleur inconnue | Documenter quantités, providers et technologie de chaleur | ⚠ |
| Matière | Rendement issu d'une source allemande ; résine inconnue | Valider le rendement et documenter la résine | ⚠ |
| Transport | À vérifier | Rechercher distances et modes pertinents | ? |
| Fin de vie | À vérifier | Définir ultérieurement le périmètre et les scénarios | ? |
| Incertitudes | Informations incomplètes sur plusieurs intrants | Documenter les sources et niveaux de confiance | ? |

## 9. Décision de régionalisation

- [ ] Conserver le dataset tel quel
- [ ] Conserver avec documentation
- [ ] Modifier certains providers
- [ ] Modifier certains paramètres
- [ ] Créer un dérivé Québec
- [ ] Reconstruire le dataset

**Décision actuelle :** à vérifier. Le dataset est un candidat pertinent, mais aucune option ne peut être retenue avant la validation du rendement matière, du bois, de la résine UF et de la chaleur. Aucune modification openLCA/ecoinvent n'est réalisée à ce stade.

## 10. Historique

| Date | Modification | Auteur |
|---|---|---|
| 2026-09-01 | Création de la fiche pilote | Équipe projet |
