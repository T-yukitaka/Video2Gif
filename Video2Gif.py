import os
import cv2
import glob
from PIL import Image
from tqdm import tqdm

data_dir = './data'
save_dir = './results'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def Video2Gif(video_path, save_dir, gif_size_rate=1):
    print('{} is currently being converted to a GIF file.'.format(video_path))
    video_name = video_path.split('/')[-1].split('.')[0]
    video = cv2.VideoCapture(video_path)
    img_0 = None
    imgs = []
    frames_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    save_width = int(width * gif_size_rate)
    save_height = int(height * gif_size_rate)

    for i in tqdm(range(frames_count)):
        _, frame = video.read()
        try:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = img.resize((save_width, save_height))
            img = img.convert('RGBA')
            if i == 0:
                img_0 = img
            elif i % 5 == 0:
                imgs.append(img)
            else:
                pass
        except:
            pass
    img_0.save('{}/{}.gif'.format(save_dir, video_name), save_all=True, append_images=imgs, loop=0)
    if os.path.exists('{}/{}.gif'.format(save_dir, video_name)):
        print('Saved: {}/{}.gif'.format(save_dir, video_name))
    else:
        print('ERROR: {}/{}.gif has not been saved'.format(save_dir, video_name))


def main():
    video_paths = glob.glob(data_dir+'/*')
    if len(video_paths) == 0:
        print('No video files found in {}'.format(data_dir))
    else:
        print('The number of vieos: {}'.format(len(video_paths)))
    for _, path in enumerate(video_paths):
        Video2Gif(path, save_dir, gif_size_rate=0.3)

if __name__ == '__main__':
    main()