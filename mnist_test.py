from mnist import MNIST
from PIL import Image 
import numpy as np
import random
import cm1k

mndata = MNIST('./mnist')
random.random()

def train(sample=10):
    print "Loading MNIST training data..."
    data = mndata.load_training()
    print "Finished loading data!"
    data = zip(*data)

    training_subset = random.sample(data, sample) 

    for img, label in training_subset:
        img = np.array(img).reshape(28, 28)    
        img = Image.fromarray(img.astype('uint8')).convert('L')
        img = img.resize((16, 16)) # must resize imgs to 16x16 to fit in vector

        resized_img = np.asarray(img).flatten()
        print resized_img, label, label + 1
        cm1k.train_vector(resized_img, label+1)


def test():
    data = mndata.load_testing()

    return data
    # put NSR into KNN mode

if __name__ == '__main__':
    train()
