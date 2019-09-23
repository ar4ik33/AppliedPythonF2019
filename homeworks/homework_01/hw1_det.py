#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    det = 1.0
    m = len(list_of_lists)
    n = len(list_of_lists[0])
    if m == n:
        b = 1.0
        k = 1.0
        e = 1.0
        for i in range(m):
            for j in range(i+1, n):
                if list_of_lists[j][i] != 0:
                    b = list_of_lists[i][i] / list_of_lists[j][i]
                    for s in range(m):
                        e = list_of_lists[j][s] * b
                        list_of_lists[j][s] = e * b - list_of_lists[i][s]
                k = k / b
        for i in range(n):
            det = det * list_of_lists[i][i]
        det = det * k
        return det
