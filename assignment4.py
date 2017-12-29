import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import sys

outfile = open('myAnswer.txt', 'w')
outfile2 = open('retrievedData.txt', 'w')
infile = open(sys.argv[1], 'r')
columnName = infile.readline()
columnName = columnName.rstrip('\n')
columnName = columnName.split(',')
# ['State of Dist', 'Total Vote', 'Electoral', 'Obama', 'Romney', 'Johnson', 'Stein', 'Others']
# ['STATE','TOTAL VOTES','BARACK OBAMA','JOHN McCAIN']

names = []
sys.argv[2] = sys.argv[2].rstrip('\n')
sys.argv[2] = sys.argv[2].split(
    ',')  # *****arg2 = #['BARACK OBAMA', 'JOHN McCAIN'] ///// ['Obama', 'Romney', 'Johnson', 'Stein']

for name in sys.argv[2]:
    names.append(name)

# names----> ['BARACK OBAMA', 'JOHN McCAIN'] ///// ['Obama', 'Romney', 'Johnson', 'Stein']

def retrieveData(filename, nom_names):
    outList = []
    global columns
    columns = defaultdict(list)

    with open(filename) as csvfile:
        readcsv = csv.DictReader(csvfile)
        for row in readcsv:
            for (key, value) in row.items():
                columns[key].append(value)
    for nom in nom_names:
        outList.extend(columns[nom])
    outList = [int(i) for i in outList]
    outfile2.write(str(outList))
    return outList


def DispBarPlot():
    states = columns[columnName[0]]
    fig, ax = plt.subplots()
    index = np.arange(len(states))
    bar_width = 0.15
    columns[eachtotalVote[sortedList[1]]] = [int(i) for i in columns[eachtotalVote[sortedList[1]]]]
    columns[eachtotalVote[sortedList[0]]] = [int(i) for i in columns[eachtotalVote[sortedList[0]]]]
    nom1 = plt.bar(index + 2 * bar_width, columns[eachtotalVote[sortedList[1]]], bar_width, color='r',
                   label=eachtotalVote[sortedList[1]])
    nom2 = plt.bar(index + 3 * bar_width, columns[eachtotalVote[sortedList[0]]], bar_width, color='b',
                   label=eachtotalVote[sortedList[0]])
    plt.xlabel('States')
    plt.ylabel('Vote Count')
    plt.xticks(index + 3 * bar_width, states, rotation='vertical', ha='center', fontsize=7)
    plt.subplots_adjust(left=0.12, right=0.9, top=0.9, bottom=0.21)
    plt.xlim((0, len(states)))
    plt.legend()
    plt.tight_layout()
    plt.savefig('ComparativeVotes.pdf', bbox_inches=None)
    plt.close()


def compareVoteonBar():
    nom = []  # nom = ['Obama', 'Romney', 'Johson', 'Stein']
    for i in range(len(sortedList)):
        name = eachtotalVote[sortedList[i]]
        nom.append(name)

    data = [float("%.3f" % ((100 * vote) / sum(sortedList))) for vote in sortedList]  # [51.258, 47.384, 0.992, 0.365]
    perdata = [str(i) + '%' for i in data]
    x_pos = [x for x in range(len(data))]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    colorsBox = ['r', 'b', 'y', 'c', 'purple', 'green', 'k', 'magenta', 'firebrick']

    for x in range(len(nom)):
        ax.bar(x_pos[x], data[x], color=colorsBox[x], label=nom[x], align='center')

    plt.xticks(x_pos, perdata)
    plt.xlabel('Nominees')
    plt.ylabel('Vote percentages')

    # fmt = '%.0f%%'
    # xticks = ticker.FormatStrFormatter(fmt)
    # ax.xaxis.set_major_formatter(xticks)

    plt.legend()
    plt.tight_layout()
    plt.savefig('CompVotePercs.pdf', bbox_inches=None)
    plt.close()


def obtainHistogram(givenlist):
    out = []
    for num in givenlist:
        if len(str(num)) == 1:
            givenlist[givenlist.index(num)] = '0' + str(num)
    for flag in range(0, 10):
        flag = str(flag)
        count = 0
        for num in givenlist:
            num = str(num)
            if num[-1] == flag:
                count += 1
            if num[-2] == flag:
                count += 1
        result = count / (2 * len(givenlist))
        out.append(result)
    return out


