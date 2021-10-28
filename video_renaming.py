import shutil
import os
import re
import cv2
import tqdm
import numpy as np
import json

source = '../data/WLASL2000/'
sink = '../data/videos/'
fps = 24

dataset = {
    662:'bus',
    1105: 'excuse',
    404: 'hospital',
    553: 'hungry',
    1164: 'me',
    122: 'movie',
    566: 'my',
    164: 'name',
    569: 'one',
    963: 'rain',
    995: 'start',
    781: 'stop',
    333: 'thank you',
    615: 'thirsty',
    1018: 'three',
    73: 'time',
    336: 'today',
    1024: 'two',
    30: 'what',
    346: 'when',
    256: 'where'
}

def video_rename():
    for file in os.listdir(source):
        video_id = re.findall("([0-9]+)", file)[0] # re.findall("_([a-z\s]+).mp4", file)[0]
        new_file_path = video_id + ".mp4"
        shutil.copyfile(source + file, source + new_file_path)
        os.remove(source + file)

def video_resize():
    for file in os.listdir(source):
        cap = cv2.VideoCapture(source + file)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(sink + file, fourcc, fps, (224, 224))

        while True:
            ret, frame = cap.read()
            if ret == True:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                b = cv2.resize(frame, (224, 224), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                out.write(b)
            else:
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def load_dictionary():
    a_dictionary = {}
    # a_file = open("../code/I3D/preprocess/wlasl_class_list.txt")
    # a_file = open("./preprocess/wlasl_class_list.txt")
    a_file = open("./preprocess/wlasl_class_asl_list.txt")
    for line in a_file:
        # print('String strip + split: {}'.format(tuple(line.strip('\n').split(' '))))
        line_ext = tuple(line.strip('\n').split(' ')) # line.strip('\n').split('   ')
        key = line_ext[0]
        value = line_ext[1]
        a_dictionary[key] = value

    return a_dictionary

# Function that checks if a subset of the dictionary satisfies our selected one
def class_per_dataset():
    # split_file = "../code/I3D/preprocess/nslt_100.json"
    # split_file = "../code/I3D/preprocess/nslt_300.json"
    split_file = "../code/I3D/preprocess/nslt_1000.json"
    # split_file = "../code/I3D/preprocess/nslt_2000.json"

    with open(split_file, 'r') as f:
        nslt_dataset = json.load(f)
    nslt_set = set([nslt_dataset[elem]['action'][0] for elem in nslt_dataset])

    print(nslt_set)
    main_dict = load_dictionary()
    for elem in set(dataset.keys()):
        print('Is \"{}\" in nslt_300? {}'.format(main_dict[str(elem)], elem in nslt_set))
    # nls_dict = set(list(main_dict.values())[:300])
    # print(nls_dict)

def get_video_info():
    video_path = '../data/WLASL2000/20201.mp4'

    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print('Video length: {}'.format(length))

    # for video in video_list:
    #
    info = {'name_video': {"subset": "test", "action": [0, 1, length]}}
    print('Video info: {}'.format(info))


def get_all_video_info():
    #source = '../data/inference/'
    source = './videos/'
    sink = 'preprocess/nslt_'
    #sink = '../code/I3D/preprocess/nslt_'
    video_list = os.listdir(source)
    video_info = {}
    # video_path = '../data/WLASL2000/20201.mp4'

    print(video_list)
    for video in video_list:
        if(video!=".DS_Store"):
            print(video)
            cap = cv2.VideoCapture(source + video)
            length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            info = { video[:-4]: {"subset": "test", "action": [0, 1, length]}}
            video_info.update(info)

    sink += str(len(video_info)) + '.json'
    print('Sink address: {}'.format(sink))
    with open(sink, 'w') as f:
        json.dump(video_info, f)
    print('Video info: {}'.format(video_info))
    print('Video info dimension: {}'.format(len(video_info)))
    return len(video_info)

# class_per_dataset()
# get_video_info()
# get_all_video_info()

"""

for file in os.listdir(source):
    video_filepath = source + file
    # get the video stream
    video_stream = cv2.VideoCapture(video_filepath)
    fname = video_filepath[video_filepath.rfind("/") + 1:-4]
    label = re.findall("_([a-z\s]+)", fname)[0]

    # used to format the names of frames during saving
    count = 0

    # for each frame of the video
    while True:

        # read the next frame from the file
        (grabbed, frame) = video_stream.read()

        # if the frame was not grabbed, then we have reached the end
        # of the stream
        if not grabbed:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224, 224)).astype("float32")

        cv2.imwrite("/content/extracted_video_frames/train/{}/{}_{}.png".format(label, fname, count), frame)
        count += 1

"""