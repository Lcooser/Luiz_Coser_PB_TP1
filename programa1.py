import time
import sys

def bubble_sort(files):
    n = len(files)
    for i in range(n):
        for j in range(0, n-i-1):
            if files[j] > files[j+1]:
                files[j], files[j+1] = files[j+1], files[j]
    return files

def selection_sort(files):
    n = len(files)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if files[j] < files[min_idx]:
                min_idx = j
        files[i], files[min_idx] = files[min_idx], files[i]
    return files

def insertion_sort(files):
    for i in range(1, len(files)):
        key = files[i]
        j = i - 1
        while j >= 0 and key < files[j]:
            files[j + 1] = files[j]
            j -= 1
        files[j + 1] = key
    return files

def measure_time_and_memory(sort_func, files):
    start_time = time.time()
    before_size = sys.getsizeof(files)
    sorted_files = sort_func(files)
    end_time = time.time()
    after_size = sys.getsizeof(sorted_files)
    
    time_taken = end_time - start_time
    memory_used = after_size - before_size
    return time_taken, memory_used

def main():
    with open("file_list.txt", "r") as f:
        files = f.readlines()
    files = [file.strip() for file in files]

    bubble_time, bubble_memory = measure_time_and_memory(bubble_sort, files.copy())
    selection_time, selection_memory = measure_time_and_memory(selection_sort, files.copy())
    insertion_time, insertion_memory = measure_time_and_memory(insertion_sort, files.copy())

    with open("tempos.txt", "w") as f:
        f.write(f"Bubble Sort Time: {bubble_time} seconds\n")
        f.write(f"Selection Sort Time: {selection_time} seconds\n")
        f.write(f"Insertion Sort Time: {insertion_time} seconds\n")
        f.write(f"Bubble Sort Memory: {bubble_memory} bytes\n")
        f.write(f"Selection Sort Memory: {selection_memory} bytes\n")
        f.write(f"Insertion Sort Memory: {insertion_memory} bytes\n")

if __name__ == "__main__":
    main()
