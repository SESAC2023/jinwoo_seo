"""
시간 제한이 0.15초인 문제로, 반복문을 통해 해결하려 한다면
1,000,000,000 같은 입력값이 들어왔을 경우 당연히 시간 초과가 나고 말 것이다.
그렇다면 단순 계산식을 통해 해결할 수 있는 문제라는 말이다.
단순히 생각해보자면, 낮에 A만큼 올라가고 밤에 B만큼 미끄러지니 하루에 A-B 만큼 올라간다는 것을 알 수 있다.
다만, V만큼 올라가기만 하면 B만큼 내려오는 것은 계산에 포함하면 안 된다.
따라서 최대 높이에서 미끄러질 길이를 미리 빼 주면 된다.
그리고 남은 높이를 하루에 올라가는 비율로 나눠주면 끝.
"""

import sys
input = sys.stdin.readline
import math
a,b,v = map(int,input().split())
print(math.ceil((v-b)/(a-b)))
