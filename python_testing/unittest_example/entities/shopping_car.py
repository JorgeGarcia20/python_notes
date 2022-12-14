from entities.product import Product


class ShoppingCar:

    def __init__(self) -> None:
        #self.__products = list()
        self.__products: list[Product] = []

    @property
    def products(self):
        return self.__products.copy()

    @property
    def total(self) -> float:
        return sum([(product.price - product.discount)
                   for product in self.__products])

    # Validar que el argumento sea de tipo Product y validad con ut
    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def empty(self) -> bool:
        return len(self.__products) == 0

    def has_products(self):
        return not self.empty()

    def remove_product(self, product: Product) -> None:
        self.__products.remove(product)
