# External_Merge_Sort
## Python program for external merge sort
External sorting is required when the data being sorted do not fit into the main memory of a computing device (usually RAM) and instead they must reside in the slower external memory (usually a hard drive).External sorting typically uses a hybrid sort-merge strategy.  
### Sorting Phase
1. Read chunks of data small enough to fit in main memory.  
2. Sort data in chunk.  
3. Write chunks to temp files.  
### Merge Phase  
1. Load a portion of sorted data from temp files to memory.  
2. Perform K-way merge.
3. Write data to a single file.
### Command to run
`` python  	extmrgsrt.py <filename> ``
