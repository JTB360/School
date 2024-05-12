class ItemToPurchase:
    def __init__(self):
        # Item attributes
        self.item_name="none"
        self.item_price=0
        self.item_quantity=0
    #Creates function to print outputs    
    def print_item_cost(self):
        print(self.item_name,self.item_quantity,'@ $',end='')
        print(self.item_price,'= $',end='')
        
        # calculates the item price multipled by the quantity
        cost=self.item_price*self.item_quantity
        print(cost)

        
# Body of the code
if __name__=="__main__":
    # Objects item1 and item2 are created         
    item1=ItemToPurchase()
    item2=ItemToPurchase()
    
    # Takes three user inputs for item1
    print('Item 1')
    item1.item_name=str(input('Enter the item name:\n'))
    item1.item_price=float(input('Enter the item price:\n'))
    item1.item_quantity=int(input('Enter the item quantity:\n'))
    
    # Takes three user inputs for item2 
    print('\nItem 2')
    item2.item_name=str(input('Enter the item name:\n'))
    item2.item_price=float(input('Enter the item price:\n'))
    item2.item_quantity=int(input('Enter the item quantity:\n'))
    
    # prints the costs 
    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    
    # prints the total cost 
    print('\nTotal: $',end='')
    total_cost=item1.item_price*item1.item_quantity+item2.item_price*item2.item_quantity
    print (round(total_cost,1))
