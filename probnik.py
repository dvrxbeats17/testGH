import requests
import hashlib
import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha512(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == self._hash_password(password)

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.user = None
        self.db_conn = sqlite3.connect('weather_history.db')
        self.db_cursor = self.db_conn.cursor()
        self.create_table()

    def create_table(self):
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS search_history
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             username TEXT,
                             search_query TEXT,
                             search_type TEXT,
                             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.db_conn.commit()

    def register(self, username, password):
        self.user = User(username, password)

    def login(self, username, password):
        self.user = User(username, password)

    def search_weather_by_city_name(self, city_name):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}'
        response = requests.get(url)
        weather_data = response.json()
        self.save_search_history(city_name, 'city_name')
        return weather_data

    def search_weather_by_coordinates(self, lat, lon):
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}'
        response = requests.get(url)
        weather_data = response.json()
        self.save_search_history(f'lat: {lat}, lon: {lon}', 'coordinates')
        return weather_data

    def save_search_history(self, search_query, search_type):
        if self.user:
            self.db_cursor.execute('''INSERT INTO search_history (username, search_query, search_type) VALUES (?, ?, ?)''', (self.user.username, search_query, search_type))
            self.db_conn.commit()


api_key = 'e402ec61210133af1a2b0ed568f79d37'
weather_app = WeatherApp(api_key)

def main():
    while True:
        print("1. регистрация\n2. логин\n3. поиск по городу\n4. поиск по координатам\n5. история просмотра\n6. выход")
        choice = input("что вы хотите: ")

        if choice == '1':
            username = input("напишите юз: ")
            password = input("напишите пароль: ")
            weather_app.register(username, password)
            print("успешная регистрация")

        elif choice == '2':
            username = input("введите юз: ")
            password = input("введите пароль: ")
            if weather_app.user and weather_app.user.username == username and weather_app.user.check_password(password):
                print("успешно вошли")
            else:
                print("неправильные данные")

        elif choice == '3':
            city_name = input("введите город: ")
            weather_data = weather_app.search_weather_by_city_name(city_name)
            print(weather_data)

        elif choice == '4':
            lat = input("введите широту: ")
            lon = input("введите долготу: ")
            weather_data = weather_app.search_weather_by_coordinates(lat, lon)
            print(weather_data)


        elif choice == '6':
            print("выход")
            break

        else:
            print("неправильно")

if __name__ == "__main__":
    main()
