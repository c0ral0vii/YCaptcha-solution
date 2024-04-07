import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

all_items = [
    'lamp',
    'energy',
    'look',
    'warning',
    'time',
    'hand',
    'pile',
    'clip',
    'pen',
    'bucket',
    't-shirt',
    'file',
    'glass',
    'book',
    'microphone',
    'camera',
    'heart',
    'smile',
    'umbrella',
    'home',
    'lights',
    'people',
    'fire',
    'cart',
    'keyboard',
    'sound',
    'wrench',
    'compass',
    'fabric',
    'sky',
    'flag',
    'market-cart',
    'mail',
    'desktop',
    'start',
    'lock',
    'water',
    'scissors',
    'up',
    'key',
    'ticket',
]

# Загрузка данных
train_data_dir = '/train'
test_data_dir = '/test'
batch_size = 32

train_datagen = ImageDataGenerator(rescale=1. / 255)
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(100, 100),
    batch_size=batch_size,
    class_mode='binary'
)

test_datagen = ImageDataGenerator(rescale=1. / 255)
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(100, 100),
    batch_size=batch_size,
    class_mode='binary'
)

# Создание модели
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Компиляция модели
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Обучение модели
epochs = 10
history = model.fit(train_generator, epochs=epochs, validation_data=test_generator)

# Оценка производительности модели
test_loss, test_acc = model.evaluate(test_generator)
print(f"Точность на тестовых данных: {test_acc:.2f}")