import csv
from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4


class Wallet:
    def __init__(self, owner_id: str, balance: float = 0.0):
        self.balance = balance
        self.deposit = 0.0
        self.owner_id = owner_id


class User:
    def __init__(self, id: str, username: str, password: str, birthday: datetime):
        self.id = id
        self.username = username
        self.password = password
        self.birthday = birthday

    @property
    def wallet(self) -> Optional[Wallet]:
        for w in database["wallets"]:
            if w.owner_id == self.id:
                return w
        return None


class Transaction:
    def __init__(
        self,
        from_id: str,
        to_id: str,
        amount: float,
        transfer_datetime: datetime,
        description: str,
    ):
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount
        self.transfer_datetime = transfer_datetime
        self.description = description

    def __repr__(self) -> str:
        return f"Отправлено пользователю: {self.to_id} ID. Переведено: {self.amount} KZT. Время: {self.transfer_datetime}. Комментарий: {self.description}"


class BankService:
    def __init__(self):
        self.__current_user: User = None

    def create_transaction(self):
        if self.__current_user is None:
            print("Сначала войдите в аккаунт!")
            return

        from_id = self.__current_user.id
        to_id = input("Введите ID пользователя: ")

        try:
            amount = float(input("Введите сумму для перевода: "))
        except ValueError:
            print("Введена неправильная сумма")
            return

        transfer_datetime = datetime.now(tz=timezone.utc)
        description = input("Оставьте сообщение к переводу: ")

        new_transaction = Transaction(
            from_id=from_id,
            to_id=to_id,
            amount=amount,
            transfer_datetime=transfer_datetime,
            description=description,
        )

        to_user: User = None
        for user in database["users"]:
            if user.id == to_id:
                to_user = user

        if to_user is None:
            print("Пользователь не найден!")
            return

        if to_user.wallet is None:
            print("У получателя нет кошелька")
            return

        if self.__current_user.wallet is None:
            print("У вас нет кошелька")
            return

        if self.__current_user.wallet.balance < amount:
            print("Недостаточно денег для перевода")
            return

        self.__current_user.wallet.balance -= amount
        to_user.wallet.balance += amount
        database["transactions"].append(new_transaction)
        print("Транзакция выполнена")

    def put_deposit(self):
        pass

    def take_deposit(self):
        pass

    def get_balance(self):
        if self.__current_user is None:
            print("Сначала войдите в аккаунт!")
            return

        for wallet in database["wallets"]:
            if wallet.owner_id == self.__current_user.id:
                print("Ник вашего аккаунта:", self.__current_user.username)
                print("Ваш баланс:", wallet.balance, "KZT")
                print("На депозите:", wallet.deposit, "KZT")

    def create_user(self):
        user_id = str(uuid4())
        username = input("Введите ник пользователя: ")
        password = input("Введите пароль пользователя: ")
        birthday = input("Введите ДР пользователя в формате - мм.дд.гггг : ")

        try:
            birthday = datetime.strptime(birthday, "%m.%d.%Y")
        except ValueError:
            print("Вы ввели день рождения в неправильном формате")
            return

        user = User(
            id=user_id,
            username=username,
            password=password,
            birthday=birthday,
        )
        wallet = Wallet(owner_id=user_id)

        database["users"].append(user)
        database["wallets"].append(wallet)

        print("Вы успешно зарегистрированы!")

    def logout(self):
        pass

    def login(self):
        print("*" * 10)
        username = input("Введите ник: ")
        password = input("Введите пароль: ")

        if len(username) == 0 or len(password) == 0:
            print("Неправильные данные!")
            return

        for user in database["users"]:
            if username == user.username and password == user.password:
                self.__current_user = user

                print("Вы успешно зашли!")
                print("*" * 10)
                return
        print("Неправильные данные!")

    def get_transactions(self):
        if self.__current_user is None:
            print("Сначала войдите в аккаунт!")
            return

        # transactions = list(
        #     filter(
        #         lambda t: self.__current_user.id == t.from_id,
        #         database["transactions"],
        #     )
        # )
        transactions = [
            t for t in database["transactions"] if t.from_id == self.__current_user.id
        ]
        if len(transactions) == 0:
            print("Транзакций нет")
        else:
            for index, transaction in enumerate(transactions):
                print(f"{index + 1}. {transaction}")


database = {
    "users": [],
    "wallets": [],
    "transactions": [],
}

with open("users.csv", encoding="UTF-8") as users_file:
    fieldnames = ["id", "username", "password", "birthday"]
    data = csv.DictReader(users_file)
    for el in data:
        print(el)
        database["users"].append(
            User(
                id=el["id"],
                username=el["username"],
                password=el["password"],
                birthday=el["birthday"],
            )
        )

print(database["users"])
bank_service = BankService()  # создание объекта класса BankService


commands = {
    "Войти": bank_service.login,
    "Зарегистрироваться": bank_service.create_user,
    "Выйти": bank_service.logout,
    "Положить деньги на депозит": bank_service.put_deposit,
    "Взять деньги с депозита": bank_service.take_deposit,
    "Посмотреть баланс": bank_service.get_balance,
    "Перевести деньги на другой счет": bank_service.create_transaction,
    "Посмотреть историю переводов": bank_service.get_transactions,
}

while True:
    keys = list(commands.keys())
    for index in range(len(keys)):
        print(f"{index + 1}. {keys[index]}")
    command_index = int(input("Выберите номер комманды: "))
    try:
        command_key = keys[command_index - 1]
        commands[command_key]()
    except IndexError:
        print("Такой комманды нету")
