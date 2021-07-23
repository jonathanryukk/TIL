# 1번



```python
def movie_info(movie):  # movie딕셔너리에 저장된 값중 추출해야할 값들만 추출후 리턴
    info =  {'id': movie['id'], 
            'title' : movie['title'],
            'poster_path':movie['poster_path'],
            'vote_average' : movie['vote_average'],
            'overview': movie['overview'], 
            'genre_ids':movie['genre_ids']}
    return info
```





# 2번

```python
def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.

    genres_name = [] # 새로운 딕셔너리에 name값 저장

    for i in genres:	
        for genre_id in movie['genre_ids']:
            if i['id'] == genre_id:
                genres_name.append(i['name'])
    
    info = {
        'id' : movie['id'],
        'title' : movie['title'],
        'poster_path' : movie['poster_path'],
        'vote_average' : movie['vote_average'],
        'overview' : movie['overview'],
        'genres_name' : genres_name
    }
    return info
```



# 3번

```python
def movie_info(movies, genres):

     
    highscore_movies = [] # Top20 영화들의 각각의 result 값 저장
    for i in range(20):   # `movies` 안 영화들의 `vote_average`값이 정렬되어 있어 원본을 사용                   
        result = {}
        genres_name = []  
        for genre in genres:   #problem b 참고하여 장르 name 추출
            for genre_id in movies[i]['genre_ids']:
                if genre['id'] == genre_id:
                    genres_name.append(genre['name'])
        result = {
            'id': movies[i]['id'],
            'overview' : movies[i]['overview'],
            'poster_path' : movies[i]['poster_path'],
            'title' : movies[i]['title'],
            'vote_average' : movies[i]['vote_average'],
            'genres_name' : genres_name
        }
        highscore_movies.append(result)    # `highscore_movies` 리스트에 영화 정보 추가
    return highscore_movies
```



# 4번

```python
def max_revenue(movies):
# for 반복문을 이용해 `movie_id`를 key로, `revenue`를 value로 dictionary 생성
    movie_revenues = {}
    for i in range(len(movies)):
        movie_id = movies[i]['id']
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_detail = json.load(movie_json)

        movie_revenues[movie_id] = movie_detail['revenue']

    for movie in movies:
        # `movie_revenues` dictionary의 max value를 갖는 key 값을 출력 & `title` 배포
        if movie['id'] == max(movie_revenues, key=lambda k: movie_revenues[k]):
            return movie['title']   
        
```



# 5번

```python
def dec_movies(movies):
# 12월에 개봉한 영화들을 찾아 `December_movie`에 저장
    December_movie = {}
    for i in range(len(movies)):
        # `movie_id`를 이름으로 하는 파일 입력
        movie_id = movies[i]['id']
        movie_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_detail = json.load(movie_json)

        # 입력된 파일에서 `release_date` 값을 찾아 12월 개봉 영화의 `id` 저장
        if movie_detail['release_date'][5:7] == '12':
            December_movie[movie_id] = movie_detail['release_date']
    
    # 위에서 얻은 `id` 기반 영화의 `title` 출력
    December_movie_list = []
    for movie in movies:
        if movie['id'] in December_movie.keys():
            December_movie_list.append(movie['title'])
    
    return December_movie_list 
        
```

