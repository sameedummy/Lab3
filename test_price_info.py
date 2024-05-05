import price_info as info

def test_total_cost_shopping():
    result = 0
    fruit = 'apple'
    total_cost = 6.0

    result = info.total_cost_shopping(fruit)

    assert (result == total_cost)


def test_cost_of_fruit():
    result = 0
    fruit = 'apple'
    quantity = 10
    cost_of_fruit = 12.0

    result = info.cost_of_fruits(fruit, quantity)

    assert (result == cost_of_fruit)
