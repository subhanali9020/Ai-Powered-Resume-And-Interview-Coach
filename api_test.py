import requests
def fetch_dummy_data():
    url = "https://jsonplaceholder.typicode.com/users/1"
    print("Calling the API....\n")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            user_data = response.json()
            print("--- Success! Data is Fetched ---")
            print(f"Name: {user_data['name']}")
            print(f"Email: {user_data['email']}")
            print(f"Company: {user_data['company']['name']}")
        else:
            print(f"Server Error. Status Code: {response.status_code}") 
    except Exception as e:
        print(f"Network Error: {e}")           
fetch_dummy_data()        