#-------------------------------------------------------------------------------
# HA3.py
# Student Name: Huma Safdar
# Version: Python 3.X
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Any notes to grader: For example: Easy
#-------------------------------------------------------------------------------
# Code starts below this line
#----------------------------------------------------------------------------
# This is the most effective of all LESS controls

def build_dict_by_id(items):
    dict_ID = {}
    for item in items:
        parts = item.split(',')
        item_id = parts[0].strip()
        category = parts[1].strip().lower()
        description = parts[2].strip()
        price = parts[3]
        rating = parts[4]
        dict_ID[item_id] = [category, description, price, rating]
    return dict_ID
    

def build_dict_by_category(items):
    dict_category = {}
    for item in items:
        parts = item.split(',')
        item_id = parts[0].strip()
        category = parts[1].strip().lower()
        if category in dict_category:
            dict_category[category].append(item_id)
        else:
            dict_category[category] = [item_id]
    return dict_category
     

def checkout(cart, dict_ID):
    total = 0.0
    print('Thanks for shopping at Amazing.')
    print('You purchased the following item(s):')
    for item in cart:
        print(item, dict_ID[item.upper()])
        total += float(dict_ID[item.upper()][2])
    return total

def build_list_by_ratings(dict_category, dict_ID, user_category, min_rating):
    '''
    Populate and return a list from dict_category 
    where items will have minimum of min_raing
    '''
    ratings_list = []
    for item_id in dict_category[user_category]:
        rating = float(dict_ID[item_id][3])
        if rating >= min_rating:
            ratings_list.append(item_id)

    return ratings_list




def main():
    items = ['B001,book,Patriot Games, 15.95, 3.75', 'B002,book,Origin, 19.95, 2.5', 'C001,cloth,Armani Suit, 800.00, 3.5',
          'B003,book,Animal Farm, 9.97, 4', 'B004,book,Grant, 22.50, 4.2', 'F001,food,Moose Drool Ale 6-pack, 9.95, 4.6',
          'C002,cloth,Pants, 39.95, 2.7', 'B005,book,Prairie Fires, 18.95, 1.2','C003,cloth,Vasque Hiking Boots, 109.00, 2.3',
          'C004,cloth,Wool Hat, 14.00, 4.5', 'F002,food,Jumbo shrimp, 12.50, 4','C005,cloth,Wrangler Jeans, 24.50, 4.1',
          'B005,book,Ragtime, 17.25,3','F003,food,Fusili - 16 oz., 2.95, 4', 'C006,cloth,Nike T-shirt, 19.00, 5',
          'C007,cloth,Gore-Tex Gloves, 39.00, 0.1','C008,cloth,North Face Fleece Jacket, 89.95, 4.3',
          'C009,cloth,Nationals Logo Sweatshirt, 49.00, 2.9','F004,food,Lamb Chops, 21.95, 4.95',
          'C010,cloth,New Balance Trail Runners,69.95, 3.6','B006,book,Future Shock, 8.95, 2.5']


    dict_ID = build_dict_by_id(items)
    dict_category = build_dict_by_category(items)
    cart = []
    print('Welcome to shopping at Amazing!')
    print('We sell items in the following categories:', list(dict_category.keys()))

    while True:
        user_input = input("Please input a category name or input 'checkout' to quit: ").strip().lower()

        if user_input == 'checkout':
            break

        elif user_input in dict_category:
            answer = input('Would you like to see items in this category filtered by minimum customer ratings (0-5)? Y/N: ').strip().upper()

            if answer == 'Y':
                min_rating = float(input('Please enter the minimum rating: '))
                item_list = build_list_by_ratings(dict_category, dict_ID, user_input, min_rating)
            else:
                item_list = dict_category[user_input]

            for item_id in item_list:
                print('Item ID:', item_id, 'Information:', dict_ID[item_id])

            chosen_item = input('Please input item ID or type any key to return: ').strip()

            if chosen_item.upper() in item_list:
                cart.append(chosen_item.lower())
                print(chosen_item.upper(), 'added to cart')

            print('Welcome to shopping at Amazing!')

        else:
            print('We sell items in the following categories:', list(dict_category.keys()))

    total = checkout(cart,dict_ID)
    print('The amount is: $', total)


main()
    
