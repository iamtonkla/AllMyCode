
time = 0
password = 'Amazon'
max_time = 3
#Variables Zone

#Password Insert vvvv
while True:

    PIN = input('Enter password')

    if PIN == password:
        print(':)')
        break 
        

    else:
        print ("Try Again")
        time +=1
        
    if time == max_time:
            print('FAIL')
            break
#Time limit /\/\/\/\/\
    