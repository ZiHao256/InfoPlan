import argparse
import os
import sys
import numpy as np
import networkx as nx
from Preprocessing.word2vec import node2vec
from gensim.models import Word2Vec
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from GenerateTreeNodeSet.get_DFS_node_list import AQPs2Tree
from GenerateTreeNodeSet.get_DFS_node_list import DFS


def parse_args():
    """
    解析得到node2vec的参数：
        input:          输入图的edge列表
        output:         输出训练得到数据——node index 和 vector
        dimensions:     得到的vector的维度，embedding size
        walk-length:    每个walk的长度
        num-walks:      对于nodes循环num-walks次构建walk
        window-size:    似乎和num-walks的值相同
        iter:           Number of epochs in SGD
        workers:        Number of parallel workers. Default is 8
        p:              Return hyperparameter，控制random walk的DFS概率
        q:              Inout hyperparameter，控制random walk的BFS概率，或相反
        weighted:       Boolean specifying (un)weighted
        directed:       Graph is (un)directed
    :return: 返回包含上述参数的arg实例
    """
    parser = argparse.ArgumentParser(description="Run node2vec.")
    # 输入数据集（节点树）的路径
    parser.add_argument('--input', nargs='?', default=input_file_name+'.json')
    # 输出训练数据的路径（node_index-vecotr字典）
    parser.add_argument('--output', nargs='?', default=os.path.abspath('.')+'/output/nodeindex-weightmetric.emb')
    # node vector的维度
    parser.add_argument('--dimensions', type=int, default=128)
    parser.add_argument('--walk-length', type=int, default=80)
    parser.add_argument('--num-walks', type=int, default=10)
    parser.add_argument('--window-size', type=int, default=10)
    parser.add_argument('--iter', default=1, type=int, help='Number of epochs in SGD')
    parser.add_argument('--workers', type=int, default=8, help='Number of parallel workers. Default is 8.')
    # p和q用于控制random walk的DFS和BFS的概率
    parser.add_argument('--p', type=float, default=1, help='Return hyperparameter. Default is 1.')
    parser.add_argument('--q', type=float, default=0.1, help='Inout hyperparameter. Default is 1.')
    parser.add_argument('--weighted', dest='weighted', action='store_true',
                        help='Boolean specifying (un)weighted. Default is unweighted.')
    parser.add_argument('--unweighted', dest='unweighted', action='store_false')
    parser.set_defaults(weighted=False)
    parser.add_argument('--directed', dest='directed', action='store_true',
                        help='Graph is (un)directed. Default is undirected.')
    parser.add_argument('--undirected', dest='undirected', action='store_false')
    parser.set_defaults(directed=False)

    return parser.parse_args()


def read_graph_from_edgelist():
    """
	Reads the input network in networkx.
	# 调用networkx包的read_edgelist函数，读入edgelist文件，得到 A networkx Graph or other type specified with create_using
	"""
    print("read the edgelist file from: ", args.input)
    if args.weighted:
        G = nx.read_edgelist(args.input, nodetype=str, data=(('weight', float),), create_using=nx.DiGraph())
    else:
        # 默认unweighted
        # Read a graph from a list of edges.
        G = nx.read_edgelist(args.input, nodetype=str, create_using=nx.DiGraph())
        for edge in G.edges():
            G[edge[0]][edge[1]]['weight'] = 1

    if not args.undirected:
        G = G.to_undirected()
    return G


def read_graph_from_tree(json_contents, AQP_tree_roots):
    """
    从python对象实现的AQP tree中构建networkx graph
    :param json_contents: AQP的个数
    :param AQP_tree_roots: 每个AQP的根节点序列
    :return: 处理得到的networkx图
    """
    # print(root_nodes)
    # 得到每个AQP的DFS遍历节点序列，得到每个AQP的root id
    AQP_DFS_node_list = []
    AQP_id = []
    for i in range(len(json_contents)):
        AQP_DFS_node_list.append(DFS(AQP_tree_roots[i]))
        AQP_id.append(AQP_tree_roots[i].id)

    # 创建networkx图，并加入每个AQP的所有节点、边
    G = nx.DiGraph()
    for i in range(len(json_contents)):
        # 加入一个AQP的所有node
        for j in range(len(AQP_DFS_node_list[i])):
            G.add_node(AQP_DFS_node_list[i][j].name + ":" + str(AQP_DFS_node_list[i][j].cost))
        # 加入一个AQP的所有edge
        for j in range(len(AQP_DFS_node_list[i])):
            if AQP_DFS_node_list[i][j].children:
                u = AQP_DFS_node_list[i][j]
                for k in range(len(AQP_DFS_node_list[i][j].children)):
                    v = (AQP_DFS_node_list[i][j].children)[k]
                    G.add_edge(
                        u.name + ":" + str(u.cost),
                        v.name + ":" + str(v.cost)
                    )
    # print(G.nodes)
    # print(G.edges)
    # 给边赋权重
    if args.weighted:
        raise Exception("TODO:weighted")
    else:
        for edge in G.edges():
            G[edge[0]][edge[1]]['weight'] = 1
    # 设置为undirected
    if not args.undirected:
        G = G.to_undirected()
    return G


