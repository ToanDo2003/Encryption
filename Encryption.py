




def encode():
    '''Encodes a input text from a message to a code.
    
    Argument:
    There's no argument because the code used the local variable which is created by running the function
    '''

    input_text = input('Please enter the text to be processed: ',)                                      
    alphabets = ('abcdefghijklmnopqrstuvwxyz')                                                          

    new_cipher_text = check_cipher()                                                                    

    if new_cipher_text == False:                                                                        
        return False                                                                                    
    else:                                                                                               
        code_dict = dict(zip(alphabets, new_cipher_text))                                                                                 
        output_text = ''                                                                                

        for i in range (len(input_text)):                                                               
            if input_text[i] in code_dict.keys():                                                       
                output_text += code_dict[input_text[i]]                                                 

        print('Your cipher is valid.')                                                                  
        return output_text                                                                              
def decode():
    '''Decodes a code from a message to a message.
    
    Argument:
    There's no argument because the code used the local variable which is created by running the function
    '''

    input_text = input('Please enter the text to be processed: ',)                                      
    alphabets = ('abcdefghijklmnopqrstuvwxyz')                                                          

    new_cipher_text = check_cipher()                                                                    

    if new_cipher_text == False:                                                                        
        return False                                                                                    
    else:                                                                                               
        code_dict = dict(zip(new_cipher_text, alphabets))                                                                                 
        output_text = ''                                                                                

        for i in range (len(input_text)):                                                               
            if input_text[i] in code_dict.keys():                                                       
                output_text += code_dict[input_text[i]]                                                 

        print('Your cipher is valid.')                                                                  
        return output_text                                                                              
def check_cipher():
    '''Lower the cipher text, make the cipher text into a unique cipher and check the new cipher if it is alphanumeric and has 26 characters. Then return the a new cipher if it is valid. 
    
    Argument:
    There's no argument because the code used the local variable which is created by running the function
    '''

    cipher_text = input('Please enter the cipher text: ',)                                              

    low_cipher_text = cipher_text.lower()                                                              

    cipher_unique = ''                                                                                
    for i in range(len(low_cipher_text)):                                                             
        if low_cipher_text[i] not in cipher_unique:                                                     
            cipher_unique += low_cipher_text[i]                                                        
    new_cipher_text = cipher_unique                                                                    

    if len(new_cipher_text) == 26 and new_cipher_text.isalnum() == True:                                
        return new_cipher_text                                                                          
    else:                                                                                              
        return False                                                                                    
    
print("ENDG 233 Encryption Program")                                                                        
### Main program code here
text_option = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ',)                  
while text_option != '1' and text_option != '2' and text_option != '0':
    text_option = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ',)
while text_option == '1' or text_option == '2':                                                               
    if text_option == '1':                                                                                  
        output = encode()                                                                                   
        if output == False:                                                                                 
            print('Your cipher must contain 26 unique elements of a-z or 0-9')                              
        else:                                                                                               
            print(f'Your output is: {output}')                                                              
            print('')                                                                                       
            text_option = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ',)
            while text_option != '1' and text_option != '2' and text_option != '0':
                text_option = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ',)  
    elif text_option == '2':                                                                                
        output = decode()                                                                                   
        if output == False:                                                                                 
            print('Your cipher must contain 26 unique elements of a-z or 0-9')                              
        else:                                                                                                      
            print(f'Your output is: {output}')                                                              
            print('')                                                                                       
            text_option = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ',)
            while text_option != '1' and text_option != '2' and text_option != '0':
                text_option = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ',)  

    
if text_option == '0':                                                                                     
    print('Thank you for using the encryption program.')                                                   
