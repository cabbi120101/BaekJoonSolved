T = int(input())
for tc in range(1,T+1):
    W = input()
    K = int(input())
    w_dict = dict()
    w_check = dict()
    for idx,i in enumerate(W):
        if i in w_dict:
            w_dict[i] += 1
            w_check[i] += [idx]
        else:
            w_dict[i] = 1
            w_check[i] = [idx]
    word_list = [i for i in w_dict if w_dict[i] >= K]

    ans1 = -1
    ans2 = len(W)

    if not word_list:
        print(-1)
    else:
        for word in word_list:
            for i in range(len(w_check[word])-K+1):
                ans1 = max(ans1, w_check[word][i+K-1] - w_check[word][i]+1)
                ans2 = min(ans2, w_check[word][i+K-1] - w_check[word][i]+1)
        print(ans2, ans1)