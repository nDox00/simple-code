
# Print
loc = input('Location? ') .title()

if loc == 'Home':
    print('Welcome Home')
    
elif loc == 'Shopping':
    print('Enjoy!')
else:
    print('Come Home!')
    
 # Number Counter
 x = 0

while x<5:
    print(f'The current value of x is {x}')
    print(f' x <5 so adding 1')
   #print('Continuing...')
    x += 1
    if x < 5:
        print('Continuing...') 
else:
    print('x is not <5')


#Number Checker
def any_num_check(mylist):
    
    even_num = []
    odd_num = []
    
    for _ in mylist:
        if _ %2 == 0:
            #print(_)
            even_num.append(_)
        
        elif _ %2 != 0:
            #print(_)
            odd_num.append(_)
        
        
         #return False
        #pass
    if len(even_num) >0:
        return even_num
    else:
        return odd_num
  
  
# Capitalisation Counter
    def uppercaseit(s):
    uppercase = 0
    lowercase = 0
    
    for _ in s:
        if _.isupper():
            uppercase += 1
        elif _.islower():
            lowercase += 1
        else:
            pass
    print(f'No. of Upper case characters: {uppercase}')
    print(f'No. of Upper case characters: {lowercase}')
