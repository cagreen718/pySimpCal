def main():
  print("Welcome! Here are some important information about the benefits of vitamins!")
  print("0)Exit\n1)VitiminA\n2)VitiminB6\n3)VitaminC\n4)VitaminD\n5)VitaminB12")
  opt=int(input("Please enter a number from 1 to 5 but 6 if you want quit:"))
  
  while opt!=0:
    if opt==1:
      print ("Vitamin A protects eyes fromnight blindness")
    if opt>5:
      print("Error! Invalid number!")

    if opt==2:
      print ("Vitamin B6 promotes brain health")
    if opt>5:
      print("Error! Invalid number!") 

    if opt==3:
      print ("Vitamin C protects your health from cancer and strokes")  
    if opt>5:
      print("Error! Invalid number!")

    if opt==4:
      print ("Vitamin D reduces the risk of diabetes")
    if opt>5:
      print("Error! Invalid number!")
      
    if opt==5:
      print("Vitamin B12 may decrease homo-cystenine")    
    if opt>5:
      print("Error! Invalid number!")

    print("0)Exit\n1)VitiminA\n2)VitiminB6\n3)VitaminC\n4)VitaminD\n5)VitaminB12")
    opt= int(input("Please select one of options above:"))
  print("Goodbye")
main()  