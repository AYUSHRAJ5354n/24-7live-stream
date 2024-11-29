import subprocess

# Replace with your YouTube stream key
stream_key = 'YOUR_YOUTUBE_STREAM_KEY'
# URL to your pre-recorded video on cloud storage
video_url = 'https://your-cloud-storage-url/video.mp4'  # Replace with your actual URL

# FFmpeg command to stream the video
command = [
    'ffmpeg',
    '-re',
    '-stream_loop', '-1',
    '-i', video_url,
    '-c:v', 'libx264',
    '-preset', 'veryfast',
    '-maxrate', '3000k',
    '-bufsize', '6000k',
    '-pix_fmt', 'yuv420p',
    '-g', '50',
    '-c:a', 'aac',
    '-b:a', '160k',
    '-ar', '44100',
    '-f', 'flv',
    f'rtmp://a.rtmp.youtube.com/live2/{stream_key}'
]

# Run the command
subprocess.run(command)
