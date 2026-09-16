# Synthèse des spécificités québécoises — RECQ36

Livrable demandé par Nicolas en réunion de validation métier du **2026-09-15**. Ce document rassemble ce que les analyses déjà présentes dans le dépôt démontrent effectivement à propos du contexte québécois de l'ébénisterie, et le sépare explicitement de ce qui reste une hypothèse ou un point à vérifier.

**Règle de rédaction de ce document :** chaque affirmation de la section 1 doit pouvoir être reliée à un lot de diagnostic ou une fiche fabricant sourcée du dépôt. Aucune connaissance générale non sourcée n'est utilisée pour compléter un trou. Là où l'information manque, elle est explicitement listée en section 2, pas devinée.

---

## 1. Ce qui est démontré par les analyses existantes

### 1.1 Un dataset localisé `Canada, Quebec` ne prouve pas des données primaires québécoises

C'est l'enseignement méthodologique le plus solidement démontré, répété indépendamment sur **deux familles distinctes** :

- **Contreplaqué (Lot 2A / fiche pilote [`plywood-ca-qc.md`](inventaire/panneaux/plywood-ca-qc.md)) :** le dataset `plywood production`, localisé `Canada, Quebec`, est décrit dans sa propre documentation comme une copie du modèle européen reposant sur un échantillon de production **allemande**. Les quantités technologiques centrales (bois, résine, énergie, eau) inspectées sont identiques ou se recomposent à la même somme entre la variante `CA-QC` et la variante `RER` (Europe), et les émissions directes de procédé inspectées sont elles aussi identiques.
- **Sciage de bois massif hardwood (Lot 2C) :** le dataset de sciage porte une variante `Canada, Quebec`, mais celle-ci est **déclarée identique au modèle mondial** dans sa documentation, dans le but explicite de permettre le linking vers des marchés régionaux — pas pour représenter une technologie de sciage québécoise réelle.

**Conclusion démontrée :** la présence de la géographie `CA-QC` sur un dataset Ecoinvent doit systématiquement être vérifiée au niveau des quantités et de la documentation narrative avant d'être interprétée comme une donnée primaire québécoise.

### 1.2 Deux cas où une donnée régionale québécoise a réellement été trouvée

Deux exceptions notables à 1.1, où la géographie régionale est corroborée par des données ou une documentation réellement spécifiques :

- **Carton ondulé (Lot 2A) :** le marché québécois `market for corrugated board box` s'appuie sur un procédé de fabrication (`corrugated board box production`) et sur un intrant majeur, le *fluting medium* (`containerboard production, fluting medium, semichemical, 40% recycled content`), tous deux décrits comme reposant sur la collecte réelle d'une usine québécoise (données de fabrication datées de 2008). C'est, à ce jour, **le cas le plus favorablement régionalisé identifié dans l'ensemble des diagnostics**. Réserve documentée : le linerboard (le plus gros intrant en masse) et l'électricité restent non vérifiés.
- **Eau de procédé / nettoyage (Lot 2G-bis) :** une variante `market for tap water`, localisée **Québec**, a été identifiée et inspectée directement — c'est le seul cas, à ce stade, où un dataset géographiquement québécois a été trouvé, inspecté et jugé fonctionnellement pertinent (eau distribuée traitée, pas un prélèvement environnemental brut) sans réserve majeure.

### 1.3 La transformation générique efface systématiquement la traçabilité d'essence pour le bois massif

Démontré au **Lot 2C**, sur les quatre essences P1 étudiées :

- Érable et frêne : **aucune trace de l'essence, à aucun stade de la chaîne**, y compris à la foresterie (recherches `maple`/`Acer` et `Fraxinus`/`ash` infructueuses).
- Merisier/bouleau jaune et chêne rouge : un procédé forestier au nom vernaculaire proche existe (`birch`, `oak`), mais géographiquement en **Suède** et en **Allemagne** respectivement — sans confirmation botanique de l'espèce nord-américaine visée, et sans donnée québécoise.
- Dans tous les cas, dès que la chaîne entre dans la catégorie de transformation générique `hardwood`, l'essence n'est plus distinguée dans le flow Ecoinvent.

### 1.4 Les technologies de panneaux bruts sont documentées, mais d'origine européenne/mixte, jamais québécoise

Démontré au **Lot 2B** : le panneau de particules brut (`market for particleboard, uncoated`) et le MDF brut (`market for medium density fibreboard`) ont une fonction bien représentée (norme EN 312 citée explicitement), mais leur recette, leur mix de liants et leur profil énergétique proviennent de données EPF (Europe) et, pour le panneau de particules, d'une extrapolation depuis un dataset brésilien à base d'eucalyptus. Aucune donnée primaire québécoise n'a été identifiée pour ces deux produits.

### 1.5 La richesse de représentation d'Ecoinvent n'est pas uniforme entre technologies concurrentes

