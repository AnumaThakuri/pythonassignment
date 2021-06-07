'''print the following:
00000000
 000000
  000
   0'''

for length in range(1,8,2):
    print(' '*(length-1)+"O "*(8-length))

