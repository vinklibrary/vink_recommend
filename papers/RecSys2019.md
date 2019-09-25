# ShortPapers

## [A Generative Model for Review-Based Recommendations by Oren Sar Shalom](), 
**by Guy Uziel, Amir Kantor**

用户的评论数据富含很大的信息量，也因此在最近的推荐系统领域获得了很多关注。 本文工作中，我们提出了一个生成潜变量模型，来解释观察到的评级和文本评论。 这种潜变量模型允许将任何传统的协同过滤方法与任何深度学习架构结合起来进行文本处理。 通过四个基准数据集的实验结果证明了它与所有基线推荐系统相比的优越性。 此外，运行时分析表明，这种方法比相关基线快了一个数量级。

## [A Simple Multi-Armed Nearest-Neighbor Bandit for Interactive Recommendation]()
**by Javier Sanz-Cruzado, Pablo Castells, Esther López**

在推荐系统研究中越来越多地考虑推荐任务的循环性质。可以将循环的推荐系统问题视为真正的强化学习问题。多臂老虎机问题（multi-armed bandit approaches）越来越被视为应对推荐的双重开发/探索目标的手段。在本文中，我们开发了一种基于邻居协同过滤的简单多臂老虎机。该方法可被视为最近邻算法的变体，但通过Thompson采样的无参数应用，赋予用户邻域的受控随机探索能力。我们的方法基于正式开发进行了相当简单的设计，其目的是易于复制和进一步阐述。我们使用来自不同域的数据集报告实验，显示基于邻居的多臂老虎机算法确实在中长期内实现了推荐系统准确性的增强。

## [Adversarial Tensor Factorization for Context-aware Recommendation]()
**by Huiyuan Chen, Jing Li**

诸如时间，位置或标签之类的上下文因素会影响用户对特定item的偏好。因此，与仅基于用户-项目交互的传统推荐系统相比，上下文感知（content-aware）推荐系统对于提高推荐系统的效果和可解释性有着更好的能力。张量分解机器以一种统一的方式将用户，项目和上下文因素通用集成，从而实现了最先进的性能。然而，很少有工作集中在上下文感知推荐系统的稳健性上。 由于观察到的张量的稀疏性和张量因子分解的多线性特性，提高基于张量的模型的鲁棒性是具有挑战性的。 在本文中，我们提出了ATF，一种将张量因子分解和对抗性学习结合起来用于情境感知建议的模型。 这样做可以让我们获得张量因子分解的好处，同时增强推荐器模型的稳健性，从而提高其性能。 对两个真实世界数据集的实证研究表明，所提出的方法优于基于标准张量的方法。

## [Aligning Daily Activities with Personality: Towards A Recommender System for Improving Wellbeing]()
**by Mohammed Khwaja, Miquel Ferrer, Jesus Omana Iglesias, A. Aldo Faisal, Aleksandar Matic**

Recommender Systems have not been explored to a great extent for improving health and subjective wellbeing. Recent advances in mobile technologies and user modelling present the opportunity for delivering such systems, however the key issue is understanding the drivers of subjective wellbeing at an individual level. In this paper we propose a novel approach for deriving personalized activity recommendations to improve subjective wellbeing by maximizing the congruence between activities and personality traits. To evaluate the model, we leveraged a rich dataset collected in a smartphone study, which contains three weeks of daily activity probes, the Big-Five personality questionnaire and subjective wellbeing surveys. We show that the model correctly infers a range of activities that are ‘good’ or ‘bad’ (i.e. that are positively or negatively related to subjective wellbeing) for a given user and that the derived recommendations greatly match outcomes in the real-world. **推荐新场景**

## [Asymmetric Bayesian Personalized Ranking for One-Class Collaborative Filtering]
**by Shan Ouyang, Lin Li, Weike Pan, Zhong Ming**

In this paper, we propose a novel preference assumption for modeling users’ one-class feedback such as ‘thumb up’ in an important recommendation problem called one-class collaborative filtering (OCCF). Specifically, we address a fundamental limitation of a recent symmetric pairwise preference assumption and propose a novel and first asymmetric one, which is able to make the preferences of different users more comparable. With the proposed asymmetric pairwise preference assumption, we further design a novel recommendation algorithm called asymmetric Bayesian personalized ranking (ABPR). Extensive empirical studies on two large and public datasets show that our ABPR performs significantly better than several state-of-the-art recommendation methods with either pointwise preference assumption or pairwise preference assumption. **辅助推荐**

