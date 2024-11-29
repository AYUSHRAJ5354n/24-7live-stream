import subprocess

# Replace with your YouTube stream key
stream_key = 'YOUR_YOUTUBE_STREAM_KEY'
# URL to your pre-recorded video on Google Drive
video_url = 'https://drive.google.com/file/d/12xAAqdTmRDiUNWC_0R_pxXUa6GbPMVN8/view?usp=drivesdk'  # Replace with your actual file ID

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
