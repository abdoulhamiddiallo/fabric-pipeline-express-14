"""Génère les demandes de réservation pour la visite de Machu Picchu du lundi 2 novembre 2026 (données fictives).

Un seul CSV : une ligne par demande d'agence, avec le circuit voulu et la taille du groupe.
Les capacités des circuits sont fixées pour l'exercice ; la demande les dépasse, il faudra arbitrer.
"""
import csv, random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(1414)
OUT = Path(__file__).resolve().parent.parent / "data" / "requests"
OUT.mkdir(parents=True, exist_ok=True)

CIRCUITS = [("C1 Terrasse haute", 0.27), ("C2 Classique", 0.42), ("C3 Huayna Picchu", 0.13), ("C4 Montagne", 0.18)]
AGENCIES = ["Andes Vivas", "Cusco Raymi Tours", "Inti Trek", "Valle Sagrado Viajes", "Qorikancha Travel", "Ollantay Expediciones",
            "Pachamama Routes", "Urubamba Explorer", "Condor Pass", "Salkantay Partners", "Wayna Tours", "Puno Andina"]
ORIGINS = ["Pérou", "États-Unis", "France", "Allemagne", "Brésil", "Chili", "Japon", "Espagne", "Mexique", "Royaume-Uni", "Canada", "Argentine"]
rows, t = [], datetime(2026, 10, 1, 8, 0, 0)
for i in range(1, 431):
    t += timedelta(minutes=random.randint(20, 160))
    circuit = random.choices([c for c, _ in CIRCUITS], [w for _, w in CIRCUITS])[0]
    rows.append([140000 + i, random.choice(AGENCIES), random.choice(ORIGINS), circuit, random.choice([2, 2, 4, 6, 8, 10, 12, 14, 16]), t.strftime("%Y-%m-%d %H:%M:%S")])
with open(OUT / "requests_2026-11-02.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["request_id", "agency", "origin_country", "circuit", "visitors", "requested_at"]); w.writerows(rows)
print(len(rows), "demandes,", sum(r[4] for r in rows), "visiteurs")
