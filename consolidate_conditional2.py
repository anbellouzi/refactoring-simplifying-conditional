# by Kami Bigdely
# Consolidate conditional expressions
def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)
    
def not_cucumber(ingredients):
    return 'cucumber' not in ingredients

def not_onion(ingredients):
    return 'onion' not in ingredients

def not_tomato(ingredients):
    return 'tomato' not in ingredients

def not_lemon_juice(ingredients):
    return 'lemon juice' not in ingredients


def make_shirazi_salad(ingredients):
    if not_cucumber(ingredients):
        print('lacks ingredients.')
        return
    if not_tomato(ingredients):
        print('lacks ingredients.')
        return
    if not_onion(ingredients):
        print('lacks ingredients.')
        return
    if not_lemon_juice(ingredients):
        print('lacks ingredients.')
        return
    
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])