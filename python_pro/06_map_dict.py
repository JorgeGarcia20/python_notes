products = [
    {
        'name': 'shirt', 
        'price': 120
    },
    {
        'name': 'pant', 
        'price': 220
    },
    {
        'name': 'shoes', 
        'price': 520
    },
    {
        'name': 'socks', 
        'price': 50
    },
    {
        'name': 'sweater', 
        'price': 160
    }
]

# the map function creates a new list instead of modifying the existing one.
prices = list(map(lambda product: product['price'], products ))
print(prices)


# if we apply this function to the products dictionary, we are going to modify it, and this is not a good practice
# to avoid this problem, we can make a copy of the products dictionary.
def apply_taxes(products):
    TAX = 0.15
    new_products = products.copy()
    new_products['taxes'] = new_products['price'] * TAX
    return new_products

products_taxes = list(map(apply_taxes, products))
print(products_taxes)
print(products)

