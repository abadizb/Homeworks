import os
import shelve
from datetime import datetime
def searcher(x, search):
    List = []
    Dict = shelve.open(x)
    
    query=input("Enter:")

    dt1 = datetime.now()
    if "or" in (query) and "and" not in (query):
        query.remove("or")
        print (query)
            for item in query:
                if (item in Dict):
                    query = []
                    query = query+Dict[item]
                    query = set(query)
                    query = list(query)
                    for item in query:
                        print(item)
                        dt2= datetime.now()
                        print("Execution time:", dt2.microsecond-dt1.microsecond)
    elif "and" in (query):
        query.remove("and")
        if "or" in (query):
            query.remove("or")
        print (query)
        Dict_list1 = Dict [query[0]]
        for x in query:
            Dict_list2 = Dict[x]
            Dict_list1 = set.intersection(Dict_list2)
            Dict_list1 = list.intersection(Dict_list2)
            for quote in Dict_list1:
                print(quote)
                dt2= datetime.now()
                print("Execution time:", dt2.microsecond-dt1.microsecond)
    else:
        print (query)
        Dict[query[0]]
        Dict = set (query)
        Dict = list (query)
        for value in Dict[query[0]]:
                print(value)
                dt2= datetime.now()
                print("Execution time:", dt2.microsecond-dt1.microsecond)

searcher()
        
