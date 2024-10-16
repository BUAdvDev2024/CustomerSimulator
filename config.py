user_details = dict(
    email = "valid_user@gmail.com",
    password = "pword123"
)
urls = dict (
    route_url = "http://localhost",
    user_management = {
        "port": "5000",
        "route_path": "/api",
        "endpoints" : {
            "login": "/login",
            "register": "/register"
        }
    },
    table_reservation = {
        "port": "8000",
        "route_path": "",
        "endpoints": {
            "reserve": "/",
            "test": "/test"
        }
    }
    
)
