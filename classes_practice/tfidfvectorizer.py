from cnt_vctzer import CountVectorizer
from tfidftransformer import TfidfTransformer


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tf_idf_transformer = TfidfTransformer()

    def fit_transform(self, part: list[str]) -> list[list]:
        """
        Makes feature from text with CountVectorizer class;
        Makes tf-idf matrix from count matrix with
            TfidfTransformer class
        """
        cnt_matrix = super().fit_transform(part)
        return self.tf_idf_transformer.fit_transform(cnt_matrix)
