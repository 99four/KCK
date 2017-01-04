from matplotlib import pyplot as plt
from skimage import data, feature, filters, morphology

plt.figure(figsize=(9, 9))
for i, file_name in enumerate(['samolot01.jpg', 'samolot03.jpg', 'samolot17.jpg', 'samolot07.jpg', 'samolot14.jpg',
                               'samolot16.jpg']):
    image = data.imread(file_name, True)
    image = feature.canny(image, sigma=3)
    image = morphology.dilation(image, morphology.disk(2))
    plt.subplot(3, 2, i + 1)
    plt.axis('off')
    plt.imshow(image, cmap="gray")

plt.savefig('images.pdf')
