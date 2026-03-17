from PySide6.QtWidgets import QApplication
import subprocess
import json
import os

def load_stylesheet(app, theme):
    base_dir = os.path.dirname(__file__)
    style_path = os.path.join(base_dir, "styles", f"{theme}.qss")

    with open(style_path, "r") as f:
        app.setStyleSheet(f.read())

def set_light_theme(self):
    load_stylesheet(QApplication.instance(), "light")

def set_dark_theme(self):
    load_stylesheet(QApplication.instance(), "dark")

def extract_sensors():
    result = subprocess.run(["sensors", "-j"], capture_output=True, text=True)
    return json.loads(result.stdout)

def extract_temperatures(sensor_data):
    temps = []

    for chip_name, chip_data in sensor_data.items():
        if not isinstance(chip_data, dict):
            continue

        adapter = chip_data.get("Adapter", "Unknown")

        for feature_name, feature_data in chip_data.items():
            if feature_name == "Adapter":
                continue

            if not isinstance(feature_data, dict):
                continue

            for key, value in feature_data.items():
                if key.endswith("_input"):
                    temps.append({
                        "chip": chip_name,
                        "adapter": adapter,
                        "feature": feature_name,
                        "label": key,
                        "value": value
                    })
    return temps