# CCL2019-Chinese-Humor-Computation 1st place solution 
### 运行
	1.在pretrain下生成预训练模型
	
	2.添加任务数据到对应路径，并在路径下运行preproces.py，生成训练数据
	
	3.任务一和任务二分别运行run_bert.sh和run_bert_cls3.sh，生成任务模型以及模型预测 

	4.选取不同的预训练模型和预测结果，运行F1.py和F2.py进行模型融合，生成最终预测结果

### 赛题介绍
	幽默是一种特殊的语言表达方式，在日常生活中扮演着化解尴尬、活跃气氛、促进交流的重要角色。
	而幽默计算是近年来自然语言处理领域的新兴热点之一，其主要研究如何基于计算机技术对幽默进行识别、分类与生成，具有重要的理论和应用价值。
	子任务一：生成幽默识别 **F1**
	该子任务是二分类任务，标签有：生成幽默（label=0）、非生成幽默（label=1）。任务采用F1值进行评价
	子任务二：中文幽默等级划分 **MacroF**
	该子任务是三分类任务，标签有：弱幽默（label=1）、普通幽默（label=3）、强幽默（label=5）。任务采用宏平均（Macro-Average）进行评价。宏平均首先对每一个类统计评价指标值
	队伍最终的得分由两个子任务的得分综合决定，即：
	Score=0.6*子任务一得分+0.4*子任务二得分
### 赛题分析
	两个子任务均是分类任务，按照传统的思想，按照以下步骤进行
	1.预训练
	2.传统模型/BERT等模型训练与调试
	3.local CV 验证
	4.模型向下接网络层
	5.模型融合
	6.其他trick
	*对于本题，task1区分度较task2大，任务得分权重较大0.6，task2*0.4，针对任务，应该优先优化task1
	*本团队在任务进行当中，发现两个任务存在上下游的关系，尝试使用多任务联合学习，并使用任务二的数据对任务一进行数据扩充，取得了明显的效果。
###  further pre-train BERT or other models on within-task training data and in-domain data
	所使用的预训练模型一共四个，分别是bert/bert_wwm/bert_wwm_ex/roberta，在不同数据上进一步与训练得到下面八个模型： 
	pytorchmodeltask12_bert_1005 
	pytorchmodeltask12_roerta_1005 
	pytorchmodeltask12_wwm_1005 
	pytorchmodeltask12_wwm_ex_1005 
	pytorchmodeltaskalldata_bert_1005 
	pytorchmodeltaskalldata_roerta_1006 
	pytorchmodeltaskalldata_wwm_1005 
	pytorchmodeltaskalldata_wwm_ex_1005 
### fine-tune
	用bert等事先训练好的预训练模型，采用输出的[CLS]token的向量作为特征，向下接线性分类层。 
### 模型结构
![](Readme_data/model.jpg)
### 融合策略
	对于cv内的每个模型，分别在其预留验证集上对结果进行微调，找到最佳的分类阈值，并用在测试集的预测结果。综合所有模型的微调结果，投票生成最终预测。 
### Multi-task learning


### 提升细节：
	task1：
		加入任务二数据 
		调整各类损失权重 
		融合模型时学习最佳分类阈值 
	task2：
		调整各类损失权重 
		融合模型时学习最佳分类阈值 
		不同batch_size训练模型融合 
		融合模型时学习最佳分类阈值 
### 结果对比
