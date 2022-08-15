#The my_map function takes a function and a sequence and will then complete it
def my_map(func, *sequences):
       result = []
       if len(sequences) > 0:
           minl = min(len(subseq) for subseq in sequences)
           for i in range(minl):
              result.append(func(*[subseq[i] for subseq in sequences]))
       return result

#The filter function this takes a function and a sequence and will then filter it 
def my_filter(func,sequence):
    remainder=[]
    for variable in sequence :
        if func(variable):
            remainder.append(variable)
    return remainder

#The Reduce function takes a function and a sequence will then reduce it
def my_reduce(func, seq):
     first = seq[0]
     for i in seq[1:]:
         first = func(first, i)
     return first