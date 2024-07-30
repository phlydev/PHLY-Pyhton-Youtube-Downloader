import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp as youtube_dl
import threading
import os

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("600x500")
        self.root.configure(bg="#2c2f33")

        self.download_log = []

        self.create_widgets()

    def create_widgets(self):
        # URL Label and Entry
        self.url_label = tk.Label(self.root, text="YouTube URL:", bg="#2c2f33", fg="#ffffff")
        self.url_label.pack(pady=10)
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)

        # Download Button
        self.download_button = tk.Button(self.root, text="Download", command=self.start_download, bg="#7289da", fg="#ffffff")
        self.download_button.pack(pady=20)

        # Progress Bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # File Size Label
        self.size_label = tk.Label(self.root, text="", bg="#2c2f33", fg="#ffffff")
        self.size_label.pack(pady=10)

        # Download Log Label
        self.log_label = tk.Label(self.root, text="Download Log:", bg="#2c2f33", fg="#ffffff")
        self.log_label.pack(pady=10)

        # Download Log Listbox
        self.log_listbox = tk.Listbox(self.root, width=80, height=10, bg="#23272a", fg="#ffffff")
        self.log_listbox.pack(pady=10)

    def start_download(self):
        url = self.url_entry.get()

        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.start()

    def download_video(self, url):
        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'ffmpeg_location': 'C:/ffmpglocation', #YOUR FFMPEG LOCATION
                'outtmpl': os.path.join("C:/videolocation", '%(title)s.%(ext)s'), # YOUR OUTPUT LOCATION
                'merge_output_format': 'mkv',
                'progress_hooks': [self.on_progress],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                video_title = info_dict.get('title', 'Unknown Title')
                video_filesize = info_dict.get('filesize', 0)
                video_quality = info_dict.get('format', 'Unknown Quality')

                if video_filesize:
                    filesize_mb = video_filesize / (1024 * 1024)
                    self.size_label.config(text=f"File Size: {filesize_mb:.2f} MB")

                ydl.download([url])

                # Add to download log
                self.download_log.append(f"Title: {video_title}, Quality: {video_quality}")
                self.update_log()

                # Display the quality information after download
                messagebox.showinfo("Success", f"Download completed!\nTitle: {video_title}\nQuality: {video_quality}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_log(self):
        self.log_listbox.delete(0, tk.END)
        for entry in self.download_log:
            self.log_listbox.insert(tk.END, entry)

    def on_progress(self, d):
        if d['status'] == 'downloading':
            total_size = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)
            if total_size:
                percentage = (downloaded / total_size) * 100
                self.progress['value'] = percentage
                self.root.update_idletasks()
        elif d['status'] == 'finished':
            self.progress['value'] = 100
            self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
