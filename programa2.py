import time
import sys
import collections

def measure_time_and_memory(structure_type, data, operation="insert"):
    start_time = time.time()
    before_size = sys.getsizeof(data)

    if structure_type == "hashtable":
        hashtable = {}
        if operation == "insert":
            for file in data:
                hashtable[file] = True
        elif operation == "get":
            hashtable[data[0]]  
        after_size = sys.getsizeof(hashtable)

    elif structure_type == "stack":
        stack = []
        if operation == "insert":
            for file in data:
                stack.append(file)
        elif operation == "get":
            stack[-1]  
        after_size = sys.getsizeof(stack)

    elif structure_type == "queue":
        queue = collections.deque()
        if operation == "insert":
            for file in data:
                queue.append(file)
        elif operation == "get":
            queue[0]  
        after_size = sys.getsizeof(queue)

    end_time = time.time()
    time_taken = end_time - start_time
    memory_used = after_size - before_size
    return time_taken, memory_used

def main():
    with open("file_list.txt", "r") as f:
        files = f.readlines()
    files = [file.strip() for file in files]

    hashtable_insert_time, hashtable_memory = measure_time_and_memory("hashtable", files)
    stack_insert_time, stack_memory = measure_time_and_memory("stack", files)
    queue_insert_time, queue_memory = measure_time_and_memory("queue", files)

    with open("tempos.txt", "a") as f:
        f.write(f"Hashtable Insert Time: {hashtable_insert_time} seconds\n")
        f.write(f"Stack Insert Time: {stack_insert_time} seconds\n")
        f.write(f"Queue Insert Time: {queue_insert_time} seconds\n")
        f.write(f"Hashtable Memory: {hashtable_memory} bytes\n")
        f.write(f"Stack Memory: {stack_memory} bytes\n")
        f.write(f"Queue Memory: {queue_memory} bytes\n")

if __name__ == "__main__":
    main()
