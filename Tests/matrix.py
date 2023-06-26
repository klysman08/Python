

# Python code below
# Use print("messages...") to debug your solution.

def compute_recall(m):
    recall = m.true_positive / (m.true_positive + m.false_negative)
    return recall

def compute_precision(m):
    precision = m.true_positive / (m.true_positive + m.false_positive)
    return precision
    
def compute_specificity(m):
    specificity = m.true_negative / (m.true_negative + m.false_positive)
    return specificity

def compute_accuracy(m):
    accuracy = (m.true_positive + m.true_negative) / (m.true_positive + m.true_negative + m.false_positive + m.false_negative)
    return accuracy

