def solution(genres, plays):
    answer = []
    sort_with_genre=[]
    genre_idx=[]
    for g in range(len(genres)):
        if genres[g] not in genre_idx:
            genre_idx.append(genres[g])
            temp=[g]
            tempp=plays[g]
            for i in range(g+1,len(genres)):
                if genres[i]==genres[g]:
                    temp.append(i)
                    tempp+=plays[i]
            sort_with_genre.append([temp,tempp])
    sort_with_genre.sort(key=lambda x: x[1],reverse=True)
    for s in sort_with_genre:
        s[0].sort(key=lambda x: plays[x],reverse=True)
        if len(s[0])>1:
            answer.append(s[0][0])
            answer.append(s[0][1])
        else:
            answer.append(s[0][0])
    print(answer)
    return answer
solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])