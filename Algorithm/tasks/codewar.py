#1
#Check to see if a string has the same amount of 'x's and 'o's. 
#The method must return a boolean and be case insensitive. The string can contain any char.

"""def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('xo'))
print(xo('xox'))
print(xo('xxo'))
print(xo('aaaddr'))"""


#2
#Write a function that takes an integer as input, and returns the number of bits that are equal to one 
# in the binary representation of that number. You can guarantee that input is non-negative.


    #print("{0} in binary {0:08b}".format(n))
"""def count_bits(n):
    count=0
    while(n):
        count+=n&1
        n>>=1
    return count
   
print(count_bits(9))"""


#3
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, 
# pictures or other items. We want to create the text that should be displayed next to such an item.
#Implement a function likes :: [String] -> String, which must take in input array, containing the names 
# of people who like an item. It must return the display text as shown in the examples:

"""def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

print(likes(['Roman','Vasss']))"""