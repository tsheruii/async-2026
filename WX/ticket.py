import sys  # Imports the sys module to access command-line arguments

def calculate_ticket_price(age):

    if age < 12:
        return 120  # Return 120 Baht

    elif age <= 60:
        return 200  # Return 200 Baht

    else:
        return 150  # Return 150 Baht


# Main function
def main():

    if len(sys.argv) > 1:

        test_age = int(sys.argv[-1])

        result = calculate_ticket_price(test_age)

        print(result)

    else:
        test_age = 25

        result = calculate_ticket_price(test_age)

        print(f"Age: {test_age} -> Ticket Price: {result} Baht")


if __name__ == "__main__":
    main()