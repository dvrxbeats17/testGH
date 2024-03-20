import requests


def get_student():
    response = requests.get("http://10.60.1.10:8000/students/")
    return response.json()

def create_user():
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    data = {
        "name": name,
        "age": age
    }
    response = requests.post("http://10.60.1.10:8000/students/", json=data)
    return response.json()

def get_user_by_id():
    id = input("Введите id: ")
    response = requests.get(f"http://10.60.1.10:8000/students/{id}")
    return response.json()

def update_user_by_id():
    id = input("Введите id которого изменить: ")
    name = input("Введите новое имя: ")
    age = input("Введите новый возраст: ")
    data = {
        "name": name,
        "age": age
    }
    response = requests.put(f"http://10.60.1.10:8000/students/{id}", json=data)
    return response.json()

def delete_user_by_id():
    id = input(" id которого удалить: ")
    response = requests.delete(f"http://10.60.1.10:8000/students/{id}")
    return response.json()



print(get_student())
print(create_user())
print(get_user_by_id())
print(update_user_by_id())
print(delete_user_by_id())
