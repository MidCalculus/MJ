import rect_price
order = rect_price.rectangle(15, 13, 20)
print("the size of the plate: {}m^2".format(order.get_area()))
print("The total amount of purchase: ${}".format(order.get_price()))