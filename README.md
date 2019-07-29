# 1. 什么是推荐系统？为什么需要推荐系统
推荐系统一般根据用户的历史行为，用户的基本属性，用户和商品的交互行为（上下文特征）来猜测用户的兴趣，和搜索广告比较类似，但是相比较搜索，一般不提供query，非主动触发，相对于广告，优化目标可能略有区别。

搜索是为了尽快地满足用户，而推荐更多的是增加用户的停留时长。 推荐系统主要应用于：信息过载 以及 用户大部分时候没有明确目标的情况下。

推荐系统的基本任务是联系用户和物品，解决信息过载的问题。从物品的角度出发，推荐系统可以更好地发掘物品的长尾。

几乎所有推荐系统都是由前台的展示页面，后台的日志系统以及推荐算法系统3部分构成。

其实推荐系统在工业界算法只占20%。 80%在系统工程上面。比如需要毫秒级的反馈。

对于推荐系统来说存在两大场景即评分预测（rating prediction）与Top-N推荐（item recommendation，item ranking）。评分预测场景主要用于评价网站，比如用户给自己看过的电影评多少分（MovieLens），或者用户给自己看过的书籍评价多少分（Douban）。其中矩阵分解技术主要应用于该场景。Top-N推荐场景主要用于购物网站或者一般拿不到显式评分信息的网站，即通过用户的隐式反馈信息来给用户推荐一个可能感兴趣的列表以供其参考。其中该场景为排序任务，因此需要排序模型来对其建模。因此，我们接下来更关心评分预测任务。


# 2. 推荐系统如何评测
什么才是好的推荐系统？这是推荐系统评测需要解决的首要问题。 一个完整的推荐系统一般存在3个参与方：用户，内容提供者以及提供推荐系统的网站。在评测一个推荐系统的时候，需要同时考虑三方的利益，一个好的推荐系统是能够令三方共赢的系统。
为了全面评测推荐系统对三方利益的影响，我们需要从不同角度提出不同的指标。这些指标包括：
准确度，覆盖度，新颖度，惊喜度，信任度，透明度等。 这些指标中，有些可以离线计算，有些只有在线才可以计算，有些则只能通过用户问卷获得。

## 试验方法
## 评判指标
1. 召回率，准确率以及覆盖率
2. 
## 评测维度

# 3. 推荐系统通用模型
## 3.1 基于内容的推荐
## 3.2 协同过滤
* 基本假设：一个用户的行为，可以由跟他行为相似的用户进行推测。
CF要解决的问题用数学化的语言来表达就是：一个矩阵的填充问题。
### User-Based
给你推荐相似用户购买过的但是你还没有购买的商品。
1. 找到和目标用户兴趣相似的用户集合
2. 找到这个集合中的用户喜欢的，且目标用户没有交互的物品推荐给用户。
** 步骤1的关键 就是计算两个用户之间的相似性。

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

## 3.3 基于关联规则的推荐
## 3.4 基于知识的推荐
## 3.5 混合推荐

