def jim_orders(orders):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/jim-and-the-orders/problem

    Jim's Burgers has a line of hungry customers. Orders vary in the time it takes to prepare them. Determine the order
    the customers receive their orders. Start by numbering each of the customers from 1 to n, front of the line to the
    back. You will then be given an order number and a preparation time for each customer.

    The time of delivery is calculated as the sum of the order number and the preparation time. If two orders are
    delivered at the same time, assume they are delivered in ascending customer number order.

    Solve:
        We store the orders in a dictionary with the key being the total prep time for each customer. The value is then
        a list containing the customer number, so if we have multiple customers with the same prep time, we just append
        to the list. We then iterate through the dictionary in increasing prep time order and extend those customers
        to a final list containing the order in which customers will receive their burgers

    Args:
        orders (list): list of tuples containing the order number and prep time for customer[i]

    Returns:
        list: list containing the order in which customers will receive their burgers
    """
    times = {}
    for i, order in enumerate(orders):
        time = sum(order)
        if time in times:
            times[time].append(i+1)
        else:
            times[time] = [i+1]
    customers = []
    for i in sorted(times):
        customers.extend(times[i])
    return customers


if __name__ == "__main__":
    print(jim_orders([[1, 3], [2, 3], [3, 3]]))
    print(jim_orders([[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]))