Démontré au **Lot 2E**, en comparant trois technologies de surface visant la même fonction : le TFL/mélamine (Lot 2B) dispose d'un service de revêtement complet et documenté (`coating service, melamine impregnated paper, double-sided`), alors que le HPL et le placage de bois naturel n'ont, pour toute représentation, que des précurseurs chimiques isolés (HPL) ou une grume forestière générique plusieurs étapes en amont (placage). Ce contraste n'est pas géographique — il porte sur la technologie elle-même.

### 1.6 Les adhésifs d'atelier ne sont représentés, au mieux, que par leurs précurseurs chimiques

Démontré au **Lot 2F**, sur les quatre adhésifs métier étudiés : aucun n'existe comme produit formulé dans les recherches menées. Ecoinvent propose au mieux un monomère (vinyl acetate pour la PVA) ou une résine/copolymère (EVA pour le hot-melt) sans formulation ni additifs, et rien du tout pour la colle contact. Le Lot 2F a toutefois confirmé, par un candidat rejeté (`adhesive, for metal`, adhésif époxy pour cadres de fenêtres aluminium), qu'Ecoinvent contient bien, dans d'autres familles, des adhésifs réellement formulés — l'absence observée est donc spécifique à ces quatre technologies, pas une limite générale de la base sur les adhésifs.

### 1.7 Le transport générique est fondé sur un mix de flotte européen, sans représentativité nord-américaine établie

Démontré au **Lot 2G** : `market for transport, freight, lorry, unspecified` (location `Global`) combine des parts de classes d'émission EURO3 à EURO6 (mix EURO3 ≈ 45 %, EURO4 ≈ 39 %, EURO5 ≈ 14 %, EURO6 ≈ 2 %) sans qu'aucune documentation inspectée ne précise une géographie de flotte. La représentativité du parc routier québécois/nord-américain n'a pas été établie.

### 1.8 Le gaz naturel et les eaux usées n'ont pas de variante québécoise pour le service final, mais une brique amont gaz existe

Démontré aux **Lots 2G et 2G-bis** : ni le marché de chaleur au gaz naturel (`market for heat, central or small-scale, natural gas` — variantes Suisse/Europe sans Suisse/Rest-of-World seulement) ni le marché de traitement des eaux usées (`market for wastewater, average` — mêmes trois variantes) ne disposent d'une variante québécoise ou nord-américaine. En revanche, un marché de **gaz naturel haute pression spécifique au Québec** (`market for natural gas, high pressure`, brique amont, pas le service de chaleur) a été identifié — démontrant que la granularité nord-américaine existe dans Ecoinvent pour certains flux amont, sans se propager systématiquement jusqu'au produit/service final recherché.

### 1.9 L'électricité québécoise n'a pu être ni confirmée ni infirmée — limite d'outil démontrée, pas lacune de contenu démontrée

Démontré aux **Lots 2A et 2G** : la recherche du dataset `market for electricity, medium voltage`, location `CA-QC`, a échoué avec l'interface MCP utilisée (recherche par nom sans filtre géographique exposé, extraction de masse en timeout). Un dataset provincial pour l'Île-du-Prince-Édouard a néanmoins été observé dans un lot antérieur, ce qui démontre qu'**une modélisation électrique provinciale canadienne existe en principe dans Ecoinvent** — sans permettre de conclure sur le contenu du dataset québécois spécifiquement. C'est une limite d'accès, pas une lacune de contenu.

### 1.10 Des fabricants québécois publics existent pour plusieurs familles de panneaux, avec des informations techniques partiellement documentées

Ces informations proviennent des **fiches fabricant** (`docs/inventaire/`), fondées sur des sources publiques (sites, fiches techniques, certifications). **Elles ne constituent pas une preuve de correspondance Ecoinvent** — voir le rappel méthodologique du [README inventaire](inventaire/README.md) : *« Une fiche fabricant n'est pas une preuve de correspondance avec Ecoinvent. »* Elles documentent en revanche une réalité industrielle québécoise vérifiable, utile comme future source de données primaires :

