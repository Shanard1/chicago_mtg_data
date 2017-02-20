numbers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']

#print (len(numbers)-3)/4

letter_groups_to_make = (len(numbers)-3)/4

for i in xrange(letter_groups_to_make):
    print i, numbers[2], numbers[(i*4)+3], numbers[(i*4)+4], numbers[(i*4)+5], numbers[(i*4)+6]

letter_group = {
    'name': numbers[2]
}

'''
for i in xrange((len(numbers)-3)/4):
    letter_group = {'name': numbers[2],
        letter_group['pickles'] = 'value'
    }
'''