class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def __repr__(self):
        return_string = f'Items in the {self.name} catalogue:\n'
        return_string += '\n'.join(sorted(self.products))
        return return_string

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        filtered_list = [item for item in self.products if first_letter == item[0]]
        return filtered_list


catalogue = Catalogue('Furniture')
catalogue.add_product('Sofa')
catalogue.add_product('Mirror')
catalogue.add_product('Desk')
catalogue.add_product('Chair')
catalogue.add_product('Carpet')
print(catalogue.get_by_letter('C'))
print(catalogue)

#fix this