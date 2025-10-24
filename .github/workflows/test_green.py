def read(filepath: str = 'inventory.json') -> List[Item]:
    """Reads the JSON file and returns a list of Item objects."""
    # File opening handles FileNotFoundError and IOError implicitly.
    # json.load handles JSONDecodeError implicitly.
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    # Converts list of dictionaries to list of Item objects in a single line
    # Note: This relies on the keys ('name', 'price', 'count') being present.
    return [Item(d['name'], d['price'], d['count']) for d in data]

def check_if_item_in_stock(item):
  read(inventory.json)
  if count(item) > 0:
    assert(true)

# DID NOT FINISH, GOT UP UNTIL HERE
  
