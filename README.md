# Web scraping avec Selenium
 
 ## Objectif

L'objectif de ce projet est d'utiliser un outil de web scraping et le combiner avec une base de données afin de faire de la data viz avec des données récolté sur internet.

J'ai fais le choix de tout utiliser en containers avec Selenium pour le scraping, PostgreSQL pour la base et Grafana pour la data viz. Le tout est hébergé sur une VM Google Cloud.

## Mise en place du docker-compose

Afin de créer l'intégralité des containers et du réseau avec une seule commande nous utilisons le fichier [docker-compose](/docker-compose.yml). Il contient les informations pour chaque containers.

Pour lancer le docker-compose il faut utilise la commande `docker-compose up -d`,  cela va lancer la création et le lancement des 2 containers.

### Scraping

J'ai fais le choix de récupérer le cours de multiples cryptomonnaies sur le site [CoinCap](https://coincap.io/) à l'aide du module Selenium.
Pour ce faire j'ai deux scripts python, chacun en container. Il s'agit de scraper et saver.
- Le script `scraper` utilise Selenium pour récupérer les données du site grace aux balises HTML et les stocker dans un fichier json toutes les 10 secondes
- Le script `saver` s'occupe de charger les fichiers json afin de les insérer dans la base PostgreSQL toutes les 30 secondes

### PostgreSQL

Afin de créer la table à la création du containers j'utilise un volume pour lier le fichier SQL avec le dossier `docker-entrypoint-initdb.d` du container.
Ce script va être exécuté au lancement du docker-compose et créer la table `data`.

### Grafana

Afin de charger la datasource et le dashboard à la création du container il faut utiliser des volumes pour se servir des dossier `datasources` et `dashboards` à l'initialisation de grafana.

- Le dossier datasources contient un fichier [datasource.yml](/grafana/datasources/datasource.yml) qui défini toutes les informations de connection à la base de données PostgreSQL
- Le dossier dashboards contient un fichier [dashboard.yml](/grafana/dashboards/dashboard.yml) qui contient les informations de création du dashboards ainsi qu'un fichier [dashboard.json](/dashboards/dashboard.json) qui contient les informations des graph.

Le fichier [docker-compose](/docker-compose.yml) contient aussi des variables d'environnement pour définir le dashboard par défaut et ajouter un profil viewer.

## Accéder à Grafana

Pour accéder à Grafana il faut se rendre sur [localhost:80](http://127.0.0.1:80) (ou [13.36.87.26](http://http://104.199.52.73/) pour la version sur Google Cloud)
L'accès est en view only mais il est possible de se connecter avec les identifiants par défaut qui sont:

- `user: admin`
- `password: admin` 

On peut donc visualiser les deux graph actualisé en temps réel qui sont:

- Le cours du Bitcoin 
- Le cours de l'Etherum

![image](/dashboard.png)
