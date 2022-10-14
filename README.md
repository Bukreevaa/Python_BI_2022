# Python_BI_2022
## Homework1

This script was created as a part of study prosses.

The program includes the following subprograms :

transcribe - Generation of the RNA sequence based on the input DNA sequence;
reverse - Generation of the reverse DNA sequence based on the input DNA sequence;
complement - Genetation of the complementation DNA sequence based on the input DNA sequence;
reverse complement - Genetation of the reverse omplementation DNA sequence based on the input DNA sequence.
The program run untill 'exit' command.


## Fastq filtrator - Homework2

A program for working with fastq files.

The program is able to:

* Filter reeds by GC composition
* Filter reeds by quality
* Filter reeds by length
* Save the results to a file


The main function accepts the following arguments: 

1. input_fastq - path to the file to be input to the program (usual uncompressed fastq file)
2. output_file_prefix - path prefix to the file where the result will be written. The prefix is preceded by "_passed.fastq" for files with filtered reads, and "_failed.fastq" for files with filtered reads (only if the save_filtered argument is True).
3. gc_bounds - GC composition interval (in percent) for filtering (by default it is (0, 100), i.e. all reeds are saved). If you pass a single number as an argument, it is considered as an upper bound. Examples: gc_bounds = (20, 80) - you can save only reads with a GC composition between 20 and 80%. gc_bounds=44.4 - program save reads with a GC composition lower than 44.4%.
4. length_bounds - the length interval for filtering, everything is similar to gc_bounds, but by default it is equal to (0, 2**32).
5. quality_threshold - threshold value of average quality of read for filtering, the default value is 0 (phred33 scale). Reads with average quality for all nucleotides below the threshold are discarded.
6. save_filtered - whether to save filtered reads, the default value is False. 
