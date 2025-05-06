from agents import function_tool


# function to read a file and return its content
@function_tool
def store_information() -> str:
    """
    All data about the store can be find in this file.

    Returns:
        str: The content of the file.
    """
    with open("store.txt", 'r', encoding="utf-8") as file:
        return file.read()

@function_tool
def menu() -> str:
    """
    All data about the menu can be find in this file.

    Returns:
        str: The content of the file.
    """
    with open("menu.txt", 'r', encoding="utf-8") as file:
        return file.read()

@function_tool
def create_order(order_items) -> str:
    """
    Create an order and return the order details.
    
    Args:
        order_items (dict): The items to be ordered.

    Returns:
        str: The order details.
    """
    #open the file in append mode to add the order details
    #convert the order_items dictionary to a string for storage
    order_items = str(order_items)
    with open("orders.txt", 'a', encoding="utf-8") as file:
        file.write(order_items + "\n")
    return f"Order for {order_items} has been created successfully."