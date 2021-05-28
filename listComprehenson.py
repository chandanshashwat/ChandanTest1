#list Comprehensions
def listComp1():
    input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
    list_using = [i for i in input_list if i % 2 == 0 ]
    return(list_using)

def listComp2():
    input_list = [1,2,3,4,5]
    list_using = [i*i for i in input_list]
    return(input_list, list_using)