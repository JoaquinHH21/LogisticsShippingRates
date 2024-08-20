#Shipping Cost Calculator

##Input package weight and shipping rate
weight = float(input("Enter the weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilograms: "))

## Calculate the shipping cost
shipping_cost = weight*rate

## Display the result
print(f"Shipping Cost:  {shipping_cost} USD")
