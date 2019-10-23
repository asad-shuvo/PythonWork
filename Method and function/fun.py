
def pig_atin(w):
    first_letter=w[0]
    if first_letter in 'aeiou' :
        return w+'ay'
    else:
        return w[1:]+w[0]+'ay'

print(pig_atin('appale'))
print(pig_atin('ppale'))


