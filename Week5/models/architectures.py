from keras import layers
from keras import models
from keras import optimizers

def RoJoPow(input_shape=(256,256,3)):
    # -- FIRST BLOCK -- #
    inputs = layers.Input(shape=input_shape)
    x = layers.Conv2D(filters=32, kernel_size=5, strides=2, padding='same')(inputs)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- SECOND BLOCK -- #
    x = layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,32))(y)
    y = layers.Dense(units=8,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=32,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- THIRD BLOCK -- #
    x = layers.Conv2D(filters=64, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,64))(y)
    y = layers.Dense(units=16,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=64,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- FOURTH BLOCK -- #
    x = layers.Conv2D(filters=64, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,64))(y)
    y = layers.Dense(units=16,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=64,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- FIFTH BLOCK -- #
    x = layers.Conv2D(filters=128, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,128))(y)
    y = layers.Dense(units=32,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=128,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- SIXTH BLOCK -- #
    x = layers.Conv2D(filters=128, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,128))(y)
    y = layers.Dense(units=32,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=128,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- DECISION BLOCK -- #
    x = layers.Conv2D(filters=8, kernel_size=1, strides=1, padding='valid')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,8))(y)
    y = layers.Dense(units=8,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=8,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Activation('softmax')(x)

    return models.Model(inputs, x)

def RoJoPow2(input_shape=(256,256,3)):
    # -- FIRST BLOCK -- #
    inputs = layers.Input(shape=input_shape)
    x = layers.Conv2D(filters=64, kernel_size=5, strides=2, padding='same')(inputs)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- SECOND BLOCK -- #
    x = layers.Conv2D(filters=64, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,64))(y)
    y = layers.Dense(units=16,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=64,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- THIRD BLOCK -- #
    x = layers.Conv2D(filters=128, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,128))(y)
    y = layers.Dense(units=32,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=128,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- FOURTH BLOCK -- #
    x = layers.Conv2D(filters=128, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,128))(y)
    y = layers.Dense(units=32,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=128,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- DECISION BLOCK -- #
    x = layers.Conv2D(filters=8, kernel_size=1, strides=1, padding='valid')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,8))(y)
    y = layers.Dense(units=8,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=8,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Activation('softmax')(x)

    return models.Model(inputs, x)

def RoJoPow3(input_shape=(256,256,3)):
    # -- FIRST BLOCK -- #
    inputs = layers.Input(shape=input_shape)
    x = layers.Conv2D(filters=32, kernel_size=5, strides=2, padding='same')(inputs)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- SECOND BLOCK -- #
    x = layers.Conv2D(filters=64, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,64))(y)
    y = layers.Dense(units=16,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=64,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- THIRD BLOCK -- #
    x = layers.Conv2D(filters=128, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,128))(y)
    y = layers.Dense(units=32,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=128,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- FOURTH BLOCK -- #
    x = layers.Conv2D(filters=128, kernel_size=3, strides=1, padding='same')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,128))(y)
    y = layers.Dense(units=32,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=128,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.MaxPooling2D(pool_size=2)(x)
    # -- DECISION BLOCK -- #
    x = layers.Conv2D(filters=8, kernel_size=1, strides=1, padding='valid')(x)
    x = layers.Activation('relu')(x)
    x = layers.BatchNormalization()(x)
    y = layers.GlobalAveragePooling2D()(x)
    y = layers.Reshape((1,1,8))(y)
    y = layers.Dense(units=8,kernel_initializer='he_normal')(y)
    y = layers.Activation('relu')(y)
    y = layers.Dense(units=8,kernel_initializer='he_normal')(y)
    y = layers.Activation('sigmoid')(y)
    x = layers.multiply([x, y])
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Activation('softmax')(x)

    return models.Model(inputs, x)

if __name__ == "__main__":
    model = RoJoPow()
    model.summary()
    model = RoJoPow2()
    model.summary()
    model = RoJoPow3()
    model.summary()