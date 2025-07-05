import numpy as np
from Feature.CKSAAP import GetCKSAAP_4
from Feature.CTDC import GetCTDC_4
from Feature.PAAC import GetPAAC_4
import csv
from Feature.TPEMPPS import GetTPEMPPS


def GetCCP_4(train_negative, train_positive, test_negative, test_positive):
    X_train1, y_train, X_test1, y_test, r = GetCKSAAP_4(train_negative, train_positive, test_negative, test_positive)
    X_train2, y_train, X_test2, y_test = GetCTDC_4(train_negative, train_positive, test_negative, test_positive)
    X_train3, y_train, X_test3, y_test = GetPAAC_4(train_negative, train_positive, test_negative, test_positive)

    X_train = np.concatenate((X_train1, X_train2, X_train3), axis=1)
    X_test = np.concatenate((X_test1, X_test2, X_test3), axis=1)

    # print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
    return X_train, y_train, X_test, y_test, r


def GetProtT5_K_4(train_negative, train_positive, test_negative, test_positive):
    with open(train_negative, mode='r') as file1:
        csv_reader1 = csv.reader(file1)
        train_negative_ProtT5 = np.array([row[1:] for row in csv_reader1])

    with open(train_positive, mode='r') as file2:
        csv_reader2 = csv.reader(file2)
        train_positive_ProtT5 = np.array([row[1:] for row in csv_reader2])

    with open(test_negative, mode='r') as file3:
        csv_reader3 = csv.reader(file3)
        test_negative_ProtT5 = np.array([row[1:] for row in csv_reader3])

    with open(test_positive, mode='r') as file4:
        csv_reader4 = csv.reader(file4)
        test_positive_ProtT5 = np.array([row[1:] for row in csv_reader4])

    X_train = np.concatenate((train_negative_ProtT5, train_positive_ProtT5), axis=0)
    X_test = np.concatenate((test_negative_ProtT5, test_positive_ProtT5), axis=0)

    N_train_Pos = train_positive_ProtT5.shape[0]
    N_train_Neg = train_negative_ProtT5.shape[0]
    N_test_Pos = test_positive_ProtT5.shape[0]
    N_test_Neg = test_negative_ProtT5.shape[0]
    num_P = N_train_Pos + N_test_Pos
    num_N = N_train_Neg + N_test_Neg

    ratio = num_P / num_N if num_P > num_N else num_N / num_P
    # 提取特征和标签数据的值
    y_train_Negative = np.zeros(train_negative_ProtT5.shape[0])
    y_train_Positive = np.ones(train_positive_ProtT5.shape[0])
    y_train = np.concatenate((y_train_Negative, y_train_Positive), axis=0)

    y_test_Negative = np.zeros(test_negative_ProtT5.shape[0])
    y_test_Positive = np.ones(test_positive_ProtT5.shape[0])
    y_test = np.concatenate((y_test_Negative, y_test_Positive), axis=0)
    print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
    return X_train, y_train, X_test, y_test, round(ratio, 2)


def GetTPEMPPS_CCP(train_negative, train_positive, test_negative, test_positive):
    X_train1, y_train, X_test1, y_test, ratio = GetCCP_4(train_negative, train_positive, test_negative,
                                                         test_positive)
    X_train2, y_train, X_test2, y_test, ratio = GetTPEMPPS(train_negative, train_positive, test_negative,
                                                           test_positive)

    X_train = np.concatenate((X_train2, X_train1), axis=1)
    X_test = np.concatenate((X_test2, X_test1), axis=1)

    print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
    return X_train, y_train, X_test, y_test, ratio