def learn_embeddings(walks):
    """
	Learn embeddings by optimizing the Skipgram objective using SGD.
	"""
    # 对walks中的每个长度为walk_length的walk，将其中的元素node index由int转为str；
    # 并将str序列组成列表
    walks = [list(map(str, walk)) for walk in walks]
    # print(walks)
    # 调用Word2Vec函数，对walks列表进行训练：
    #   sentence: 训练数据，
    #   vector_size: 维度为dimensions
    #   window: 值与num_walk相同，Maximum distance between the current and predicted word within a sentence.
    #   sg: 训练算法为skip gram
    #
    model = Word2Vec(walks, vector_size=args.dimensions, window=args.window_size, min_count=0, sg=1,
                     workers=args.workers, epochs=args.iter)
    # 将训练得到的vector存储
    model.wv.save_word2vec_format(args.output)
    print("Store the input-hidden weight matrix to: ", args.output)
    return


def process_emb():
    # 将emb文件分解为NodeIndex文件和NodeVector文件
    w_file_NodeIndex = open(os.path.abspath(os.path.dirname(os.getcwd())) + "/GenerateTreeVector/dictfile/new/AQPNodeIndex.txt", 'w')
    w_file_NodeVector = open(os.path.abspath(os.path.dirname(os.getcwd())) + "/GenerateTreeVector/dictfile/new/AQPNodeVector.txt", 'w')

    # 读入每行，并将第一列存储，剩余另存储
    try:
        file = open(args.output, "r")  # 以读模式打开文件
    except FileNotFoundError:  # 如果文件不存在，给提示
        print("file is not found")
    else:
        contents = file.readlines()  # 读取全部行
        contents.pop(0)
        for content in contents:  # 显示一行
            # 将一行分为第一列和后面列
            content = content.split(' ', 1)
            w_file_NodeIndex.write(content[0] + '\n')  # 每行用逗号分隔后，取第一个元素
            w_file_NodeVector.write(content[1])
    w_file_NodeVector.close()
    w_file_NodeIndex.close()


def main(args):
    """
	Pipeline for representational learning for all nodes in a graph.
    """
    # 将json格式的AQP转换为Python对象的Tree
    input_path = os.path.abspath(os.path.dirname(os.getcwd())) + args.input
    json_contents, AQP_tree_roots = AQPs2Tree(input_path)

    # 构建networkx的图
    nx_G = read_graph_from_tree(json_contents, AQP_tree_roots)

    # 调用networkx包的read_edgelist函数，读入edgelist文件，得到 A networkx Graph or other type specified with create_using
    # nx_G = read_graph_from_edgelist()
    # 使用networkx中的graph、undirected、p和q作为参数，构建一个node2vec中的Graph实例
    G = node2vec.Graph(nx_G, args.directed, args.p, args.q)
    # Preprocessing of transition probabilities for guiding the random walks.
    G.preprocess_transition_probs()
    # Repeatedly simulate random walks from each node.
    walks = G.simulate_walks(args.num_walks, args.walk_length)
    # print(len(walks), walks)
    # Learn embeddings by optimizing the Skipgram objective using SGD.
    learn_embeddings(walks)

    # 将nodeindex-weightmetric文件处理并存储到GenerateTreeVector/dictfile/new目录中
    process_emb()


if __name__ == "__main__":

    print("input input file name(drop out .json)")
    input_file_name = input()
    input_file_name = '/Preprocessing/input/'+input_file_name
    # 解析得到node2vec的输入参数
    args = parse_args()
    main(args)
