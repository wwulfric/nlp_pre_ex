- 不需要分词
- 应该移出标点符号，并按照语句划分块，不应该存在跨语句的二元词组。UTF8没找到比较好的标点符号的正则范围，所以可以考虑使用黑名单过滤标点符号，并按照特定的标点划分语句块（逗号，句号，分号等）
- 速度比较慢，sort 的时间复杂度是 nlgn，但题意要求只需要输出前十个，事实上时间复杂度可以压到 n 的，代码上需要稍作处理 
- 可以考虑剔除包含停止词的二元词组，比如的，了等
- 自然语言处理是个技术+脏活的组合，需要耐心细致和钻研的精神