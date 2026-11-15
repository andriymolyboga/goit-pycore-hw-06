from collections import UserDict


class Field:
    """Базовий клас для полів запису."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Клас для зберігання імені контакту."""

    pass


class Phone(Field):
    """Клас для зберігання номера телефону."""

    def __init__(self, value):
        # Перевіряємо, що номер складається рівно з 10 цифр
        if not value.isdigit() or len(value) != 10:
            raise ValueError(
                "Номер телефону повинен складатися з 10 цифр"
            )

        super().__init__(value)


class Record:
    """Клас для зберігання інформації про контакт."""

    def __init__(self, name):
        # Зберігаємо ім'я як об'єкт класу Name
        self.name = Name(name)

        # Список телефонів буде містити об'єкти класу Phone
        self.phones = []

    def add_phone(self, phone):
        """Додати телефон до контакту."""
        phone_object = Phone(phone)
        self.phones.append(phone_object)

    def remove_phone(self, phone):
        """Видалити телефон."""
        found_phone = self.find_phone(phone)

        if found_phone:
            self.phones.remove(found_phone)

    def edit_phone(self, old_phone, new_phone):
        """Замінити старий номер телефону на новий."""
        found_phone = self.find_phone(old_phone)

        if found_phone:
            # Створюємо новий Phone, щоб новий номер теж пройшов валідацію
            new_phone_object = Phone(new_phone)

            # Замінюємо значення номера
            found_phone.value = new_phone_object.value
        else:
            raise ValueError("Телефон не знайдено")

    def find_phone(self, phone):
        """Знайти телефон у списку телефонів контакту."""
        for phone_object in self.phones:
            if phone_object.value == phone:
                return phone_object

        return None

    def __str__(self):
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {'; '.join(p.value for p in self.phones)}"
        )


class AddressBook(UserDict):
    """Клас для зберігання та керування контактами."""

    def add_record(self, record):
        """Додати запис до адресної книги."""
        self.data[record.name.value] = record

    def find(self, name):
        """Знайти запис за ім'ям."""
        return self.data.get(name)

    def delete(self, name):
        """Видалити запис за ім'ям."""
        if name in self.data:
            del self.data[name]


# ============================
# Приклад використання
# ============================

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

# Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")