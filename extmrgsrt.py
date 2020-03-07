import os 
import glob
import subprocess
from heapq import merge


large_filename = "/home/xenial/Desktop/extnalmergesort/a"

def split_file(file_name):
    
    count=0
    data = []
    out = subprocess.Popen(['wc', '-l', file_name],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    total_lines = int(stdout.split()[0])+1
    chunk_size = int(total_lines/5)+1

    large_file_handler = open(file_name)
    while total_lines > 0:
        count+=1;print(count)
        if total_lines < chunk_size:
            chunk_size = total_lines
            total_lines=0
        total_lines = total_lines - chunk_size
        print(chunk_size)
        data = [next(large_file_handler) for x in range(chunk_size)]
        data.sort(key = lambda x: x.lower())    
        small_filename = "/home/xenial/Desktop/extnalmergesort/{}.txt".format(count)
        with open(small_filename,"w") as s_file:
            for line in data:
                s_file.write(line)
        data=[]

def merge_file():
    out = open("sorted","w+")
    mem = []
    file_handlers=[]
    chunk_files = glob.glob('/home/xenial/Desktop/extnalmergesort/*.txt')
    for i in chunk_files:
        file_handlers.append(open(i))
    while file_handlers:
        for i in file_handlers:
            data=[]
            for j in range(100):
                line = i.readline()
                if not line:
                    i.close()
                    file_handlers.remove(i)
                    break 
                data.append(line)
            mem = merge(mem,data)
        for i in mem:
            out.write(i)
    out.close()

split_file(large_filename)
merge_file()