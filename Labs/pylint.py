
"""
The module does ...
"""

def count(sequence, item_number):
    """
    The function does ...
    """
    item_count = 0
    for number in sequence:
        if number == item_number:
            item_count += 1
    return item_count


#Original code:
#def count(sequence, item):
#  y = 0
#  for n in sequence:
#    if n == item:
#      y += 1
#  return y
