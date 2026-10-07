import json
import random
from datetime import datetime, timedelta

print("🤖 Iniciando Motor de Simulación Demoscópica Completo...")

encuestadoras = ["Sigma Dos", "SocioMétrica", "40dB", "NC Report", "CIS", "GAD3"]

base = {
    "PP": 33.5, "PSOE": 29.5, "VOX": 11.5, "SUMAR": 6.5, "PODEMOS": 3.0,
    "MAS MADRID": 1.5, "ADELANTE": 0.5, "ERC": 1.8, "JUNTS": 1.7, "EH BILDU": 1.5,
    "PNV": 1.1, "BNG": 0.8, "CC": 0.4, "UPN": 0.2, "CHA": 0.1, "OTROS": 2.0
}

encuestas = []
# Fijamos la fecha a hoy (7 de octubre de 2026)
fecha_actual = datetime.now()

for i in range(40):
    encuesta = {
        "f": fecha_actual.strftime("%Y-%m-%d"),
        "c": random.choice(encuestadoras),
        "d": {k: round(v, 1) for k, v in base.items()}
    }
    encuestas.append(encuesta)

    # Vamos restando días para generar el pasado
    fecha_actual -= timedelta(days=random.randint(2, 6))

    base["PP"] += random.uniform(-0.5, 0.4)
    base["PSOE"] += random.uniform(-0.4, 0.5)
    base["VOX"] += random.uniform(-0.25, 0.2)
    base["SUMAR"] += random.uniform(-0.2, 0.2)
    
    for p in base:
        if p not in ["PP", "PSOE", "VOX", "SUMAR"]:
            base[p] += random.uniform(-0.05, 0.05)
        base[p] = max(0.1, round(base[p], 1))

encuestas.reverse()

with open('datos_encuestas.json', 'w', encoding='utf-8') as f:
    json.dump(encuestas, f, ensure_ascii=False, indent=4)
    
print(f"✅ ¡Éxito! Base de datos inicializada.")
