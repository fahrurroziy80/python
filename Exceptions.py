try:
  print(10 / 2)
except ArithmeticError:
  print("Error in calculation")
except:
  print("Something else went wrong")


try:
    print (10 + -1212)
except ArithmeticError:
    print("hasilnya eror")
except:
    print("hasilnya benar")

