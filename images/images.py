from matplotlib import pyplot as plt
from skimage import data, feature, filters, morphology

plt.figure(figsize=(9, 9))
for i, file_name in enumerate(['samolot02.jpg', 'samolot03.jpg', 'samolot09.jpg', 'samolot12.jpg', 'samolot14.jpg',
                               'samolot16.jpg']):
    image = data.imread(file_name, True)
    image = feature.canny(image, sigma=3)
    image = morphology.dilation(image)
    image = filters.gaussian(image, sigma=1)
    plt.subplot(3, 2, i + 1)
    plt.axis('off')
    plt.imshow(image, cmap="gray")

plt.savefig('images.pdf')
