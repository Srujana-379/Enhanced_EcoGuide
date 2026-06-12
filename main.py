from flask import Flask, render_template, request
from app.eco_logic import calculate_ecoscore, generate_recommendations
import json
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path('data/sample_profile.json')

def load_profile():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {'energy_kwh': 240, 'transport_km': 120, 'waste_kg': 18, 'water_liters': 4200, 'recycling': 2}

@app.route('/', methods=['GET', 'POST'])
def index():
    profile = load_profile()
    if request.method == 'POST':
        profile = {
            'energy_kwh': float(request.form.get('energy_kwh', 0)),
            'transport_km': float(request.form.get('transport_km', 0)),
            'waste_kg': float(request.form.get('waste_kg', 0)),
            'water_liters': float(request.form.get('water_liters', 0)),
            'recycling': float(request.form.get('recycling', 0)),
        }
    score = calculate_ecoscore(profile)
    tips = generate_recommendations(profile, score)
    return render_template('index.html', profile=profile, score=score, tips=tips)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)