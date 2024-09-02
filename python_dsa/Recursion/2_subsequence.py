



def print_subseq(str1, output, index, ans):
    if index==len(str1):
        ans.append(output)
        return

    print_subseq(str1, output+ str1[index] , index+1, ans)
    print_subseq(str1, output, index + 1, ans)

ans=[]
print_subseq("abc", "", 0, ans)
print(ans)
