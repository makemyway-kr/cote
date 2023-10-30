today = "2022.05.19"
terms = 	["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
answer = []


def getTimeStamp(year,month, day):
  return 28*12*year + 28*month + day
[year, month, day] = list(map(int, today.split('.')))
timeStamp = getTimeStamp(year, month, day)
termsMap = {}
for t in terms:
  splittedTerm = t.split(' ')
  termsMap[splittedTerm[0]] = int(splittedTerm[1]) * 28

for i, privacy in enumerate(privacies):
  monthDiff = 0
  [date, term] = privacy.split(' ')
  [y,m,d] = list(map(int,date.split('.')))
  dateDiff = timeStamp - getTimeStamp(y,m,d)
  if dateDiff >= termsMap[term]:
    answer.append(i+1)