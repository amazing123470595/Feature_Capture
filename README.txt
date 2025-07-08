This repository uses the feature extraction method from https://github.com/Zhangqingchao-Ch/RLSuccSite.
The ProtT5 feature for a single amino acid has 1024 dimensions, and the TPEM-PPS_CCP feature for an amino acid sequence of length 41 has 1118 dimensions.
The resulting CSV files have labels in the first column, and features starting from the second column.
For ProtT5, the labels correspond to file names, while for TPEM-PPS_CCP, the features are binary values (0 or 1).

1.Environment：
pip install -r requirements.txt

2.Add your data
Place the amino acid sequence data in .txt format into the data folder.

3.Convert data types
Modify the filename in Divide_sample.py and run the program.
(Input: X.txt;  Output: pos_X.fasta, neg_X.fasta)

4.Extract ProtT5 features
Modify the filename in Feature/ProtT5.py and run the program.
(Input: pos_X.fasta, neg_X.fasta;  Output: pos_X_CD_ProtT5_features.csv, pos_X_CD_ProtT5_features.csv)

5.Extract the feature of a single amino acid
To extract the feature of a single amino acid, Modify the filename in Feature/ProtT5_T.py, replace the number 20 in line 24 of ProtT5_T in

features = features[20]

with the amino acid’s index (zero-based).
(Input: pos_X_CD_ProtT5_features.csv, pos_X_CD_ProtT5_features.csv;  Output: pos_X_CD_ProtT5_features_T.csv, pos_X_CD_ProtT5_features_T.csv)

6.Extract TPEM-PPS_CCP features
Modify the filename in ZccFccp.py and run the program.
(Input: pos_X1.fasta, neg_X1.fasta, pos_X2.fasta, neg_X2.fasta;  Output: X1_TPEMPPS_CCP_features.csv, X2_TPEMPPS_CCP_features.csv)

