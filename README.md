# AmnaDev Video Downloader

AmnaDev Video Downloader is a web application built with Streamlit that allows users to download YouTube videos in various formats (MP4, MP3, etc.) and in different languages. The app features multi-language support, including English, Urdu, Chinese, Spanish, French, German, Hindi, Arabic, Japanese, and Russian.

## Features

- **YouTube Video Downloader:** Download videos in MP4 format.
- **YouTube to MP3 Converter:** Convert YouTube videos to MP3 format.
- **Multi-language Support:** The app supports multiple languages and allows users to select their preferred language from the sidebar.
- **Responsive Design:** The app is designed to be user-friendly and works across different devices.
- **Asynchronous Downloads:** The app uses asynchronous tasks to download videos and convert them to different formats concurrently.

## Installation

To install and run this project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit app in your browser. You can select the desired language from the sidebar.
2. Choose the page you want to use:
    - **YouTube Video Downloader:** Enter the YouTube video URLs (comma-separated) and click "Download Videos."
    - **YouTube to MP3 Converter:** Enter the YouTube video URLs (comma-separated) and click "Convert and Download MP3s."
3. The app will process your request and display the download links or results.

## Requirements

- Python 3.7+
- Streamlit
- yt-dlp
- googletrans

## License

This project is licensed under the MIT License.
