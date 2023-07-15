# Description: 主要是获取redis中AQP的DFS node, 然后调用两层sent2vec模型, 最后求vector之间的欧式距离
import os
import redis
import numpy as np
from dictfile.read_dict import get_AQP_node_dict
from dictfile.read_dict import read_rule_file
from sent2vec import Word
from sent2vec import Sentence
from sent2vec import sentence_to_vec
from sklearn import preprocessing
import collections
import time


class AQP:
    def __init__(self, id, key, statement, vector):
        self.id = id  # AQP的自增ID
        self.key = key  # Id
        self.statement = statement  # 由sent2vec中的Word实例（node index：vector）序列够成
        self.vector = vector  # 初始为空，后续补充为该method对应的sentence vector
        self.distance = -1.0  # AQP与QEP之间的向量距离
        self.distance_norm = -1.0  # 归一化后的距离


def getAQPWords(nodes):
    """
    对于给定method的每个node，根据node index在node-vec字典中找到其对应的vector，调用sent2vec中的Word构造函数，并将Word实例加入到该method对应的Word序列method_vec_list
    :param nodes:
    :return:
    """
    AQP_node_vec_list = []
    for index in nodes:
        if index in AQP_node_dict.keys():
            word_list.append(index)
            word = Word(index, AQP_node_dict[index])
            AQP_node_vec_list.append(word)
    return AQP_node_vec_list


def getRedisAQPs():
    """
    为redis数据库中收集的每个method（key：value），以method的id、key、line、Word序列构建Method实例，并得到Method实例序列
    :return:
    """
    AQPs = []
    for i in range(data_size):
        key = keys[i].decode()
        # 将redis中的一个AQP分解为多个node，分隔符为`,`
        node_seq = jedis.get(keys[i]).decode().split(",")
        AQP_nodes = list(node_seq)
        vector = []
        # 调用sent2vec，得到该method_i对应的Word序列，组成statement
        statement = getAQPWords(AQP_nodes)
        # 构建Method实例
        aqp = AQP(i, key, statement, vector)
        AQPs.append(aqp)
    return AQPs


def get_word_counts(word_list):
    word_counts = collections.Counter(word_list)
    return word_counts


def get_word_frequency(word_text, word_counts, word_list_len):
    word_count = word_counts.get(word_text)
    if (word_count != None):
        # print(word_text, word_count, word_list_len)
        return (word_counts.get(word_text) * 1.0 / (word_list_len * 1.0))
    else:
        return 1.0


def getWordFrequencyDict(word_list):
    """
    根据
    :param word_list:
    :return:
    """
    word_counts = get_word_counts(word_list)
    word_list_len = len(word_list)
    rule_indexs = read_rule_file(AQP_node_index_path)

    # 清空fre_dict
    f_dict = open(AQP_node_fre_path, 'w')
    f_dict.truncate(0)

    for word_text in rule_indexs:
        word_frequency = get_word_frequency(word_text, word_counts, word_list_len)
        # a_value = a / (a + word_frequency)
        with open(AQP_node_fre_path, 'a+') as fw:
            s = str(word_text) + " " + str(word_frequency) + '\n'
            fw.write(s)


def getAvalueDict():
    """
    根据fredict.txt文件中的index-value序列，创建以index为索引，值为value的一维数组avaluedict
    :return:
    """
    getWordFrequencyDict(word_list)
    avaluedict = {}
    for line in open(AQP_node_fre_path):
        kv = line.split(" ")
        avaluedict[kv[0]] = kv[1].replace("\n", "")
    return avaluedict


def getVectorAQPs():
    """
    对于AQP实例序列，补充每个AQP实例的sentence vector
    :return:
    """
    AQPs = getRedisAQPs()  # AQP 实例序列
    avaluedict = getAvalueDict()  # 根据fredict.txt，构建以node index为索引，单词频率为值的一维数组
    sentence_list = []  # Sentence实例（AQP节点序列）的序列
    # 将每个AQP对应的Word实例序列，作为参数创建一个Sentence实例
    for i in range(len(AQPs)):
        sentence_list.append(Sentence(AQPs[i].statement))
    # 将每个method对应的Sentence实例转换为vector
    sentence_vectors = sentence_to_vec(sentence_list, embedding_size, avaluedict)
    # 将sentence_vectors赋值给method中对应的成员变量
    for i in range(len(AQPs)):
        AQPs[i].vector = sentence_vectors[i]
    return AQPs


def cal_l2_dist(vec1, vec2):
    return np.sqrt(np.sum(np.square(vec1 - vec2)))


def cal_distance(vec1, vec2):
    dist = np.linalg.norm(vec1 - vec2)
    return dist


