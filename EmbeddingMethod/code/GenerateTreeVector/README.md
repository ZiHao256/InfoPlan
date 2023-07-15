`GenerateTreeVector`目录：
- 主要完成Step2、Step3：得到sentence vector，并比较欧氏距离

`generate_and_compare.py`
- 首先，从redis数据库中读取到，被检测源码的node序列；
- 接着，从`dictfile`下读取到训练数据，接着构建node-vector字典；
- 接着，Step2：调用sent2vec模型，基于node-vector字典得到每个AQP的vector
- 最后，Step3：并比较欧氏距离