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


def knapsack(itemList, amount):

    sorted_items = sorted(itemList, key=price_per_weight, reverse=True)

    total_value = 0
    total_weight = 0
    selected = []

    for item in sorted_items:

        if total_weight + item.get_weight() <= amount:
            selected.append(item)

            total_value += item.get_price()
            total_weight += item.get_weight()


    print(f"Knapsack Size: {amount} kg")
    print("===============================")

    for item in selected:
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")

    print(f"Total: {total_value} THB")





def main():
    import json
    items = []
    num_items = int(input())

    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1

    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)

main()
