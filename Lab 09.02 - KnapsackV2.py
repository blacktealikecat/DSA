class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight

    def get_cost(self):

        if self.weight == 0:
            return float("inf")
        return self.price / self.weight


def price_per_weight(item):
    return item.get_cost()


def get_item_name(item):
    return item.get_name()


def knapsackV2(itemList, amount):
    n = len(itemList)
    amount = int(amount)

    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = itemList[i - 1]
        weight = int(item.get_weight())
        value = item.get_price()

        for w in range(amount + 1):

            if weight <= w:
                not_take = dp[i - 1][w]
                take = dp[i - 1][w - weight] + value
                dp[i][w] = max(not_take, take)

            else:
                dp[i][w] = dp[i - 1][w]

    w = amount
    selected = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = itemList[i - 1]
            selected.append(item)
            w -= int(item.get_weight())

    selected.sort(key=get_item_name) 

    print(f"Total: {dp[n][amount]}")
    for item in selected:
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")





def main():
    import json

    raw_items = json.loads(input())
    amount = int(input())

    items = []
    for name, price, weight in raw_items:
        items.append(Item(name, price, weight))

    knapsackV2(items, amount)

main()