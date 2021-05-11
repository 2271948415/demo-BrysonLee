def judge(a,b,c,tag):
    #分别判断边长是否在允许范围内，不在则提示错误信息。
    if 1<=a<=200 and 1<=b<=200 and 1<=c<=200:
        tag = True
        return tag
    else:
        tag = False
        if a<1 or a>200:
            print("a不在允许取值的范围内！")
        if b<1 or b>200:
            print("b不在允许取值的范围内！")
        if c<1 or c>200:
            print("c不在允许取值的范围内！")
        return tag
def tran(a,b,c):
    #根据边长判断三角形类型
    if a<b+c and b<a+c and c<a+b:
        if a==b and b==c:
            print("等边三角形")
        elif a!=b and b!=c and c!=a:
            print("普通三角形")
        else:
            print("等腰三角形")
    else:
        print("非三角形")
if __name__ == '__main__':
    try:
        tag = True
        a = int(input("请输入a的边长: "))
        b = int(input("请输入b的边长: "))
        c = int(input("清输入c的边长: "))
        DEMO = judge(a,b,c,tag)
        if DEMO is True:
            tran(a,b,c)
    except Exception as e:
        print("请输入数字！")