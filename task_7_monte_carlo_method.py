import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_trials):
    # словник для зберігання кількості випадінь кожної суми від 2 до 12
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum_dice = dice1 + dice2
        results[sum_dice] += 1

    # обчислення ймовірностей у відсотках
    probabilities = {key: value / num_trials *
                     100 for key, value in results.items()}
    return probabilities


num_trials = 1000000
probabilities = monte_carlo_simulation(num_trials)

# Відображення результатів у вигляді таблиці
print("Сума\tІмовірність")
for key, value in probabilities.items():
    print(f"{key}\t{value:.2f}% ({value/100:.2f})")

# Відображення результатів у вигляді графіка
plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel('Сума')
plt.ylabel('Імовірність')
plt.title('Імовірність суми при киданні двох кубиків (Метод Монте-Карло)')
plt.xticks(range(2, 13))
plt.show()
