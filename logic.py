#import string




def convert_measurements(input_str): #function to convert input into ints
    """
    
    """
    input_str = input_str.lower() # convert any uppercase letter into lowercase for easier processing
    mainList=list()  #creating a list to store the values
    def Char_To_Num(letter):
        if letter!="_":  #convert letters to ascsi except underscore
            return(ord(letter)-96)
        else:
            return 0
        
    inputLength = len(input_str)

    if inputLength==1:
        mainList.append(Char_To_Num(input_str[0])) #if there is only one value in the list return the value of it 
        return mainList
    
    elif inputLength<=0:
        return "Invalid input" #if there is no input return invalid input 
    
    else:    #this is where the main logic is processed
        counter=0 #i
        while(True):
            if counter>=inputLength: 
                break
            else:
                steps=0  #resets the cycle to 0
                while(input_str[counter]=='z'):  #if the first letter is Z use it to to count the number of steps, we start with the Z special cases , first while loop is for the cycling 
                    steps+=Char_To_Num(input_str[counter])
                    counter+=1
                steps += Char_To_Num(input_str[counter]) 

                if steps==0:
                    mainList.append(0)  #underscore case 
                    break

                indexSum=0


                for d in range(steps):    #counts the number of steps to count to process them and adding the values 
                    counter+=1
                    if counter>=inputLength:
                        break

                    while(input_str[counter]=='z'):      #2nd Z case, if there is multiple Z's in the same cycle 
                        indexSum+=Char_To_Num(input_str[counter])
                        counter+=1
                    
                    indexSum+=Char_To_Num(input_str[counter])

                counter+=1
                mainList.append(indexSum)
            
        return mainList


print(convert_measurements("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa"))
print(convert_measurements("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_"))
print(convert_measurements("dz_a_a"))
print(convert_measurements("azza"))
print(convert_measurements("dz_a_aazzaaa"))
print(convert_measurements("abbcc"))
print(convert_measurements("a"))
print(convert_measurements("aa"))
print(convert_measurements("a_"))
print(convert_measurements("abcdabcdab"))
print(convert_measurements("abcdabcdab_asas"))
print(convert_measurements("_"))
print(convert_measurements("_ad"))
print(convert_measurements("a_"))
print(convert_measurements("_______"))
print(convert_measurements("aaa"))



# if z inside a cycle dont  count step only value
# if z is the first letter that indicates a cycle add the number next to it to the number of steps