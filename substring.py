def count_substring(string, sub_string):
    c=0
    sub=[string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]
    for i in sub:
        if i==sub_string:
            c+=1
    return c
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
