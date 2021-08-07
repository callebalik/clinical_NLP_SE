from typing import Any, List
from numpy import ndarray
from sklearn.metrics import confusion_matrix


def generate_confusion_matrix(
    annotation_set_1: List, annotation_set_2: List, classes: List
):
    """Classes reorders the matrix"""
    y_true = annotation_set_1
    y_pred = annotation_set_2

    return confusion_matrix(y_true, y_pred, labels=classes)
