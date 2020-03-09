import os 
import glob
import subprocess
import heapq

def sorting(pointers):
    out = []
    heap = []
    mem = [[],[],[],[],[]]

    # read first 100 lines of all file in mem
    for i in range(5):
        for j in range(100):
            mem[i].append(pointers[i][1].readline())

    # initiate heap with first value from all mem parts
    for i in range(len(mem)):
        heapq.heappush(heap,(mem[i][2],i))

    
    #initiate first push operation
    val,ptr = heapq.heapreplace(heap,(mem[1].pop(0),1))
    
    #append result
    out .append(val)

    # loop until heap is empty
    while heap:
        #if any mem get exhausted refill it
        #check if memory exhausted
        if not mem[0]:
            # check if file pointer for that memory exist
            if pointers[0]:
                for i in range(100):
                    # readline
                    line = pointers[0][1].readline()
                    # if no data then close file make file pointer none and break
                    if not line:
                        pointers[0][1].close()
                        pointers[0]=None
                        break
                    # else load line to memory
                    mem[0].append(line)
        # repeat for all memory
        if not mem[1]:
            if pointers[1]:
                for i in range(100):
                    line = pointers[1][1].readline()
                    if not line:
                        pointers[1][1].close()
                        pointers[1]=None
                        break
                    mem[1].append(line)
        if not mem[2]:
            if pointers[2]:
                for i in range(100):
                    line = pointers[2][1].readline()
                    if not line:
                        pointers[2][1].close()
                        pointers[2]=None
                        break
                    mem[2].append(line)
        if not mem[3]:
            if pointers[3]:
                for i in range(100):
                    line = pointers[3][1].readline()
                    if not line:
                        pointers[3][1].close()
                        pointers[3]=None
                        break
                    mem[3].append(line)
        if not mem[4]:
            if pointers[4]:
                for i in range(100):
                    line = pointers[4][1].readline()
                    if not line:
                        pointers[4][1].close()
                        pointers[4]=None
                        break
                    mem[4].append(line)
        
        # push next data into heap and append result to output
        val,ptr = heapq.heappop(heap)
        out.append(val.strip('\n'))
        if mem[ptr]:
            heapq.heappush(heap,(mem[ptr].pop(0),ptr))
        # if output reach 100 lines write into file and flush output
        if len(out) == 100:
            with open("sorted","a") as file:
                file.write("-----------wrote------\n")
                for i in out:
                    file.write(i+'\n')
            out=[]
                

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
        
        # Calculating the no. of line in file to be read (specially for ast file)
        if total_lines < chunk_size:
            chunk_size = total_lines
            total_lines=0
        total_lines = total_lines - chunk_size

        # Reading lines from file into list and sort the list
        data = [next(large_file_handler) for x in range(chunk_size)]
        data.sort(key = lambda x: x.lower())    
        
        # Open temp file and write lines into temp file
        small_filename = "{}.txt".format(count)
        with open(small_filename,"w") as s_file:
            for line in data:
                s_file.write(line)
        
        # Empty the memory
        count+=1
        data=[]

# Merge function. 
# This function will do a k-way merge on temp file. 
# result will be a bigfile with sorted data.
def merge_file():
    
    # Open chunk files and store pointers
    pointers = [0]*5
    for i in range(5):
        file = '{}.txt'.format(i)
        f = open(file,"r")
        pointers[i] = (i,f)
    
    sorting(pointers)

large_filename = "large"
split_file(large_filename)
merge_file()