import numpy as np
import torch
from sklearn.metrics import confusion_matrix, f1_score, roc_auc_score, recall_score, average_precision_score
from tensordict import TensorDict
from tensordict.nn import TensorDictModule
from torch import nn
from torch.distributions import OneHotCategorical
from torchrl.data import DiscreteTensorSpec
from torchrl.modules import ProbabilisticActor
import torch.nn.functional as F
from Features import GetProtT5_K_4, GetTPEMPPS_CCP
import pandas as pd


ZccFCCP_test_negative = "MyData/neg_Independent.fasta"
ZccFCCP_test_positive = "MyData/pos_Independent.fasta"
ZccFCCP_train_negative = "MyData/neg_Training.fasta"
ZccFCCP_train_positive = "MyData/pos_Training.fasta"

X_ZccFCCP_train, y_train, X_ZccFCCP_test, y_test, r = GetTPEMPPS_CCP(ZccFCCP_train_negative, ZccFCCP_train_positive,
                                                                     ZccFCCP_test_negative, ZccFCCP_test_positive)
X_ZccFCCP_train = X_ZccFCCP_train.astype(np.float32)
X_ZccFCCP_test = X_ZccFCCP_test.astype(np.float32)


y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

# 拼接 y 和 X：第一列是 y（标签），后面是 X（1118维特征）
train_data = np.hstack((y_train, X_ZccFCCP_train))
test_data = np.hstack((y_test, X_ZccFCCP_test))

train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

train_df.to_csv("MyData/Training_TPEMPPS_CCP_features.csv", index=False, header=False)
test_df.to_csv("MyData/Independent_TPEMPPS_CCP_features.csv", index=False, header=False)

print("训练和测试特征已成功保存到 CSV 文件。")

