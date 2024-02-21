# Cahier des charges

## Index

- [Introduction](#introduction)
  - [Résumé](#résumé)
  - [Analyse client](#analyse-client)
  - [Objectifs (release v.1.0)](#objectifs-de-release-v10)
- [Gestion du projet](#gestion-du-projet)
  - [Spécifications](#spécifications)
  - [Outils](#outils)
- [Déroulement du projet](#déroulement-du-projet)
- [Documents](#documents)

## Introduction

### Résumé

Créer un outil de manipulation de données, écrit en Python, selon le processus Extract-Transform-Load. Cet outil permettra d'extraire des données de diverses sources, de les transformer en fonction de besoins spécifiques, puis de les charger dans différents formats de sortie. L'objectif est de concevoir un système modulaire, pilotable en ligne de commande de manière déclarative, et potentiellement intégrable dans d'autres applications. La première livraison du projet se concentrera sur la lecture de données depuis différents types de sources, leur transformation selon des critères prédéfinis, et leur stockage dans divers formats. Ce projet sera mené selon des méthodologies agiles, favorisant le travail collaboratif et itératif, avec un accent sur la spécification, le développement et les tests.

### Analyse client

#### Objectifs du Projet

##### Objectif Principal

Le client souhaite disposer d'un outil ETL écrit en Python qui soit flexible, modulaire et capable de traiter diverses sources de données. Cet outil doit offrir une solution déclarative, permettant d'automatiser les tâches d'extraction, de transformation et de chargement de données.

##### Objectifs Spécifiques

**Flexibilité et Modularité** : L'outil doit être suffisamment modulaire pour faciliter l'ajout de nouvelles fonctionnalités sans nécessiter une refonte du code existant.

**Pilotage Déclaratif** : Le client souhaite une approche déclarative pour piloter l'outil, simplifiant ainsi la configuration et l'exécution des tâches.

**Interface en Ligne de Commande** : L'outil doit être utilisable en ligne de commande pour garantir une facilité d'utilisation et d'intégration dans divers environnements.

**Intégration comme Module** : Le client a l'intention d'utiliser cet outil comme module au sein d'applications tierces, nécessitant une conception compatible et une documentation claire pour les développeurs tiers.

##### Besoins Fonctionnels

**Extraction de Données** : L'outil doit être capable de lire des données à partir de fichiers textuels, fichiers JSON, XML, HTML, bases de données relationnelles et APIs, éventuellement simultanément.

**Transformation de Données** : Les fonctionnalités de transformation incluent le filtrage des données selon des critères définis, la correction des données manquantes ou aberrantes, et la réalisation de calculs complexes basés sur les attributs des jeux de données.

**Chargement de Données** : L'outil doit être en mesure de stocker les données transformées dans une base de données relationnelle, un fichier JSON ou XML, et potentiellement dans plusieurs formats simultanément.

**Configuration Déclarative** : Le client souhaite décrire le pipeline de traitement des données à l'aide d'un fichier YAML, offrant ainsi une configuration déclarative et lisible.

### Objectifs de release v1.0

**Lecture de données depuis différentes sources** : L'outil sera capable d'extraire des données à partir de diverses sources telles que des fichiers textuels, des fichiers JSON, XML, HTML, des bases de données relationnelles et des API.

**Transformation des données** : Les données extraites pourront être transformées selon divers critères, notamment le filtrage, la correction des données manquantes ou aberrantes, les calculs, la normalisation des valeurs et l'ajout d'attributs.

**Stockage des données dans différents formats** : Une fois transformées, les données pourront être stockées dans différents formats de sortie, tels que des bases de données relationnelles, des fichiers JSON ou XML.

## Gestion du projet

### Spécifications

**Durée** : 1 semaine

**Taille de l'Équipe** : 4 personnes

**Évaluation du temps de travail** : 1 semaine

**Liste fonctionnelle** :

Configuration :

- Création d'un fichier YAML pour décrire le pipeline de traitement des données.

Extraction de données :

- Lecture de données à partir de fichiers textuels (CSV, TXT, etc.).
- Extraction de données depuis des fichiers JSON, XML, et HTML.
- Connexion à des bases de données relationnelles (MySQL, PostgreSQL, etc.) pour extraire des données.
- Intégration avec des API pour récupérer des données distantes.
- Possibilité de lire des données depuis plusieurs sources simultanément.

Transformation de données :

- Filtrage des données selon des critères spécifiques (valeurs, conditions, etc.).
- Correction des données manquantes ou aberrantes.
  Calculs basés sur des attributs des jeux de données (somme, moyenne, etc.).
- Normalisation des valeurs pour uniformiser les formats.
- Ajout d'attributs calculés ou dérivés à partir des données existantes.

Chargement de données :

- Stockage des données transformées dans une base de données relationnelle (SQLite, etc.).
- Sauvegarde des données transformées dans des fichiers JSON ou XML.
- Possibilité de choisir le format de sortie en fonction des besoins spécifiques.
- Gestion de plusieurs formats de sortie simultanément si nécessaire.

**Outils** :

- [Trello](https://www.trello.com) (gestion des tâches)

- [Pandas](https://pandas.pydata.org/) (librairie de data analyse en python)

## Déroulement du projet

- Constitution de l'équipe
- Lecture et compréhension du brief
- Recherches sur le fonctionnement d'un ETL
- Définitions de tâches préliminaires au développement (mise en place et veille)
- Création d'un environnement de travail sur [Trello](https://www.trello.com)
- Mise en place des documents de support / livrables (Cahier des charges, documentation)
- Définition de l'architecture & fonctionnement du projet
- Choix des outils
- Découpage en tâches
- Écriture du code

## Documents
