## 多智能体系统第一次编程作业报告

`201300066 麻超 人工智能学院`

### 实验说明

本次实验要求复现论文`Kinny, D., and M. George. "[Commitment and Effectiveness of Situated Agents](https://www.ijcai.org/Proceedings/91-1/Papers/014.pdf)." IJCAI-91. 1991.`中的实验，在游戏环境中设计实用推理来尽可能得到更多的分数。这篇论文主要探讨了一种名为“承诺”的人工智能机制，该机制使得在多智能体系统中的代理能够通过采取不同的行动来表达和实现它们的承诺。具体而言，这篇论文讨论了两种类型的承诺：义务性承诺和意向性承诺。义务性承诺是一种代理通过言语或行动而对另一个代理做出的承诺，它是明确的、强制性的和必须遵守的。而意向性承诺则是一种代理对未来行动的表达，它可能会受到外部环境的影响而改变，因此并不是强制性的。

为了使代理能够实现承诺，论文提出了一种基于逻辑的机制，该机制将承诺建模为约束条件，并将它们合并为一个代理的行动选择问题。然后，论文提出了一种基于置信度的机制，该机制允许代理根据不同的信息来源和信任水平来确定其他代理的承诺可信程度，并在此基础上做出决策。

在该游戏中，实用推理Agent主要包括两个步骤：

* 慎思过程：Agent通过感知外界信息以更新信念状态，以此确定自己的下一步行动
* 目标手段推理：Agent根据意图给出合理规划

在本实验中，主要探讨得分率和Agent的规划时间、环境刷新频率、Agent规划逻辑等的关系。

### 实验结果

##### 实验一：

![figure1](D:\Code\AgentWork\201300066\figure1.png)

![figure2](D:\Code\AgentWork\201300066\figure2.png)

##### 实验二：

![figure3](D:\Code\AgentWork\201300066\figure3.png)

![figure4](D:\Code\AgentWork\201300066\figure4.png)

##### 实验三：

![figure5](D:\Code\AgentWork\201300066\figure5.png)

![figure6](D:\Code\AgentWork\201300066\figure6.png)

![figure7](D:\Code\AgentWork\201300066\figure7.png)

##### 实验四：

![figure8](D:\Code\AgentWork\201300066\figure8.png)

![figure9](D:\Code\AgentWork\201300066\figure9.png)

![figure10](D:\Code\AgentWork\201300066\figure10.png)

在实验中，我们复现了论文中承诺属性的影响，其承诺属性有三种，Bold的Agent（除非达到意图否则不会重新计划新的意图），Cautious的Agent每次行动后都重新考虑意图，Normal的Agent每4次行动后重新考虑意图。在大多数情况下，Bold的Agent能获得更高的分数，因为其减少了很多重新思考的过程，而Normal的Agent大多数情况下也是优于Cautious的Agent.