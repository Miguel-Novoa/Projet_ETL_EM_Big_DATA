# Projet ETL

## Introduction

Durant cette semaine, le projet que vous aurez à réaliser consiste à écrire un outil de manipulation des données, souvent appelé ETL (acronyme de Extract-Transform-Load).

Le but de ce projet est, naturellement, de produire un logiciel, mais il doit surout être le support de méthodologies de travail de groupe. Nous allons ici détailler les deux aspects de ce travail.

### Qu'est-ce qu'un ETL ?

Le processus est en soi assez simple à comprendre. Un ETL se décompose en trois phases :
1. **Extraction** : phase consistant à importer des données depuis des sources ; ces sources peuvent être de nature très diverses.
1. **Transformation** : phase permettant de transformer les données de manière à ce qu'elles correspondent aux besoin d'une application locale
1. **Chargement** : phase durant laquelle les données transformées seront écrites sur de nouveaux supports, qui peuvent là aussi être de nature très diverses.

L'ensemble de ces trois phases représent ce que l'on appelle un « **pipeline** », assez comparable dans l'esprit aux combinaisons de commandes que l'on trouve dans UNIX.
Contrairement au shell UNIX, les pipelines ETL ne sont pas nécessairement linéaires. Ils peuvent souvent être représentés sous formes de graphes, de treillis, voire être parallélisés.

#### Extraction

Généralement, les sources à partir desquelles l'on veutr acquérir des données sont dans des formats très classiques :
- des fichiers « _plats_ », non structurés
- des fichiers semi-structurés, comme JSON ou CSV
- des fichiers structurés comme XML ou HTML
- des bases de données (relationnelles ou NoSQL)

Il faut en général développer des connecteurs permettant de mettre les données dans un format « _neutre_ », ou en tout cas commun, pour  qu'elles puissent être facilement transformées

LA phase d'extraction comprend également souvent un phase de validation des données, c'est-à-dire que celles-ci correspondent bien à ce que l'on attend. Par exemple, que contient un « _colonne_ » nommée `country` ? Les données sont-elles utilisables ou non ?

#### Transformation

La phase de tranformation est celle qui est la pus vaste puisqu'elle consiste à applique tout type de traitement qui viera à rendre les données compatibles avec les besoins de l'organisation qui met en œuvre l'ETL. Cela couvre  :
- le nettoyage des données (manquantes, aberrantes, etc.)
- la normalisation des données (p.ex. toutes les dates doivent être dans le même format)
- l'encodage des données catégorielles (p.ex. 'Homme' -> 1, 'Femme' -> 2)
- le changement de format des données (p.ex. CSV -> JSON, ou plus couramment vers un format intermédiaire de Python)
- la restriction ou la sélection à l'intérieur du jeu de données
- la fusion de sources de données
- la déduplication des données
- le calcul de nouvelles valeurs à partir des sources de données
- la transposition du tableau (matrice)  de données
- etc.

