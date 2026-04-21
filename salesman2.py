bags=int(input("enter number of bags"))
cost=int(input("enter cost"))
damaged_bag=5
total_bags=bags-damaged_bag
cost_of_one_bag=cost//total_bags
print( "cost of one bag is:",cost_of_one_bag)