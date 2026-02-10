def swap_case(s):
    return ''.join([aa.lower() if aa.isupper() else aa.upper() for aa in list(s)])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result) 
