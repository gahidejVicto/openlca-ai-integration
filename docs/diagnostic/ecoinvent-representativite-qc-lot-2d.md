# Diagnostic Ecoinvent — Lot 2D
## Composants sans produit fonctionnel direct : bandes de chant + quincaillerie

Projet ACV mobilier québécois — Base Ecoinvent 3.11, système Cutoff, via openLCA/MCP.

## Portée et conclusion QC

Portée stricte : 10 produits métier (4 bandes de chant + 6 quincailleries). Aucun produit fonctionnel direct correspondant n'a été identifié par les recherches process/flow disponibles. Ce constat ne constitue pas une preuve absolue d'absence au-delà des capacités d'interrogation utilisées.

Le lot distingue quatre types de lacunes qui doivent rester séparés : **absence de dataset produit**, **absence de nomenclature/composition**, **absence de procédé pertinent**, et **reconstruction matière + procédé possible mais non validée**.

## Bandes de chant

### Bois véritable préencollé

Les recherches `edge band`, `edgebanding`, `veneer tape`, `sliced veneer` et `veneer sheet` n'ont fourni aucun produit fini ni brique de placage mince exploitable. Les flows de type `sawlog and veneer log` sont plusieurs étapes trop en amont.

**Verdict : produit absent.** Une reconstruction n'est pas suffisamment étayée dans Ecoinvent sans brique de placage/bois mince. Données fournisseur nécessaires : essence, masse ou grammage/épaisseur, largeur, adhésif et grammage de colle, pertes éventuelles.

### Bois véritable non encollé

Même résultat pour la composante bois, sans la question de l'adhésif.

**Verdict : produit absent.** Données fournisseur nécessaires : essence, masse ou grammage/épaisseur, largeur et pertes éventuelles.

### ABS

Aucune bande de chant ABS n'a été trouvée. La matière existe via `market for acrylonitrile-butadiene-styrene copolymer` (`ca074112-8461-32ac-b814-2d7749b7b862`, GLO). Des services d'extrusion plastique existent, notamment `extrusion, plastic pipes` (`8bb6fcd6-e6dc-3397-ae07-499a2f71be3c`, RoW), mais leur géométrie ne correspond pas à une bande rigide plate et aucun indice observé ne démontre une spécificité ABS.

La variante CA-QC du service d'extrusion est déclarée comme copie des exchanges globaux permettant notamment le linking régional : sa localisation ne démontre donc pas une technologie québécoise primaire.

**Verdict : matière + procédé potentiellement reconstructibles, faible confiance.** Ce serait un proxy à tester, pas un modèle validé. Variables fournisseur : masse/m, largeur, épaisseur, formulation/additifs et procédé réel.

### PVC

Aucune bande de chant PVC finie n'a été trouvée. La matière existe via `market for polyvinyl chloride, suspension polymerised` (`fa6532b7-7f96-3bbb-8f42-c300d800d5ff`). Le service `calendering, rigid sheets` (`d0a9fc16-0991-3ab1-b75e-340dbf4c0506`, Europe) constitue une brique de transformation plus proche de la forme recherchée.

Un exchange `waste polyvinylchloride` de 0,00339 kg/kg constitue un **indice quantitatif fort que le procédé est modélisé spécifiquement pour une transformation du PVC**, même si le nom du dataset reste générique. Il ne démontre ni l'origine empirique précise du dataset ni son applicabilité aux chants de meuble. La documentation indique par ailleurs un dataset ancien hérité d'Ecoinvent v2.

**Verdict : matière + procédé potentiellement reconstructibles.** `PVC + calandrage rigide` est un proxy potentiel à tester ; `PVC + extrusion` n'a pas été démontré par ce lot. Variables fournisseur : masse/m, dimensions, formulation/additifs et procédé réel.

## Quincaillerie

### Vis #6 et #8

Aucun flow/process de vis de mobilier n'a été identifié ; les résultats `screw` observés étaient des faux positifs liés aux compresseurs. Ecoinvent fournit néanmoins des briques telles que `market for steel, low-alloyed` (`1af29f22-5a0a-3130-a65d-6ea9928f522a`), `wire drawing, steel` (`5563eb07-b684-33b5-bf13-a8f604fe5b06`) et `zinc coating, pieces` (`9cc6fb22-00d5-3d78-8971-0d46751d263c`). Les étapes spécifiques de frappe à froid et roulage du filet n'ont pas été identifiées.

**Verdict : matière + procédé partiel potentiellement reconstructibles.** Un même modèle générique pourrait être envisagé pour #6 et #8 **si le fournisseur confirme une composition, un procédé et un revêtement équivalents**. La masse par pièce serait alors le principal paramètre différenciant. L'absence de distinction de taille dans Ecoinvent ne démontre pas que les produits réels diffèrent uniquement par leur masse.

### Charnière invisible

Aucun produit fonctionnel n'a été identifié. Des briques génériques de métal, traitement de surface et metal working existent, mais aucune nomenclature interne de la charnière n'est disponible et aucun procédé spécifique n'a été établi.

**Verdict : matière seulement / données insuffisantes pour décider.** La composition fabricant est une donnée bloquante : masse totale, matériaux constitutifs et leurs parts, revêtement, nombre de pièces et origine.

### Coulisse de tiroir

