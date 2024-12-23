import random
import time

class TurboCarnival:
    def __init__(self):
        self.rides = ["Ferris Wheel", "Turbo Coaster", "Bumper Cars", "Haunted House"]
        self.tickets = []

    def buy_ticket(self, name):
        ticket_id = f"TC-{random.randint(1000, 9999)}"
        ride = random.choice(self.rides)
        ticket = {"name": name, "ticket_id": ticket_id, "ride": ride}
        self.tickets.append(ticket)
        print(f"🎟️ Ticket purchased! {name}, your ticket ID is {ticket_id} for the {ride} ride.")
        return ticket

    def enter_ride(self, ticket_id):
        for ticket in self.tickets:
            if ticket["ticket_id"] == ticket_id:
                print(f"🎢 Welcome, {ticket['name']}! Enjoy the {ticket['ride']}!")
                return
        print(f"🚫 Invalid ticket ID: {ticket_id}")

    def list_rides(self):
        print("🎡 Available rides at Turbo Carnival:")
        for i, ride in enumerate(self.rides, 1):
            print(f"{i}. {ride}")

    def print_tickets(self):
        if not self.tickets:
            print("🚨 No tickets sold yet!")
        else:
            print("🎟️ Tickets sold:")
            for ticket in self.tickets:
                print(f" - {ticket['name']} | ID: {ticket['ticket_id']} | Ride: {ticket['ride']}")

def main():
    print("🎉 Welcome to Turbo Carnival! 🎉")
    carnival = TurboCarnival()

    while True:
        print("\nChoose an option:")
        print("1. Buy a ticket 🎟️")
        print("2. Enter a ride 🎢")
        print("3. List all rides 🎡")
        print("4. View sold tickets 📝")
        print("5. Exit 🚪")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            name = input("Enter your name: ")
            carnival.buy_ticket(name)
        elif choice == "2":
            ticket_id = input("Enter your ticket ID: ")
            carnival.enter_ride(ticket_id)
        elif choice == "3":
            carnival.list_rides()
        elif choice == "4":
            carnival.print_tickets()
        elif choice == "5":
            print("👋 Thanks for visiting Turbo Carnival! Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

        time.sleep(1)

if __name__ == "__main__":
    main()
