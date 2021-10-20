def solution(genres, plays):
    answer = []
    sort_with_genre=[]
    genre_idx=[]
    for g in range(len(genres)):
        if genres[g] not in genre_idx:
            genre_idx.append(genres[g])
            temp=[g]
            for i in range(g+1,len(genres)):
                if genres[i]==genres[g]:
                    temp.append(i)
            sort_with_genre.append(temp)
    sort_with_genre.sort(key=lambda x: len(x))
    print(sort_with_genre)
    return answer
solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])