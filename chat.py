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
