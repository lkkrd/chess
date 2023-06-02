#działanie: trace(B5 zwraca (5, 2))
def trace(field: str):
   if len(field) != 2:
      print ('Wrong field given (too long)')
      return
   
   y = field[0].upper()
   x = field[1]
   cols = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

   if not (y in cols):
      print (f'y () not in cols')

   if not int(x) in range (1, 9):
      print(f'Wrong field given! ({x} not exitst)')
      return
      
   try:
      return (int(x), int(cols[y]))
   except:
      print('wrong field given')
      return


# cols = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
# print(cols['E'])
print(trace('e4'))
print(trace('a5'))
print(trace('97'))