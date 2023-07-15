完成Step1:解析JSON格式AQP，对其DFS遍历，得到node序列
- 一个Node的表示：`OpName:Cost`
  - 例如`root:3908.3007938916053`
- DFS顺序的Node序列，使用`,`隔开：`OpName:Cost, OpName:Cost`
  - 一个Node序列代表一个AQP：`root:3908.3007938916053, InnerHashJoin:3908.3007938916053`

- 传入redis中：
  - key：AQP的id
    - 例如：`1`
  - value：上述的AQP序列