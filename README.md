# goit-algo2-hw-05

----

# Першочергові налаштування
1. Сворюємо віртуальне середовище:
```
python -m venv venv
```
2. Активуємо віртуальне середовище:
```
source venv/bin/activate
```
3. Проінсталюйте залежності:
```
pip install -r requirements.txt 
```

----

# Завдання 1. Перевірка унікальності паролів за допомогою фільтра Блума

#### Приклад використання
```
python task1.py
```

#### Виведе:
```
Пароль 'password123' — вже використаний.
Пароль 'newpassword' — унікальний.
Пароль 'admin123' — вже використаний.
Пароль 'guest' — унікальний.
```

# Завдання 2. Порівняння продуктивності HyperLogLog із точним підрахунком унікальних елементів

#### Приклад використання
```
python task2.py
```

#### Виведе:
|                          | Точний підрахунок | HyperLogLog |
|--------------------------|-------------------|-------------|
| Унікальні елементи       | 28          | 28.023953075428718     |
| Час виконання (сек.)     | 0.35244           | 0.46489     |

### Підсумок:
Різниця може бути через маленький розмір лог-файлу: алгоритм HyperLogLog показує точніші результати на великих даних, а на малих наборах похибка може бути меншою, що дає схожий результат з точним підрахунком.