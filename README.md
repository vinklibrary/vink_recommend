# 什么是推荐系统？为什么需要推荐系统
推荐系统一般根据用户的历史行为，用户的基本属性，用户和商品的交互行为（上下文特征）来猜测用户的兴趣，和搜索广告比较类似，但是相比较搜索，一般不提供query，非主动触发，相对于广告，优化目标可能略有区别。
搜索是为了尽快地满足用户，而推荐更多的是增加用户的停留时长。
信息过滤，解决选择困难症。
## 信息过载
## 用户大部分时候没有明确目标

其实推荐系统在工业界算法只占20%。 80%在系统工程上面。比如需要毫秒级的反馈。

对于推荐系统来说存在两大场景即评分预测（rating prediction）与Top-N推荐（item recommendation，item ranking）。评分预测场景主要用于评价网站，比如用户给自己看过的电影评多少分（MovieLens），或者用户给自己看过的书籍评价多少分（Douban）。其中矩阵分解技术主要应用于该场景。Top-N推荐场景主要用于购物网站或者一般拿不到显式评分信息的网站，即通过用户的隐式反馈信息来给用户推荐一个可能感兴趣的列表以供其参考。其中该场景为排序任务，因此需要排序模型来对其建模。因此，我们接下来更关心评分预测任务。

# 推荐系统如何评测
## 试验方法
## 评判指标
## 评测维度

# 推荐系统通用模型
## 用户模型
## 推荐对象模型


## 推荐算法模块
### 基于内容的推荐
### 协同过滤推荐
### 基于关联规则的推荐
### 基于知识的推荐
### 混合推荐

# 推荐算法详述
## 基于内容的推荐
## 协同过滤
* 基本假设：一个用户的行为，可以由跟他行为相似的用户进行推测。
CF要解决的问题用数学化的语言来表达就是：一个矩阵的填充问题。
### User-Based
给你推荐相似用户购买过的但是你还没有购买的商品。
### Item-Based
给你推荐你购买过的商品极其容易一起购买的其他商品
### Model-Based
用机器学习的思想来解决问题：矩阵分解等。
协同过滤算法主要有两个模型，最邻近点对模型和潜在语义模型。第一个模型就是定义权值计算相似度。

### 协同过滤算法
1. 用关联算法做协同过滤
2. 用聚类算法做协同过滤
3. 用分类算法做协同过滤
4. 用回归算法做协同过滤
5. 用矩阵分解做协同过滤

## 基于关联规则的推荐
## 基于知识的推荐
## 混合推荐

# 数据来源

# 冷启动问题

# 推荐系统实例

# 深度推荐系统介绍
1. Training Deep AutoEnocders for Collaborative Filtering

1. The Wisdom of The Few 豆瓣阿稳在介绍豆瓣猜的时候极力推荐过这篇论文，豆瓣猜也充分应用了这篇论文中提出的算法；2. Restricted Boltzmann Machines for Collaborative Filtering 目前Netflix使用的主要推荐算法之一；3. Factorization Meets the Neighborhood: a Multifaceted Collaborative Filtering Model 这个无需强调重要性，LFM几乎应用到了每一个商业推荐系统中；4. Collaborative Filtering with Temporal Dynamics 加入时间因素的SVD++模型，曾在Netflix Prize中大放溢彩的算法模型；5. Context-Aware Recommender Systems 基于上下文的推荐模型，现在不论是工业界还是学术界都非常火的一个topic；6. Toward the next generation of recommender systems 对下一代推荐系统的一个综述；7. Item-Based Collaborative Filtering Recommendation Algorithms 基于物品的协同过滤，Amazon等电商网站的主力模型算法之一；8. Information Seeking-Convergence of Search, Recommendations and Advertising 搜索、推荐和广告的大融合也是未来推荐系统的发展趋势之一；9. Ad Click Prediction: a View from the Trenches 可以对推荐结果做CTR预测排序；10. Performance of Recommender Algorithm on top-n Recommendation Task TopN预测的一个综合评测，TopN现在是推荐系统的主流话题，可以全部实现这篇文章中提到的算法大概对TopN有个体会；

11. http://dsec.pku.edu.cn/~jinlong/publication/wjlthesis.pdf 北大一博士对Netflix Prize算法的研究做的毕业论文，这篇论文本身对业界影响不大，但是Netflix Prize中运用到的算法极大地推动了推荐系统的发展；通过这些论文可以对推荐系统有个总体上的全面认识，并且能够了解一些推荐系统的发展趋势。剩下的就是多实践了。Good luck！


# 图算法
If embedding users and items into a heterogeneous graph, user-to-item behaviors could be treated as directed edges and item-to-item similarities could be encoded into the graph. Then recommendation task could be transformed as the graph link prediction problem. Such transition may bring a new view of recommendation system and further trigger novel algorithms to solve the bottleneck of behavior prediction problem.


# References
1. https://github.com/chocoluffy/deep-recommender-system
2.
