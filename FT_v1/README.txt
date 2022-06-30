
1. FT: including the hdf5 file generation method (e.g., generation_hdf5_resnet_coco_pre, and you can refer to the "README.txt" in the sub folder);
           models (including the proposed model and competing models, the details are contained in README.txt in the sub folder);
           caption-eval-master (including the traditional BLEU, METEOR, ROUGE_L and CIDEr evaluation, also we explore the emotion evaluation, and you can read the "README.txt" for using);
           vocabulary_refine.txt: the vocabulary including the fact words and emotion words.
2. Using procedure:
   (1) split the dataset into factvideo1, factvideo2 and EmVidCap;
   (2) build the caffe in caffe-master-20160829-mat;
   (3) pre-train the model on MSCOCO, and extract visual feature for all video frames (code in pre_train_factvideo1, pre_train_factvideo2, EmVidCap);
   (4) generate hdf5 file for training
   (5) build M1, M2, M3, M4, M5, M6, M7 and FT, and optimize the models
   (6) generate sentences for test videos
   (7) evaluate the generated sentences with traditional metrics and emotion metrics
