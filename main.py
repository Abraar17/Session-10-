def calculate_ticket_price(miles):
    if miles >= 30:
        ticket_price = 12
    elif 20 <= miles <= 29:
        ticket_price = 10
    elif 10 <= miles <= 19:
        ticket_price = 8
    else:
        ticket_price = 5
    return ticket_price

total_ticket_price = 0

while True:
    user_input = input("calculate price? (Yes/No): ").strip().lower()
    if user_input != "yes":
        break  # Exit the loop if the user doesn't want to continue

    last_name = input("Enter your last name: ")
    miles = int(input("Enter miles from downtown Chicago: "))

    ticket_price = calculate_ticket_price(miles)
    total_ticket_price += ticket_price

    print(f"Ticket price for {last_name}: ${ticket_price}")

print(f"Total ticket price for all passengers: ${total_ticket_price}")