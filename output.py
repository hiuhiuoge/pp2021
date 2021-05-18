def cal_gpa(name):
    for key in D:
        if name in str(key.name[0]) + ' ' + str(key.name[1]):
            sco = np.array([D[key].course[ke] for ke in D[key].course])
            cre = np.array([randint(1,5) for i in range(len(sco))])
            return tuple((name, math.floor(sco.dot(cre)/sum(cre)*10)/10))
def sort():
    ls = []
    for key in D:
        ls.append(cal_gpa(str(key.name[0]) + ' ' + str(key.name[1])))
    for i in sorted(ls, key = lambda x : x[1], reverse=True):
        print(i[0] + ': ' + str(i[1]))
sort()
