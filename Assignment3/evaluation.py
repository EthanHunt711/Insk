import numpy as np
import matplotlib.pyplot as plt


def pre_rec_list(gold_standard, query):
    precision_1 = []
    recall_1 = []
    rel = []
    recall_lev = []
    for j, i in enumerate(query):
        if i in gold_standard:
            rel.append(i)
            recall_1.append(len(rel)/len(gold_standard))
            precision_1.append(len(rel)/(j+1))
            recall_lev.append((j+1, precision_1[j]))
        else:
            if j == 0:
                recall_1.append(0)
                precision_1.append(0)
                recall_lev.append((j+1, precision_1[j]))
            else:
                recall_1.append(len(rel)/len(gold_standard))
                precision_1.append(precision_1[j-1])
                recall_lev.append((j+1, precision_1[j]))
    return precision_1, recall_1


def pre_rec_curv(precision_1, recall_1, precision_3, recall_3):
    precision_2 = np.array(precision_1)
    recall_2 = np.array(recall_1)
    precision_4 = np.array(precision_3)
    recall_4 = np.array(recall_3)

    recall = np.linspace(0.0, 1.0, num=len(recall_2))
    precision = precision_2
    precision2 = precision.copy()
    i = recall.shape[0] - 2

    recalll = np.linspace(0.0, 1.0, num=len(recall_4))
    precisionn = precision_4
    precisionn2 = precisionn.copy()
    i = recall.shape[0] - 2

    # interpolation...
    while i >= 0:
        if precision_2[i + 1] > precision_2[i] and precision_4[i + 1] > precision_4[i]:
            precision_2[i] = precision_2[i + 1]
            precision_4[i] = precision_4[i + 1]
        i = i - 1

    # plotting...
    fig, ax = plt.subplots()
    for i in range(recall.shape[0] - 1):
        ax.plot((recall[i], recall[i]), (precision[i], precision[i + 1]), 'k-', label='', color='red')  # vertical
        ax.plot((recall[i], recall[i + 1]), (precision[i + 1], precision[i + 1]), 'k-', label='',
                color='red')  # horizontal
        ax.plot((recalll[i], recalll[i]), (precisionn[i], precisionn[i + 1]), 'k-', label='', color='blue')  # vertical
        ax.plot((recalll[i], recalll[i + 1]), (precisionn[i + 1], precisionn[i + 1]), 'k-', label='',
                color='blue')  # horizontal

    ax.plot(recall, precision2, 'k--', color='green')
    ax.plot(recalll, precisionn2, 'k--', color='yellow')
    ax.legend()
    ax.set_xlabel("recall")
    ax.set_ylabel("precision")
    plt.savefig('fig.jpg')
    fig.show()


"""The queries use ring to refer to Lord of the Rings trilogy"""

if __name__ == '__main__':
    gold_standard = [29, 32, 31, 17, 11, 23, 7, 22]

    query1 = [29, 32, 31, 16, 30, 0, 9, 22, 18, 2, 23]  # the ring in his pocket should return to the mountain
    query2 = [29, 32, 6, 31, 2, 1, 14, 4, 19, 27, 5]  # whenever the people asked about the ring say nothing

    m = pre_rec_list(gold_standard, query2)
    m1 = pre_rec_list(gold_standard, query1)

    pre_rec_curv(m[0], m[1], m1[0], m1[1])
