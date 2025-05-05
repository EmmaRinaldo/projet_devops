# 📚 BookReview API

Une API REST simple développée avec **FastAPI** pour gérer une collection de livres. Elle permet d’ajouter, lister, rechercher et supprimer des livres, avec une note et un commentaire.


## Sommaire
- [Introduction](#introduction)
- [Pré-requis & Installation](#pré-requis--installation)
- [Choix des technologies](#choix-des-technologies)
- [Architecture](#architecture)
- [Schéma d'architecture](#schema-darchitecture)
- [Endpoints](#endpoints)


## Pré-requis & Installation

### Prérequis

Avant d’installer le projet, assurez-vous d’avoir :
- Python 3.10+
- `pip`
- Docker & Docker Compose

---

### Étapes d'installation

```bash
# 1. Cloner le projet
git clone https://github.com/EmmaRinaldo/projet_devops.git
cd bookreview-api

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l’API en local
uvicorn app.main:app --reload

```

---

### Supervision avec Prometheus + Grafana + Loki

```bash
# 4. Démarrer l’écosystème d’observabilité
docker-compose up -d
```

Lancement de :
- **Prometheus** : scrape les métriques exposées par FastAPI
- **Grafana** : dashboard visuel pour analyser les performances
- **Loki** : collecte les logs applicatifs
- **Promtail** : envoie les logs à Loki

Accès aux interfaces :
- Prometheus : http://localhost:9090
- Grafana : http://localhost:3000 (Identifiants : `admin` / `admin`)
- Loki : http://localhost:3100


### Tests

```bash
# Exécuter la suite de tests
pytest --cov=app
```


## Choix des technologies

| Outil / Techno              | Rôle |
|-----------------------------|------|
| **FastAPI**                 | Framework Web pour la création d'API modernes |
| **Pydantic**                | Validation des données avec les modèles |
| **Uvicorn**                 | Serveur ASGI ultra-rapide |
| **pytest / pytest-cov**     | Framework de tests unitaires et couverture |
| **Prometheus**              | Collecte des métriques applicatives |
| **Grafana**                 | Visualisation des métriques |
| **Loki / Promtail**         | Centralisation et visualisation des logs |


## Architecture

```
├── .github/ 
│   └── workflows/
│       ├── docker.yml       # CI/CD : Build d’image Docker
│       └── test.yml         # CI : Exécution des tests pytest
├── app/ 
│   ├── database.py          # Stockage temporaire des livres (liste Python)
│   ├── main.py              # Points d’entrée de l’API FastAPI
│   └── models.py            # Modèles Pydantic utilisés pour la validation des données
├── tests/
│   └── test_main.py         # Tests unitaires avec pytest
├── docker-compose.yml       # Supervision (Prometheus, Grafana, Loki)
├── requirements.txt         # Dépendances du projet
├── README.md                # Documentation du projet
```


## Schéma d'architecture

```
                        +---------------------+
                        |     Développeur     |
                        +----------+----------+
                                   |
                          Push / Pull Request
                                   |
                        +----------v----------+
                        |   GitHub Actions    |
                        |  (.github/workflows)|  
                        +----+----------+-----+
                             |          |
                  +----------v--+    +--v-----------+
                  | Tests unit. |    | Build Docker |
                  |  (pytest)   |    |   (docker.yml)|
                  +-------------+    +---------------+
                             |
        ------------------------------------------
                             |
             (Exécution locale ou en prod)
                             |
                     +-------v-------+
                     |   Client API  |
                     +-------+-------+
                             |
                   +---------v----------+
                   |     FastAPI        |
                   |   (main.py)        |
                   +----+----------+----+
                        |          |
              +---------v+        +v---------+
              | Validation|        | Routing |
              | (models)  |        | (main)  |
              +-----------+        +---------+
                     |                  |
             +-------v------------------v-------+
             |  Stockage temporaire (database)  |
             +----------------+-----------------+
                              |
      +-----------------------v------------------------+
      |  Exportation de métriques (/metrics Prometheus)|
      +----------------+------------------------------+
                       |
             +---------v--------+     +-------------+
             |   Prometheus     |<--->|   Grafana   |
             +------------------+     +-------------+
                       ↑
             +---------v--------+
             |     Loki         |
             +--------^---------+
                      |
             +--------v--------+
             |   Promtail      |
             |  (logs API)     |
             +-----------------+
```


## Endpoints

| Méthode | Endpoint             | Description                           |
|---------|----------------------|---------------------------------------|
| GET     | `/`                  | Message d'accueil                     |
| POST    | `/books`             | Ajouter un livre                      |
| GET     | `/books`             | Lister tous les livres                |
| GET     | `/books/{title}`     | Obtenir les infos d’un livre par titre|
| DELETE  | `/books/{title}`     | Supprimer un livre par titre          |

### Exemple JSON (POST `/books`)
    
```json
{
  "title": "1865",
  "author": "Lewis Carroll",
  "rating": 5,
  "comment": "Embark on a delightful adventure with Lewis Carroll's 'Alice's Adventures in Wonderland.' This timeless classic whisks readers away into a fantastical realm where nothing is quite as it seems..."
}
```