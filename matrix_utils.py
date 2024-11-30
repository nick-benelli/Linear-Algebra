#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility functions for matrix operations, including projection, transposition,
reduced row echelon form (RREF) calculation, and transition probabilities.

Author: Nick Benelli
Date: February 23, 2021
"""

import numpy as np
import sympy

# Identity matrix
IDENTITY_MATRIX = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])


def array_to_np_matrix(array: list[list[float]]) -> np.ndarray:
    """
    Converts a 2D list to a NumPy array.

    Parameters:
    - array (list[list[float]]): Input 2D list.

    Returns:
    - np.ndarray: Equivalent NumPy array.
    """
    return np.asarray(array)


def transpose_matrix(matrix: list[list[float]]) -> np.ndarray:
    """
    Computes the transpose of a given matrix.

    Parameters:
    - matrix (list[list[float]]): Input 2D list or array.

    Returns:
    - np.ndarray: Transposed matrix.
    """
    return np.asarray(matrix).transpose()


def project_b_colspace(b: np.ndarray, colspace_a: np.ndarray, need_transpose: bool = False) -> np.ndarray:
    """
    Projects vector b onto the column space of matrix A.

    Parameters:
    - b (np.ndarray): The vector to project.
    - colspace_a (np.ndarray): Matrix defining the column space.
    - need_transpose (bool): If True, transposes `b` before projection.

    Returns:
    - np.ndarray: The projected vector.
    """
    if need_transpose:
        b = b.transpose()

    a_trans = colspace_a.transpose()
    ata = np.matmul(a_trans, colspace_a)
    a_trans_a_inv = np.linalg.inv(ata)
    projection_matrix = np.matmul(colspace_a, np.matmul(a_trans_a_inv, a_trans))
    projection = np.matmul(projection_matrix, b)

    print(projection)  # Debug print
    return projection


def rref(matrix: list[list[float]]) -> tuple:
    """
    Computes the Reduced Row Echelon Form (RREF) of a matrix.

    Parameters:
    - matrix (list[list[float]]): Input matrix.

    Returns:
    - tuple: A tuple containing the RREF matrix and pivot columns (sympy format).
    """
    sympy_matrix = sympy.Matrix(matrix)
    rref_matrix = sympy_matrix.rref()

    print(rref_matrix)  # Debug print
    return rref_matrix


def transition_probability(initial_prob: np.ndarray, transition_matrix: np.ndarray, periods: int) -> np.ndarray:
    """
    Calculates the state probabilities after a given number of transitions.

    Parameters:
    - initial_prob (np.ndarray): Initial probability distribution.
    - transition_matrix (np.ndarray): Transition probability matrix.
    - periods (int): Number of transition periods.

    Returns:
    - np.ndarray: Final probability distribution.
    """
    transition_matrix = np.asarray(transition_matrix)
    initial_prob = np.asarray(initial_prob)

    transition_power = np.linalg.matrix_power(transition_matrix, periods)
    print(transition_power)  # Debug print

    final_prob = np.matmul(initial_prob, transition_power)
    return final_prob
