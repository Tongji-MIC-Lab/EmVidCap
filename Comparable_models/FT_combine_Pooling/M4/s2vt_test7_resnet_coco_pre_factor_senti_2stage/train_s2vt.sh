#!/usr/bin/env bash

GPU_ID=7   #PU_ID=9
#/home/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt/Youtube/naacl15_pool_vgg_fc7_mean_fac2.caffemodel
#/home/tpj/tpj/caffe-recurrent/caffe_recurrent-recurrent/examples/coco_caption/lrcn_googlenet_20160418/models/lrcn_google_iter_110000.caffemodel

#DATA_DIR=./examples/coco_caption/h5_data/
#if [ ! -d $DATA_DIR ]; then
#    echo "Data directory not found: $DATA_DIR"
#    echo "First, download the COCO dataset (follow instructions in data/coco)"
#    echo "Then, run ./examples/coco_caption/coco_to_hdf5_data.py to create the Caffe input data"
#    exit 1
#fi

#/home/tpj/tpj/S2VT/caffe-recurrent/build/tools/caffe train \
/data/tpj/tpj/caffe-master-20160829/caffe-master/build/tools/caffe train \
    -solver /data/tpj/Sentivideo_v2_20190910/FT_combine_Pooling/M4/s2vt_test7_resnet_coco_pre_factor_senti_2stage/s2vt_solver.prototxt \
    -weights /data/tpj/Sentivideo_v2_20190910/FT_combine_Pooling/M4/s2vt_test7_resnet_coco_pre_factor_senti_2stage/s2vt_youtube_resnet_iter_140000.caffemodel \
    -gpu $GPU_ID
