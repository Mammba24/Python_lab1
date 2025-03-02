""""родительский класс социальные сети"""
class SocialNetwork:
    def __init__(self, name: str, users: int):
        self.name = name
        self.users = users

    def __str__(self) -> str:
        return f"Социальная сеть: {self.name}, Кол-во пользователей: {self.users}"

    def __repr__(self) -> str:
        return f"Социальная сеть({self.name}, Кол-во пользователей: {self.users})"

    """""Добавление пользователей"""
    def add_users(self, count: int):
        self.users +=count
""""дочерний класс телеграм"""
class Telegram(SocialNetwork):
    def __init__(self, users: int, groups: int):
        super().__init__(name='Telegram', users=users)
        self.groups = groups

    def __str__(self) ->str:
        return f"Телеграм: Кол-во пользователей: {self.users}, Групп: {self.groups}"

    def __repr__(self) ->str:
        return f"Телеграм(Кол-во пользователей: {self.users}, Групп: {self.groups})"

    def add_users(self, count: int):
        super().add_users(count)
        self.groups =+ count // 1000



if __name__ == "__main__":
    # Write your solution here
    pass
