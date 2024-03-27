all_prob_dic = {}
topics = []

f = open('neetcodeproblemtable.md', 'r')
data = f.read().split('###')
for group in data:
    g = group.split('\n')
    topics.append(g[0].strip())
    prob_dic = {}
    group_list = []
    for line in g:
        if line[:6]=="<sub>[":
            problem = line.split("</sub>")[0][5:]
            prob_dic['id'] = (problem.split(']')[0][1:].split(' - ')[0], problem.split(']')[0][1:].split(' - ')[1],problem.split(']')[1][1:-1])
            group_list.append(prob_dic)
    all_prob_dic[g[0].strip()] = group_list

            # prob_info = {}
            # prob_info{}
            

#print(data[1].split('<sub>'))
f.close()
for p in all_prob_dic:
    print(p)
    for s in all_prob_dic[p]:
        print('\t', s)