"""D. Yet Another Yet Another Task
time limit per test1.5 seconds
memory limit per test512 megabytes
inputstandard input
outputstandard output
Alice and Bob are playing yet another card game. This time the rules are the following. There are n cards lying in a row in front of them. The i-th card has value ai.

First, Alice chooses a non-empty consecutive segment of cards [l;r] (l≤r). After that Bob removes a single card j from that segment (l≤j≤r). The score of the game is the total value of the remaining cards on the segment (al+al+1+⋯+aj−1+aj+1+⋯+ar−1+ar). In particular, if Alice chooses a segment with just one element, then the score after Bob removes the only card is 0.

Alice wants to make the score as big as possible. Bob takes such a card that the score is as small as possible.

What segment should Alice choose so that the score is maximum possible? Output the maximum score.

Input
The first line contains a single integer n (1≤n≤105) — the number of cards.

The second line contains n integers a1,a2,…,an (−30≤ai≤30) — the values on the cards.

Output
Print a single integer — the final score of the game.

Examples
inputCopy
5
5 -2 10 -1 4
outputCopy
6
inputCopy
8
5 2 5 3 -30 -30 6 9
outputCopy
10
inputCopy
3
-10 6 -15
outputCopy
0
Note
In the first example Alice chooses a segment [1;5] — the entire row of cards. Bob removes card 3 with the value 10 from the segment. Thus, the final score is 5+(−2)+(−1)+4=6.

In the second example Alice chooses a segment [1;4], so that Bob removes either card 1 or 3 with the value 5, making the answer 5+2+3=10.

In the third example Alice can choose any of the segments of length 1: [1;1], [2;2] or [3;3]. Bob removes the only card, so the score is 0. If Alice chooses some other segment then the answer will be less than 0."""









n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(1,31):
    res=0
    for j in arr:
        res+=j
        if(j>i):res=0

        res=max(res,0)
        ans=max(ans,res-i)
print(ans)