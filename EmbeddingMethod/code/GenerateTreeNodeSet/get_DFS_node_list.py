import json
import os
import redis
import time


class AQPNode:
    def __init__(self, cost, name):
        self.cost = cost  # 每个节点都有cost
        self.name = name  # 除了根节点都有name，根节点name为空
        self.id = -1  # 只有根节点有id，其他为-1
        self.children = []


def build_AQP(json_object):
    """
    递归构建树形的AQP
    :param json_object: 部分JSON数据，dict/list
    :return: 根node
    """
    object_node_keys = json_object.keys()
    if "content" in object_node_keys:
        # 为根节点
        node = AQPNode(json_object.get("cost"), "root")
        content_node = build_AQP(json_object.get("content"))
        node.children.append(content_node)
        return node
    else:
        # 为content内部节点
        node = AQPNode(cost=json_object.get("cost"), name=json_object.get("name"))
        if json_object.get("child_flag"):
            # 有孩子节点
            json_array = json_object.get("child")
            for i in range(len(json_array)):
                child_node = build_AQP(json_array[i])
                node.children.append(child_node)
        return node


def DFS(root):
    """
    DFS遍历AQP Tree
    :param root: AQP Tree的root node
    :return: DFS顺序的AQP Tree Node序列
    """
    stack = []
    AQP_DFS_node_list = []
    stack.append(root)

    while stack:
        cur_node = stack.pop()
        AQP_DFS_node_list.append(cur_node)
        # print(cur_node.name, cur_node.id, cur_node.cost)
        if cur_node.children:
            for i in reversed(range(len(cur_node.children))):
                stack.append(cur_node.children[i])
    return AQP_DFS_node_list


def AQPs2Tree(input_path):
    json_contents_str = ""

    f = open(input_path)  # 打开文件
    iter_f = iter(f)  # 创建迭代器
    for line in iter_f:  # 遍历文件，一行行遍历，读取文本
        json_contents_str = json_contents_str + line

    # 解析JSON文件的str格式为dict和list
    json_contents = json.loads(json_contents_str)
    # print(json_contents)

    # 构建多个AQP Trees
    AQP_tree_roots = []
    for i in range(len(json_contents)):
        AQP_tree_roots.append(build_AQP(json_contents[i]))
        # 每个AQP根节点的id设置为自增
        AQP_tree_roots[i].id = i
    return json_contents, AQP_tree_roots


def get_DFS_node_list(input_file_name):
    time_start = time.time()
    print("开始时间：", time.time())

    # 读入input/AQPs.json
    input_path = os.getcwd() + '/input/' + input_file_name + '.json'

    # 从json——>Tree
    json_contents, AQP_tree_roots = AQPs2Tree(input_path)

    # 得到每个AQP的DFS遍历节点序列，得到每个AQP的root id
    AQP_DFS_node_list = []
    AQP_id = []
    for i in range(len(json_contents)):
        AQP_DFS_node_list.append(DFS(AQP_tree_roots[i]))
        AQP_id.append(AQP_tree_roots[i].id)
    # print(AQP_DFS_node_list)
    # print(AQP_id)

    # 收集每个AQP
    sentences = []
    for i in range(len(json_contents)):
        sentence = ""
        for j in range(len(AQP_DFS_node_list[i])):
            sentence += \
                AQP_DFS_node_list[i][j].name + ":" + \
                str(AQP_DFS_node_list[i][j].cost) + ","
        sentences.append(sentence)

    # 连接redis
    pedis = redis.Redis(host='127.0.0.1', port=6379, db=0)

    # 清空
    for element in pedis.keys():
        pedis.delete(element)

    # 将每个AQP的id作为key，id-name-cost序列作为value，存储到redis中
    for i in range(len(json_contents)):
        pedis.set(AQP_id[i], sentences[i])

    return time_start


if __name__ == '__main__':

    while 1:
        print('input the name of query file(q to quit)')
        input_file_name = input()
        if input_file_name == 'q':
            break

        time_start = get_DFS_node_list(input_file_name)

        time_end = time.time()
        print("结束时间：", time.time())

        # 记录消耗时间
        print('time cost', time_end - time_start, 's')
        fout_time = open(
            os.getcwd() + '/output/' + input_file_name[0:4] + '/' + input_file_name[5:] + '/generate_nodeset_time.txt',
            'w+')
        fout_time.write(str(time_end - time_start))
        fout_time.close()
