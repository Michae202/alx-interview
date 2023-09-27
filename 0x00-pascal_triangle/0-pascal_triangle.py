#!/usr/bin/python3
"""
0-main

"""


def pascal_triangle(n):
    """
    Print the triangle
    """
    outer_List = []
    if n <= 0:
        return outer_List
    for i in range(n):
        inner_List = []
        if i == 0:
            inner_List.append(1)
        elif i == 1:
            inner_List.append(1)
            inner_List.append(1)

        else:
            for a in range(i + 1):
                if a == 0 or a == i:
                    inner_List.append(1)

                else:
                    j = outer_List[i - 1][a - 1] + outer_List[i - 1][a]
                    inner_List.append(j)

        outer_List.append(inner_List)
    return outer_List
