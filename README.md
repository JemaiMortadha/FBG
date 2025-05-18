---

# 📚 Système de Feedback sur des Produits Numériques [GraphQL]

> Un service web basé sur **GraphQL** pour collecter et gérer les avis utilisateurs sur des produits numériques.

## 🎯 Description
Ce projet implémente un système permettant aux utilisateurs de laisser des commentaires et des notes sur des produits numériques après leur utilisation. Il est conçu comme une API GraphQL simple et fonctionnelle, idéale pour un projet universitaire ou une démonstration technique.

---

## 🛠 Technologies Utilisées

| Technologie | Rôle |
|------------|------|
| **Python** | Langage principal |
| **FastAPI** | Framework web asynchrone |
| **Strawberry** | Bibliothèque GraphQL moderne |
| **In-Memory Storage** | Stockage temporaire des données (facile à remplacer par SQLite ou PostgreSQL) |

---

## 🧪 Fonctionnalités

L'API GraphQL supporte les opérations suivantes :

| Opération | Type | Description |
|----------|------|-------------|
| `createFeedback` | Mutation | Ajoute un nouveau feedback avec un commentaire et une note |
| `feedbacks` | Query | Liste tous les feedbacks |
| `feedbackByUser(userId: ID!)` | Query | Liste tous les feedbacks d’un utilisateur spécifique |
| `feedbackByProduct(productId: ID!)` | Query | Liste tous les feedbacks d’un produit spécifique |
| `deleteFeedback(id: ID!)` | Mutation | Supprime un feedback par son ID |

---

## 🚀 Comment Exécuter le Projet

### 1. Installer les Dépendances

```bash
pip install fastapi strawberry-graphql uvicorn
```

> Vous pouvez aussi utiliser `requirements.txt` si vous en avez un.

### 2. Lancer le Serveur

```bash
uvicorn main:app --reload
```

Le serveur sera accessible à l’adresse :  
👉 [http://localhost:8000/graphql](http://localhost:8000/graphql)

Cela ouvre l’interface interactive **GraphiQL** où vous pouvez tester vos requêtes/mutations.

---

## 🧾 Exemples d'utilisation

### A. Créer un Feedback

```graphql
mutation {
  createFeedback(input: {
    userId: "1",
    productId: "2",
    rating: 5,
    comment: "Incroyable produit !"
  }) {
    id
    comment
    rating
    date
  }
}
```

### B. Obtenir Tous les Feedbacks

```graphql
query {
  feedbacks {
    id
    userId
    productId
    rating
    comment
    date
  }
}
```

### C. Obtenir les Feedbacks par Produit

```graphql
query {
  feedbackByProduct(productId: "2") {
    id
    rating
    comment
    date
  }
}
```

### D. Supprimer un Feedback

```graphql
mutation {
  deleteFeedback(id: 0)
}
```

---

## 📁 Structure du Projet

```
product-feedback-graphql/
│
├── main.py                # Point d'entrée FastAPI
├── schema.py              # Schéma GraphQL et résolveurs
├── models.py              # Modèles de données (classes Python)
├── database.py            # Gestion des données en mémoire
└── README.md              # Ce fichier
```

---

## 🧩 Modèles de Données

### `User`
```python
id: str
name: str
email: str
```

### `Product`
```python
id: str
name: str
description: str
```

### `Feedback`
```python
id: int
userId: str
productId: str
rating: int
comment: str
date: str (ISO format)
```

---

## 📌 Documentation GraphQL

Une fois le serveur lancé, vous pouvez explorer le schéma complet via l’interface GraphiQL à l’URL suivante :

🔗 [http://localhost:8080/graphql](http://localhost:8080/graphql)

---

## 📬 Contact

Si vous avez des questions ou besoin d’aide, n’hésitez pas à me contacter !

- **GitHub**: JemaiMortadha
- **Email**: jemaimortadha@gmail.com

---

## ✅ Remerciements

Merci à notre enseignant pour ce cahier des charges clair. Ce projet répond pleinement aux critères pédagogiques demandés.

---

## 📥 Téléchargement et Installation Rapide

```bash
git clone https://github.com/votrenom/votre-projet.git
cd votre-projet
pip install -r requirements.txt  # Si applicable
uvicorn main:app --reload
```

---

