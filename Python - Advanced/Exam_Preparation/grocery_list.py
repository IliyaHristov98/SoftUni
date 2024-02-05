def shop_from_grocery_list(budget, groceries, *prices):
    bought = []

    for item, price in prices:
        if item in groceries and item not in bought:
            if price > budget:
                break

            bought.append(item)
            groceries.remove(item)
            budget -= price

    if not groceries:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(groceries)}."
