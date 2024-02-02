import argparse
from itertools import combinations

valid_charset = ['(',')','.','*',';','^']
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
			
		

def handle_input():
	payload = input("enter your string :")
	for i in payload:
		payload_char_set.append(i)


def extract_char(list):
	characters_extracted_list = []
	for tuple_item in list:
		for char in tuple_item:
			characters_extracted_list.append(char)

	return characters_extracted_list

def display_paylaod(list):
	for i in list:
		print(i, end='')




def encode_payload():
	encoded_payload_set = []
	encoded_payload_string_set = []
	for char in payload_char_set:
		encoded_payload_set.append(find_xor_combination(valid_charset,char))

	for list in encoded_payload_set:
		characters_extracted_list = extract_char(list)
		encoded_payload_string_set.append('(')
		for char in characters_extracted_list:
			encoded_payload_string_set.append(char_wrap)
			encoded_payload_string_set.append(char)
			encoded_payload_string_set.append(char_wrap)

			if(char != characters_extracted_list[-1]):
				encoded_payload_string_set.append('^')

		encoded_payload_string_set.append(')')
		if (list != encoded_payload_set[-1]):
			encoded_payload_string_set.append('.')


	
	display_paylaod(encoded_payload_string_set)






handle_input()
encode_payload()




