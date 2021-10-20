import os
import random
import string

file1 = open('dataStoredFile.py', 'w')

i = 4
while i > 0:
  #print(i)
  # alphabetical strings
  A = (random.randrange(7, 15))
  alphabetical_strings1 = string.ascii_letters
  alphabetical_strings = ''.join((random.choice(alphabetical_strings1) for i in range(A)))
  #print(alphabetical_strings)

  # real numbers =
  real_numbers = round(random.uniform(1, 150), 2)
  #print(real_numbers)

  # generate random integers
  integers = (random.randrange(1, 1000000))
  #print(integers)

  # making spaces for alphanumerics
  B = (random.randrange(7, 15))
  alphanumerics1 = string.ascii_letters + string.digits
  alphanumerics2 = ''.join((random.choice(alphanumerics1) for i in range(B)))
  #print(alphanumerics2)
  spaces = (random.randrange(0, 10)) #make spaces
  q = " " * spaces
  # print(" " *spaces+alphanumerics+" " *spaces
  alphanumerics = q + alphanumerics2 + q
  #print(q + alphanumerics2 + q)

  print(alphabetical_strings + "," + str(real_numbers) + "," + str(integers) + "," + alphanumerics)
  store_file=(alphabetical_strings + "," + str(real_numbers) + "," + str(integers) + "," + alphanumerics)
  file1.writelines(store_file)
  file1.writelines("\n")

  i -= 1


# Find the file size for stored data file

file_size = os.path.getsize('dataStoredFile.py')
file_size_in_Mega1 = round(file_size / (1024 * 1024), 3)
file_size_in_Mega = str(file_size_in_Mega1)
print(file_size_in_Mega + "MB")
