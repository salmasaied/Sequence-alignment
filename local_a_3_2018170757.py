# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:13:25 2020

@author: Salma Mohamed
"""

# To help in matrix
import numpy as np

seq1 = "ACCGTT"
seq2 = "AGTTCA"

main_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1))
check_matrix = np.zeros((len(seq1), len(seq2)))

match = 1
mismatch= -1
gap= -1


for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            check_matrix[i][j] = match
        else:
            check_matrix[i][j] = mismatch
        if (check_matrix[i][j] < 0):
            main_matrix[i][j] = 0

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        main_matrix[i][j] = max(main_matrix[i - 1][j - 1] + check_matrix[i - 1][j - 1],
                                main_matrix[i - 1][j] + gap,
                                main_matrix[i][j - 1] + gap)

        if(main_matrix[i][j]<0):
            main_matrix[i][j]=0

aligned_1 = ""
aligned_2 = ""


tracei = len(seq1)
tracej = len(seq2)

maxval=np.max(main_matrix)
for i in range(len(seq1)+1):
    for j in range (len(seq2)+1):
        if(main_matrix[i][j]==maxval):
            tracei=i
            tracej=j


while (tracei > 0 and tracej > 0):
#diagonal condition
    if(main_matrix[tracei][tracej]==0):
        break
    if (tracei > 0 and tracej > 0 and main_matrix[tracei][tracej] == main_matrix[tracei - 1][tracej - 1] +
            check_matrix[tracei - 1][ tracej - 1]):

        aligned_1 = seq1[tracei - 1] + aligned_1
        aligned_2 = seq2[tracej - 1] + aligned_2

        tracei -= 1
        tracej -= 1

    elif (tracei > 0 and main_matrix[tracei][tracej] == main_matrix[tracei - 1][tracej] + gap and tracej !=0):

        aligned_1 = seq1[tracei - 1] + aligned_1
        aligned_2 = "*" + aligned_2

        tracei -= 1
    else:
        aligned_1 = "*" + aligned_1
        aligned_2 = seq2[tracej - 1] + aligned_2

        tracej -= 1


print("The Matrix after filling \n",main_matrix)
print("The global alignment of the two sequences")
print(aligned_1)
print(aligned_2)