| Thème | Fait documenté | Fabricant / usine | Fiche |
|---|---|---|---|
| Composition des panneaux | Densité typique 525 kg/m³ (33 lb/pi³) pour le MDF Ultralite, mesurée à l'usine, 18 mm, humidité 4–6 % | Uniboard, Mont-Laurier (QC) | [`uniboard-mont-laurier.md`](inventaire/panneaux/uniboard-mont-laurier.md) |
| Composition des panneaux | Fibre Ultralite déclarée 100 % fibres de bois résineux ; fibre MDF générale déclarée 100 % fibres recyclées/récupérées préconsommation (fiche environnementale) | Uniboard, Mont-Laurier (QC) | [`uniboard-mont-laurier.md`](inventaire/panneaux/uniboard-mont-laurier.md) |
| Système de liants | Technologie PureBond : collage à base de soja, sans formaldéhyde ajouté, confirmée pour les produits PureBond | Columbia Forest Products, Saint-Casimir (QC) | [`columbia-forest-products-saint-casimir.md`](inventaire/panneaux/columbia-forest-products-saint-casimir.md) |
| Système de liants | OSB fabriqué avec résines PF (phénol-formaldéhyde) selon la fiche de sécurité consultée ; système résine/cire général confirmé, dosage non publié | Arbec, Shawinigan/Amos (QC) | [`arbec-osb-quebec.md`](inventaire/panneaux/arbec-osb-quebec.md) |
| Matière première | Fibres de bois recyclées et récupérées déclarées comme matière ; programme Rewood de récupération de bois post-industriel dans l'Est canadien | Tafisa Canada, Lac-Mégantic (QC) | [`tafisa-lac-megantic.md`](inventaire/panneaux/tafisa-lac-megantic.md) |
| Présence industrielle QC — HPL | Usine de fabrication de stratifié décoratif haute pression (HPL) confirmée à Saint-Jean-sur-Richelieu — **fait notable** : un fabricant HPL québécois existe alors qu'Ecoinvent ne représente aucun produit HPL (voir 1.5 ci-dessus et Lot 2E) | Formica Canada, Saint-Jean-sur-Richelieu (QC) | [`formica-saint-jean-sur-richelieu.md`](inventaire/panneaux/formica-saint-jean-sur-richelieu.md) |
| Présence industrielle QC — OSB | Capacité annuelle annoncée de 550 millions pi² (base 3/8 po) ; numéro d'usine APA 556 | West Fraser, Chambord (QC) | [`west-fraser-osb-chambord.md`](inventaire/panneaux/west-fraser-osb-chambord.md) |
| Résidus/sous-produits | Certificat de chaîne de traçabilité SFI couvrant aussi copeaux, particules et écorce comme sous-produits (quantités et destinations non publiées) | Arbec, Shawinigan (QC) | [`arbec-osb-quebec.md`](inventaire/panneaux/arbec-osb-quebec.md) |

Ces faits ne sont **pas encore reliés** à une correspondance Ecoinvent ; ils constituent des pistes de collecte de données primaires pour une phase ultérieure de régionalisation, pas des conclusions de représentativité.

---

## 2. Ce qui reste une hypothèse ou un point à vérifier

Ces éléments sont explicitement **non démontrés** par les analyses existantes. Ils sont listés ici pour éviter qu'une lecture rapide du référentiel les confonde avec la section 1.

- **Extension par analogie aux essences non encore diagnostiquées (tilleul, bois feuillu exotique) :** le référentiel note, par analogie méthodologique avec l'érable et le frêne, qu'une perte de traçabilité de l'essence est *plausible* pour ces essences — ceci n'a **pas** été vérifié spécifiquement et ne doit pas être présumé.
- **Contreplaqué merisier / yellow birch / Baltic plywood :** le changement d'appellation décidé le 2026-09-15 n'a **pas** encore été suivi d'une recherche Ecoinvent dédiée à ces termes précis. La correspondance du dataset générique `plywood production` avec ce produit reprécisé est une hypothèse de travail hérité de l'ancienne appellation, pas une conclusion vérifiée. Voir la [liste structurée pour la prochaine passe OpenLCA](diagnostic/prochaine-passe-openlca.md).
- **HDF brut, OSB, panneau plaqué en atelier, stratifié/placage en atelier avec presse PVA :** aucune recherche Ecoinvent n'a encore été menée ; toute affirmation sur leur représentativité serait une supposition.
- **Existence d'un dataset électricité `CA-QC` :** ni confirmée ni infirmée (voir 1.9) — l'existence d'un dataset provincial pour l'Île-du-Prince-Édouard ne permet pas de déduire le contenu du dataset québécois.
- **Applicabilité des fiches fabricant à une correspondance Ecoinvent :** les faits de la section 1.10 sont des données d'industrie réelle, mais aucun travail n'a encore établi de lien quantitatif entre ces fiches et un dataset Ecoinvent particulier ; ce lien reste à construire, produit par produit, selon la méthode déjà documentée dans le [README inventaire](inventaire/README.md).
- **Bandes de chant PE, papier mélaminé appliqué en atelier, matériau d'emballage blanc en rouleau, ferrure de suspension :** nouveaux objets ajoutés le 2026-09-15, sans aucune recherche Ecoinvent à ce stade — toute spécificité québécoise pour ces objets reste, par définition, à établir.
- **Pratiques de fin de vie réelles des chutes/résidus en atelier québécois** (bois massif, panneaux, sciures, résidus contaminés) : le Lot 2G documente les scénarios de traitement *disponibles* dans Ecoinvent (décharge, incinération), mais aucune donnée n'établit laquelle de ces filières est réellement pratiquée par les ateliers québécois visés.

---

*Ce document consolide exclusivement des faits déjà sourcés dans le dépôt (`docs/diagnostic/`, `docs/inventaire/`). Aucune recherche openLCA/MCP ni recherche Web n'a été effectuée pour le produire. Toute correspondance Ecoinvent non encore établie mentionnée ci-dessus doit être vérifiée dans OpenLCA avant d'être utilisée pour une décision de modélisation — voir [`diagnostic/prochaine-passe-openlca.md`](diagnostic/prochaine-passe-openlca.md).*
