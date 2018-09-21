import math

fr = open("prime_nums.txt" , "r")
text = fr.read()
fr.close()

number_list = text.split()
number = int(number_list[-1])


not_prime = 0

while True:
     number += 1
     num = 1
     for i in range(number-2):
          num += 1
          if number % num == 0:
               not_prime = 1

     if not_prime == 1:
          not_prime = 0
     else:
          number_list.append(number)
          fr = open("prime_nums.txt" , "r")
          text = fr.read()
          fr.close()
          
          fw = open("prime_nums.txt" , "w")
          fw.write(text + "\n" + str(number))
          fw.close()
          
          print(number)

                    
                    

     

