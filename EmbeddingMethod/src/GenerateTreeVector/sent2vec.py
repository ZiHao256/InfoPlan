# 句向量模型
import numpy as np
from sklearn.decomposition import PCA
from typing import List
np.set_printoptions(suppress=True)
class Word:
    def __init__(self, text, vector):
        self.text = text        # node index
        self.vector = vector    # skip gram模型训练得到的vector

class Sentence:
    def __init__(self, word_list):
        self.word_list = word_list

    def len(self): #-> int:
        return len(self.word_list)

def cal_distance(vec1, vec2):
    dist = np.linalg.norm(vec1 - vec2)
    return dist

def sentence_to_vec(sentence_list: List[Sentence], embedding_size: int, fredict):
    """
    首先，对每个method对应的Word序列，用每个单词权重乘每个Word vector，将一个sentence中的所有Word Vector相加（1*embedding）。
    接着，将得到的vs合并为一个数组sentence_set
    然后，对sentence_set进行主成分分析，并进行加权平均，得到每个method对应的sentence vector
    :param sentence_list: 每个method对应的Sentence实例（Word实例的序列）
    :param embedding_size: 每个Word中vector的维度——128
    :param fredict: 以fredict.txt中数据的，node index为索引，词频为值，创建的一维数组
    :return: 返回处理得到的sentence vector序列，为embedding_size * n，n为method的个数即sentence的个数
    """
    sentence_set = []
    a = 0.1  # 参考teccd近日方法改动：对词向量加权平均，初步得到一个句子向量。包含一个单词权重公式，其中a为超参数，如果一个单词在语料库中出现的越频繁，则权重越低

    for sentence in sentence_list:
        vs = np.zeros(embedding_size)       # 初始化128个0的数组
        sentence_length = sentence.len()    # 该sentence实例中Word的个数
        for word in sentence.word_list:     # 考虑该sentence中每个word
            if(len(fredict) == 0):          # 语料库为空？
                a_value = a / (a + 1)       # 单词权重公式中的词频p(w)默认为1
            else:                           # 非也
                a_value = a / (a + np.float(fredict.get(word.text)))    # 词频p(w)，从fredict字典中以node index为索引， 得到词频作为p(w)
            vs = np.add(vs, np.multiply(a_value, word.vector))          # 首先对word vector中每个元素都乘该单词权重a_value，
                                                                        # 接着将该sentence所有的word vector都相加
        vs = np.divide(vs, sentence_length)
        sentence_set.append(vs)                                         # 将经过单词权重处理、相加、归一化，得到的所有sentence vector构成一个序列

    # Principal Component Analysis:主成分分析法，用于高维数据的降维，提取数据的主要特征
    # 参考：https://zhuanlan.zhihu.com/p/77151308
    # pca = PCA(n_components=embedding_size)             # PCA设置的参数n_components必须 <= min(样本量，特征量).
    pca = PCA(n_components=min(embedding_size, len(sentence_list)))
    pca.fit(np.array(sentence_set))                    # 用训练数据embedding_size * n填充模型，
    u = pca.components_[0]                             # components为特征空间中的主轴，表示数据中最大方差的方向。等价地，中心输入数据的右奇异向量，平行于其特征向量。组件按explained_variance_递减排序。
    u = np.multiply(u, np.transpose(u))                # u矩阵对角化
    if len(u) < embedding_size:                        # 不太理解,填充u矩阵？
        for i in range(embedding_size - len(u)):
            u = np.append(u, 0) 
    sentence_vecs = []
    for vs in sentence_set:                            # 对于sentence_set中的每个sentence_vec
        sub = np.multiply(u, vs)                        # 求得u和vs的内积sub
        sentence_vecs.append(np.subtract(vs, sub))      # 将vs各元素减去内积sub矩阵各元素，并将其append到sentence_vecs序列中
    return sentence_vecs
