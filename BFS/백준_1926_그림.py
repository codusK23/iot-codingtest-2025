'''
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값 갱신

2. 시간복잡도
- BFS: O(V+E)
- V: 500 *500
- E: 4 * 500 * 500
- V + E: 5 * 250000 = 100만 < 2억 >> 가능!

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문: bool[][]
- queue(BFS)
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
maxv = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    
    while q:
        ey, ex = q.popleft()
        
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            
            if 0 <= ny < n and 0 <= nx < m:
                if pic[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny, nx))
                    rs += 1

    return rs

for j in range(n):
    for i in range(m):
        if pic[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j, i))
            
print(cnt)
print(maxv)