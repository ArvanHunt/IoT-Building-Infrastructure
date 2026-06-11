import time
import random
import json
import logging
import threading
from datetime import datetime
from flask import Flask, jsonify

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Flask app for health check
app = Flask(__name__)

# Building configurations
BUILDINGS = [
    {"id": "building-001", "name": "Tower A", "floors": 10},
    {"id": "building-002", "name": "Tower B", "floors": 8},
    {"id": "building-003", "name": "Tower C", "floors": 15},
]

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "sensor-simulator"}), 200

@app.route('/metrics')
def metrics():
    data = []
    for building in BUILDINGS:
        data.append(generate_sensor_data(building))
    return jsonify(data), 200

def generate_sensor_data(building):
    return {
        "building_id": building["id"],
        "building_name": building["name"],
        "timestamp": datetime.utcnow().isoformat(),
        "sensors": {
            "temperature": {
                "value": round(random.uniform(18.0, 28.0), 2),
                "unit": "celsius",
                "status": "normal"
            },
            "occupancy": {
                "value": random.randint(0, building["floors"] * 20),
                "unit": "people",
                "status": "normal"
            },
            "energy_consumption": {
                "value": round(random.uniform(100.0, 500.0), 2),
                "unit": "kwh",
                "status": "normal"
            },
            "air_quality": {
                "value": random.randint(0, 100),
                "unit": "aqi",
                "status": "normal"
            },
            "access_events": {
                "entries": random.randint(0, 50),
                "exits": random.randint(0, 50),
                "unauthorized_attempts": random.randint(0, 2)
            }
        }
    }

def simulate_sensors():
    logger.info("Starting IoT Building Sensor Simulator...")
    logger.info(f"Monitoring {len(BUILDINGS)} buildings")

    while True:
        for building in BUILDINGS:
            data = generate_sensor_data(building)
            logger.info(f"Building: {data['building_name']} | "
                       f"Temp: {data['sensors']['temperature']['value']}°C | "
                       f"Occupancy: {data['sensors']['occupancy']['value']} people | "
                       f"Energy: {data['sensors']['energy_consumption']['value']} kWh | "
                       f"AQI: {data['sensors']['air_quality']['value']}")

            if data['sensors']['temperature']['value'] > 26.0:
                logger.warning(f"HIGH TEMPERATURE ALERT: {data['building_name']} - "
                              f"{data['sensors']['temperature']['value']}°C")

            if data['sensors']['air_quality']['value'] > 80:
                logger.warning(f"POOR AIR QUALITY ALERT: {data['building_name']} - "
                              f"AQI: {data['sensors']['air_quality']['value']}")

            if data['sensors']['access_events']['unauthorized_attempts'] > 0:
                logger.warning(f"SECURITY ALERT: {data['building_name']} - "
                              f"Unauthorized access attempts: "
                              f"{data['sensors']['access_events']['unauthorized_attempts']}")

        logger.info("---")
        time.sleep(5)

if __name__ == "__main__":
    # Run sensor simulation in background thread
    sensor_thread = threading.Thread(target=simulate_sensors, daemon=True)
    sensor_thread.start()

    # Run Flask app
    logger.info("Starting HTTP server on port 8080...")
    app.run(host='0.0.0.0', port=8080)