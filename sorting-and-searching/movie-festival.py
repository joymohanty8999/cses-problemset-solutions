import sys
from typing import List, Tuple

input = sys.stdin.readline

def solution(movies: List[Tuple[int,int]]) -> int:

    #sort on basis of end time
    movies.sort(key=lambda x : x[1])

    timeElapsed, moviesWatched = 0,0

    for movie in movies:

        if movie[0] >= timeElapsed:
            moviesWatched += 1
            timeElapsed = movie[1]

    return moviesWatched


def main():

    n = int(input())
    movies = list()

    for i in range(0,n):
        start,end = map(int, input().split())
        movies.append((start,end))

    print(solution(movies))


if __name__ == '__main__':
    main()
