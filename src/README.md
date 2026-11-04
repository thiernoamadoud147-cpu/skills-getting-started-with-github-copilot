# API des activités du lycée de Mergington

Une application FastAPI très simple qui permet aux élèves de consulter les activités extrascolaires et de s’y inscrire.

## Fonctionnalités

- Consulter toutes les activités extrascolaires disponibles
- S’inscrire à des activités

## Démarrage

1. Installez les dépendances :

   ```
   pip install fastapi uvicorn
   ```

2. Lancez l’application :

   ```
   python app.py
   ```

3. Ouvrez votre navigateur et accédez à :
   - Documentation de l’API : http://localhost:8000/docs
   - Documentation alternative : http://localhost:8000/redoc

## Points de terminaison de l’API

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Obtenir toutes les activités, leurs détails et le nombre actuel de participants |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Inscrire un élève à une activité                                   |

## Modèle de données

L’application utilise un modèle de données simple avec des identifiants explicites :

1. **Activités** — Le nom de l’activité sert d’identifiant :

   - Description
   - Horaires
   - Nombre maximal de participants autorisés
   - Liste des adresses e-mail des élèves inscrits

2. **Élèves** — L’adresse e-mail sert d’identifiant :
   - Nom
   - Niveau scolaire

Toutes les données sont stockées en mémoire ; elles sont donc réinitialisées au redémarrage du serveur.
