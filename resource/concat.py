import imageio


def save_gif(images, name):
    # Save the images as a gif
    imageio.mimsave(f'{name}.gif', images, duration=10.0, loop=0)  # 'duration' controls the speed of the animation

# Paths to your images
image_path = [
    ['hanshu/source.jpeg', 'hanshu/results.png'],
    ['jiashi/source.jpeg', 'jiashi/result.png'],
    ['junhao/source.png', 'junhao/results.png'],
    ['vincent/source2.png', 'vincent/result2.png'],
    ['yujun/source1.jpg', 'yujun/results1.png']
]
name = ['hanshu', 'jiashi', 'junhao', 'vincent', 'yujun']


for i in range(len(image_path)):
    # Read images
    image1 = imageio.imread(image_path[i][0])
    image2 = imageio.imread(image_path[i][1])

    # Create a list of images
    images = [image1, image2]
    save_gif(images, name[i])
