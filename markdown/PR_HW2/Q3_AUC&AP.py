def Count(x,l):
    n=0
    for i in range(len(l)):
        if x==l[i]:
            n+=1
    return n

scores=[]
for i in range(10):
    scores.append(round(1.0-i*0.1,1))

labels=[1,2,1,1,2,1,2,2,1,2]

#Question c swap line 9 and line 10
#labels=[1,2,1,1,2,1,2,2,2,1]

P = [1.0]
R = [0.0]
AUC_PR=[]
AP=[]

for i in range(len(scores)):
    P.append(Count(1,labels[:i+1])/(i+1))
    R.append(Count(1,labels[:i+1])/Count(1,labels))
    AUC_PR.append((P[i+1]+P[i])*(R[i+1]-R[i])/2)
    AP.append((R[i+1]-R[i])*P[i+1])
AUC_PR_SUM=sum(AUC_PR)
AP_SUM=sum(AP)

print('P:', ['%.4f' % f for f in P])
print('R:', ['%.4f' % f for f in R])
print('AUC_PR:', ['%.4f' % f for f in AUC_PR])
print('AUC_PR_SUM:', '%.4f' % AUC_PR_SUM)
print('AP:', ['%.4f' % f for f in AP])
print('AP_SUM:', '%.4f' % AP_SUM)