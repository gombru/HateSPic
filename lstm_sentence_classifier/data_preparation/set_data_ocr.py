from preprocess_tweets import tweet_preprocessing
import os
import json

base_path = '../../../../datasets/HateSPic/HateSPic/img_text/txt/'
out_path = '../../../../datasets/HateSPic/lstm_data/img_txt/'
out_file = open(out_path + 'img_text.test', 'w')

for file in os.listdir(base_path):
    print file
    img_text = json.load(open(base_path + file))['img_text']
    try:
        text = tweet_preprocessing(img_text.encode('utf-8'))
        # Discard short tweets
        if len(text) < 5: continue
        if len(text.split(' ')) < 3: continue
        out_file.write(file.strip('.json') + ',' + text +'\n')

    except:
        print("Error with file: " + file)
        continue

print "DONE"