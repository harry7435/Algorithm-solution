def solution(genres, plays):
    answer = []
    music = {}
    play = {}
    # 고유번호, (장르, 재생횟수) 순으로 music_list 생성
    # 장르별 총 재생횟수 playlist 생성
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        music[i] = (g, p)
        if g in play:
            play[g] += p
        else:
            play[g] = p
    # 재생횟수 큰 순 정렬
    music_list = list(music.items())
    music_list.sort(key=lambda x: (x[1][0], -x[1][1]))
    playlist = list(play.items())
    playlist.sort(key=lambda x: -x[1])
    # 베스트 앨범 수록
    for song in playlist:
        genre = song[0]
        limit = 0
        for info in music_list:
            info_genre = info[1][0]
            song_number = info[0]
            if info_genre == genre:
                answer.append(song_number)
                limit += 1
            # 최대 2곡까지 수록
            if limit == 2: break

    return answer