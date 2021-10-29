try:
    f = open("hgb.txt", "w")
    while True:
        s = input('请输入字符串（按Q结束）')
        if s.upper() == 'Q': break
        f.write(s + '\n')
except KeyboardInterrupt:
    print("程序中断（ctr+c）")
finally:
    f.close()
