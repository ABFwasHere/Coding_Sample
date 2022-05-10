import pandas as pd
import numpy as np
import ast

pd.options.display.max_columns = 100
df = pd.read_msgpack("../../MP_General/2020 Election/L2.msg").iloc[:, range(0,9)].drop([0,1,2,3,170960,170961])

def L2_Query():
    df = pd.read_msgpack("../../MP_General/2020 Election/L2.msg").iloc[:, range(0,9)].drop([0,1,2,3,170960,170961])
    def search_col():
        print(df.columns)
        query_split = input("enter a column to view all possible values or 'back' to return to query main: ")
        for i in df.columns:
            if i == str(query_split):
                print(getattr(df, query_split).unique())
                query_split = input("search again? [y/n] ")
                if query_split == "y":
                    return search_col()
                elif query_split == "n":
                    return L2_Query()
        if query_split == "back":
            return L2_Query()
    query_split = input("enter 'columns' to view all columns or pass to query: ")
    if query_split == "columns":
        return search_col()
    filters = ast.literal_eval(input("enter filters as a dictionary: "))
    variables = ast.literal_eval(input("enter variables as a list: "))
    for key, item in filters.items():
        df = df[df[key].isin([item])]
    dfReset = df
    for var in variables:
        for unique in getattr(df, var).unique():
            df = df[df[var].isin([unique])]
            print(str(filters) + " " + var + " " + unique + " Total " + str(df["Total Voters"].sum()))
            print("Hispanic Voters " + str(df["Hispanic Voters"].sum()))
            print("Non-Hispanic Voters " + str(df["Total Voters"].sum() - df["Hispanic Voters"].sum()))
            print(" ")
            df = dfReset
    query_split = input("search again? [y/n] ")
    if query_split == "y":
        return L2_Query()
    elif query_split == "n":
        pass
# L2_Query({"State" : "TX"}, ["Gender"])


# def filterTest(filters):
#     df = pd.read_msgpack("../../MP General/L2.msg").iloc[:, range(0,9)].drop([0,1,2,3,170960,170961])
#     for key, item in filters.items():
#         df = df[df[key].isin([item])]

# filterTest({"State" : "TX", "Party Affiliation" : "Democratic"})

# def varTest(variables):
#     count = 0
#     nonHispanic = 0
#     df = pd.read_msgpack("../../MP General/L2.msg").iloc[:, range(0,9)].drop([0,1,2,3,170960,170961])
#     dfReset = df
#     for var in variables:
#         for unique in getattr(df, var).unique():
#             df = df[df[var].isin([unique])]
#             print(var + " " + unique + " Total " + str(df["Total Voters"].sum()))
#             print("Hispanic Voters " + str(df["Hispanic Voters"].sum()))
#             print("Non-Hispanic Voters " + str(df["Total Voters"].sum() - df["Hispanic Voters"].sum()))
#             print(" ")
#             df = dfReset
# varTest(["Gender", "Age Range"])
