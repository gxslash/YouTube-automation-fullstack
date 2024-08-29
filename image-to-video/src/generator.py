import os
import subprocess

def create_image_list(folder):
    images = [f for f in os.listdir(folder) if f.endswith('.jpg')]
    with open('images.txt', 'w') as f:
        for image in images:
            f.write(f"file '{image}'\n")

def create_video():
    # Create a list of image files
    create_image_list('./old/images')
    
    # Run FFmpeg command to create the video
    ffmpeg_command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'images.txt', '-vsync', 'vfr',
        '-pix_fmt', 'yuv420p', '-r', '1/5', '-t', '150', 'output.mp4'
    ]
    subprocess.run(ffmpeg_command)

if __name__ == '__main__':
    create_video()
