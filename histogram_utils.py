import matplotlib.pyplot as plt
def build_histogram(data):
    histogram = {}
    for item in data:
        histogram[item] = histogram.get(item, 0) + 1
    return histogram
    
def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


