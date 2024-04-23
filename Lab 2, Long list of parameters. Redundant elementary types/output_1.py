def calculate_score(person_data):
    # Розпакування даних із словника
    name, age, gender, height, weight, *scores = person_data.values()

    # Обчислення загального балу
    total_score = sum(scores)

    # Перевірка чи користувач є повнолітнім
    is_adult = age >= 18

    # Виведення результатів
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Height:", height)
    print("Weight:", weight)
    print("Total Score:", total_score)
    print("Adult:", is_adult)


# Приклад виклику функції
person_data = {
    "name": "John",
    "age": 25,
    "gender": "Male",
    "height": 175,
    "weight": 70,
    "score1": 85,
    "score2": 90,
    "score3": 75,
    "score4": 88,
    "score5": 92
}

calculate_score(person_data)