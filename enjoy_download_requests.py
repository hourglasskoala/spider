import requests

if __name__ == '__main__':
    image_url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
    r = requests.get(image_url, stream=True)

    with open('./images/image2.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
