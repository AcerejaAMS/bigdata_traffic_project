import random
import csv

rows = 1000000  # Puede subir

with open("traffic_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sensor_id", "event_time", "location", "speed", "vehicle_count"])

    for i in range(rows):
        sensor_id = random.randint(1, 50)
        timestamp = f"2025-01-{random.randint(1,30)} {random.randint(0,23)}:00:00"
        location = random.choice(["Norte", "Sur", "Este", "Oeste", "Centro"])
        speed = random.uniform(5, 120)
        vehicles = random.randint(1, 200)

        writer.writerow([sensor_id, timestamp, location, speed, vehicles])
