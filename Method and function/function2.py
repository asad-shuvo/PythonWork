
def check(str):
    if 'dd' in str:
        return True
    else:
        return False

ret = check('dd in it')
print(ret)

def check2(str):
    return 'dd' in str

print(check2('dd in it'))