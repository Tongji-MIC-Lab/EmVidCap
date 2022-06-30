The project mainly includes two parts: FT_v1 and FT_combine. The first is for EmVidCap-S evaluation and the second is for EmVidCap evaluation.
In detail, there are four folders included:

1. code_preprocess: it is a folder for visual feature extraction (the detail description is shown in README.txt in the subfolder);

2. dataset (will be released later): there subfolders are included:
   1) dataset_v1: it includes the original Youtube2Text clip-sentence pairs, the rewritten emotional sentences for EmVidCap-S and the used vocabulary
   2) dataset_v2: it includes the clip-sentence pairs for EmVidCap-L, where longer and complex sentences with emotions are annotated
   3) dataset_combine: it includes the used vocabulary and clip-sentence pairs in the EmVidCap dataset, where EmVidCap-S and EmVidCap-L are combined

3. FT_v1: it is the FT model evaluated on the EmVidCap-S dataset. The folder includes three sub folders: 
   1) caption-eval-master: evaluation metrics including BLEU, METEOR, CIDEr, and the emotion evaluation code
   2) generate_hdf5_resnet_coco_pre: to generate hdf5 file for model traning
   3) models: refers to the "README.txt" in the subfolder for each model training and testing (including M1-M7 and FT)

4. FT_combine: it is the FT model evaluated on the EmVidCap dataset. A few required subfolders are ignored since they can be found in FT_v1
   1) FT: refers to the "README.txt" in the subfolder for each model training and testing (including M2, M4, M7 and FT) 
   note: if the data preprocessing and evaluation are conducted, you can refer to the code in the folders of code_preprocess and FT_v1 

5. Comparable_models: a few comparable models including Deep-Fusion and LSTM-YT implemented on the EmVidCap-S and EmVidCap datasets. The details can be seen in README.txt.

