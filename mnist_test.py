from mnist import MNIST
from PIL import Image 
import numpy as np
import random
from cm1k import * 
from tqdm import tqdm
import os
import errno

mndata = MNIST('./mnist')
random.random()
cm1k = CM1K()

def process_image(img):
    img = np.array(img).reshape(28, 28)    
    img = Image.fromarray(img.astype('uint8')).convert('L')
    img = img.resize((16, 16)) # must resize imgs to 16x16 to fit in vector

    resized_img = np.asarray(img).flatten()
    return resized_img

def train_knn():
    print "Loading MNIST training data..."
    data = mndata.load_training()
    print "Finished loading data!"
    data = zip(*data)

    sample = 1024
    training_subset = random.sample(data, sample) 
    print "Training..."
    cm1k.write(REG_FORGET)
    cm1k.write(REG_NSR, 0x10) # put cm1k in sr mode
    for img, label in tqdm(training_subset, desc="Training CM1K", unit="samples"):
        resized_img = process_image(img)
        cm1k.train_vector(resized_img, label+1)
    print "Done training!"


def train(sample=1024):
    print "Loading MNIST training data..."
    data = mndata.load_training()
    print "Finished loading data!"
    data = zip(*data)

    training_subset = random.sample(data, sample) 
    print "Training..."
    cm1k.write(REG_NSR, 0x20)
    cm1k.write(REG_FORGET)
    for img, label in tqdm(training_subset, desc="Training CM1K", unit="samples"):
        resized_img = process_image(img)
        cm1k.train_vector(resized_img, label+1)
    print "Done training!"

def output_models(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
                    
    cm1k.write(REG_NSR, 0x10) # put cm1k into NSR mode
    cm1k.write(REG_RESETCHAIN)
    while True:
        data = cm1k.read_component()
        cat = cm1k.read(REG_CAT)
        img = np.array(data).reshape(16, 16)
        img = Image.fromarray(img.astype('uint8')).convert('L')
        img.save('%s/%d.bmp' % (path, (cat-1)))
        print cat
        if cat==0:
            break
    cm1k.write(REG_NSR, 0x00)

def test(sample=100):
    data = mndata.load_testing()
    data = zip(*data)
    data = random.sample(data, sample)
    correct = 0.0
    total = 0.0
    print "Testing!"
    cm1k.write(REG_NSR, 0x20) # put into KNN mode
    t = tqdm(data, desc="Testing CM1K", unit="samples")
    for img, label in t:
        img = process_image(img)
        cm1k.broadcast_vector(img)
        cm1k.read(REG_DIST)
        cat = cm1k.read(REG_CAT)
        total += 1
        if label == cat + 1:
            correct += 1
        t.set_postfix({"%": correct/total*100})
    cm1k.write(REG_NSR, 0x0) # reset from KNN mode
    print "Done testing!!"
    print float(correct)/total

def test_knn(k=3, sample=100):
    print "Loading test data..."
    data = mndata.load_testing()
    data = zip(*data)
    data = random.sample(data, sample)
    print "Done loading test data!"
    correct = 0.0
    total = 0.0
    cm1k.write(REG_NSR, 0x20) # put into KNN mode
    t = tqdm(data, desc="Testing CM1K w/ KNN (k=%d)" % k, unit="samples")
    for img, label in t:
        img = process_image(img)
        cm1k.broadcast_vector(img)
        categories = [0] * 10
        for _ in xrange(k):
            cm1k.read(REG_DIST)
            cat = cm1k.read(REG_CAT)
            categories[cat-1] += 1
        max_val = max(categories)
        identified = categories.index(max_val)

        total += 1
        if label == identified:
            correct += 1
        t.set_postfix({"%": correct/total*100})

    cm1k.write(REG_NSR, 0x0) # reset from KNN mode
    print "Done testing!!"
    print "Correctly identified: %.2f%%" %  (float(correct)/total * 100)

if __name__ == '__main__':
    train(1024)
    test()
