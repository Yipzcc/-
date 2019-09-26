# 多段图-向前处理算法


grap_out = {'0': [('1', 9), ('2', 7)],
            '1': [('3', 2), ('4', 1)],
            '2': [('3', 7)],
            '3': [('5', 3)],
            '4': [('5', 5), ('6', 6)],
            '5': [('7', 2)],
            '6': [('7', 5)],
            '7': []
            }         # K段图字典形式的表示(出边表)


def f_graph(n):
    cost = [100] * n
    d = [0] * (n-1)
    p = []

    cost[n-1] = 0                   # 将多段图最后一个结点置0
    for i in range(n-2, -1, -1):   # 遍历 6-0 结点的多段图
        e = grap_out[str(i)]        # i所有的出度的边

        for s in e:
            m = s[1] + cost[int(s[0])]       # 设r是一个这样的结点,<i,r>是边,且使 c(i, r)+cost(r) 取最小值
            if m < cost[i]:
                cost[i] = m                  # 使 c(i, r)+cost(r) 取最小值
                d[i] = s[0]                  # 记录当前结点的下一个结点

    p.append('0'); #p[k-1] = str(n-1)           # 将开始结点 和 结束结点 初始化
    j = 1
    # for j in range(1, k):                   # 计算其余k-2个结点 range生成1到k-1数组
    length = d.__len__()-1
    while int(p[j-1]) < length:
        p.append(d[int(p[j-1])])              # p[j-1]记录当前结点的下一个最短路径结点
        j += 1

    print(p)                                 # 输出最短路径
    print(cost[0])

if __name__ == '__main__':
    f_graph(grap_out.__len__())          # k=5(即5段图),共12个结点