## [Attribute-based Evaluation for Recommender Systems: Incorporating User and Item Attributes in Evaluation Metrics]()
**by Pablo Sánchez, Alejandro Bellogín**

Research in Recommender Systems evaluation remains critical to study the efficiency of developed algorithms. Even if different aspects have been addressed and some of its shortcomings — such as biases, robustness, or cold start — have been analyzed and solutions or guidelines have been proposed, there are still some gaps that need to be further investigated. At the same time, the increasing amount of data collected by most recommender systems allows to gather valuable information from users and items which is being neglected by classical offline evaluation metrics. In this work, we integrate such information into the evaluation process in two complementary ways: on the one hand, we aggregate any evaluation metric according to the groups defined by the user attributes, and, on the other hand, we exploit item attributes to consider some recommended items as surrogates of those interacted by the user, with a proper penalization. Our results evidence that this novel evaluation methodology allows to capture different nuances of the algorithms performance, inherent biases in the data, and even fairness of the recommendations.

## [Combining Text Summarization and Aspect-based Sentiment Analysis of Users’ Reviews to Justify Recommendations]()
**by Cataldo Musto, Gaetano Rossiello, Marco de Gemmis, Pasquale Lops, Giovanni Semeraro**

In this paper we present a methodology to justify recommendations that relies on the information extracted from users’ reviews discussing the available items. The intuition behind the approach is to conceive the justification as a summary of the most relevant and distinguishing aspects ofthe item, automatically obtained by analyzing the available reviews. To this end, we designed a pipeline of natural language processing techniques based on aspect extraction, sentiment analysis and text summarization to gather the reviews, process the relevant excerpts,and generate a unique synthesis presenting the main characteristics of the item. Such a summary is finally presented to the target user as justification of the recommendation she received. In the experimental evaluation we carried out a user study in the movie domain (N=141) and the results showed that our approach is able to make the recommendation process more transparent, engaging and trustful for the users. Moreover, the proposed method also beat another review-based explanation technique, thus confirming the validity of our intuition.

## [Compositional Network Embedding for Link Prediction]()
**by Tianshu Lyu, Fei Sun, Peng Jiang, Wenwu Ou, Yan Zhang**

Network embedding has proved extremely useful in a variety of network analysis tasks such as node classification, link prediction, and network visualization. Almost all the existing network embedding methods learn to map the node IDs to their corresponding node embeddings. This design principle, however, hinders the existing methods from being applied in real cases. Node ID is not generalizable and, thus, the existing methods have to pay great effort in cold-start problem. The heterogeneous network usually requires extra work to encode node types, as node type is not able to be identified by node ID. Node ID carries rare information, resulting in the criticism that the existing methods are not robust to noise. To address this issue, we introduce Compositional Network Embedding, a general inductive network representation learning framework that generates node embeddings by combining node features based on the ‘principle of compositionally’. Instead of directly optimizing an embedding lookup based on arbitrary node IDs, we learn a composition function that infers node embeddings by combining the corresponding node attribute embeddings through a graph-based loss. For evaluation, we conduct the experiments on link prediction under four different settings. The results verified the effectiveness and generalization ability of compositional network embeddings, especially on unseen nodes.

## [Data Mining for Item Recommendation in MOBA Games]()
**by Vladimir Araujo, Felipe Rios, Denis Parra**

E-Sports has been positioned as an important activity within MOBA (Multiplayer Online Battle Arena) games in recent years. There is existing research on recommender systems in this topic, but most of it focuses on the character recommendation problem. However, the recommendation of items is also challenging because of its contextual nature, depending on the other characters. We have developed a framework that suggests items for a character based on the match context. The system aims to help players who have recently started the game as well as frequent players to take strategic advantage during a match and to improve their purchasing decision making. By analyzing a dataset of ranked matches through data mining techniques, we can capture purchase dynamic of experienced players to use it to generate recommendations. The results show that our proposed solution yields up to 80% of mAP, suggesting that the method leverages context information successfully. These results, together with open issues we mention in the paper, call for further research in the area.

