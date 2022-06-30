#!/usr/bin/env bash

GPU_ID=3
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
    -solver /data/tpj/Sentivideo_v2_20190910/FT_S_Glove/M7/lf_resnet_coco_pre_factor_pre_train_factvideo1_2stream_M7/solver_cocolm_deepfus_img512_s2vt_glove.prototxt \
    -gpu $GPU_ID