Tous ces types de transformation sont indépendant les uns des autres et doivent pouvoir être combinés (c'est dans la notion  _pipeline_). C'est pourquoi il est important de faire en sorte que le format d'entrée et le format de sortie de chasue module de transformation soit facilement interprétable par les autres modules.

En pratique, chaque module de transformation peut être implémenté comme une bibliothèque, intégrée dans un catalogue, qui pourra être ajoutée ou supprimée de l'application.

#### Chargement

La phase finale est un peu l'inverse de la première. 
Une fois le jeu de données transformé selon nos besoins, nous n'aurons plus qu'à le sauvegarder sur un support (voire plusieurs).
Cela nécessitera éventuellement la définition d'un modèle de sortie comme sun schéma de base de données relationnelle.

Les données une fois sauvegardées seront généralement utilisées comme sources pour d'autres appllications de l'organisation qui met en œuvre l'ETL.

#### Outils

Il existe de nombreux outils d'ETL. Parmi les plus connus, on citera ;
- **Talend**, un outil d'entreprise très complet reposant sur une interface graphique, libre
- **ELK**, une pile d'outils reposant sur la base de données **Elascticsearch**, essentiellement en ligne de commande, libre
- **Bonobo**, une bibliothèque Python pour les priojets ETL, support de développement, libre
- **AWS Glue**, d'Amazon
- **Hadoop**, de la fonction Apache, libre 
- **Google Data FLow**
- etc.

### Méthodologie de travail

Cette semaine de projet doir permettre de mettre en œuvre des méthodes de travail collectif et de suivi de projet.

Généralement, cela implique plusieurs volets :
1. Constitution d'une équipe
1. Définition des objectifs du projets
1. Lecture des « _exigences_ » du projet (les fonctionnalités attenduesn par exemple)
1. La mise en place d'outils de partage de code
1. La mise ne place d'outils de gestion des tâches
1. La production d'ubn document de spécification technique
1. La production d'un cahier de tâches (ou « backlog », quelquefois surnommé « frigo »)
1. Une hiérarchisation et une planification des tâches
1. La mise en place de cycles de développement (on raisonnera en mode Agile souple) pendant lesquels on insistera sur :
    - la préparation du cycle, c'est-à-dire la sélection d'un groupe de tâches à réaliser en priorité et l'anticipation du tempsnéceesaire à la réalisation de chaque tâche (parfois surnommé la réunion de « _poker planning_ ») 
    - les rituels, comme les briefings (dans notre cas journaliers) bi-quotidiens (matin, soir) pour préparer puis commenter la journée (chaque briefing devant être le plus concis possible)
    - la sélection et la répartition des tâches journalières (chaque tâche du _backlog_ doit être suffisamment petite pour pouvoir être réalisée dans la journée.
    - des modes de coomunication agiles, de manière à prévenir les éventuels blocages du développement (chacun est responsabvle d'une partie du travail, mais il ne faut jamais oublier que c'est malgré tou un travail d'équipe)
    - des temps de production de la documentation
    - un temps de fin de cycle pour faire le point sur l'état des lieux ét éventullement faiure une présentation (au client, par exemple)

Le méthodes itératives de développement sont maintenant souvent redoublées par des méthodes prenant en compte l'intégralité du cycle de vie logiciel, comme par exemple :
- **DevOps**, qui fait la jonction entre le développement, le déploiement et la maintenance du logiciel
- **DataOps**, qui prend en compte le cycle de vie des données depuis leur production, leur modélisatrion, jusquà leur utilisation par des non-techniciens
- **MLOps**, qui s'applique à l'apprentissage automatique et modélise la production, la maintenance et l'utilisation de modèles prédictifs

## Le projet

### Pitch

Votre mission est donc de développer un nouvel outil d'ETL. Les contraintes sur cet outil sont les suivantes :
1. Il doit être écrit en Python
1. Il doit donner accès à diverses sources de données
1. Il doit être suffisamment modulaire poour pouvoir ajouter de nouvelles fonctionnalités sans réécriture de code
1. Il devrait pouvoir être piloté de manière déclarative
1. Il sera utilisé en ligne de commande
1. Il devrait pouvoir être utilisé comme module dans une application tierce

Dans une première livraison, nous aimerions pouvoir :
1. Lire des données depuis ;
    - des fichiers textuels
    - des fichiers JSON, XML, HTML
    - des bases de données relationnelles
    - des API
    - _(éventuelklement depuis plusieurs sources simultanément)_
1. Transformer des données afin de :
    - filter le jeu de données suivant un certain critère
    - repérer des données manquantes et les corriger
    - repérer des données aberrantes et les corriger
    - effectuer un calcul
        - soit à partir de deux (ou plus) attributs du jeux de données
        - soit à partir d'un attribuet et d'une valeur externe (comme une constante)
    - normaliser les valeurs comme :
        - utiliser des types uniformes
        - utiliser des catégories uniformes, d'après un modèle local
        - utiliser des dates uniformes
    - ajouter un attribut au jeu de données
    - _(ces transformations peuvent être cumulées)_
1. Stocker des données:
    - dans une base de données relationnelle
    - dans un fichier JSON ou XML
    - _(éventullement dans plusieurs formats simultanément)_

Nous aimerions également décrire le pipeline de traitement des données par le biais d'un fichier YAML, comparable dans l'idée à un fichier de configuration Symfony ou Github Actions, qui serait lu  par un interpréteur chargé d'exécuter les commandes.

### Tâches

A partir de cette description succincte, vous aurez différentes tâches à accomplir :
1. Comprendre (et interpréter) les objectifs du projet
1. Estimer la faisabilité du projet
1. Faire un état des lieux des outils disponibles pour la réalisation du projet
1. Formaliser le périmètre d'une première livraison
1. Choisir un modèle de représentation interne (uniforme) pour les données
1. Produire une spécification technique de l'implémentation logicielle
1. Lister les tâches à accomplir pour l'achèvement du projet (ou de sa première livraison)
1. Produire le code du projet
1. Produire une documentation à l'usage  des utilisateurs futurs

### Rendu

En termes de rendu, volci ce que nous attendons de vous :
1. Un dépôt partagé contenant :
    - le code de votre projet
    - un cahier de spécification résumant les fonctionnalités développées et les choix techniques
    - un exemple de jeu de données
1. Une trace de vos compte-rendus de réunion, résumant vos choisx en matière d'organisation du travail
    - avec un plan de travail partégé
1. Une présentation orale avec une démonstration de votre projet.


## Agile

- Méthode itérative
- Méthode vise à augmenter le confort de travail
- Eviter le stress
- Eviter le travail inutile
- Eviter de réfléchir trop en avance

Spécification -> Développement -> Tests -> Recette

- cycle de développement
- 1 - 3 semaines
- Question : Qu'avons le temps de faire en 2 semaines ?
- Que pourrons-nous présenter à la fin de ces 2 semaines ?

- Phase 1 :
- Etude du projet
   - Analyser le projet
        - produire un "pitch"
   - Comprendre les objectifs
   - Diviser le travail en un certain de tâches à réqliser (cas d'utilisation)
       - lister les fonctionnalités que doit remplir notre système
       - partie de spécification
       - spécification non-fonctionnelle (ergonomie, performance, déploiement, maintenance, etc.)
   - produire un backlog
       - catalogue des tâches à réaliser
       - outil de collaboration (Trello, etc.)
- Le backlog n'est pas figé

- Phase 2 :
- Cycle de travail
   - Tests (unitaoires, fonctionnels)
        - TDD (Test Driven Development)
        - Pair-programming (binôme : 1 pour les tests, 1 développe le code)
            - (1 pour la veille technique (rechercher les solutiosn existantes, 1 qui travaille sur le code) 
   - Rituels
       - Optimiser la communication entre les membres de l'équipe
       - Scrum, XP, etc...
       - Rituels quotidien
           - matin : 15 min.
           - fin de journée
       - Rituels d'organisation
            - début de cycle
                - choisir les tâches à réaliser (consensus)
                    - hiérarchiser les tâches -> développer un noyau (MVP : minimal viable product)
                    - se répartir les tâches
                    - se coordonner
                    - spécifier finement les tâches
                        - schémas UML
                    - tests
            - fin de cycle
                    - bilan du cycle passé
                    - quels sont les problèmes en suspens ?
                        - Au départ il y a des choses qu'on ne sait pas qu'on ne sait pas

- Phase 3 :
- Livraison (Release) Version majeure du logiciel
    - version stable, qui correspond à une demande du client
    - Recette
        - Faire une démonstration
        - Lister avec le client les fonctionnalités
            - Se mettre d'accord sur une définition du terme "fini"
    - Déploiement
        - CI/CD
    - Release à date fixe
        - Symfony : 1 livraison par an
        - Firefox : 6 mois
            - ne pas attendre que tout soit "parfait" (Drupal 8) 












