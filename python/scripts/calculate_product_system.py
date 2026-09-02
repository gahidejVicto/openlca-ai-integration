"""
Script de référence pour piloter openLCA via olca-ipc.

Objectif
--------
Ce script valide la chaîne technique suivante :

    Python
        ↓
    olca-ipc
        ↓
    serveur IPC openLCA
        ↓
    base ACV active
        ↓
    calcul LCIA

Le script recherche un Product System et une méthode d'impact par leur nom,
récupère l'unité fonctionnelle définie dans openLCA, lance le calcul LCIA,
affiche les résultats, puis libère le résultat temporaire côté openLCA.

Cas de validation actuel
------------------------
Product System :
    Paper cup use

Méthode d'impact :
    IPCC 2007

Résultat de référence attendu :
    climate change - GWP 100a ≈ 39.733528 kg CO2-Eq

Important
---------
Le calcul doit reprendre explicitement :
    - target_amount ;
    - target_unit ;
    - target_flow_property.

Ne pas fournir ces informations peut provoquer une erreur d'échelle lorsque
l'unité fonctionnelle du Product System diffère de l'unité de référence du flux.

Sécurité
--------
Ce script est destiné à la lecture et au calcul uniquement.
Il ne crée, ne modifie et ne supprime aucune donnée dans openLCA.
"""

import olca_ipc as ipc
import olca_schema as o


PORT_IPC = 8080
NOM_SYSTEME_PRODUIT = "Paper cup use"
NOM_METHODE_IMPACT = "IPCC 2007"


def rechercher_reference_par_nom(client, type_objet, nom):
    """
    Recherche la référence d'un objet openLCA à partir de son nom exact.

    Args:
        client:
            Client IPC openLCA utilisé pour interroger la base active.

        type_objet:
            Type d'objet openLCA recherché, par exemple
            o.ProductSystem ou o.ImpactMethod.

        nom:
            Nom exact de l'objet à rechercher.

    Returns:
        La référence openLCA correspondant au nom demandé.

    Raises:
        ValueError:
            Si aucun objet portant exactement ce nom n'est trouvé.
    """
    references = client.get_descriptors(type_objet)

    for reference in references:
        if reference.name == nom:
            return reference

    raise ValueError(
        f"Aucun objet de type {type_objet.__name__} "
        f"nommé '{nom}' n'a été trouvé dans la base openLCA active."
    )


def charger_systeme_produit(client, reference_systeme):
    """
    Charge un système de produit complet à partir de sa référence.

    Cette étape est nécessaire pour récupérer notamment l'unité
    fonctionnelle définie dans openLCA :
    - quantité cible ;
    - unité cible ;
    - propriété de flux cible.

    Args:
        client:
            Client IPC openLCA.

        reference_systeme:
            Référence du système de produit à charger.

    Returns:
        L'objet ProductSystem complet correspondant à la référence.
    """
    return client.get(
        o.ProductSystem,
        reference_systeme.id,
    )


def creer_configuration_calcul(
    systeme,
    reference_systeme,
    reference_methode,
):
    """
    Crée la configuration d'un calcul ACV pour un système de produit.

    La quantité, l'unité et la propriété de flux sont reprises directement
    du Product System afin de respecter exactement l'unité fonctionnelle
    définie dans openLCA.

    Cette précision est importante : utiliser uniquement la référence du
    Product System peut provoquer une mauvaise interprétation de l'échelle
    de calcul si l'unité cible diffère de l'unité de référence du flux.

    Args:
        systeme:
            Objet ProductSystem complet.

        reference_systeme:
            Référence du Product System utilisé comme cible du calcul.

        reference_methode:
            Référence de la méthode d'évaluation des impacts.

    Returns:
        Un objet CalculationSetup prêt à être envoyé à openLCA.
    """
    return o.CalculationSetup(
        target=reference_systeme,
        impact_method=reference_methode,
        amount=systeme.target_amount,
        unit=systeme.target_unit,
        flow_property=systeme.target_flow_property,
    )


def afficher_resultats(
    systeme,
    nom_systeme,
    nom_methode,
    impacts,
):
    """
    Affiche les informations principales du calcul et les impacts LCIA.

    Args:
        systeme:
            Système de produit calculé.

        nom_systeme:
            Nom lisible du système de produit.

        nom_methode:
            Nom de la méthode d'impact utilisée.

        impacts:
            Collection de résultats LCIA retournée par openLCA.
    """
    print(f"Système de produit : {nom_systeme}")
    print(
        "Unité fonctionnelle :",
        systeme.target_amount,
        systeme.target_unit.name,
    )
    print(f"Méthode d'impact : {nom_methode}")
    print()

    for impact in impacts:
        print(
            f"{impact.impact_category.name} : "
            f"{impact.amount:.6f} "
            f"{impact.impact_category.ref_unit}"
        )


def executer_calcul():
    """
    Exécute un calcul LCIA complet via le serveur IPC openLCA.

    Le déroulement est le suivant :
    1. connexion au serveur IPC ;
    2. recherche du Product System ;
    3. chargement de son unité fonctionnelle ;
    4. recherche de la méthode d'impact ;
    5. création de la configuration de calcul ;
    6. lancement du calcul dans openLCA ;
    7. récupération et affichage des impacts ;
    8. libération du résultat temporaire côté openLCA.

    Raises:
        ValueError:
            Si le système de produit ou la méthode d'impact demandée
            n'existe pas dans la base openLCA active.
    """
    client = ipc.Client(PORT_IPC)

    reference_systeme = rechercher_reference_par_nom(
        client,
        o.ProductSystem,
        NOM_SYSTEME_PRODUIT,
    )

    systeme = charger_systeme_produit(
        client,
        reference_systeme,
    )

    reference_methode = rechercher_reference_par_nom(
        client,
        o.ImpactMethod,
        NOM_METHODE_IMPACT,
    )

    configuration = creer_configuration_calcul(
        systeme,
        reference_systeme,
        reference_methode,
    )

    resultat = client.calculate(configuration)

    try:
        etat = resultat.wait_until_ready()

        if etat.error:
            raise RuntimeError(
                f"openLCA a retourné une erreur de calcul : {etat.error}"
            )

        impacts = resultat.get_total_impacts()

        afficher_resultats(
            systeme,
            NOM_SYSTEME_PRODUIT,
            NOM_METHODE_IMPACT,
            impacts,
        )

    finally:
        resultat.dispose()


if __name__ == "__main__":
    executer_calcul()