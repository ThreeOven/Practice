def get_user_input():
    print("\n--- ON-SITE RENOVATION QUOTATION ---")
    
    # Property type validation
    prop_type = input("Enter Property Type (HDB/Condo/Landed): ").strip().upper()
    while prop_type not in ["HDB", "CONDO", "LANDED"]:
        prop_type = input("Invalid! Enter HDB, Condo, or Landed: ").strip().upper()

    # Request text
    request_text = input("Enter Renovation Request: ").strip()
    while not request_text:
        request_text = input("Request cannot be empty. Enter Request: ").strip()

    # Measurements validation
    length = get_valid_number("Enter Room Length (m): ")
    width = get_valid_number("Enter Room Width (m): ")

    return {
        "property_type": prop_type,
        "request_text": request_text,
        "length": length,
        "width": width
    }

def get_valid_number(prompt_text):
    while True:
        try:
            val = float(input(prompt_text))
            if val > 0:
                return val
            print("Must be greater than 0.")
        except ValueError:
            print("Invalid number format! Enter a number.")

def print_receipt(record):
    print("\n" + "="*40)
    print("         OFFICIAL QUOTATION")
    print("="*40)
    print(f"Property:  {record['property_type']}")
    print(f"Request:   {record['request_text']}")
    print(f"Area:      {record['area']} sqm")
    print("-" * 40)
    print(f"AI Tasks:  {', '.join(record['ai_tasks'])}")
    print(f"Materials: {', '.join(record['ai_materials'])}")
    print("-" * 40)
    print(f"Material Cost (incl 10% waste): ${record['material_cost']:.2f}")
    print(f"Labor Cost:                     ${record['labor_cost']:.2f}")
    print(f"HDB Permit Surcharge:           ${record['surcharges']:.2f}")
    print("-" * 40)
    print(f"TOTAL COST:                     ${record['total_cost']:.2f}")
    print(f"STATUS:                         {record['status']}")
    print("="*40 + "\n")