
This file is for supplement of the work "Emotion Expression with Fact Transfer for Video Description". 

Four sub files including two extra frameworks for video captioning implemented on our proposed two datasets, are contained in this file. The details of each sub file are described as follows.

1. FT_combine_Glove: in this sub file, the Deep-Fusion framework (Venugopalan S, Hendricks LA, Mooney R, and Saenko K. Improving lstm-based video description with linguistic knowledge mined from text, in EMNLP2016) is employed to implement our proposed FT and other comparable models (including M2, M4, M5 and M7) on the EmVidCap dataset. Besides the files of FT, M2, M4, M5 and M7 for implementation details, there are 3 files included:
 1) generate_hdf5_resnet152_coco_pre_pre_train: to generate the hdf5 file for FactVideo1 subset
 2) generate_hdf5_resnet152_coco_pre_senti: to generate the hdf5 file for the EmVidCap dataset
 3) caption-eval-master: to evaluate the performance (including BLEU, METEOR, RGOUGE-L, CIDEr) of each model on the EmVidCap dataset. Additionally, the statistical results of emotion words are generated with the source code.

2. FT_combine_Pooling: the LSTM-YT framework (Venugopalan S, Xu H, Donahue J, Rohrbach M, Mooney R, and Saenko K. Translating videos to natural language using deep recurrent neural networks. in NAACL2015) is employed to implement our proposed FT and other comparable models (incuding M2, M4, M5 and M7) on the EmVidCap dataset. The content of each sub file is similar to FT_combine_Glove.

3. FT_S_Glove: the Deep-Fusion framework is employed to implement our proposed FT and other comparable models (incuding M2, M4, M5 and M7) on the EmVidCap-S dataset. And the function of each sub file is similar to FT_combine_Glove and FT_combine_Glove.

4. FT_S_Pooling: the LSTM-YT framework is employed to implement our proposed FT and other comparable models (incuding M2, M4, M5 and M7) on the EmVidCap-S dataset. The content of each sub file is similar to FT_S_Glove.