def min_max_normalization(distance_list):
    min_max_scaler = preprocessing.MinMaxScaler()
    distance_list_norm = min_max_scaler.fit_transform(np.array(distance_list).reshape(-1, 1))
    return distance_list_norm


def method_compare():
    """
    对于redis中的每个method（由Word实例序列够成），通过sent2vec，
    利用单词频次和权重，处理得到每个method的sentence vector，
    接着，两两计算得到sentence vector间的欧氏距离
    :return: 返回欧氏距离矩阵
    """
    # 得到redis中每个AQP对应的AQP class实例：包含sentence vector
    AQPs = getVectorAQPs()

    # 输出AQP个数
    print("the number of AQPs:", len(AQPs))

    # 得到每个AQP与QEP的向量距离
    distance_list = [0]
    for i in range(len(AQPs)):
        if i == 0:
            continue
        distance_list.append(cal_l2_dist(AQPs[0].vector, AQPs[i].vector))

    # 得到归一化的向量距离
    distance_list_norm = min_max_normalization(distance_list)
    for i in range(len(AQPs)):
        AQPs[i].distance_norm = distance_list_norm[i][0]
        AQPs[i].distance = distance_list[i]

    # 按照向量距离从大到小对AQPs排序
    AQPs_sorted = sorted(AQPs, key=lambda aqp: aqp.distance, reverse=True)

    print("farthest AQP from QEP: ", AQPs_sorted[0].id, AQPs_sorted[0].distance_norm)
    print("closet AQP from QEP: ", AQPs_sorted[len(AQPs) - 1].id, AQPs_sorted[len(AQPs) - 1].distance_norm)
    return AQPs_sorted


def i_tips(cnt):
    return AQPs_sorted[cnt]


def b_tips(k):
    return AQPs_sorted[:k]


def calculate_interestingness(selected_AQPs):
    """
    对
    :param selected_AQPs:
    :return:
    """

    interestingness = 0

    return interestingness


if __name__ == '__main__':
    # 输入查询name
    print('input the name of query')
    query_name = input()

    # 得到被检测源码中每个method的key
    jedis = redis.Redis(host='127.0.0.1', port=6379, db=0)
    keys = jedis.keys()

    data_size = len(keys)  # redis中method的个数/记录的条数
    word_list = []  # 存储redis中存在于node-vec字典中的node index
    embedding_size = 128  # 记录node vector的维度

    # 得到node-vec字典训练数据
    dict_path = os.path.abspath(os.path.dirname(os.getcwd())) + '/GenerateTreeVector/dictfile/new/'
    AQP_node_index_path = dict_path + 'AQPNodeIndex.txt'
    AQP_node_vector_path = dict_path + 'AQPNodeVector.txt'
    AQP_node_fre_path = dict_path + 'AQPNodeFreDict.txt'

    # 得到skip gram模型训练得到的node-vec字典
    AQP_node_dict = get_AQP_node_dict(AQP_node_index_path, AQP_node_vector_path)

    time_start = time.time()
    print("开始时间：", time.time())
    print("data_size: ", data_size)

    # 比较得到QEP与每个AQP vector间的欧氏距离
    AQPs_sorted = method_compare()
    time_end = time.time()
    print("结束时间：", time.time())
    print('time cost', time_end - time_start, 's')

    # 记录消耗时间
    print('time cost', time_end - time_start, 's')
    fout_time = open(
        os.getcwd() + '/output/' + query_name[0:4] + '/' + query_name[5:] + '/generate_aqp_vector_time.txt',
        'w+')
    fout_time.write(str(time_end - time_start))
    fout_time.close()

    # choose TIPS
    print("i(i-tips) / b(b-tips?")

    choose = input()

    if choose == 'i':
        cnt = 0
        while choose == 'i':
            t = i_tips(cnt)
            print(cnt, t.id, t.distance_norm)
            cnt += 1
            choose = input()
    elif choose == 'b':
        # get k
        print("input the number of AQPs to be selected(q to quit)")
        k = input()

        # get name & id
        db_name = query_name[0:4]
        query_id = query_name[5:]

        # 将selected AQP序号写入到相应文件中
        output_file_path = (os.path.abspath(
            os.path.dirname(os.getcwd())) + '/GenerateTreeVector/output/' + db_name + '/' + query_id + '/' + str(k) + '_selected_aqps.txt')

        # get selected AQPs
        aqps = b_tips(int(k))

        # convert to string
        selected_query = ''
        for i in range(int(k)):
            print(i, aqps[i].id, aqps[i].distance_norm)
            selected_query += str(aqps[i].id)+'\n'
        selected_query = selected_query.rstrip('\n')

        # storage
        output_file = open(output_file_path, 'w')
        output_file.write(selected_query)
        output_file.close()

    else:
        print("wrong char")
