import os
import yt_dlp

def download_youtube_audio_as_wav(youtube_url, output_dir="downloads"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '0',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"Downloaded and converted to WAV successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        youtube_link = input("Enter YouTube link (or type 'exit' to quit): ")
        
        if youtube_link.lower() == 'exit':
            print("Exiting the program.")
            break
            
        download_youtube_audio_as_wav(youtube_link)