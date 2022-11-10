import sys
sys.stdin = open("sources/sample_input.txt", "r")


TC = int(input())
for i in range(1, TC+1):
    N = input()
    cnt = len(N)-1
    # print(round(int(N[:3])/10))
    if round(int(N[:3])/10) == 100:
        cnt += 1
        print("#{} {}*10^{}".format(i, round(int(N[:2])/10)/10, cnt))
    else:
        print("#{} {}*10^{}".format(i, round(int(N[:3])/10)/10, cnt))
