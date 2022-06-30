
import os

class EmotionVocab():
    def __init__(self):
        self.label = ''   #label_name
        self.words_id = []   #list of words id
        self.times = 0


class EmotionWord():
    def __init__(self):
        self.label_id = 0    #label id
        self.context = '' #what is the word
        self.times = 0

def is_number(str):
    if ord(str) >= ord('0') and ord(str) <= ord('9'):
        return True
    return False

def is_letter(str):
    if ord(str) >= ord('a') and ord(str) <= ord('z'):
        return True
    if ord(str) >= ord('A') and ord(str) <= ord('Z'):
        return True
    return False

def get_Emotion(emotion_path):
    Emotion_list = []
    Words_list = []
    main_path = emotion_path
    dir = os.listdir(main_path)
    dir.sort()
    for filename in dir:
        emotion = EmotionVocab()
        emotion.label = filename.split('.')[0]
        open_path = os.path.join(main_path, filename)
        f = open(open_path, 'r')
        for line in f.readlines():
            str = line.split()
            if len(str) == 0: continue
            if is_number(str[0][0]):
                word = ''
                for char in str[1]:
                    if is_letter(char):
                        word += char
                    else:
                        break
                emotion_word = EmotionWord()
                emotion_word.label_id = len(Emotion_list)
                emotion_word.context = word
                emotion.words_id.append(len(Words_list))
                Words_list.append(emotion_word)
        Emotion_list.append(emotion)
    return Emotion_list, Words_list

