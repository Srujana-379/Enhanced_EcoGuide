def calculate_ecoscore(profile):
    energy = max(0, 100 - profile['energy_kwh'] / 4)
    transport = max(0, 100 - profile['transport_km'] / 3)
    waste = max(0, 100 - profile['waste_kg'] * 2)
    water = max(0, 100 - profile['water_liters'] / 60)
    recycling = min(100, profile['recycling'] * 12)
    return round((energy + transport + waste + water + recycling) / 5, 1)

def generate_recommendations(profile, score):
    tips = []
    if profile['energy_kwh'] > 200:
        tips.append('Use LED bulbs and switch off idle devices.')
    if profile['transport_km'] > 80:
        tips.append('Choose public transport, cycling, or carpooling more often.')
    if profile['waste_kg'] > 10:
        tips.append('Carry reusable bags and reduce single-use packaging.')
    if profile['water_liters'] > 3000:
        tips.append('Fix leaks and take shorter showers to save water.')
    if profile['recycling'] < 3:
        tips.append('Separate dry waste and recycle consistently.')
    if score >= 80:
        tips.append('Great job! Keep improving with small daily habits.')
    elif score >= 60:
        tips.append('You are on track, but a few changes can raise your score.')
    else:
        tips.append('Start with one habit at a time and build a routine.')
    return tips