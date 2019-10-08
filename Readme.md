# CCL2019-Chinese-Humor-Computation 1st place solution 
### run
	任务一和任务二分别运行run_bert.sh和run_bert_cls3.sh 

	选取不同的预训练模型和任务数据即可

### 赛题介绍
	幽默是一种特殊的语言表达方式，在日常生活中扮演着化解尴尬、活跃气氛、促进交流的重要角色。而幽默计算是近年来自然语言处理领域的新兴热点之一，其主要研究如何基于计算机技术对幽默进行识别、分类与生成，具有重要的理论和应用价值。
	子任务一：生成幽默识别 **F1**
	子任务二：中文幽默等级划分 **MacroF**

### 赛题分析

### Pre-train
	所使用的预训练模型一共八个： 
	pytorchmodeltask12_bert_1005 
	pytorchmodeltask12_roerta_1005 
	pytorchmodeltask12_wwm_1005 
	pytorchmodeltask12_wwm_ex_1005 
	pytorchmodeltaskalldata_bert_1005 
	pytorchmodeltaskalldata_roerta_1006 
	pytorchmodeltaskalldata_wwm_1005 
	pytorchmodeltaskalldata_wwm_ex_1005 
### fine-tune
用bert等预训练模型，采用输出的[CLS]token的向量作为特征，向下接线性分类层。 
### 模型结构

### 融合策略
	任务一包括在bert_keras上训练的模型一起融合 

	分别之于任务一二训练八个五折模型。 
### Multi-task


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
