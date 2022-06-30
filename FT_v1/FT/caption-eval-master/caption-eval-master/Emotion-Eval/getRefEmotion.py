
from getEmationVocab import EmotionVocab, EmotionWord, get_Emotion


def getRef(emtion_path, ref_path):
    Emotion_list, Words_list = get_Emotion(emtion_path)
    f = open(ref_path)
    Ref = []
    vid_id_now = ''
    dict = {}
    for line in f.readlines():
        str = line.split()
        if str[0] != vid_id_now:
            if vid_id_now != '':
                Ref.append(dict)
            dict = {}
            dict['vid_id'] = str[0]
            dict['emotion'] = []

        for i in range(1, len(str)):
            for w in Words_list:
                if str[i] == w.context:
                    if Emotion_list[w.label_id].label not in dict['emotion']:
                        dict['emotion'].append(Emotion_list[w.label_id].label)
        vid_id_now = str[0]
    Ref.append(dict)
    return Ref
