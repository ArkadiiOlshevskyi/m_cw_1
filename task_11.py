'''
lest make good and simple description for task in python:
Task Description: Creating a sorting function

Input:
Create a Client class with attributes
(id, name, age).

Objectives:
Your goal is to create an array(container) of product instances and function,
that sorts clients with age over 30 and preserves original container order
'''


class Client():
    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age


def client_age_sort_30y(data):
    sorted_clients = [client for client in data if client.age >= 30]
    for client in sorted_clients:
        print(f"ID: {client.id}\nName: {client.name}\nAge: {client.age}")


if __name__ == '__main__':
    client_1 = Client(1, 'Paul', 45)
    client_2 = Client(2, 'John', 36)
    client_3 = Client(3, 'Margaret', 18)
    client_4 = Client(4, 'Lena', 32)
    client_5 = Client(5, 'Anna', 23)

    clients_db = [client_1, client_2, client_3, client_4, client_5]

    client_age_sort_30y(clients_db)
