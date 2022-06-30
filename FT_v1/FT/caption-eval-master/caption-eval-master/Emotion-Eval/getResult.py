import io
import getRefEmotion
from getEmationVocab import EmotionVocab, EmotionWord, get_Emotion
from getRefEmotion import getRef
import csv


def clean(str):
    from getEmationVocab import is_letter
    string = ''
    for char in str:
        if is_letter(char):
            string += char
    return string

def get_result(file_name, emotion_path, ref_path):
    Emotion_list, Words_list = get_Emotion(emotion_path)
    result = []
    f = open(file_name, 'r')
    have_score = 0
    right_score = 0
    wrong_score = 0
    counter = 0
    Ref = getRef(emotion_path, ref_path)

    for line in f.readlines():
        str = line.split()

        dict = {}
        dict['vid_id'] = str[1]
        dict['caption right emotion'] = []
        dict['caption wrong emotion'] = []
        Ref_emotion = []       
        for i in range(len(Ref)):
            if Ref[i]['vid_id'] == str[1]:
                Ref_emotion = Ref[i]['emotion']
                dict['Reference emotion'] = Ref_emotion

        have_emotion = False
        counter += 1

        for i in range(1, len(str)):
            for j in range(len(Words_list)):
                if clean(str[i]) == Words_list[j].context:
                    have_emotion = True

                    label = Emotion_list[Words_list[j].label_id].label
                    Words_list[j].times += 1
                    Emotion_list[Words_list[j].label_id].times += 1

                    if label in Ref_emotion:
                        if label not in dict['caption right emotion']:
                            dict['caption right emotion'].append(label)
                            right_score += 1
                    
                    else:
                        if label not in dict['caption wrong emotion']:
                            dict['caption wrong emotion'].append(label)
                            wrong_score += 1
                    break

        if have_emotion:
            have_score += 1
            dict['have emotion'] = True
        else:
            dict['have emotion'] = False
        result.append(dict)

    #file_name = file_name.split('/')[-1].split('\\')[1].split('.')[0] + '.csv'
    file_name = 'pre_train_2stage_160000.csv'
    
    csv_f = open(file_name, 'wb')
    csv_f = csv.writer(csv_f, dialect='excel')

    '''
    csv_f.writerow(['number of sentiment sentences',have_score])
    csv_f.writerow([])

    for l in Emotion_list:
        for i in l.words_id:
            csv_f.writerow([l.label, Words_list[i].context, Words_list[i].times])

    csv_f.writerow([])

    for l in Emotion_list:
        csv_f.writerow([l.label, l.times])
    '''


    csv_f.writerow(['vid_id', 'Have emotion?', 'Right emotion', 'Wrong emotion', 'Reference'])
    csv_f.writerow(['total', have_score, right_score, wrong_score])
    for dict in result:
        rowline = []
        rowline.append(dict['vid_id'])
        if dict['have emotion'] == True:
            rowline.append('Yes')
        else: rowline.append('No')

        rowline.append(' '.join(dict['caption right emotion']))
        rowline.append(' '.join(dict['caption wrong emotion']))
        rowline.append(' '.join(dict['Reference emotion']))
        csv_f.writerow(rowline)

    f.close()
