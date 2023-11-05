from cnt_vctzer import CountVectorizer
from math import log


def tf_transform(cnt_matrix: list) -> list[list]:
    """Transform a Term Frequency matrix with a count_matrix"""
    tf_mat = []
    for part in cnt_matrix:
        total_summ = sum(part)
        tf_mat.append([el / total_summ for el in part])
    return tf_mat


def idf_transform(cnt_matrix: list) -> list[float]:
    """Transform an Inverse Document Frequency (IDF) vector"""
    idf_mat = []
    len_corpus_matrix = len(cnt_matrix) + 1
    for i in range(len(cnt_matrix[0])):
        word_docs = 1
        for part in cnt_matrix:
            if part[i] > 0:
                word_docs += 1
        idf_mat.append(log(len_corpus_matrix / word_docs) + 1)
    return idf_mat


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(f'The result of .get_feature_names method:'
          f'\n  {vectorizer.get_feature_names()}\n')
    print(f'The count matrix:'
          f'\n  {count_matrix[0]},'
          f'\n  {count_matrix[1]}\n ')

    print(tf_transform(count_matrix), '\n')
    print(idf_transform(count_matrix), '\n')
