import argparse
from itertools import combinations
from colorama import Fore, Style

valid_charset = []
char_separator = '.'
char_wrap = "'"


payload_char_set= []


def xor_character(char1,char2):
	result = chr(ord(char1)^ord(char2))
	return result

def charset_combination(valid_charset):
	charset = []
	for r in range(1, len(valid_charset) + 1):
		combinations_r = list(combinations(valid_charset, r))
		charset.extend(combinations_r)
	return charset

def find_xor_combination(valid_charset,char):
	xor_combination = []
	charset_combinations = charset_combination(valid_charset)
	for combination in charset_combinations:
		result = combination[0]
		for j in combination[1::]:
			result = xor_character(result,j)
		if (result == char):
			xor_combination.append(combination)
	return xor_combination

def handle_payload(payload):
	for i in payload:
		payload_char_set.append(i)


def extract_char(list):
	characters_extracted_list = []
	for tuple_item in list:
		for char in tuple_item:
			characters_extracted_list.append(char)

	return characters_extracted_list

def replace_char(list,old_char,new_char):
        index = list.index(old_char)
        list[index] = new_char

def display(list):
    for i in list:
        print(i,end='')

def display_payload(list,flag):
    if(flag==1):

        print(f"{Fore.GREEN}{Style.BRIGHT}[{Fore.WHITE}{Style.BRIGHT}#{Fore.GREEN}{Style.BRIGHT}] {Fore.GREEN}{Style.BRIGHT}Encoded Payload : {Style.RESET_ALL}",end='')
        for i in list:
            print(i, end='')

    else:
        print(f"{Fore.RED}{Style.BRIGHT}[{Fore.WHITE}{Style.BRIGHT}!{Fore.RED}{Style.BRIGHT}] {Fore.RED}{Style.BRIGHT}Couldn't find any encoded payload with the given charset !")




def encode_payload(valid_charset, char_separator, char_wrap,case_sensitive):
    flag =1
    encoded_payload_set = []
    encoded_payload_string_set = []


    if(case_sensitive=="0"):
        for char in payload_char_set:
            if(find_xor_combination(valid_charset,char)!=[]):
                encoded_payload_set.append(find_xor_combination(valid_charset, char))
            else:
                if(char.isalpha()):
                    if(char==char.upper()):
                        if(find_xor_combination(valid_charset,char.lower())!=[]):
                            encoded_payload_set.append(find_xor_combination(valid_charset,char.lower()))
                            replace_char(payload_char_set,char,char.lower())
                        else:
                            encoded_payload_set.append(find_xor_combination(valid_charset,char))
                    else:
                        if(find_xor_combination(valid_charset,char.upper())!=[]):
                            encoded_payload_set.append(find_xor_combination(valid_charset,char.upper()))
                            replace_char(payload_char_set,char,char.upper())
                        else:
                            encoded_payload_set.append(find_xor_combination(valid_charset,char))

                else:
                    encoded_payload_set.append(find_xor_combination(valid_charset,char))    

    elif(case_sensitive=="1"):
          for char in payload_char_set:
                encoded_payload_set.append(find_xor_combination(valid_charset,char))

    else:
        print("variiable case senstivie is a string")
              

                    

                              
                
                      
              
    i=0
    for list in encoded_payload_set:
        i=i+1
        k=len(encoded_payload_set)
        extracted_chars = extract_char(list)
        if(extracted_chars == []):
            flag =0
            break
		
        encoded_payload_string_set.append('(')
        for char in extracted_chars:
            encoded_payload_string_set.append(char_wrap)
            encoded_payload_string_set.append(char)
            encoded_payload_string_set.append(char_wrap)
            if (char != extracted_chars[-1]):
                encoded_payload_string_set.append('^')
        encoded_payload_string_set.append(')')
        if(i != k):
             encoded_payload_string_set.append(char_separator)
        

			

	
			
    if(case_sensitive=="0"):
        print(f"{Fore.YELLOW}{Style.BRIGHT}[{Fore.WHITE}{Style.BRIGHT}/{Fore.YELLOW}{Style.BRIGHT}] {Fore.YELLOW}{Style.BRIGHT}Payload not senstive case :{Style.RESET_ALL}", end=" ")
        display(payload_char_set)

    print()
    display_payload(encoded_payload_string_set,flag)
    print()



def display_logo():
	print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣦⡀⠀⠹⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣤⣤⣤⣬⣿⣤⣄⠘⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣆⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[31;1m__   __     _____      ______ \033[0m     _     ___
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀\033[31;1m \\ \\ / /    |  __ |    | ____ \\\033[0m    (_)   /  _|
⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠶⠶⠶⠶⠶⠶⠀\033[31;1m\\ V /     | | | |    | |_/  /\033[0m     _    | |_    _   _
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[31;1m/   \\     | | | |    |  _  /\033[0m     | |   |  _|  | | | |
⠀⠀⠀⠀⠀⠀⣼⠏⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[31;1m/ /^\\ \\    \\ \\_/ /    | | \\ \\\033[0m     | |   | |    | |_| |
⠀⠛⠛⠛⢛⣿⠛⠋⢠⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \033[31;1m\\/   \\/     \\___/     \\_|  \\_|\033[0m    |_|   |_|    \\__,  |
⠀⠀⠀⣰⠟⠁⠀⣰⣿⣿⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                               __/  |
⠀⠀⠀⠁⠀                                               \033[92;1m@F0^l1shF0x\033[0m           |_____/⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	   
	   """)                                               


	





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="XOR encoding script")
    parser.add_argument("--payload")
    parser.add_argument("--valid_charset", default=['(', ')', '.', '*', ';', '^'])
    parser.add_argument("--char_separator", default='.')
    parser.add_argument("--char_wrap", default="'")
    parser.add_argument("--case_sensitive",default=1)

    args = parser.parse_args()
    payload = args.payload
    valid_charset = list(args.valid_charset)
    char_separator = args.char_separator
    char_wrap = args.char_wrap
    case_sensitive = args.case_sensitive

    payload_char_set = []
    display_logo()
    handle_payload(payload)
    print(f"{Fore.CYAN}{Style.BRIGHT}[{Fore.WHITE}{Style.BRIGHT}+{Fore.CYAN}{Style.BRIGHT}] {Fore.CYAN}{Style.BRIGHT}Char_set :{Style.RESET_ALL}",valid_charset)
    print(f"{Fore.MAGENTA}{Style.BRIGHT}[{Fore.WHITE}{Style.BRIGHT}*{Fore.MAGENTA}{Style.BRIGHT}] {Fore.MAGENTA}{Style.BRIGHT}Payload :{Style.RESET_ALL}",payload)
    

         

    encode_payload(valid_charset, char_separator, char_wrap,case_sensitive)





