def validate_user(user):
    return user[1] is not None and "@" in user[2]

def validate_product(product):
    return product[2] > 0

def validate_order(order):
    return order[3] > 0
