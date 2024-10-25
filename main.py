from tkinter import Button, Label, Tk
import config
from modules import UserManagement
from modules import TableReservation

def handle_button():
    print("test")

def main():
    print(f"Hello world - config: {config.user_details["email"], config.user_details["password"]}")
    TableReservation.createTableReservation({
        "date": "2024-10-01",
        "time": "18:00",
        "party_size": 4,
        "customer_name": "John Doe",
        "customer_phone": "1234567890"
    })

    root = Tk()
    root.title = "Customer Simulator"
    w = Label(root, text='Customer Simulator')
    w.pack()
    button = Button(root, text='Run', width=25, command=handle_button)
    button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()