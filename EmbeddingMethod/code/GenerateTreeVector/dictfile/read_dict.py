def read_rule_file(file_name):
    result = []
    file = open(file_name)
    for line in file.readlines():
        line = line.strip()
        result.append(line)
        if not len(line) or line.startswith('#'):
            continue
    return result


# 根据skip gram训练得到的node索引rule_index和对应的vec，得到node-vec字典——rule_dict
def get_AQP_node_dict(rule_index_file, rule_vec_file):
    rule_dict = {}
    rule_index = read_rule_file(rule_index_file)
    rule_vec_str = read_rule_file(rule_vec_file)

    rule_vec = []
    for r in rule_vec_str:
        r_vec = []
        rr = r.split(' ')
        for s in rr:
            r_vec.append(float(s))
        rule_vec.append(r_vec)

    for i in range(len(rule_index)):
        rule_dict.__setitem__(rule_index[i], rule_vec[i])
    return rule_dict

