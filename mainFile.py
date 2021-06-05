from dependentFile import addition, subtraction
from newPack import sample1
from NewSubpack import sample2
from Loops import loopsUses
from listComprehenson import *
from DictionaryComp import *
import os
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # print("the addition of two numbers are : " + addition(20, 10))
    # print("the subtraction of two numbers are : " + subtraction(20, 10))
    # print("the multiplication of two numbers are : " + sample1.multiplication(20, 10))
    # print("the division of two numbers are : " + sample2.division(20, 10))
    # loopsUses.rangeloop()
    # list1 = listComp1()
    # print(list1)
    # list2, value2 = listComp2()
    # print(list2)
    # print(value2)
    # dict1 = dictComp()
    # print(dict1)
    # number_list = [1, 2, 3]
    # str_list = ['one', 'two', 'three']
    #
    # # No iterables are passed
    # result_list = zip(number_list)
    #
    # # Converting iterator to list
    # print(result_list)
    # result_set = set(result_list)
    # print(result_set)
    # globals()

    # def make_pretty(func):
    #     def inner():
    #         print("I got decorated")
    #         func()
    #     return inner
    #
    # def ordinary():
    #     print("I am ordinary")
    #
    # pretty = make_pretty(ordinary)
    # print(ordinary)
    # pretty()
    # var = os.getcwd()
    # print(var)
    # data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'])
    # ser = pd.Series(data)
    # print(ser)
    # importing pandas as pd
    # import pandas as pd

    # dictionary of lists
    # dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
    #         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
    #         'score': [90, 40, 80, 98]}

    # creating a dataframe from a dictionary
    # df = pd.DataFrame(dict)
    # print(df)

    # iterating over rows using iterrows() function
    # for i, j in df.iterrows():
    #     print(i)
    #     if(j["name"]=="aparna"):
    #         j["degree"]="NA"
    #     print(j)
    # for key, value in df.iteritems():
    #     print(key)
    #     print(value)
# columns = list(df)
#
# for i in columns:
#     # printing the third element of the column
#     print(i)
#     print(df[i][2])
#     print("*"*20)y

    # importing pandas as pd
    # import pandas as pd
    #
    # # Creating a dictionary
    # d = {'id': ['1', '2', '3'],
    #      'Column 1.1': [14, 15, 16],
    #      'Column 1.2': [10, 10, 10],
    #      'Column 1.3': [1, 4, 5],
    #      'Column 2.1': [1, 2, 3],
    #      'Column 2.2': [10, 10, 10], }
    #
    # # Converting dictionary into a data-frame
    # df = pd.DataFrame(d)
    # print(df)
    #
    # groupby_dict = {'Column 1.1': 'Column 1',
    #                 'Column 1.2': 'Column 1',
    #                 'Column 1.3': 'Column 1',
    #                 'Column 2.1': 'Column 2',
    #                 'Column 2.2': 'Column 2'}

    # Set the index of df as Column 'id'
    # df = df.set_index('id')
    #
    # # Groupby the groupby_dict created above
    # df = df.groupby(groupby_dict, axis=1).sum()
    # print(df)
    # data = pd.date_range('1/1/2011', periods=10, freq='H')
    #
    # print(data)
    # Create the Timestamp object
    # ts = pd.Timestamp(year=2011, month=11, day=21,
    #                   hour=10, second=49, tz='US/Central')
    #
    # # Print the Timestamp object
    # print(ts)
    # print(ts.date())
    # this is one dimensional array

    # a = np.arange(24)
    # print(a)
    # print(a.ndim)
    #
    # # now reshape it
    # b = a.reshape(3, 4, 2)
    # print (b)
    # print(b.ndim)
    # b is having three dimensions

    # x = np.linspace(10, 11.5, 5)
    # print(x)
    # x = np.array([[1, 2], [3, 4], [5, 6]])
    # y = x[[1, 1, 1], [1, 1, 0]]
    # print(y)
    # a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
    # b = np.array([1.0, 2.0, 3.0])
    # print(a*b)
