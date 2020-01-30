from keras import models
from keras import layers
from keras import optimizers


def final(input_shape=(256,256,3), optimizer=optimizers.Adam()):
    inputs = layers.Input(shape=input_shape)

    x = layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same')(inputs)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)

    x = layers.MaxPooling2D(pool_size=2)(x)

    x = layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)

    x = layers.MaxPooling2D(pool_size=2)(x)

    x = layers.Conv2D(filters=64, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(filters=64, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)

    x = layers.MaxPooling2D(pool_size=2)(x)

    x = layers.Conv2D(filters=128, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(filters=128, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)

    x = layers.Dropout(0.5)(x)

    x = layers.Conv2D(filters=8, kernel_size=1, strides=1, padding='valid')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)

    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Activation('softmax')(x)

    model = models.Model(inputs, x)

    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    return model
