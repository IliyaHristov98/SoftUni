class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered = [word for word in Catalogue.products if word.startswith(first_letter)]
        return filtered

    def __repr__(self):
        result = "Items in the {0} catalogue:\n" \
                 "{1}".format(self.name, '\n'.join(sorted(self.products)))
        return result
