

# DISPREDICT_PATH = './downloaded_dataset/DisPredict_V2.0/Software/Output/prediction/'
# dispredict_ext = ".dispredict2.sl477.predict"


def get_disorder(pdb_id):
  with open(DISPREDICT_PATH + pdb_id + "/" + pdb_id + ".dispredict2.sl477.predict") as f:
    return_matrix = [0, 0, 0, 0] # for 1 and -1
    length = 0
    for line in f:
      length += 1
      line_items = line.split(" ")
      if line_items[0] == "-1":
        return_matrix[0] += float(line_items[1])
        return_matrix[1] += float(line_items[2]) 
      
      elif line_items[0] == "1":
        return_matrix[2] += float(line_items[1])
        return_matrix[3] += float(line_items[2])
        #pass
    return [x/length for x in return_matrix]

alphabets = ['A',	'C',	'D',	'E',	'F',	'G',	'H',	'I',	'K',	'L',	'M',	'N',	'P', 'Q',	'R',	'S',	'T',	'V',	'W',	'Y']


energy = [
[-1.65,  -2.83, 1.16,	1.80,	-3.73,	-0.41,	1.90,	-3.69,	0.49,	-3.01,	-2.08,	0.66,	1.54,	1.20,	0.98, -0.08,  0.46, -2.31,	0.32,	-4.62],
[-2.83,	-39.58,	-0.82,	-0.53,	-3.07,	-2.96,	-4.98,	0.34,	-1.38,	-2.15,	1.43,	-4.18,	-2.13,	-2.91,	-0.41,	-2.33,	-1.84,	-0.16,	4.26,	-4.46],
[1.16,	-0.82,	0.84,	1.97,	-0.92,	0.88,	-1.07,	0.68,	-1.93,	0.23,	0.61,	0.32,	3.31,	2.67,	-2.02,	0.91,	-0.65,	0.94,	-0.71,	0.90],
[1.80,	-0.53,	1.97,	1.45,	0.94,	1.31,	0.61,	1.30,	-2.51,	1.14,	2.53,	0.20,	1.44,	0.10,	-3.13,	0.81,	1.54,	0.12,	-1.07,	1.29],
[-3.73,	-3.07,	-0.92,	0.94,	-11.25,	0.35,	-3.57,	-5.88,	-0.82,	-8.59,	-5.34,	0.73,	0.32,	0.77,	-0.40,	-2.22,	0.11,	-7.05,	-7.09,	-8.80],
[-0.41,	-2.96,	0.88,	1.31,	0.35,	-0.20,	1.09,	-0.65,	-0.16,	-0.55,	-0.52,	-0.32,	2.25,	1.11,	0.84,	0.71,	0.59,	-0.38,	1.69,	-1.90],
[1.90,	-4.98,	-1.07,	0.61,	-3.57,	1.09,	1.97,	-0.71,	2.89,	-0.86,	-0.75,	1.84,	0.35,	2.64,	2.05,	0.82,	-0.01,	0.27,	-7.58,	-3.20],
[-3.69,	0.34,	0.68,	1.30,	-5.88,	-0.65,	-0.71,	-6.74,	-0.01,	-9.01,	-3.62,	-0.07,	0.12,	-0.18,	0.19,	-0.15,	0.63,	-6.54,	-3.78,	-5.26],
[0.49,	-1.38,	-1.93,	-2.51,	-0.82,	-0.16,	2.89,	-0.01,	1.24,	0.49,	1.61,	1.12,	0.51,	0.43,	2.34,	0.19,	-1.11,	0.19,	0.02,	-1.19],
[-3.01,	-2.15,	0.23,	1.14,	-8.59,	-0.55,	-0.86,	-9.01,	0.49,	-6.37,	-2.88,	0.97,	1.81,	-0.58,	-0.60,	-0.41,	0.72,	-5.43,	-8.31,	-4.90],
[-2.08,	1.43,	0.61,	2.53,	-5.34,	-0.52,	-0.75,	-3.62,	1.61,	-2.88,	-6.49,	0.21,	0.75,	1.90,	2.09,	1.39,	0.63,	-2.59,	-6.88,	-9.73],
[0.66,	-4.18,	0.32,	0.20,	0.73,	-0.32,	1.84,	-0.07,	1.12,	0.97,	0.21,	0.61,	1.15,	1.28,	1.08,	0.29,	0.46,	0.93,	-0.74,	0.93],
[1.54,	-2.13,	3.31,	1.44,	0.32,	2.25,	0.35,	0.12,	0.51,	1.81,	0.75,	1.15,	-0.42,	2.97,	1.06,	1.12,	1.65,	0.38,	-2.06,	-2.09],
[1.20,	-2.91,	2.67,	0.10,	0.77,	1.11,	2.64,	-0.18,	0.43,	-0.58,	1.90,	1.28,	2.97,	-1.54,	0.91,	0.85,	-0.07,	-1.91,	-0.76,	0.01],
[0.98,	-0.41,	-2.02,	-3.13,	-0.40,	0.84,	2.05,	0.19,	2.34,	-0.60,	2.09,	1.08,	1.06,	0.91,	0.21,	0.95,	0.98,	0.08,	-5.89,	0.36],
[-0.08,	-2.33,	0.91,	0.81,	-2.22,	0.71,	0.82,	-0.15,	0.19,	-0.41,	1.39,	0.29,	1.12,	0.85,	0.95,	-0.48,	-0.06,	0.13,	-3.03,	-0.82],
[0.46,	-1.84,	-0.65,	1.54,	0.11,	0.59,	-0.01,	0.63,	-1.11,	0.72,	0.63,	0.46,	1.65,	-0.07,	0.98,	-0.06,	-0.96,	1.14,	-0.65,	-0.37],
[-2.31,	-0.16,	0.94,	0.12,	-7.05,	-0.38,	0.27,	-6.54,	0.19,	-5.43,	-2.59,	0.93,	0.38,	-1.91,	0.08,	0.13,	1.14,	-4.82,	-2.13,	-3.59],
[0.32,	4.26,	-0.71,	-1.07,	-7.09,	1.69,	-7.58,	-3.78,	0.02,	-8.31,	-6.88,	-0.74,	-2.06,	-0.76,	-5.89,	-3.03,	-0.65,	-2.13,	-1.73,	-12.39],
[-4.62,	-4.46,	0.90,	1.29,	-8.80,	-1.90,	-3.20,	-5.26,	-1.19,	-4.90,	-9.73,	0.93,	-2.09,	0.01,	0.36,	-0.82,	-0.37,	-3.59,	-12.39,	-2.68],
]


