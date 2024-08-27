from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

IMAGE_FOLDER = 'static/images'
VIDEO_FOLDER = 'static/videos'

def load_media_links(file_path):
    images = []
    videos = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            section = None
            for line in lines:
                line = line.strip()
                if line.startswith('#'):
                    section = line[2:]
                elif section == 'Image Links' and line:
                    images.append(line)
                elif section == 'Video Links' and line:
                    videos.append(line)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found.")
    return images, videos

IMAGES, VIDEOS = load_media_links('media_links.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/designs')  # تغيير المسار من /gallery إلى /designs
def designs():
    return render_template('designs.html', images=IMAGES, videos=VIDEOS)

@app.route('/static/images/<filename>')
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/static/videos/<filename>')
def get_video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
