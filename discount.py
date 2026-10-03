def apply_discount(price,discount):
    Discounted_price = price-(price *(discount/100))
    return Discounted_price

def flat_discount(price, discount=50):
    discounted_price = price-discount
    return discounted_price
