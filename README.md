# 📚 Système de Feedback sur des Produits Numériques [ Feedback Gate ]

> API RESTful en Python pour la gestion des retours utilisateurs sur des produits numériques.

## 🧾 Description

Ce projet implémente un système permettant de collecter, stocker et consulter les avis d'utilisateurs sur des produits numériques via une API REST.  
Il est développé en **Python** avec le framework **Flask** et utilise une base de données **SQLite** pour la persistance des données.

## 🔧 Technologies Utilisées

- **Python 3.x**
- **Flask** – Framework léger pour construire l'API
- **Flask-SQLAlchemy** – ORM pour interagir avec la base de données
- **SQLite** – Base de données locale simple et sans serveur
- **JSON** – Format d'échange standardisé
- **HTTP** – Protocole utilisé pour les requêtes

## 📁 Structure du Projet

```
product-feedback-api/
│
├── app.py                # Point d'entrée de l'application Flask
├── models.py             # Définition des modèles SQLAlchemy
├── database.db           # Base de données SQLite (générée automatiquement)
├── README.md             # Ce fichier
└── examples/
    └── sample_requests.sh  # Exemples de requêtes cURL
```

## 🛠️ Fonctionnalités (Endpoints)

| Méthode | Chemin                        | Description                             |
|--------|-------------------------------|-----------------------------------------|
| POST   | `/users`                      | Créer un utilisateur                    |
| POST   | `/products`                   | Créer un produit                        |
| POST   | `/feedback`                   | Soumettre un feedback                   |
| GET    | `/feedback`                   | Obtenir tous les feedbacks              |
| GET    | `/products/<id>/feedback`     | Obtenir les feedbacks d’un produit      |
| GET    | `/users/<id>/feedback`        | Obtenir les feedbacks d’un utilisateur  |
| DELETE | `/feedback/<id>`              | Supprimer un feedback spécifique        |

## 🚀 Lancement du Projet

### Étape 1 : Installer les dépendances

```bash
pip install flask flask-sqlalchemy
```

### Étape 2 : Lancer l'application

```bash
python app.py
```

Le serveur sera accessible à l’adresse : `http://localhost:5000`

La base de données `database.db` sera générée automatiquement dans le répertoire racine.

---

## 🧪 Exemples de Requêtes

### 📥 Ajouter un utilisateur

```bash
curl -X POST http://localhost:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name":"Alice", "email":"alice@example.com"}'
```

### 📥 Ajouter un produit

```bash
curl -X POST http://localhost:5000/products \
     -H "Content-Type: application/json" \
     -d '{"name":"App A", "description":"Une application incroyable"}'
```

### 📥 Soumettre un feedback

```bash
curl -X POST http://localhost:5000/feedback \
     -H "Content-Type: application/json" \
     -d '{"user_id":1, "product_id":1, "rating":5, "comment":"Très bon produit!"}'
```

### 📤 Récupérer tous les feedbacks

```bash
curl http://localhost:5000/feedback
```

### 🗑️ Supprimer un feedback

```bash
curl -X DELETE http://localhost:5000/feedback/1
```

---

## 🧼 Bonnes Pratiques Suivies

- ✅ Code organisé et propre
- ✅ Utilisation de **SQLAlchemy** pour l’accès aux données
- ✅ Gestion des erreurs HTTP bien définie
- ✅ Validation basique des entrées
- ✅ Facile à étendre (ajout de filtres, authentification, etc.)

---

## 🧩 Idées d’Améliorations Possibles

- 🔐 Ajouter l'authentification JWT
- 📊 Calculer la note moyenne par produit
- 📦 Passer à PostgreSQL ou MySQL
- 🧪 Ajouter des tests unitaires avec `pytest`
- 🐳 Containeriser avec Docker
- ☁️ Déployer sur Heroku, Render ou AWS Lightsail

---

## 👨‍💻 Auteur

**Jemai Abed El Mortadha**  
📧 Email: jemaimortadha@gmail.com  
🏫 Université: TEK-UP

---

## 📢 Remerciements

Merci à notre professeur Mohamed Amine Ben Rhouma pour ce projet enrichissant !

---
