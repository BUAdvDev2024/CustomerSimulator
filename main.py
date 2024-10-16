import config
from modules import UserManagement
from modules import TableReservation

def main():
    print(f"Hello world - config: {config.user_details["email"], config.user_details["password"]}")
    # should return successful loging
    UserManagement.loginWithCustomerCredentials("valid_user@gmail.com", "password123")
    # should return invalid login
    UserManagement.loginWithCustomerCredentials("invalid_user@gmail.com", "password123")
    # should return valid registration
    UserManagement.registerCustomerWithCredentials("new_user@gmail.com", "")
    # should return invalid registration
    UserManagement.registerCustomerWithCredentials("existing_user@gmail.com", "")

    TableReservation.createTableReservation({
        "date": "2024-10-01",
        "time": "18:00",
        "party_size": 4,
        "customer_name": "John Doe",
        "customer_phone": "1234567890"
    })

if __name__ == "__main__":
    main()