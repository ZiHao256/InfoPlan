new目录下的文件：
- `ruleindex.txt`: 在preprocessing步骤，对语料库进行skipgram模型训练，得到的random walk次序的node index序列
- `rulevector.txt`: 在preprocessing步骤，对语料库进行skipgram模型训练，得到的对应于node index序列的128维度的vector序列
- `avaluedict.txt`: 上面两个文件得到的字典
- `fredict.txt`: node index和词频对