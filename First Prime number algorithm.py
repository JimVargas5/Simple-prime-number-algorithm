def is_prime(n):
    if n%1==0:
        if n>1:
            if (n**.5)%1!=0:
                for i in range(2, int(n**.5)+1):
                    check = n%i
                    #print(check)
                    if check==0:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False
    return True


def main(alist):
    for i in alist:
        print(i, is_prime(int(i)))


List = range(1,20)
#main(List)
print(is_prime(3))