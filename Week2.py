#Banyan Girroir
#James Cagney
#CS 161
#1/19/2025

#part 1
x = 31
print (x, bin(x), hex(x))

#part 2
x = 1.825
#print (x, bin(x), hex(x))
#If decimal is typed, this error will show: TypeError: 'float' object cannot be interpreted as an integer
#This will happen because the bin function is expecting an integer not a decimal
#Change the value of x to x = 18
x = 18

#Part 3
y = 0b1011
z = 0xA3
print (y, z)

#Part 4
w = x + y + z
print ('the sum is ' , w)

#Compresstion
#This program will calculate the percent of compression given the formula:
#Percent of compression = 1 - ((Compressed Text Size + Dictionary size)  divided by original size).   (100% = 1)
original_size = 240
dictionary_size = 25
compressed_text_size = 148
print(' 	      Dictionary size:', str(dictionary_size), 'characters')
print('     compressed text size:', str(compressed_text_size), 'characters')
total = compressed_text_size + dictionary_size
print('                    Total:', str(total), 'characters')
print(f"         original size is: {original_size} characters")
percent_of_compression = (1 - ((compressed_text_size + dictionary_size) / original_size)) * 100
print (f"Percent of compression is: {percent_of_compression:.4g}%")