# 4. 数据来源
1. Netflix Prize
2. [Movielen](https://grouplens.org/datasets/movielens/) MovieLens数据集包含多个用户对多部电影的评级数据，也包括电影元数据信息和用户属性信息。
3. 

# 5. 推荐系统工程问题【2】
一般的推荐系统可以分为三部分，线上部分、线下部分以及近实时部分，当然还有其他支撑系统方面，包括：效果跟踪、效果监控，实验对比等。
## 5.0 埋点系统设计
TODO
1. **先考虑数据，再考虑模型！！**
## 5.1 线下部分
由于算法工程师需要挖取大量的关于用户以及其他方面的特征(几百维数据)，因此主要包括以下几个问题：
* 如何存储这些数据，存储介质是什么？如何做缓存？
* 如何保证线上快速的取数据？
* 如何对这些数据进行监控，保证在出现问题的时候(写入失败)能够及时报警？
## 5.2 近实时部分
近实时部分主要是如果一个用户实时产生了一些行为，如何将这个行为很快的体现在推荐结果中？以及如何能够将实时行为反应到模型上？如何反映到模型上目前很多有能力的公司正在尝试实验，通过这些可以反映应聘者是否真的关心业界动态。
## 5.3 线上部分
线上部分考察的很多。如果是系统工程师可以考察的方面包括
* 系统运维情况。包括整个系统的QPS，平均耗时，吞吐量等系统的整个架构。
* 一般推荐系统包括召回和排序。其中很重要一个考察点是如何解决系统I/O型任务之间的并发。
* 系统的缓存以及性能优化
* jvm调优等
* 如何进行线上a/b test实验的

推荐系统是一个不断优化的工程。所有复杂的性能优的系统不是一蹴而就的，是在平时不断的解决算法人员的痛点，提高工程师开发效率中不断完善的。

# 6. 具体问题探讨
## 6.1 冷启动问题
* 在推荐系统中，如果面对新的Item，能否在不重新训练Embedding的前提下得到这个新Item的Embedding向量？大家有什么实践经验分享吗？
用item的meta info 的embedding替代item；或者类似airbnb那样，用meta info找出来最相似的n个item求平均. side information!!

# 7. 推荐系统项目实例


# 8. 深度推荐系统

# 9. 推荐系统阅读列表
1. [Embedding在深度推荐系统中的3大应用方向](https://zhuanlan.zhihu.com/p/67218758)
2. [FFM及DeepFFM模型在推荐系统的探索](https://zhuanlan.zhihu.com/p/67795161) 


# 10. Papers
1. Training Deep AutoEnocders for Collaborative Filtering
2. The Wisdom of The Few 豆瓣阿稳在介绍豆瓣猜的时候极力推荐过这篇论文，豆瓣猜也充分应用了这篇论文中提出的算法；
2. Restricted Boltzmann Machines for Collaborative Filtering 目前Netflix使用的主要推荐算法之一；
3. Factorization Meets the Neighborhood: a Multifaceted Collaborative Filtering Model 这个无需强调重要性，LFM几乎应用到了每一个商业推荐系统中；
4. Collaborative Filtering with Temporal Dynamics 加入时间因素的SVD++模型，曾在Netflix Prize中大放溢彩的算法模型；
5. Context-Aware Recommender Systems 基于上下文的推荐模型，现在不论是工业界还是学术界都非常火的一个topic；
6. Toward the next generation of recommender systems 对下一代推荐系统的一个综述；
7. Item-Based Collaborative Filtering Recommendation Algorithms 基于物品的协同过滤，Amazon等电商网站的主力模型算法之一；
8. Information Seeking-Convergence of Search, Recommendations and Advertising 搜索、推荐和广告的大融合也是未来推荐系统的发展趋势之一；
9. Ad Click Prediction: a View from the Trenches 可以对推荐结果做CTR预测排序；
10. Performance of Recommender Algorithm on top-n Recommendation Task TopN预测的一个综合评测，TopN现在是推荐系统的主流话题，可以全部实现这篇文章中提到的算法大概对TopN有个体会；
11. http://dsec.pku.edu.cn/~jinlong/publication/wjlthesis.pdf 北大一博士对Netflix Prize算法的研究做的毕业论文，这篇论文本身对业界影响不大，但是Netflix Prize中运用到的算法极大地推动了推荐系统的发展；通过这些论文可以对推荐系统有个总体上的全面认识，并且能够了解一些推荐系统的发展趋势。剩下的就是多实践了。Good luck！

12. Are We Really Making Much Progress? A Worrying Analysis of Recent Neural Recommendation Approaches
> 摘要：对于那些致力于推荐系统算法方面的研究人员来说，深度学习技术已经成为他们的首先方法。但是，随着研究人员对深度学习的兴趣日益强烈，哪些方法能够代表当前最佳水平却变得难以辨别，如适用于 top-n 推荐任务的最佳方法。因此，研究者在本文中列举出了 top-n 推荐任务中提议算法的系统分析结果。具体来说，他们试验了 2018 年顶级科研会议上提出的 18 种算法，但遗憾的是，仅有 7 种算法可以通过研究人员的合理努力实现复现。然而，在这 7 种算法之中，却又有 6 种算法的效果通常弱于同类更简单的启发式方法，如基于最近邻或基于图的方法。剩下 1 种算法的效果虽然明显优于基线方法，但无法持续地优于调整好的非神经线性排序法（nonneural linear ranking method）。

# 10. 图算法
参考另一个[Repo](https://github.com/vinklibrary/Vink_GraphEmbedding)

# References
1. https://github.com/chocoluffy/deep-recommender-system
2. https://www.zhihu.com/question/57418889/answer/152951149
3. 
