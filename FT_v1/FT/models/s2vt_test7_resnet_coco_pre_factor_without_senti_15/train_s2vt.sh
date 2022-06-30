#!/usr/bin/env bash

GPU_ID=5
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
    -solver /data/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt_senti/s2vt_test7_resnet_coco_pre_factor_without_senti_15/s2vt_solver.prototxt \
    -gpu $GPU_ID