def plotHistogram():
    voteList = []
    for name in names:
        voteList.extend(columns[name])

    voteList = [int(i) for i in voteList]
    freq = obtainHistogram(voteList)
    bins = [x for x in range(10)]
    mean = [0.10 for i in range(10)]
    plt.plot(bins, mean, color='green', label='Mean', linestyle='--')
    plt.plot(bins, freq, color='r', label='Digit Dist.')
    plt.title('Histogram of least sign. digits')
    plt.xlabel('Digits')
    plt.ylabel('Distribution')
    plt.legend()
    plt.tight_layout()
    plt.savefig('Histogram.pdf', bbox_inches=None)
    plt.close()


def produceRandom(end, givenSize):
    out = np.random.randint(0, end, size=givenSize)
    out = out.tolist()
    return out


def plotHistogramWithSample():
    bins = [x for x in range(10)]
    mean = [0.10 for i in range(10)]

    freqList = [obtainHistogram(produceRandom(101, 10)),
                obtainHistogram(produceRandom(101, 50)),
                obtainHistogram(produceRandom(101, 100)),
                obtainHistogram(produceRandom(101, 1000)),
                obtainHistogram(produceRandom(101, 10000))]

    title = 'Histogram of least sign. digits - Sample:{}'
    colorsBox = ['r', 'b', 'y', 'c', 'purple']
    savefigName = 'HistogramofSample{}.pdf'
    sampleCounter = 0

    for freq in freqList:
        plt.plot(bins, mean, color='green', label='Mean', linestyle='--')
        plt.plot(bins, freq, color=colorsBox[sampleCounter], label='Digit Dist.')
        plt.ylabel('Distribution')
        plt.xlabel('Digits')
        plt.title(title.format(sampleCounter + 1))
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.savefig(savefigName.format(sampleCounter + 1), bbox_inches=None)
        sampleCounter = sampleCounter + 1
        plt.close()


def calculateMSE(l1, l2):
    result = 0
    for i in range(len(l1)):
        result += (l1[i] - l2[i]) ** 2
    return result


def calculateMSEwithUniform(hist):
    mean = [0.10 for i in range(10)]
    result = calculateMSE(mean, hist)
    return result


def compareMSEs(mseUSA):
    global greater
    greater = 0
    global smaller
    smaller = 0
    for i in range(10000):
        randomMSE = calculateMSEwithUniform(obtainHistogram(produceRandom(101, sizeofData)))
        if randomMSE >= mseUSA:
            greater += 1
        elif randomMSE < mseUSA:
            smaller += 1


retrieveData(sys.argv[1], sys.argv[2])

eachtotalVote = {}  # {60933504: 'Romney', 469627: 'Stein', 1275971: 'Johnson', 65915795: 'Obama'}

for name in sys.argv[2]:
    nom_totalvote = 0
    for vote in columns[name]:
        nom_totalvote += int(vote)
    eachtotalVote[nom_totalvote] = name

sortedList = sorted(eachtotalVote, reverse=True)  # [65915795, 60933504, 1275971, 469627]

DispBarPlot()

compareVoteonBar()

plotHistogram()

plotHistogramWithSample()

voteList = []
for name in names:
    voteList.extend(columns[name])
voteList = [int(i) for i in voteList]
histUSA = obtainHistogram(voteList)

calculateMSEwithUniform(histUSA)

sizeofData = 0
for name in names:
    sizeofData += len(columns[name])

compareMSEs(calculateMSEwithUniform(histUSA))

print('MSE value of 2012 USA election is', calculateMSEwithUniform(histUSA))
outfile.write('MSE value of 2012 USA election is ' + str(calculateMSEwithUniform(histUSA)) + '\n')
print('The number of MSE of random samples which are larger than or equal to USA election MSE is', greater)
outfile.write(
    'The number of MSE of random samples which are larger than or equal to USA election MSE is ' + str(greater) + '\n')
print('The number of MSE of random samples which are smaller than USA election MSE is', smaller)
outfile.write('The number of MSE of random samples which are smaller than USA election MSE is ' + str(smaller) + '\n')
print('2012 USA election rejection level p is', smaller / 10000)
outfile.write('2012 USA election rejection level p is ' + str(smaller / 10000) + '\n')

if (greater / 10000) * 100 < 5:
    print('Finding: We reject the null hypothesis at the p= ' + str(smaller / 10000) + ' level')
    outfile.write('Finding: We reject the null hypothesis at the p= ' + str(smaller / 10000) + ' level' + '\n')
else:
    print('Finding: There is no statistical evidence to reject null hypothesis')
    outfile.write('Finding: There is no statistical evidence to reject null hypothesis')

# ****************************************Step 10*****************************

outfile.close()
outfile2.close()
infile.close()
