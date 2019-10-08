# CCL2019-Chinese-Humor-Computation 1st place solution 
### run
	任务一和任务二分别运行run_bert.sh和run_bert_cls3.sh 

	选取不同的预训练模型和任务数据即可
### 所使用的预训练模型一共八个： 
	pytorchmodeltask12_bert_1005 
	pytorchmodeltask12_roerta_1005 
	pytorchmodeltask12_wwm_1005 
	pytorchmodeltask12_wwm_ex_1005 
	pytorchmodeltaskalldata_bert_1005 
	pytorchmodeltaskalldata_roerta_1006 
	pytorchmodeltaskalldata_wwm_1005 
	pytorchmodeltaskalldata_wwm_ex_1005 
### 融合策略
	任务一包括在bert_keras上训练的模型一起融合 

	分别之于任务一二训练八个五折模型。 
### 模型： 
用bert等预训练模型，采用输出的[CLS]token的向量作为特征，向下接线性分类层。 

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
