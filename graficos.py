import matplotlib.pyplot as plt

def read_times():
    with open("tempos.txt", "r") as f:
        lines = f.readlines()

        bubble_time = float(lines[0].split(":")[1].strip().split()[0])
        selection_time = float(lines[1].split(":")[1].strip().split()[0])
        insertion_time = float(lines[2].split(":")[1].strip().split()[0])

        hashtable_insert_time = float(lines[6].split(":")[1].strip().split()[0])
        stack_insert_time = float(lines[7].split(":")[1].strip().split()[0])
        queue_insert_time = float(lines[8].split(":")[1].strip().split()[0])

        return (bubble_time, selection_time, insertion_time,
                hashtable_insert_time, stack_insert_time, queue_insert_time)

def plot_comparison():
    bubble_time, selection_time, insertion_time, \
    hashtable_insert_time, stack_insert_time, queue_insert_time = read_times()

    sort_times = {
        "Bubble Sort": bubble_time,
        "Selection Sort": selection_time,
        "Insertion Sort": insertion_time
    }

    structure_times = {
        "Hashtable Insert": hashtable_insert_time,
        "Stack Insert": stack_insert_time,
        "Queue Insert": queue_insert_time
    }

    plt.figure(figsize=(10, 6))
    plt.bar(sort_times.keys(), sort_times.values(), color='skyblue')
    plt.title("Comparison of Sorting Algorithms (Time)")
    plt.ylabel("Time (seconds)")
    plt.savefig("sorting_comparison.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.bar(structure_times.keys(), structure_times.values(), color='lightgreen')
    plt.title("Comparison of Data Structures (Insert Time)")
    plt.ylabel("Time (seconds)")
    plt.savefig("data_structure_comparison.png")
    plt.close()

if __name__ == "__main__":
    plot_comparison()

