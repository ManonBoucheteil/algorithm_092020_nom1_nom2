import os
import importlib
from copy import deepcopy

base_dir = os.getcwd()
with open("urls.csv", "r") as f:
    f.readline()
    coroutines = []
    while line := f.readline():
        repository_url = line.split(",")[-1]
        repository_name = repository_url.split("/")[-1].strip("\n")

        with open(f"{repository_name}.log", "w") as log:
            os.chdir(f"{base_dir}\\repositories")
            os.system(f"git clone {repository_url} -q")
            os.system(f"cd {repository_name} && git pull")

            try:
                os.chdir(repository_name)
                module = importlib.import_module("fibonacci_heap")
                os.chdir(f"{base_dir}\\logs")
            except ModuleNotFoundError as e:
                print(f"{os.getcwd()} Error : {repository_name} repository either doesn't exist or does not have public rights\n")
                os.chdir(f"{base_dir}\\logs")
                log.write(f"Error : {repository_name} repository either doesn't exist or does not have public rights\n")
                continue

            try:
                heap = module.FibonacciHeap()
            except NameError as e:
                log.write(f"Error : fibonacci_heap.py file not found\n")
            else:
                log.write("Create heap successful\n")

            try:
                heap.insert(5)
                heap.insert(1)
                heap.insert(10)
                heap.insert(0)
                heap.insert(42)
                heap.insert(15)
                heap.insert(7)
                heap.insert(19)
                heap.insert(20)
                heap.insert(2)
                heap.insert(84)
                heap.insert(50)
            except Exception as e:
                log.write(f"Error while inserting good values in the heap: {e}\n")
            else:
                log.write(f"Insert successful\n")

            try:
                minimum = heap.find_minimum()
            except Exception as e:
                log.write(f"Error while finding minimum with good values inserted in the heap : {e}\n")
                continue
            else:
                if minimum != 0:
                    log.write(f"Invalid : Found minimum {minimum} but was looking for 0\n")
                else:
                    log.write(f"Find minimum successful\n")


            try:
                heap2 = deepcopy(heap)
                heap.merge(heap2)
            except Exception as e:
                log.write(f"Error while merging two identical heap : {e}\n")
            else:
                minimum = heap.find_minimum()
                if minimum != 0:
                    log.write(f"Invalid : Found minimum {minimum} but was looking for 0\n")
                else:
                    log.write(f"Merge minimum successful\n")

            try:
                while (node := heap.delete_min()) is not None:
                    pass
            except Exception as e:
                log.write(f"Error while removing all elements : {e}\n")
            else:
                log.write(f"Delete minimum successful\n")