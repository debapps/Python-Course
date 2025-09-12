class InsufficientException(Exception):
        pass

class MobileInventory:
    def __init__(self, inventory=None):
        if inventory is None:
            self.balance_inventory = {}
        else:
            if not isinstance(inventory, dict):
                raise TypeError("Input inventory must be a dictionary")
            for model in inventory:
                if not isinstance(model, str):
                    raise ValueError("Mobile model name must be a string")
                if not isinstance(inventory[model], int) or inventory[model] < 0:
                    raise ValueError("No. of mobiles must be a positive integer")
            self.balance_inventory = inventory

    def add_stock(self, new_stock):
        if not isinstance(new_stock, dict):
            raise TypeError("Input stock must be a dictionary")
        for model in new_stock:
            if not isinstance(model, str):
                raise ValueError("Mobile model name must be a string")
            if not isinstance(new_stock[model], int) or new_stock[model] < 0:
                raise ValueError("No. of mobiles must be a positive integer")
            if model in self.balance_inventory:
                self.balance_inventory[model] += new_stock[model]
            else:
                self.balance_inventory[model] = new_stock[model]

    def sell_stock(self, requested_stock):
        if not isinstance(requested_stock, dict):
            raise TypeError("Requested stock must be a dictionary")
        for model in requested_stock:
            if not isinstance(model, str):
                raise ValueError("Mobile model name must be a string")
            if not isinstance(requested_stock[model], int) or requested_stock[model] < 0:
                raise ValueError("No. of mobiles must be a positive integer")
            if model not in self.balance_inventory:
                raise InsufficientException("No Stock. New Model Request")
            if requested_stock[model] > self.balance_inventory[model]:
                raise InsufficientException("Insufficient Stock")
            self.balance_inventory[model] -= requested_stock[model]

# if __name__ == '__main__':
#     inv1 = MobileInventory()
#     print(inv1.balance_inventory)

#     # MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
#     # MobileInventory({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
#     # MobileInventory({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'})
#     # MobileInventory({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25})

#     mi = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
#     print(mi.balance_inventory)

#     inventory = MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
#     new_stock = {'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10}
#     inventory.add_stock(new_stock)
#     print(inventory.balance_inventory)