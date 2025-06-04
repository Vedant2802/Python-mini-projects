
# 🧠 Python OOP Cheat Sheet

## 🧱 OOP Concepts

- **Class**: Blueprint for creating objects
- **Object**: Instance of a class
- **Encapsulation**: Hiding internal details (e.g., `_var`, `__var`)
- **Inheritance**: Reuse functionality from a base class
- **Polymorphism**: Same interface, different behavior
- **Abstraction**: Hiding complex implementation

---

## ✅ Class & Object

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

dog = Animal("Dog")
dog.speak()
```

---

## 🔒 Encapsulation

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance        # Protected
        self.__secret = "1234"         # Private
```

---

## 🔁 Inheritance and `super()`

```python
class Hero:
    def __init__(self, name):
        self.name = name

class Warrior(Hero):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power
```

---

## 🧠 Special (Dunder) Methods

| Method       | Purpose              |
|--------------|----------------------|
| `__init__`   | Constructor           |
| `__str__`    | String representation |
| `__repr__`   | Debug string          |
| `__len__`    | Supports `len(obj)`   |
| `__eq__`     | Equality check        |

---

## 🧮 Class & Static Methods

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return cls.__name__
```

---

## ✅ Summary Table

| Feature         | Syntax                |
|----------------|------------------------|
| Class           | `class A:`             |
| Inheritance     | `class B(A):`          |
| Constructor     | `def __init__(self):`  |
| Method          | `def method(self):`    |
| super()         | `super().__init__()`   |
| Class method    | `@classmethod`         |
| Static method   | `@staticmethod`        |
