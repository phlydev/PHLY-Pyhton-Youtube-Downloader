# PHLY YouTube Downloader

PHLY YouTube Downloader is a user-friendly application designed to download YouTube videos with ease. The tool uses `yt_dlp` to handle the downloading process and provides a graphical user interface built with `tkinter`.

## Features
- Download videos from YouTube
- Graphical user interface with progress tracking
- Display download log and video information

## Requirements
To use PHLY YouTube Downloader, you need to have the following Python packages installed:

- `yt_dlp`
- `tkinter` (typically included with Python installations)

Additionally, `ffmpeg` must be installed and correctly configured.

### Installing Dependencies

1. **Install `yt_dlp`:**

    ```bash
    pip install yt-dlp
    ```

2. **`tkinter` is typically included with Python, but if it's not installed, you can follow [these instructions](https://tkdocs.com/tutorial/install.html) to install it.**

### Installing ffmpeg

Download `ffmpeg` from the [official website](https://ffmpeg.org/download.html) and place the executable in a directory that is included in your system's PATH. Ensure you update the `ffmpeg_location` in the code to point to your `ffmpeg` installation.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/phlydev/PHLY.git
    cd PHLY
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content to specify dependencies:

    ```
    yt-dlp
    ```

## Usage

1. Run the application:

    ```bash
    python phly_youtube_downloader.py
    ```

2. The GUI will open, allowing you to enter the URL of the YouTube video you want to download and track the download progress.

## Contributing

Feel free to submit issues and suggestions to improve PHLY YouTube Downloader.

## License

PHLY YouTube Downloader is provided under the following license:

