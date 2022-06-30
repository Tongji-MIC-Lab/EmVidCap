import os
from getResult import get_result

# path for folder where models are stored
#main_path = 'D:/Program/python_project/emotion_caption/sentivideo'
main_path = '/data/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt_senti/caption-eval-master/caption-eval-master/data/s2vt_resnet_coco_pre_factor_pre_train_2stage/'


# add models : os.path.join(main_path, model_path)
path_list = [os.path.join(main_path, 'val.s2vt_youtube_resnet_iter_160000_beam_size_1.txt')
             ]

# path for folder where sentiment words are stored
#emotion_path = 'D:/Program/python_project/emotion_caption/sentivideo/sentiment words'
emotion_path = '/data/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt_senti/caption-eval-master/caption-eval-master/sentiment-words-E/'


# path for references
ref_path = '/data/tpj/tpj/S2VT/caffe-recurrent/examples/s2vt_senti/caption-eval-master/caption-eval-master/data/references.txt'

for path in path_list:
    result = get_result(path, emotion_path, ref_path)
