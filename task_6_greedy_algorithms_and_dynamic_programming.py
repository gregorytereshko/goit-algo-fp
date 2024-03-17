def greedy_algorithm(items, budget):
    items_sorted = sorted(
        items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, values in items_sorted:
        if total_cost + values["cost"] <= budget:
            total_cost += values["cost"]
            total_calories += values["calories"]
            selected_items.append(item)

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if items[list(items.keys())[i - 1]]["cost"] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[list(items.keys())
                               [i - 1]]["cost"]] + items[list(items.keys())[i - 1]]["calories"])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    return selected_items, dp[n][budget]


budget = 100

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
dp_items, dp_calories = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print("Обрані страви:", greedy_items)
print("Загальна калорійність:", greedy_calories)
print("Загальна вартість:", greedy_cost)

print("\nДинамічне програмування:")
print("Обрані страви:", dp_items)
print("Загальна калорійність:", dp_calories)
