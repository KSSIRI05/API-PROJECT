# API de Gestion des Tâches

Une API RESTful pour la gestion des tâches, construite avec **FastAPI** et **MongoDB**.

## 🛠️ Technologies

- **FastAPI** - Framework web Python moderne
- **MongoDB** - Base de données NoSQL (via Beanie ODM)
- **Docker** - Conteneurisation
- **Pytest** - Tests unitaires

## 📋 Fonctionnalités

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/v1/tasks` | Liste toutes les tâches |
| GET | `/api/v1/task/{id}` | Récupère une tâche par ID |
| POST | `/api/v1/tasks` | Crée une nouvelle tâche |
| PUT | `/api/v1/task/{id}` | Met à jour une tâche (complet) |
| PATCH | `/api/v1/task/{id}` | Met à jour une tâche (partiel) |
| DELETE | `/api/v1/task/{id}` | Supprime une tâche |

## 🚀 Installation locale

### Prérequis

- Python 3.13+
- MongoDB (local ou cloud)

### Configuration

1. **Cloner le projet**
```bash
git clone <repo-url>
cd APIproject
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**

Créer un fichier `.env` à la racine :
```env
MONGO_URI=mongodb://localhost:27017
```

5. **Lancer le serveur**
```bash
uvicorn src.main:app --reload
```

L'API sera disponible sur `http://localhost:8000`

## 🐳 Docker

### Construire et exécuter

```bash
docker build -t api-tasks .
docker run -p 8080:8080 api-tasks
```

### Avec Docker Compose

```bash
docker compose up --build
```

## 📖 Documentation API

Une fois le serveur lancé :
- **Swagger UI** : http://localhost:8000/docs
- **ReDoc** : http://localhost:8000/redoc

## ✅ Tests

```bash
pytest
```

## 📁 Structure du projet

```
APIproject/
├── src/
│   ├── main.py              # Point d'entrée FastAPI
│   ├── config/
│   │   └── configuration.py # Configuration MongoDB
│   ├── models/
│   │   └── task.py          # Modèle Beanie
│   ├── routes/
│   │   └── task.py          # Endpoints API
│   └── schema/
│       └── task.py          # Schémas Pydantic
├── test_api.py              # Tests pytest
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🔧 Variables d'environnement

| Variable | Description | Défaut |
|----------|-------------|--------|
| `MONGO_URI` | URI de connexion MongoDB | `mongodb://localhost:27017` |

## 📝 Licence

MIT