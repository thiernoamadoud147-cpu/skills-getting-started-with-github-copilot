"""
API du système de gestion du lycée

Une application FastAPI très simple qui permet aux élèves de consulter les
activités extrascolaires du lycée de Mergington et de s’y inscrire.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="API du lycée de Mergington",
              description="API pour consulter les activités extrascolaires et s’y inscrire")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Apprendre des stratégies et participer à des tournois d’échecs",
        "schedule": "Vendredis, de 15 h 30 à 17 h",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Apprendre les bases de la programmation et créer des projets logiciels",
        "schedule": "Mardis et jeudis, de 15 h 30 à 16 h 30",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Éducation physique et activités sportives",
        "schedule": "Lundis, mercredis et vendredis, de 14 h à 15 h",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Développer ses compétences en basketball et participer à des matchs",
        "schedule": "Mardis et jeudis, de 16 h à 17 h 30",
        "max_participants": 15,
        "participants": []
    },
    "Swimming Club": {
        "description": "Améliorer ses techniques de natation et son endurance",
        "schedule": "Lundis et mercredis, de 16 h à 17 h",
        "max_participants": 20,
        "participants": []
    },
    "Art Club": {
        "description": "Explorer le dessin, la peinture et différentes techniques artistiques",
        "schedule": "Mercredis, de 15 h 30 à 17 h",
        "max_participants": 15,
        "participants": []
    },
    "Drama Club": {
        "description": "Développer son expression scénique et jouer des pièces de théâtre",
        "schedule": "Jeudis, de 15 h 30 à 17 h",
        "max_participants": 20,
        "participants": []
    },
    "Science Club": {
        "description": "Réaliser des expériences et découvrir les sciences",
        "schedule": "Lundis, de 15 h 30 à 17 h",
        "max_participants": 18,
        "participants": []
    },
    "Debate Club": {
        "description": "Développer son esprit critique et ses compétences en argumentation",
        "schedule": "Vendredis, de 15 h 30 à 17 h",
        "max_participants": 16,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Inscrire un élève à une activité."""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activité introuvable")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="L’élève est déjà inscrit(e)")

    # Add student
    activity["participants"].append(email)
    return {"message": f"{email} est inscrit(e) à l’activité {activity_name}"}


@app.delete("/activities/{activity_name}/signup")
def unregister_from_activity(activity_name: str, email: str):
    """Désinscrire un élève d’une activité."""
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activité introuvable")

    activity = activities[activity_name]
    if email not in activity["participants"]:
        raise HTTPException(status_code=404, detail="Élève non inscrit(e) à cette activité")

    activity["participants"].remove(email)
    return {"message": f"{email} a été désinscrit(e) de l’activité {activity_name}"}
