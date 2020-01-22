import matplotlib.pyplot as plt

from keras.optimizers import Adam

from utils.Data import DataRetrieval
from utils.Model import NasNetMob


data_dir = '/home/mcv/datasets/MIT_split'
img_width = 224
img_height = 224
batch_size = 16
number_of_epoch = 20
validation_samples = 807

# Create model
model = NasNetMob()    
    
model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.001), metrics=['accuracy'])
for layer in model.layers:
    print layer.name, layer.trainable

# Prepare data
DR = DataRetrieval(data_dir)
train_generator = DR.get_train_data(batch_size=batch_size)
# validation_generator = DR.get_validation_data(batch_size=batch_size)
validation_generator = DR.get_test_data(batch_size=batch_size)
test_generator = DR.get_test_data(batch_size=batch_size)

history=model.fit_generator(
    train_generator,
    steps_per_epoch=(int(400//batch_size)+1),
    nb_epoch=number_of_epoch,
    validation_data=validation_generator,
    validation_steps= (int(validation_samples//batch_size)+1))


result = model.evaluate_generator(test_generator, val_samples=validation_samples)
print result

if True:
    # summarize history for accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.savefig('accuracy.jpg')
    plt.close()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.savefig('loss.jpg')
