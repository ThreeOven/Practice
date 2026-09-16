def calculate_quote(user_data, ai_data):
    # 1. Base Dimensions & Costs
    area = user_data['length'] * user_data['width']
    raw_material_cost = area * 50.0  # $50/sqm
    base_labor_cost = area * 40.0     # $40/sqm

    # 2. Rule 1: 10% Material Waste Buffer
    buffered_material_cost = raw_material_cost * 1.10

    # 3. Rule 2: HDB Wall Hacking Surcharge
    surcharges = 0.0
    if user_data['property_type'] == "HDB" and "Wall Hacking" in ai_data['tasks']:
        surcharges = 300.0  # $300 Permit Fee

    # 4. Rule 3: Safety/Complexity Multiplier
    labor_multiplier = 1.0
    status = "APPROVED_ON_SITE"
    if ai_data['has_safety_hazard'] or ai_data['complexity'] >= 4:
        labor_multiplier = 1.25  # 25% extra labor pay
        status = "REQUIRES_ENGINEER_APPROVAL"

    final_labor_cost = base_labor_cost * labor_multiplier
    total_cost = buffered_material_cost + final_labor_cost + surcharges

    return {
        "property_type": user_data['property_type'],
        "request_text": user_data['request_text'],
        "area": area,
        "ai_tasks": ai_data['tasks'],
        "ai_materials": ai_data['materials'],
        "material_cost": buffered_material_cost,
        "labor_cost": final_labor_cost,
        "surcharges": surcharges,
        "total_cost": total_cost,
        "status": status
    }