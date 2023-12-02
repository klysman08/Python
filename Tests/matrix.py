

# Python code below
# Use print("messages...") to debug your solution.

def compute_recall(m):
    return m.true_positive / (m.true_positive + m.false_negative)


def compute_precision(m):
    return m.true_positive / (m.true_positive + m.false_positive)


def compute_specificity(m):
    return m.true_negative / (m.true_negative + m.false_positive)


def compute_accuracy(m):
    return (m.true_positive + m.true_negative) / (
        m.true_positive + m.true_negative + m.false_positive + m.false_negative
    )
