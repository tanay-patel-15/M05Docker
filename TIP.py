import emoji
from colorama import Fore



def calculate_tip():
    
  # Get user inputs for bill amount, tax rate, and tip percentage.
  bill = float(input(emoji.emojize("Enter the bill amount :money_with_wings:: ")))
  tax_rate = float(input(emoji.emojize("Enter the tax rate (%) :money_bag:: "))) / 100
  tip_percentage = float(input(emoji.emojize("Enter the tip percentage (%) :money-mouth_face:: "))) / 100
  
  # Calculate the tax and tip amounts.
  tax = bill * tax_rate
  tip = bill * tip_percentage
  
  # Calculate the total cost with tax and tip added.
  total_cost = bill + tax + tip
  
  print(Fore.GREEN + "\nYour total cost includes:")
  print(Fore.MAGENTA + "%.2f in tax" % tax)
  print("%.2f in tip" % tip)
  print(emoji.emojize(Fore.GREEN + "So your total cost is %.2f. :green_circle:" % total_cost))

# Call the function to run the program.

if __name__ == "__main__":
    calculate_tip()