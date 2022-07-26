scores = [
    [49, 80, 20, 100, 80],
    [43, 60, 85, 30, 90],
    [49, 82, 48, 50, 100]
    ]
#이정도는 이해해야함
sum_score = [0, 0, 0, 0, 0]
sum_score = [for i in scores[0]]

for subject in scores:
    #i = 0
    for i, score in enumerate(subject):#subject같이 순번이 있는 것을 뽑아줌  이거 생각아안나면 주석처리 한것처럼 해도 ㄱㅊ
        sum_scores[i] += score
        #i+=1

#avg_scores = []
#for score in sum_scores:
    #avg_scores.append(score / len(scores))
avg_scores = [ score / len(scores) for score in sum_scores]

print(avg_scores)