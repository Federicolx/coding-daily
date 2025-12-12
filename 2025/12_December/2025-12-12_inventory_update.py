'''
Title:Inventory Update
Date:2025-12-12
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-12
Description:
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].

Examples:
1. update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]) 
should return [[3, "apples"], [8, "bananas"]].
Waiting:2. update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]) 
should return [[3, "apples"], [8, "bananas"], [4, "oranges"]].
Waiting:3. update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]) 
should return [[10, "apples"], [30, "bananas"], [20, "oranges"]].
Waiting:4. update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) 
should return [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]].
'''
def update_inventory(inventory, shipment):
    #1.将inventory转换为stock
    stock = {item:qty for qty,item in inventory}

    #将shipment物品转到stock
    new_items = []
    for add_aty,item in shipment:
        if item in stock:
            stock[item] += add_aty
        else:
            stock[item] = add_aty  
            new_items.append(item)
    #print(new_items)
    
    result = []
    for qty,item in inventory:
        result.append([stock[item],item])#添加原有物品到结果

    for item in new_items:
        result.append([stock[item],item])#添加新物品到结果
    return result

update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]])