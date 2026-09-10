# Diagnostic Ecoinvent — Lot 2C
## Bois massif d'ébénisterie : érable, frêne, merisier, chêne rouge

Projet ACV mobilier québécois — Base Ecoinvent 3.11, système Cutoff, via openLCA/MCP.

Portée stricte : 4 essences métier (bois scié, séché, brut/non raboté, format 4/4, acheté par l'ébéniste). Aucun dataset modifié, aucune modification Git, aucun proxy construit.

## Résultat transversal : chaîne générique hardwood

Une chaîne complète foresterie → sciage → séchage existe dans Ecoinvent au niveau générique `hardwood`. La spécificité d'essence n'est pas conservée jusqu'au produit fini d'ébénisterie.

| Étage | Dataset | UUID | Location | Essence |
|---|---|---|---|---|
| Sciage | `sawing, hardwood → sawnwood, hardwood, raw` | `6f452c2d-38ee-3916-bea2-b725fecb8d97` CA-QC / `bc9f5858-6781-3025-9357-997d6f7b1f5a` Suisse | CA-QC / Suisse | hardwood générique |
| Séchage u=10% | `board, hardwood, raw, kiln drying to u=10%` | `99775e17-490b-3860-8da0-ad9871204a75` RoW / `ab55234a-d6cf-30a4-92c4-9bf1db5e6cf6` Suisse / `e8de2fb7-8209-357f-b1be-4c035ec78ca0` Europe sans Suisse | RoW / Suisse / Europe | hardwood générique |
| Flow final | `sawnwood, board, hardwood, raw, dried (u=10%)` | `8f082e64-e307-450f-ba63-d07e65ab4954` | — | hardwood générique |

Le dataset de sciage CA-QC déclare que ses échanges sont identiques au dataset GLO afin de permettre le linking vers des marchés régionaux. Les données primaires sont attribuées à l'industrie forestière suisse. La comparaison quantitative montre notamment 19,376 kWh d'électricité et 31,839 MJ de diesel identiques entre CA-QC et Suisse. La localisation québécoise est donc administrative/régionale pour le linking, sans technologie de sciage québécoise démontrée.

Le séchage Suisse, Europe sans Suisse et RoW est identique pour les paramètres inspectés : 30,0 kWh d'électricité, 77,306 kg de copeaux internes et 140,03 kg de CO2 biogénique. Aucune variante CA-QC n'a été trouvée pour cette étape.

Le rendement de sciage est de l'ordre de 65–67 % dans le modèle générique et le séchage utilise 1,087 m³ de bois humide par m³ de bois sec. Les émissions propres au bois pendant le séchage sont explicitement exclues par Ecoinvent. Le flow final `raw, dried (u=10%)` est distinct du flow plané : il correspond donc bien au besoin métier brut/non raboté. Ecoinvent ne distingue pas les épaisseurs nominales 4/4, 5/4, etc. à l'intérieur de la catégorie `board`.

## Érable

Les recherches `maple` et `Acer` n'ont retourné aucun flow ou process pertinent. Aucun candidat spécifique à l'essence n'a été identifié. Le meilleur candidat reste le flow générique `sawnwood, board, hardwood, raw, dried (u=10%)`.

La fonction, l'état acheté et la transformation correspondent bien au produit métier, mais l'essence est absente et les données technologiques de sciage/séchage sont suisses ou dérivées de celles-ci. Le dataset CA-QC de sciage n'apporte pas de technologie primaire québécoise démontrée.

**Verdict : mauvaise essence.** Le hardwood générique peut servir de proxy documenté pour la structure du sciage/séchage, mais ne doit pas être présenté comme de l'érable.

**A — transférable :** principe du sciage et du séchage au séchoir.  
**B — à régionaliser :** électricité, chaleur, transport et origine forestière.  
**C — données fournisseur :** essence botanique réelle, densité, rendement de sciage, humidité cible et provenance.

La densité spécifique à l'érable n'est pas représentée explicitement dans le dataset générique et devra être documentée séparément.

## Frêne

Les recherches `Fraxinus` n'ont donné aucun résultat. Le terme `ash` retourne des faux positifs liés aux cendres et produits chimiques, sans résultat pertinent pour l'essence forestière.

Le meilleur candidat est donc le même hardwood générique que pour l'érable. Fonction, transformation et séchage sont représentés génériquement, mais l'essence est absente.

**Verdict : mauvaise essence.** Même décision que pour l'érable : proxy hardwood uniquement, avec réserve explicite sur l'absence de correspondance d'essence.

La densité propre au frêne réellement utilisé n'est pas représentée explicitement dans le dataset hardwood générique et devra être documentée séparément.

## Merisier / yellow birch

Un process `hardwood forestry, birch, sustainable forest management` a été identifié en Suède, UUID `885df1ec-96c0-32a2-a869-70779dc48420`. Le produit de référence est cependant le flow générique `sawlog and veneer log, hardwood`. Aucun sciage ou séchage spécifique `birch` n'a été identifié : dès la sortie de la foresterie, la chaîne retombe dans le hardwood générique.

Ecoinvent décrit ce dataset comme une production/récolte de stemwood `birch` sous gestion forestière suédoise. Ecoinvent ne précise pas l'espèce botanique au-delà du nom vernaculaire `birch`. La géographie suédoise et l'absence de mention de *Betula alleghaniensis* ne permettent donc pas d'établir une correspondance avec le merisier/bouleau jaune québécois visé.

Le système forestier est modélisé pour la Suède et ne peut pas être considéré comme représentatif du Québec sans validation de ses paramètres.

**Verdict : essence générique potentiellement adaptable.** La lacune commence en substance dès la foresterie : l'espèce métier n'est pas établie et la géographie est inadéquate. La transformation ultérieure est générique.

**A — transférable :** principe générique du sciage/séchage.  
**B — à régionaliser :** système forestier, énergie, transport.  
**C — données fournisseur :** confirmation botanique, densité, rendement de sciage, humidité cible et provenance.

## Chêne rouge

Un process `hardwood forestry, oak, sustainable forest management` a été identifié en Allemagne, UUID `1050da18-ecb1-3414-8011-a04a3151ff23`. Son flow de sortie est lui aussi générique `sawlog and veneer log, hardwood`. Aucun sciage ou séchage spécifique au chêne n'a été identifié.

Ecoinvent décrit une production/récolte de stemwood `oak` sous gestion forestière allemande, sans préciser l'espèce botanique au-delà du nom vernaculaire `oak`. La géographie allemande et l'absence de mention de *Quercus rubra* ne permettent donc pas d'établir une correspondance avec le chêne rouge nord-américain visé.

Le système forestier modélisé pour l'Allemagne comprend notamment 12,27 semis/m³ produit, 37,1 m²·an d'occupation de voirie, 15,20 MJ/m³ de diesel et 0,375 h/m³ de tronçonnage. Ces paramètres ne peuvent pas être considérés comme représentatifs du Québec sans validation.

**Verdict : essence générique potentiellement adaptable.** Comme pour le merisier, la lacune commence en substance dès la foresterie : espèce métier non établie, géographie inadéquate et transformation ultérieure générique.

**A — transférable :** principe générique du sciage/séchage.  
**B — à régionaliser :** système forestier, énergie, transport.  
**C — données fournisseur :** confirmation botanique, densité, rendement de sciage, humidité cible et provenance.

## Comparaison des quatre essences

| Critère | Érable | Frêne | Merisier | Chêne rouge |
|---|---|---|---|---|
| Essence exacte présente ? | Non | Non | Non confirmée (`birch` seulement) | Non confirmée (`oak` seulement) |
| Dataset forestier nominal | Non | Non | Oui, Suède | Oui, Allemagne |
| Sciage spécifique | Non | Non | Non | Non |
| Séchage spécifique | Non | Non | Non | Non |
| Bois scié séché | Générique hardwood | Générique hardwood | Générique hardwood | Générique hardwood |
| Premier étage lacunaire | Foresterie | Foresterie | Foresterie en substance | Foresterie en substance |
| Verdict | Mauvaise essence | Mauvaise essence | Essence générique potentiellement adaptable | Essence générique potentiellement adaptable |

## Hardwood générique comme proxy

L'inspection montre que le hardwood générique constitue un socle utilisable pour la **structure physique du sciage et du séchage**, mais pas une représentation autonome d'une essence québécoise particulière.

La densité par essence n'est pas explicitement distinguée. Le rendement de sciage est générique, autour de 65–67 %. Le séchage est lui aussi générique et ne varie pas par essence dans les datasets inspectés. L'énergie et les coproduits suivent la même logique générique. Enfin, les systèmes forestiers spécifiques observés sont suédois ou allemands et ne correspondent pas à une foresterie québécoise démontrée.

Le proxy hardwood est donc **adaptable**, à condition de documenter ou corriger les paramètres discriminants avec des données québécoises/fournisseur. Il ne doit pas être utilisé tel quel comme preuve de représentativité d'une essence.

## Où commence la lacune ?

| Essence | Premier étage lacunaire |
|---|---|
| Érable | Dès la foresterie — aucune trace spécifique |
| Frêne | Dès la foresterie — aucune trace spécifique |
| Merisier | Dès la foresterie en substance — `birch` suédois sans correspondance botanique établie avec l'essence métier |
| Chêne rouge | Dès la foresterie en substance — `oak` allemand sans correspondance botanique établie avec l'essence métier |

Pour le merisier et le chêne rouge, la présence du mot `birch` ou `oak` dans le nom du process ne suffit donc pas à établir une correspondance. La description, la géographie et la précision botanique disponible doivent être contrôlées.

## Variables minimales à obtenir ultérieurement

- confirmation botanique de l'essence réellement livrée ;
- densité ;
- rendement de sciage ;
- humidité cible ;
- provenance et distance d'approvisionnement ;
- consommation énergétique du sciage/séchage si disponible.

## Impact méthodologique

Le Lot 2C confirme l'importance de la comparaison quantitative, de la déclaration narrative et de la recherche par flow. Il ajoute trois précisions à la grille :

1. rechercher **process et flow**, car une essence peut apparaître dans le nom d'un process tout en disparaissant dans le flow de sortie ;
2. contrôler les **homonymies linguistiques** des termes de recherche, comme `ash` ;
3. suivre la **perte de traçabilité d'une caractéristique** le long de la chaîne : `birch/oak` au process forestier devient immédiatement `hardwood` dans le flow puis dans les transformations suivantes.

Pour les matériaux biologiques/forestiers, la représentativité doit donc être décomposée au minimum en cinq dimensions : **essence + système forestier + transformation + séchage + géographie**. Les différents étages peuvent avoir des niveaux de régionalisation différents : ici, le sciage possède une copie CA-QC alors que le séchage n'en possède pas.

## Synthèse

| Produit métier | Meilleur candidat | UUID | Niveau | Essence exacte | Géographie | Premier étage lacunaire | Verdict | Principale lacune | Action |
|---|---|---|---|---|---|---|---|---|---|
| Érable massif | `sawnwood, board, hardwood, raw, dried (u=10%)` | `8f082e64-e307-450f-ba63-d07e65ab4954` (flow) | sciage+séchage générique | Non | Suisse / CA-QC sciage copié | Foresterie | Mauvaise essence | essence absente | Adapter avec données fournisseur |
| Frêne massif | idem | `8f082e64-e307-450f-ba63-d07e65ab4954` | sciage+séchage générique | Non | Suisse / CA-QC sciage copié | Foresterie | Mauvaise essence | essence absente | Adapter avec données fournisseur |
| Merisier | `hardwood forestry, birch` + transformation hardwood | `885df1ec-96c0-32a2-a869-70779dc48420` | foresterie non spécifique puis générique | Non confirmée | Suède / Suisse | Foresterie en substance | Essence générique potentiellement adaptable | espèce non établie + géographie + perte de traçabilité | Confirmer essence et adapter |
| Chêne rouge | `hardwood forestry, oak` + transformation hardwood | `1050da18-ecb1-3414-8011-a04a3151ff23` | foresterie non spécifique puis générique | Non confirmée | Allemagne / Suisse | Foresterie en substance | Essence générique potentiellement adaptable | espèce non établie + géographie + perte de traçabilité | Confirmer essence et adapter |

Aucun dataset openLCA modifié. Aucun proxy construit.