def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


'''
Make sure to answer the following questions about your coding process:
Q: How does this solution ensure data immutability?
A: Data has been created and cannot be changed.
        
Q: Is this solution a pure function? Why or why not?
A: Yes it is because it's output value follows solely from its input values, without any observable side effects.
    
Q: Is this solution a higher order function? Why or why not?
A: Describing the result you want rather than explicitly specifying the steps required to get there.
       
Q: Would it have been easier to solve this problem using a different programming style?
A: Very possible. I do not hava a good answer to that. 
     
Q: Why in particular is functional programming a helpful paradigm when solving this problem?
A: Paradigms are important because they define a programming language and how it works.
'''