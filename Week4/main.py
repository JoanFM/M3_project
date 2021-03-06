import os
import numpy as np
import matplotlib.pyplot as plt

from keras.optimizers import SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam

from utils.Data import DataRetrieval
from utils.Model import NasNetMob


def print_history(history, freezed, opt_name, lr):
    if summarize_history:
        # summarize history for accuracy
        plt.plot(history.history['acc'])
        plt.plot(history.history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'validation'], loc='upper left')
        if freezed:
            plt.savefig(work_dir + os.sep + str(opt_name) + '_' + str(lr) + '_freezed_accuracy.jpg')
        else:
            plt.savefig(work_dir + os.sep + str(opt_name) + '_' + str(lr) + '_unfreezed_accuracy.jpg')

        plt.close()
        # summarize history for loss
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'validation'], loc='upper left')
        if freezed:
            plt.savefig(work_dir + os.sep + str(opt_name) + '_' + str(lr) + '_loss.jpg')
        else:
            plt.savefig(work_dir + os.sep + str(opt_name) + '_' + str(lr) + '_unfreezed_loss.jpg')
        plt.close()


def train(model, train_optimizer, generator_train,
          generator_validation, samples_train, samples_validation,
          batch, nb_epochs, freezed, opt_name, lr):
    model.compile(loss='categorical_crossentropy', optimizer=train_optimizer, metrics=['accuracy'])

    history = model.fit_generator(
        generator_train,
        steps_per_epoch=(int(samples_train // batch) + 1),
        nb_epoch=nb_epochs,
        validation_data=generator_validation,
        validation_steps=(int(samples_validation // batch) + 1))

    print_history(history, freezed, opt_name, lr)


data_dir = '/home/grupo07/datasets/MIT_400'
work_dir = '/home/grupo07/work_unfreeze'
img_width = 224
img_height = 224
batch_size = 16
epochs = 100
train_samples = 400
validation_samples = 400
test_samples = 807
run_after_unfreeze = True
summarize_history = True

# Prepare data
DR = DataRetrieval(data_dir)
train_generator = DR.get_train_data(batch_size=batch_size)
validation_generator = DR.get_validation_data(batch_size=batch_size)
test_generator = DR.get_test_data(batch_size=batch_size)

# Run experiments
optimizers = {'SGD': SGD, 'RMSprop': RMSprop, 'Adagrad': Adagrad, 'Adadelta': Adadelta, 'Adam': Adam, 'Adamax': Adamax,
              'Nadam': Nadam}
learning_rates = [item + abs(np.random.normal(0, item)) for item in np.logspace(-5, -1, 6)]
for ind1, (optimizer_name, optimizer_) in enumerate(optimizers.items()):
    for ind2, learning_rate in enumerate(learning_rates):
        # Hyperparameters
        optimizer = optimizer_(lr=learning_rate)
        dropout = 0.5
        weight_decay = 5e-5

        # Create model
        nasnetmob = NasNetMob(dropout=dropout, weight_decay=weight_decay)
        nasnetmob.freeze()

        train(nasnetmob.model, optimizer, train_generator, validation_generator
              , train_samples, validation_samples, batch_size, epochs, True, , optimizer_name, learning_rate)

        result = nasnetmob.model.evaluate_generator(test_generator, val_samples=test_samples)
        print('\nTest loss:', result[0])
        print('Test accuracy:', result[1])
        with open(work_dir + os.sep + str(optimizer_name) + '_' + str(learning_rate) + '_info_freezed.txt', 'w') as f:
            to_write = 'Optimizer: ' + optimizer_name + \
                       '\nLearning rate: ' + str(learning_rate) + \
                       '\nDropout: ' + str(dropout) + \
                       '\nWeight decay: ' + str(weight_decay) + \
                       '\nTest loss: ' + str(result[0]) + \
                       '\nTest accuracy: ' + str(result[1]) + \
                       '\nFreezed: true ' + \
                       '\nEpochs: ' + str(epochs) + \
                       '\n'
            f.write(to_write)

        if run_after_unfreeze:
            nasnetmob.unfreeze()
            unfreeze_learning_rate = 1e-5
            optimizer = optimizer_(lr=unfreeze_learning_rate)
            train(nasnetmob.model, optimizer, train_generator, validation_generator,
                  train_samples, validation_samples, batch_size, epochs, False, optimizer_name, learning_rate)

            result = nasnetmob.model.evaluate_generator(test_generator, val_samples=test_samples)
            print('\nTest loss:', result[0])
            print('Test accuracy:', result[1])
            with open(work_dir + os.sep + str(optimizer_name) + '_' + str(learning_rate) + '_info_unfreezed.txt', 'w') as f:
                to_write = 'Optimizer: ' + optimizer_name + \
                        '\nLearning rate: ' + str(unfreeze_learning_rate) + \
                        '\nDropout: ' + str(dropout) + \
                        '\nWeight decay: ' + str(weight_decay) + \
                        '\nTest loss: ' + str(result[0]) + \
                        '\nTest accuracy: ' + str(result[1]) + \
                        '\nFreezed: false ' + \
                        '\nEpochs: ' + str(epochs) + \
                        '\n'
                f.write(to_write)
