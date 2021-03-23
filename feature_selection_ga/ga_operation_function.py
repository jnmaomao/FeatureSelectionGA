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
import random


def cx_two_point_adv(ind1, ind2):
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


def mut_flip_bit_keep_point_num(individual, indpb):
    """Flip the value of the attributes of the input individual and return the
    mutant. The *individual* is expected to be a :term:`sequence` and the values of the
    attributes shall stay valid after the ``not`` operator is called on them.
    The *indpb* argument is the probability of each attribute to be
    flipped. This mutation is usually applied on boolean individuals.

    :param individual: Individual to be mutated.
    :param indpb: Independent probability for each attribute to be flipped.
    :returns: A tuple of one individual.

    This function uses the :func:`~random.random` function from the python base
    :mod:`random` module.
    """

    feature_num = len(np.nonzero(np.asarray(individual))[0])

    for i in range(len(individual)):
        if random.random() < indpb:
            individual[i] = type(individual[i])(not individual[i])

    # make the feature numbers consistent
    individual_new_np = np.asarray(individual)
    feature_num_new = len(np.nonzero(individual_new_np)[0])

    diff_feature_num = feature_num - feature_num_new
    if diff_feature_num > 0:
        # add featrue for consistent
        fix_index = np.random.choice(np.where(individual_new_np == 0)[0], diff_feature_num, replace=False)
        for index in fix_index:
            individual[index] = 1
    elif diff_feature_num < 0:
        # remove featrue for consistent
        # attention: random or numpy.random is resample cause index has same value,must set replace=False
        fix_index = np.random.choice(np.where(individual_new_np == 1)[0], abs(diff_feature_num), replace=False)

        for index in fix_index:
            individual[index] = 0

    return individual,
