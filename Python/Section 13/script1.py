try:
	with open('sad.txt', mode='e') as my_file:
		print(my_file.read())
	

except FileNotFoundError as err:
   print('file does nnot exist')
   raise err

except IOError as err:
   print('IO Error')
   raise err   


	