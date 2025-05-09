import imageio.v3 as iio

filenames = ["team-pic1.png", "team-pic2.png"]
images = []
# Read the images and append them to the list
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("team.gif", images, duration = 500, loop = 0)
# The above code creates a GIF from two images: team-pic1.png and team-pic2.png.
# The GIF is saved as team.gif with a duration of 500 milliseconds per frame and loops indefinitely.
                  