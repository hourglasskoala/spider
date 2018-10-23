import os
from urllib import urlretrieve

if __name__ == '__main__':
    os.makedirs("./images/")
    image_url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
    urlretrieve(image_url, './images/image1.png')
