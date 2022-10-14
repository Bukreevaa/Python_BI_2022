{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNMFKp4htrxLiihdmnQPrKI",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Bukreevaa/Python_BI_2022/blob/homework_2/fastq_filtrator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "x9EbJFOmCL_i"
      },
      "outputs": [],
      "source": [
        "def gc(read, gc_bounds=(0, 100)): #the function for GC filtering\n",
        "    seq = read[1].rstrip('\\n') #geting rid of '\\n' at the end of the string\n",
        "    C = seq.count('C') #counting of Cytosine in the read\n",
        "    G = seq.count('G') #counting of  Guanin in the read\n",
        "    CG = round((((int(C) + int(G)) / (len(seq) + 1)) * 100), 1) #counting of GC proportion\n",
        "    if type(gc_bounds) == tuple: #checking what type of the argument we have in conditions\n",
        "        if float(gc_bounds[0]) <= CG <= gc_bounds[1]: #checking of compliance\n",
        "            return True\n",
        "        else:\n",
        "            return False\n",
        "    elif type(gc_bounds) == int or type(gc_bounds) == float: #checking what type of the argument we have in conditions\n",
        "        if float(gc_bounds) <= CG: #checking of compliance\n",
        "            return True\n",
        "        else:\n",
        "            return False\n",
        "\n",
        "def lenght(read, length_bounds=(0, 2**32)): #the function for lenght filtering\n",
        "    seq = read[1].rstrip('\\n')\n",
        "    if type(length_bounds) == tuple:\n",
        "        if int(length_bounds[0]) <= len(seq) <= int(length_bounds[1]):\n",
        "            return True\n",
        "        else:\n",
        "            return False\n",
        "    elif type(length_bounds) == int:\n",
        "        if len(seq) <= length_bounds:\n",
        "            return True\n",
        "        else:\n",
        "            return False\n",
        "\n",
        "def quality(read, quality_threshold=0): #the function for quality filtering\n",
        "    dct = {'!': 0, '\"': 1, '#': 2, '$': 3, '%': 4, '&': 5, \"'\": 6, '(': 7, ')': 8,   #dictionary with ASCII table\n",
        "           '*': 9, '+': 10, ',': 11, '-': 12, '.': 13, '/': 14, '0': 15, '1': 16,\n",
        "           '2': 17, '3': 18, '4': 19, '5': 20, '6': 21, '7': 22, '8': 23, \"9\": 24, \":\": 25,\n",
        "           ';': 26, '<': 27, '=': 28, '>': 29, '?': 30, '@': 31, 'A': 32, 'B': 33,\n",
        "           'C': 34, 'D': 35, 'E': 36, 'F': 37, 'G': 38, 'H': 39, 'I': 40}\n",
        "    count = 0 # a quality scorecounter\n",
        "    q = read[3].rstrip('\\n')\n",
        "    for k, v in dct.items():\n",
        "        for j in range(len(read[3].rstrip('\\n'))): #a decoding cycle\n",
        "            if q[j] == k:\n",
        "                count += v\n",
        "    mean_count = count / len(q) # a score calculation\n",
        "    if float(quality_threshold) <= mean_count:\n",
        "        return True\n",
        "    else:\n",
        "        return False\n",
        "\n",
        "def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0, save_filtered=False): #the main fuction for filtering fastq files\n",
        "  with open(input_fastq, 'r') as f: #reading a fastq file\n",
        "    read = [] #making empty list for a read\n",
        "    for i in f.readlines():\n",
        "      read.append(i) #appending lines to the read list\n",
        "      if len(read) == 4: #full one read in the list\n",
        "        gc_check = gc(read, gc_bounds) #checking for GC lineup\n",
        "        lenght_check = lenght(read, length_bounds) #checking for read lenght\n",
        "        quality_check = quality(read, quality_threshold) #checking for read quality\n",
        "        if (gc_check == True) and (lenght_check == True) and (quality_check == True): #compliance\n",
        "          with open(output_file_prefix + \"_passed.fastq\", \"a+\") as f: #creating or opening _passed.fastq file\n",
        "            f.write(''.join(read)) #writting read\n",
        "            read = [] #list zeroing\n",
        "        elif ((gc_check == False) or (lenght_check == False) or (quality_check == False)) and (save_filtered == True):\n",
        "          with open(output_file_prefix + '_failed.fastq', \"a+\") as f: #creating or opening _failed.fastq file\n",
        "            f.write(''.join(read))\n",
        "            read = []"
      ]
    }
  ]
}