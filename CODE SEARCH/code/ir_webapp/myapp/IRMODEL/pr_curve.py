import numpy as np
import matplotlib.pyplot as plt
import json

def calculate_precision_recall(predictions):
    total_relevant = sum(predictions.values())
    relevant_retrieved = 0
    total_retrieved = 0
    precision_recall_points = []

    for prediction in predictions.values():
        total_retrieved += 1
        if prediction == 1:
          relevant_retrieved += 1
        precision = relevant_retrieved / total_retrieved if total_retrieved > 0 else 0
        recall = relevant_retrieved / total_relevant if total_relevant > 0 else 0

        precision_recall_points.append((precision, recall))

    return precision_recall_points

def plot_precision_recall_curve(precision_recall_points, save_path=None):
    # Sort points by recall for correct plotting
    precision_recall_points.sort(key=lambda x: x[1])

    precisions, recalls = zip(*precision_recall_points)

    plt.figure(figsize=(8, 6))
    plt.plot(recalls, precisions, marker='o', linestyle='-', color='r')
    plt.title('Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.grid(True)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

# with open('myapp/IRMODEL/pr/test.json') as json_file:
# with open('pr/test.json') as json_file:
#     predictions = json.load(json_file)

def generate_pr_curve(predictions):
  precision_recall_points = calculate_precision_recall(predictions)
  plot_precision_recall_curve(precision_recall_points)
  # plot_precision_recall_curve(precision_recall_points, save_path='myapp/IRMODEL/pr/PR_curve.png')