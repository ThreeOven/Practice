import io_manager
import ai_manager
import logic_manager
import data_manager

def start_app():
    # Load past records on startup
    history = data_manager.load_all_quotes()
    print(f"System ready. Total past quotes saved: {len(history)}")

    while True:
        # Step 1: Input
        user_inputs = io_manager.get_user_input()

        # Step 2: AI Processing
        ai_outputs = ai_manager.analyze_request(user_inputs['request_text'])

        # Step 3: Business Logic
        quote_record = logic_manager.calculate_quote(user_inputs, ai_outputs)

        # Step 4: Save Data
        data_manager.save_quote(quote_record)

        # Step 5: Output Receipt
        io_manager.print_receipt(quote_record)

        again = input("Create another quote? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    start_app()