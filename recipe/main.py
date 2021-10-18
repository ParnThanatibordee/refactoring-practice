from recipe import Recipe


def create_order(name="Coffee", coffee=0, chocolate=0, milk=0, sugar=0, price=0):
    order = Recipe(name)
    order.coffee = coffee
    order.chocolate = chocolate
    order.milk = milk
    order.sugar = sugar
    order.price = price

    return order


if __name__ == '__main__':
    recipe1 = create_order("Coffee with sugar", 4, 0, 0, 2, 30.0)
    print(recipe1)

    recipe2 = create_order("Latte", 3, 0, 1, 2, 40.0)
    print(recipe2)

    recipe3 = create_order("Hot Chocolate", 0, 3, 4, 2, 30.0)
    print(recipe3)
