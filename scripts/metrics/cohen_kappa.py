#implementation of Cohen kappa by https://gist.github.com/LouisdeBruijn

'''
Cohen’s kappa coefficient (κ) is a statistic to measure the reliability between annotators for qualitative (categorical) items. It is a more robust measure than simple percent agreement calculations, as κ takes into account the possibility of the agreement occurring by chance. It is a pairwise reliability measure between two annotators.

Cohen’s kappa statistic is the agreement between two raters where Po is the relative observed agreement among raters (identical to the accuracy), and Pe is the hypothetical probability of chance agreement. Below you will find the programmatic implementation of this evaluation metric.
'''


def cohen_kappa(ann1, ann2):
    """Computes Cohen kappa for pair-wise annotators.
    :param ann1: annotations provided by first annotator
    :type ann1: list
    :param ann2: annotations provided by second annotator
    :type ann2: list
    :rtype: float
    :return: Cohen kappa statistic
    """
    count = 0
    for an1, an2 in zip(ann1, ann2):
        if an1 == an2:
            count += 1
    A = count / len(ann1)  # observed agreement A (Po)

    uniq = set(ann1 + ann2)
    E = 0  # expected agreement E (Pe)
    for item in uniq:
        cnt1 = ann1.count(item)
        cnt2 = ann2.count(item)
        count = ((cnt1 / len(ann1)) * (cnt2 / len(ann2)))
        E += count

    return round((A - E) / (1 - E), 4)