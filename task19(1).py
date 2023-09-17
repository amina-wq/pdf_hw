def min_money_to_spend(N, costs):
    costs.sort(reverse=True)

    min_money = sum(costs)

    for i in range(2, N, 3):
        min_money -= costs[i]

    return min_money


if __name__ == "__main__":
    N = int(input("Enter the amount of products: "))
    costs = list(map(int, input("Enter the cost of each product: ").split()))

    print(min_money_to_spend(N, costs))