def get_pointwise_energy(fasta_sequence):
    returnval = []
    for res in fasta_sequence:
        if res=='X':
            pass
        elif res=='B':
            pass
        else:
            returnval.append(energy[alphabets.index(res)] )
            
    energy_matrix = [0 for x in range(len(alphabets)) ]
    for x in range(len(returnval[0]) ):
      energy_matrix[x] += round(sum(i[x] for i in returnval), 4)
    return [ x / sum(energy_matrix) for x in energy_matrix]
    
#from pssm_helpers import pssm_ddt_func, pssm_sdt_func

#experimental feature //TODO: Remove if does not work better
def get_pattern_based_pointwise_energy(fasta_sequence):
    matrix = []
    for x in fasta_sequence:
        matrix.append(energy[alphabets.index(x)])
        #print(matrix)
    returnval = [item for sublist in  pssm_ddt_func(matrix) for item in sublist]
    #print(returnval)
    return returnval
    
import numpy as np
    
if __name__ == "__main__":
    
    
    # t = 'CPP924.txt'
    t='GT_ind1476.txt'
    inputFile = open(t,'r')
    inputFile_g = inputFile.readlines()
    inputFile_long = len(inputFile_g)

#outputFile = open(r'.\script\feature_hong3.txt','w')

    outputFile = open(r'CPP924_tet.txt','w')

##
#tempFile = open(r'.\script\tempFile.txt','w')
    tempFile = open(r'CPP924_tet.txt','w')
    for eachth in range(inputFile_long):
        if inputFile_g[eachth][0] == '>':
            if eachth == 0:
                tempFile.write(inputFile_g[eachth])
            else:
                tempFile.write('\n')
                tempFile.write(inputFile_g[eachth])
        else:
            seqeach = inputFile_g[eachth].strip('\n\r')
            tempFile.write(seqeach)

    inputFile.close()        
    tempFile.close()
    
    input_tempFile = open(r'CPP924_tet.txt','r')
    input_tempFile_g = input_tempFile.readlines()
    input_tempFile_long = len(input_tempFile_g)
    
    jj=0
    re=np.zeros((1476,20))
   # re=[]
    for eachth in range(input_tempFile_long):
        if input_tempFile_g[eachth][0] == '>':
            pass
        else:
            input_tempFile_g[eachth] = input_tempFile_g[eachth].upper()   
            seq = input_tempFile_g[eachth].strip('\n\r')     
            outputFile.write("0\t")
            temp=get_pointwise_energy(seq)
            print (temp)
            re[jj]=temp
            jj=jj+1
            
	

    input_tempFile.close()
    outputFile.close()
    

    np.savetxt("filename1476.txt",re)
    
