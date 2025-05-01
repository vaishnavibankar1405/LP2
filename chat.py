class Chatbot:
    def __init__(self):
        self.products = {
            1: "Laptop: High performance laptop with 16GB RAM, 512GB SSD, and Intel i7 processor.",
            2: "Smartphone: Latest smartphone with 128GB storage, 6GB RAM, and 48MP camera.",
            3: "Headphones: Wireless noise-cancelling headphones with 20 hours of battery life."
        }
        self.faqs = {
            1: "How do I place an order? - You can place an order by choosing a product and specifying the quantity.",
            2: "What payment methods are accepted? - We accept credit/debit cards and PayPal.",
            3: "Can I return a product? - Yes, you can return products within 30 days of purchase."
        }

    def greet_user(self):
        print("Hello! I'm your friendly chatbot assistant. How can I help you today?")

    def show_menu(self):
        print("\nPlease choose an option by entering the corresponding number:")
        print("1. Show me the products")
        print("2. FAQ")
        print("3. Place an order")
        print("4. Exit")

    def show_products(self):
        print("Here are some products we offer:")
        for product_num, description in self.products.items():
            print(f"{product_num}. {description}")
        self.await_confirmation()

    def help_user(self):
        print("I can assist you with the following:")
        print("1. Show me the products")
        print("2. FAQ")
        print("3. Place an order")
        print("4. Exit")
        self.await_confirmation()

    def provide_product_info(self, product_number):
        if product_number in self.products:
            print(self.products[product_number])
        else:
            print("Sorry, that's not a valid product number.")
        self.await_confirmation()

    def place_order(self):
        print("To place an order, please let me know the product number and quantity.")
        try:
            product_number = int(input("Product Number: "))
            if product_number in self.products:
                quantity = int(input("Quantity: "))
                print(f"Your order for {quantity} {self.products[product_number].split(':')[0]}(s) has been placed!")
            else:
                print("Sorry, we don't have that product available.")
        except ValueError:
            print("Invalid input. Please try again.")
        self.await_confirmation()

    def faq(self):
        print("Frequently Asked Questions:")
        for number, faq in self.faqs.items():
            print(f"{number}. {faq.split(' - ')[0]}")  # Show only the question part
        try:
            faq_number = int(input("\nEnter the number of the FAQ you'd like to know more about: "))
            if faq_number in self.faqs:
                print(self.faqs[faq_number])
            else:
                print("Sorry, that's not a valid FAQ number.")
        except ValueError:
            print("Please enter a valid number.")
        self.await_confirmation()

    def await_confirmation(self):
        while True:
            user_input = input("\nType 'OK' to continue or 'exit' to end the conversation: ").lower()
            if user_input == 'ok':
                break
            elif user_input == 'exit':
                print("Goodbye! Have a great day!")
                exit()
            else:
                print("Sorry, I didn't understand that. Please type 'OK' to continue or 'exit' to end the conversation.")

    def handle_input(self, user_input):
        try:
            user_input = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            return True

        if user_input == 1:
            self.show_products()
        elif user_input == 2:
            self.faq()
        elif user_input == 3:
            self.place_order()
        elif user_input == 4:
            print("Goodbye! Have a great day!")
            return False
        else:
            print("Sorry, that's not a valid option. Please enter a valid number to choose an option.")
        return True

def main():
    chatbot = Chatbot()
    chatbot.greet_user()
    while True:
        chatbot.show_menu()
        user_input = input("You: ")
        if not chatbot.handle_input(user_input):
            break

if __name__ == "__main__":
    main()
"""
def chatbot():
    print("Welcome to the Student Support Chatbot!")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif "available courses" in user_input or "courses" in user_input:
            print("Chatbot: The available courses are: Computer Science, Data Science, AI & ML, Cybersecurity.")
        elif "course schedule" in user_input or "schedule" in user_input:
            print("Chatbot: Classes run from Monday to Friday, 9 AM to 4 PM.")
        elif "university location" in user_input or "location" in user_input:
            print("Chatbot: The university is located at MG Road, Pune, Maharashtra.")
        else:
            print("Chatbot: Sorry, I didn't understand that. Please ask about courses, schedule, or location.")

# Run the chatbot
chatbot()

import random

def food_ordering_chatbot():
    menu = {
        "Pizza": 250,
        "Burger": 150,
        "Pasta": 200,
        "Fries": 100,
        "Coke": 50
    }

    slogans = [
        "Savor the flavor, delivered to your door!",
        "Your hunger, our mission!",
        "Fast. Fresh. Fantastic!",
        "Zomato: Bringing joy, one meal at a time!",
        "Taste that tells a story."
    ]

    print("Welcome to Zomato Food Bot!")
    print("Here is our menu:\n")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

    print("\nType the name of the food item you want to order.")
    print("Type 'done' when you finish ordering.\n")

    order = []
    while True:
        choice = input("You: ").title()
        if choice == "Done":
            break
        elif choice in menu:
            order.append(choice)
            print(f"Chatbot: {choice} added to your order.")
        else:
            print("Chatbot: Item not available. Please choose from the menu.")

    if not order:
        print("Chatbot: You didn't order anything. Goodbye!")
        return

    total = sum(menu[item] for item in order)
    print("\nChatbot: Please select your payment mode (Cash / UPI / Card):")
    payment = input("You: ").strip().capitalize()

    print("\n------ Bill Summary ------")
    for item in order:
        print(f"{item}: ₹{menu[item]}")
    print(f"Total Amount: ₹{total}")
    print(f"Payment Mode: {payment}")
    print("--------------------------")

    # Show a random slogan
    print("\nChatbot:", random.choice(slogans))

    # Delivery feedback
    print("\nChatbot: Was your delivery on time? (yes/no)")
    feedback = input("You: ").lower()
    if feedback == "yes":
        print("Chatbot: Awesome! Glad we served you well 😊")
    else:
        print("Chatbot: Sorry for the delay. We'll improve next time! 🙏")

    print("\nChatbot: Thank you for ordering with Zomato. Enjoy your meal!")

# Run the chatbot
food_ordering_chatbot()
"""
