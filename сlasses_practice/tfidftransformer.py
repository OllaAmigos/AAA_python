from math import log


class TfidfTransformer:
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
        len_mat = len(cnt_matrix) + 1
        for i in range(len(cnt_matrix[0])):
            word_cnt = 1
            for part in cnt_matrix:
                if part[i] > 0:
                    word_cnt += 1
            idf_mat.append(log(len_mat / word_cnt) + 1)

        return idf_mat

    def fit_transform(self, cnt_matrix: list[float]) -> list[list]:
        """Make TF-IDF transformation from idf_transform and tf_transform"""
        tf_mat = self.tf_transform(cnt_matrix)
        idf_vec = self.idf_transform(cnt_matrix)

        return [[tf_vec[i] * idf_vec[i] for i in range(len(tf_vec))]
                for tf_vec in tf_mat]