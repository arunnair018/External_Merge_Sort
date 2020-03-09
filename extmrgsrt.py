import os 
import glob
import subprocess
from heapq import merge

# Ffilepath to big file
large_filename = "/home/xenial/Desktop/extnalmergesort/External_Merge_Sort/a"

# Splitting and sosrting function. 
# This function will create 5 temp files out of one big file. 
# The data in temp files will be sorted.
def split_file(file_name):
    
    count=0 
    data = []
    
    # Getting the total line in the file and calculating temp file size(chunk_size)
    out = subprocess.Popen(['wc', '-l', file_name],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    total_lines = int(stdout.split()[0])+1
    chunk_size = int(total_lines/5)+1

    # Open big file 
    large_file_handler = open(file_name)
    
    # Reading lines until file is over
    while total_lines > 0:
        count+=1

        # Calculating the no. of line in file to be read (specially for ast file)
        if total_lines < chunk_size:
            chunk_size = total_lines
            total_lines=0
        total_lines = total_lines - chunk_size

        # Reading lines from file into list and sort the list
        data = [next(large_file_handler) for x in range(chunk_size)]
        data.sort(key = lambda x: x.lower())    
        
        # Open temp file and write lines into temp file
        small_filename = "/home/xenial/Desktop/extnalmergesort/External_Merge_Sort/{}.txt".format(count)
        with open(small_filename,"w") as s_file:
            for line in data:
                s_file.write(line)
        
        # Empty the memory
        data=[]

# Merge function. 
# This function will do a k-way merge on temp file. 
# result will be a bigfile with sorted data.
def merge_file():

    # Open or create output file
    out = open("sorted","w+")
    
    # list temp files in list
    chunk_files = glob.glob('/home/xenial/Desktop/extnalmergesort/External_Merge_Sort/*.txt')
    
    # Open temp files and store file handlers in list
    pointers=[]
    for i,file in enumerate(chunk_files):
        handle = open(file,"r")
        pointers.append((i,handle))

split_file(large_filename)
merge_file()