Aucun `drawer slide`, `drawer runner`, `telescopic rail` ou équivalent exploitable n'a été identifié. Aucun système de roulement ou procédé spécifique n'a été caractérisé par les données inspectées.

**Verdict : matière seulement / données insuffisantes pour décider.** La composition et même le matériau dominant doivent être établis à partir de données fournisseur : masse, matériaux constitutifs et parts, revêtement, longueur et origine.

### Poignée métallique

Aucun produit fonctionnel de poignée de mobilier n'a été trouvé. `section bar extrusion, aluminium` constitue une brique potentiellement intéressante **uniquement si** une poignée réelle est confirmée comme profilé aluminium. Le matériau ne doit pas être présumé.

**Verdict : matière + procédé potentiellement reconstructibles sous condition.** Variable bloquante : matériau réel ; puis masse, finition, procédé, fixation incluse ou non et origine.

### Pied de nivellement

Aucun produit fonctionnel n'a été identifié ; les résultats `foot` étaient des faux positifs. Une piste `polypropylene + injection moulding` peut représenter une partie plastique **si cette composition est confirmée**, mais elle ne couvre pas un éventuel insert métallique.

**Verdict : reconstruction partielle potentielle, sous confirmation fournisseur.** Composition complète et masse sont nécessaires.

## Produit vs matière

Le Lot 2D ne justifie pas de considérer automatiquement `composant = matière`. Une reconstruction simplifiée **matière + procédé** devient envisageable lorsque la composition est confirmée, la complexité d'assemblage est faible et l'écart d'unité peut être comblé par une variable externe simple comme la masse par pièce ou par mètre.

Pour les vis, la reconstruction paraît relativement simple, mais Ecoinvent ne démontre pas que la matière seule suffit : matériau, revêtement, procédé complet et masse restent à confirmer. Pour charnière et coulisse, la nomenclature/composition est elle-même une donnée manquante majeure. Poignée et pied restent conditionnels à la confirmation de leur matériau/composition.

## Architecture des bandes de chant

- **Bois non encollé = bois/placage mince** : hypothèse non instanciable avec les briques identifiées, faute de produit de bois mince/placage fini.
- **Bois préencollé = bande bois + adhésif** : même blocage sur la composante bois ; les briques d'adhésif ne résolvent pas la lacune principale.
- **Plastique = résine + transformation + formulation/additifs** : architecture partiellement instanciable ; PVC + calandrage rigide est mieux étayé qu'ABS + extrusion pipes/film, mais aucun proxy n'est validé.

## Synthèse du Lot 2D

| Produit métier | Produit fonctionnel | Niveau Ecoinvent atteint | Verdict | Lacune principale | Action |
|---|---|---|---|---|---|
| Chant bois préencollé | Non | aucune brique de forme utile | Produit absent | placage/bande mince absent | données fournisseur avant reconstruction |
| Chant bois non encollé | Non | aucune brique de forme utile | Produit absent | placage/bande mince absent | données fournisseur avant reconstruction |
| Chant ABS | Non | matière + procédé générique mal adapté | Reconstructible, faible confiance | géométrie et formulation | proxy seulement à tester |
| Chant PVC | Non | matière + calandrage rigide | Reconstructible | forme exacte, formulation, ancienneté | proxy seulement à tester |
| Vis #6 | Non | matière + procédé partiel | Reconstructible sous conditions | mise en forme finale + données pièce | proxy après confirmation fournisseur |
| Vis #8 | Non | matière + procédé partiel | Reconstructible sous conditions | idem + paramètres propres à #8 | même architecture si équivalence confirmée |
| Charnière invisible | Non | matière/générique | Matière seulement | nomenclature/composition | données fabricant nécessaires |
| Coulisse de tiroir | Non | matière/générique | Matière seulement | composition + système fonctionnel | données fabricant nécessaires |
| Poignée métallique | Non | procédé conditionnel au matériau | Reconstructible sous condition | matériau réel inconnu | confirmer matériau puis modéliser |
| Pied de nivellement | Non | matière + procédé partiel conditionnel | Reconstructible partiellement | composition complète | confirmer corps/insert et masses |

## Variables minimales à demander

Pour les bandes de chant : matière/essence, masse par mètre ou données permettant de l'établir, dimensions, formulation/adhésif-additifs selon le cas et procédé réel.

Pour la quincaillerie : masse par pièce, composition massique par matériau constitutif, revêtement, procédé dominant et pays/région de fabrication. Pour les assemblages complexes, la nomenclature minimale des pièces et matériaux devient une donnée préalable à la modélisation.

## Impact méthodologique

Le Lot 2D confirme l'utilité des recherches process + flow et de la vérification des faux positifs linguistiques. Il ajoute deux apports importants :

1. **Typologie des composants manufacturés** : distinguer absence de dataset produit, absence de nomenclature/composition, absence de procédé, et reconstruction possible mais non validée.
2. **Critère #17 — inspecter les exchanges, notamment déchets et coproduits, pour détecter une spécificité matière qui n'apparaît ni dans le nom ni dans la description du procédé.** Le cas `calendering, rigid sheets` → `waste polyvinylchloride` illustre ce mécanisme. L'exchange constitue un indice de spécificité PVC ; il ne suffit pas à démontrer l'applicabilité au produit métier.

Aucun dataset openLCA modifié. Aucun proxy construit.
