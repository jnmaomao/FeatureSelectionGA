# -*- coding: utf-8 -*-
"""

@File : individual_gen_function.py
@Author: panyx
@Date : 2021/3/19 16:54
@Desc :


@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/3/19 16:54   panyx      1.0         None

"""
import random


def randint_scale(cls, true_proportion=0.5):
    if random.random() <= true_proportion:
        return 1
    else:
        return 0
