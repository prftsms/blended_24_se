# Task8
def invite_to_event(username):

    return f"Dear {username}, we have the honour to invite you to our event" 



# Task9

def discount_price(price, discount):
  
    def apply_discount():

        nonlocal price
        price = price * (1 - discount)
    apply_discount()
   
    return price
# Task10
def get_fullname (first_name, last_name, middle_name =""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"
