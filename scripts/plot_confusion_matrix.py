from matplotlib import pyplot
import matplotlib as mpl
from metrics.confusion_matrix import generate_confusion_matrix
import numpy


def custom_plot(x, y, ax=None, **plt_kwargs):
    if ax is None:
        ax = plt.gca()
    ax.plot(x, y, **plt_kwargs)  ## example plot here
    return ax


def plot_confusion_matrix(
    x,
    y,
    classes,
    ax=None,
    normalize=False,
    xlabel="Predicted Label",
    ylabel="True Label",
    title="Multi-class Confusion Matrix",
    cmap=pyplot.cm.Blues,
    style="default",
):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    # Compute confusion matrix
    cm = generate_confusion_matrix(x, y, classes)

    # Normalize values
    if normalize:
        cm = cm.astype("float") / cm.sum(axis=1)[:, numpy.newaxis]

    # Styling
    mpl.style.use(f"{style}")

    # defaults to .gca()
    if ax is None:
        ax = pyplot.gca()

    im = ax.imshow(cm, interpolation="nearest", cmap=cmap)
    # ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...

    ax.set(
        xticks=numpy.arange(cm.shape[1]),
        yticks=numpy.arange(cm.shape[0]),
        # ... and label them with the respective list entries
        title=title,
        ylabel=ylabel,
        xlabel=xlabel,
    )

    fnt = {"fontsize": 9, "fontweight": "normal"}

    ax.set_xticklabels(classes, fontdict=fnt)
    ax.set_yticklabels(classes, fontdict=fnt)
    # Rotate the tick labels and set their alignment.
    pyplot.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = ".2f" if normalize else "d"
    thresh = cm.max() / 2.0
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(
                j,
                i,
                format(cm[i, j], fmt),
                ha="center",
                va="center",
                color="white" if cm[i, j] > thresh else "black",
            )
    return cm, ax, im
