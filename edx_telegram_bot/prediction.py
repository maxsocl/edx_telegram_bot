# -*- coding: utf-8 -*-

import snowballstemmer
import numpy as np
import sklearn as sk
import scipy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def get_stop_words():
   result = set()
   for line in open('stopwords_en.txt', 'r').readlines():
        result.add(line.strip())
   return result


def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx


def get_test_courses(matrix_of_courses):
    output = []
    cosine_similarities = linear_kernel(matrix_of_courses[np.random.randint(0,matrix_of_courses.shape[0]-1)],
                                        matrix_of_courses).flatten()
    list_of_indexes = np.linspace(cosine_similarities.min(), cosine_similarities.max(), num=15)
    for each in list_of_indexes:
        output.append(find_nearest(cosine_similarities, each))
    return set(output)


def i_am_going_to_teach_you(learn_matrix, answer, is_right = False, teaching_coeff = 0.01 ):
    for each in answer.indices:
        if each in learn_matrix.indices:
            learn_index = np.where(learn_matrix.indices == each)[0][0]
            answer_index = np.where(answer.indices == each)[0][0]
            if is_right:
                learn_matrix.data[learn_index] = learn_matrix.data[learn_index] + np.float64(teaching_coeff)
            else:
                learn_matrix.data[learn_index] = learn_matrix.data[learn_index] - np.float64(teaching_coeff)
    return learn_matrix


def prediction(user_matrix, course_matrix):
    cosine_similarities = linear_kernel(user_matrix, course_matrix).flatten()
    related_docs_indices = cosine_similarities.argsort()
    little_random = np.random.randint(5,10)
    print courses[related_docs_indices[-little_random]]
    if raw_input('Do you like it') != '1':
        user_matrix = i_am_going_to_teach_you(user_matrix,course_matrix[related_docs_indices[-10]])
    else:
        user_matrix = i_am_going_to_teach_you(user_matrix,course_matrix[related_docs_indices[-10]], is_right=True)