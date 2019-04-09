#Change Calculator
# Read in a cost
# Read in the amount given
# Calculate the change
# Break the change into how many nickels, dimes, quarters
# loonies, toonies, $5s, $10s, $20s, $50s, $100s
# If amount is below the cost, say how much more they owe.
cost=float(input("How much does the item cost?"))
amount=float(input("How much did you pay?"))
change=amount-cost
print("Your change is",change)
#how many 100s
num100=change//100
if(num100>0):
    print("You get",num100,"$100s")
change=change%100
#how many 50s\
num50=change//50
if(num50>0):
    print("You get",num50,"$50s")
change=change%5012
#how many 20s
num20=change//20
print("You get",num20,"$20s")
change=change%20
#how many 10s
num10=change//10
if(num10>0):
   print("You get",num10,"$10s")
change=change%10
#how many 5s
num5=change//5
if(num5>0):
   print("You get",num5,"$5s")
change=change%5
#how many 2s
num2=change//2
print("You get",num2,"$2s")
change=change%2
#how many 1s
num1=change//1
print("You get",num1,"$1s")
change=change%1
#how many 0.25s
num0_25=change//0.25
if(num0_25>0):
   print("You get",num0_25,"$0.25s")
change=change%0.25
#how many 0.10s
num0_10=change//0.10
print("You get",num0_10,"$0.10s")
change=change%0.10
#how many 0.5s
num0_5=change//0.5
print("you get",num0_5,"$0.5s")
