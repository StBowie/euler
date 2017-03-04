#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:23:26 2017

@author: sbowie
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210
abc   acb   bac   bca   cab   cba

0123 0132 0213 0231 0312 0321 1023 1032 1203 1230 1302 1320 
abcd abdc acbd acdb adbc adbc bacd badc bcad bcda bdac bdca

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        sublist = [[],[]]
        pivot = list[0]
        for e in list:
            if int(e) < int(pivot):
                sublist[0].append(e)
            if int(e) > int(pivot):
                sublist[1].append(e)
            return quicksort(sublist[0]) + [pivot] + quicksort(sublist[1])
   
def create_list(a):
    result = []
    x = 0
    for a in range(0,a):
        result.append(x)
    return result

def lex_perm(p,end):
    quicksort(p)
    perm = create_list(len(p))
    current = 0
    unused_0 = p
    for a in range(0,len(unused_0)):
        perm[0] = unused_0[a]
        unused_1 = unused_0[:a] + unused_0[a+1:]
        for b in range(0,len(unused_1)):
            perm[1] = unused_1[b]
            unused_2 = unused_1[:b] + unused_1[b+1:]
            for c in range(0,len(unused_2)):
                perm[2] = unused_2[c]
                unused_3 = unused_2[:c] + unused_2[c+1:]
                for d in range(0,len(unused_3)):
                    perm[3] = unused_3[d]
                    unused_4 = unused_3[:d] + unused_3[d+1:]
                    for e in range(0,len(unused_4)):
                        perm[4] = unused_4[e]
                        unused_5 = unused_4[:e] + unused_4[e+1:]
                        for f in range(0,len(unused_5)):
                            perm[5] = unused_5[f]
                            unused_6 = unused_5[:f] + unused_5[f+1:]
                            for g in range(0,len(unused_6)):
                                perm[6] = unused_6[g]
                                unused_7 = unused_6[:g] + unused_6[g+1:]
                                for h in range(0,len(unused_7)):
                                    perm[7] = unused_7[h]
                                    unused_8 = unused_7[:h] + unused_7[h+1:]
                                    for i in range(0,len(unused_8)):
                                        perm[8] = unused_8[i]
                                        unused_9 = unused_8[:i] + unused_8[i+1:]
                                        for j in range(0,len(unused_9)):
                                            perm[9] = unused_9[j]
                                            unused_10 = unused_9[:j] + unused_9[j+1:]
                                            current += 1
                                            if current >= end:
                                                return current, perm,''.join(perm)
    return current, perm            
    
print lex_perm(['0','1','2','3','4','5','6','7','8','9'],1000000)
    
