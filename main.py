number = input ("Enter temperature: ")
type = input("Enter unit in F/f or C/c: ")

if(type == "c" or "C"):
  F= (float (number)*1.8)+32;
  print(str(float(number))+ "° in Celsius is equivalent to " + str(F) + "° Fahrenheit.")

elif(type== "f" or "F"):
  C = (float (number)-32)*5/9;
  print(str(float(number))+ "° in Fahrenheit is equivalent to " + str(C) + "Celsius° .")

else:
  print ("Invalid nuit ("+type+").")

