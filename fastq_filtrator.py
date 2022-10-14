def gc(read, gc_bounds=(0, 100)): #the function for GC filtering
    seq = read[1].rstrip('\n') #geting rid of '\n' at the end of the string
    C = seq.count('C') #counting of Cytosine in the read
    G = seq.count('G') #counting of  Guanin in the read
    CG = round((((int(C) + int(G)) / (len(seq) + 1)) * 100), 1) #counting of GC proportion
    if type(gc_bounds) == tuple: #checking what type of the argument we have in conditions
        if float(gc_bounds[0]) <= CG <= gc_bounds[1]: #checking of compliance
            return True
        else:
            return False
    elif type(gc_bounds) == int or type(gc_bounds) == float: #checking what type of the argument we have in conditions
        if float(gc_bounds) <= CG: #checking of compliance
            return True
        else:
            return False

def lenght(read, length_bounds=(0, 2**32)): #the function for lenght filtering
    seq = read[1].rstrip('\n')
    if type(length_bounds) == tuple:
        if int(length_bounds[0]) <= len(seq) <= int(length_bounds[1]):
            return True
        else:
            return False
    elif type(length_bounds) == int:
        if len(seq) <= length_bounds:
            return True
        else:
            return False

def quality(read, quality_threshold=0): #the function for quality filtering
    dct = {'!': 0, '"': 1, '#': 2, '$': 3, '%': 4, '&': 5, "'": 6, '(': 7, ')': 8,   #dictionary with ASCII table
           '*': 9, '+': 10, ',': 11, '-': 12, '.': 13, '/': 14, '0': 15, '1': 16,
           '2': 17, '3': 18, '4': 19, '5': 20, '6': 21, '7': 22, '8': 23, "9": 24, ":": 25,
           ';': 26, '<': 27, '=': 28, '>': 29, '?': 30, '@': 31, 'A': 32, 'B': 33,
           'C': 34, 'D': 35, 'E': 36, 'F': 37, 'G': 38, 'H': 39, 'I': 40}
    count = 0 # a quality scorecounter
    q = read[3].rstrip('\n')
    for k, v in dct.items():
        for j in range(len(read[3].rstrip('\n'))): #a decoding cycle
            if q[j] == k:
                count += v
    mean_count = count / len(q) # a score calculation
    if float(quality_threshold) <= mean_count:
        return True
    else:
        return False

def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0, save_filtered=False): #the main fuction for filtering fastq files
  with open(input_fastq, 'r') as f: #reading a fastq file
    read = [] #making empty list for a read
    for i in f.readlines():
      read.append(i) #appending lines to the read list
      if len(read) == 4: #full one read in the list
        gc_check = gc(read, gc_bounds) #checking for GC lineup
        lenght_check = lenght(read, length_bounds) #checking for read lenght
        quality_check = quality(read, quality_threshold) #checking for read quality
        if (gc_check == True) and (lenght_check == True) and (quality_check == True): #compliance
          with open(output_file_prefix + "_passed.fastq", "a+") as f: #creating or opening _passed.fastq file
            f.write(''.join(read)) #writting read
            read = [] #list zeroing
        elif ((gc_check == False) or (lenght_check == False) or (quality_check == False)) and (save_filtered == True):
          with open(output_file_prefix + '_failed.fastq', "a+") as f: #creating or opening _failed.fastq file
            f.write(''.join(read))
            read = []
