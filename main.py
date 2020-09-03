# Author: Haorong Xu hxx5086@psu.edu
# Collaborator: Jerry Diaz jqd5879@psu.edu
# Collaborator: Jocelyn Fafard jqf5530@psu.edu
# Collaborator: Nicholas Cole nyc5096@psu.edu


number = input ("Enter temperature: ")
type = input("Enter unit in F/f or C/c: ")

if type == "C" or type == "c":
  F= (float (number)*1.8)+32;
  print(f"{number}° in Celsius is equivalent to {F}° Fahrenheit.")


elif type== "f" or type == "F" :
  C = (float (number)-32)*5/9;
  print(f"{number}° in Fahrenheit is equivalent to {C}° Celsius.")


else:
  print(f"Invalid unit({type}).")

