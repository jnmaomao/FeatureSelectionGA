# -*- coding: utf-8 -*-
"""

@File : ga_operation_function.py
@Author: panyx
@Date : 2021/3/19 16:01
@Desc :


@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/3/19 16:01   panyx      1.0         None

"""
import numpy as np


def cxTwoPoint_adv(ind1, ind2):
    """Executes a two-point crossover on the input :term:`sequence`
    individuals. The two individuals are modified in place and both keep
    their original length and selected feature num size.
    Keep the both advantageous gene use numpy.intersect1d
    Random Keep one of the advantageous gene use numpy.setxor1d
    :param ind1: The first individual participating in the crossover.
    :param ind2: The second individual participating in the crossover.
    :returns: A tuple of two individuals.
    """
    size = min(len(ind1), len(ind2))
    ind1_np, ind2_np = np.asarray(ind1), np.asarray(ind2)
    ind1_featrue, ind2_featrue = np.where(ind1_np == 1)[0], np.where(ind2_np == 1)[0]
    interscation_feature = np.intersect1d(ind1_featrue, ind2_featrue)
    union_feature = np.setxor1d(ind1_featrue, ind2_featrue)

    ind1_featrue_new = np.hstack(
        (interscation_feature,
         np.random.choice(union_feature, len(ind1_featrue) - len(interscation_feature), replace=False)))
    ind2_featrue_new = np.hstack(
        (interscation_feature,
         np.random.choice(union_feature, len(ind2_featrue) - len(interscation_feature), replace=False)))

    for i in range(0, len(ind1)):
        if i in ind1_featrue_new:
            ind1[i] = 1
        else:
            ind1[i] = 0

    for i in range(0, len(ind2)):
        if i in ind2_featrue_new:
            ind2[i] = 1
        else:
            ind2[i] = 0

    return ind1, ind2
