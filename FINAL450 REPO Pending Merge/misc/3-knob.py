




if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        volume, bass, treble = map(int, input().split())
        #out_ = solve(volume, bass, treble)
        print(mSteps(358, 1))
        print(mSteps(357, 1))
        #print(out_)