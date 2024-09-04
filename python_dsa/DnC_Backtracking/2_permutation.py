


def print_permutation(s, i):
    if i>=len(s):
        print(s, end=' ')
        return

    s_list = list(s)
    for j in range(i, len(s)):
        s_list[i], s_list[j] = s_list[j], s_list[i]
        print_permutation("".join(s_list), i+1)
        s_list[i], s_list[j] = s_list[j], s_list[i]


if __name__ == "__main__":
    string = "abc"
    # Start the permutation process from the first index.
    print_permutation(string, 0)