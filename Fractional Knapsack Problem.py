class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    # Sort items by ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    profit = 0.0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            profit += item.value
        else:
            profit += item.ratio * capacity
            break
    
    return profit

if __name__ == "__main__":
    items = [Item(40, 10), Item(80, 20), Item(80, 20)]
    capacity = 40
    max_profit = fractional_knapsack(items, capacity)
    print(f"The profit is {max_profit}")
