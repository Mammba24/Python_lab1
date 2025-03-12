class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, name: str, users: int) -> None:
        """
        Инициализирует социальную сеть.

        :param name: Название социальной сети.
        :param users: Количество пользователей.
        """
        self._name = name  # Инкапсулируем, чтобы имя нельзя было менять
        self._users = users

    @property
    def name(self) -> str:
        """Возвращает название социальной сети."""
        return self._name

    @property
    def users(self) -> int:
        """Возвращает количество пользователей."""
        return self._users

    def __str__(self) -> str:
        return f"Социальная сеть: {self.name}, Кол-во пользователей: {self.users}"

    def __repr__(self) -> str:
        return f"SocialNetwork(name={self.name!r}, users={self.users})"

    def add_users(self, count: int) -> None:
        """
        Увеличивает количество пользователей.

        :param count: Количество новых пользователей.
        """
        if count < 0:
            raise ValueError("Число пользователей не может быть отрицательным!")
        self._users += count


class Telegram(SocialNetwork):
    """Дочерний класс для мессенджера Telegram."""

    def __init__(self, users: int, groups: int) -> None:
        """
        Инициализирует Telegram с пользователями и группами.

        :param users: Количество пользователей.
        :param groups: Количество групп.
        """
        super().__init__(name="Telegram", users=users)
        self._groups = groups

    @property
    def groups(self) -> int:
        """Возвращает количество групп."""
        return self._groups

    def __str__(self) -> str:
        return f"Телеграм: Кол-во пользователей: {self.users}, Групп: {self.groups}"

    def __repr__(self) -> str:
        return f"Telegram(users={self.users}, groups={self.groups})"

    def add_users(self, count: int) -> None:
        """
        Увеличивает количество пользователей и групп.
        Перегрузка метода add_users:
        - В Telegram группы создаются примерно 1 на 1000 пользователей.

        :param count: Количество новых пользователей.
        """
        super().add_users(count)
        self._groups += count // 1000  # 1 группа на 1000 новых пользователей


# Пример использования
if __name__ == "__main__":
    vk = SocialNetwork("VK", 90000000)
    print(vk)  # Проверяем __str__
    vk.add_users(100000)
    print(repr(vk))  # Проверяем __repr__

    tg = Telegram(users=70000000, groups=500000)
    print(tg)  # Проверяем __str__
    tg.add_users(2000000)  # Добавляем пользователей и автоматически увеличиваем количество групп
    print(repr(tg))  # Проверяем __repr__
