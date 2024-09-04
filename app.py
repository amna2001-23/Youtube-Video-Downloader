import asyncio
import yt_dlp
from concurrent.futures import ThreadPoolExecutor
import time
import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Language selection
languages = ['en', 'ur', 'zh-cn', 'es', 'fr', 'de', 'hi', 'ar', 'ja', 'ru']
lang_names = ['English', 'Urdu', 'Chinese', 'Spanish', 'French', 'German', 'Hindi', 'Arabic', 'Japanese', 'Russian']
lang_dict = dict(zip(lang_names, languages))

selected_language = st.sidebar.selectbox("Select Language", lang_names)
st.session_state.language = lang_dict[selected_language]

# Translate text based on selected language
def translate_text(text, lang):
    if lang == 'en':
        return text
    try:
        translated = translator.translate(text, dest=lang)
        return translated.text
    except Exception as e:
        st.error(f"Translation error: {e}")
        return text

# Display banner on top of the page
st.markdown(
    """
    <style>
    .banner {
        background-color: #007BFF;
        color: white;
        padding: 15px;
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }
    </style>
    <div class="banner">
        Welcome to AmnaDev Video Downloader
    </div>
    """,
    unsafe_allow_html=True
)

# Title
st.title(translate_text("YouTube Video Downloader", st.session_state.language))

# Pages
page = st.sidebar.selectbox(translate_text("Select Page", st.session_state.language), [
    translate_text("YouTube Video Downloader", st.session_state.language),
    translate_text("YouTube to MP3", st.session_state.language),
    translate_text("YouTube to MP4", st.session_state.language),
    translate_text("About Us", st.session_state.language)
])

# Create a ThreadPoolExecutor for concurrent downloads
executor = ThreadPoolExecutor(max_workers=5)

# Asynchronous function to download video with retry mechanism
async def async_download_video(url, format='mp4', retries=3):
    ydl_opts = {
        'format': f'best[ext={format}]',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
        'socket_timeout': 60,  # Increase timeout
    }
    loop = asyncio.get_event_loop()
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    
    attempt = 0
    while attempt < retries:
        try:
            await loop.run_in_executor(executor, lambda: ydl.download([url]))
            return f"Download completed for {url}!"
        except Exception as e:
            st.error(f"Download error for {url}: {e}")
            attempt += 1
            if attempt >= retries:
                return f"Failed after {retries} attempts for {url}: {e}"
            st.warning(f"Retrying download for {url} ({attempt}/{retries})...")
            time.sleep(2)

# Asynchronous function to convert video to MP3
async def async_convert_to_mp3(url, retries=3):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'socket_timeout': 60,  # Increase timeout
    }
    loop = asyncio.get_event_loop()
    ydl = yt_dlp.YoutubeDL(ydl_opts)
    
    attempt = 0
    while attempt < retries:
        try:
            await loop.run_in_executor(executor, lambda: ydl.download([url]))
            return f"MP3 file downloaded successfully for {url}!"
        except Exception as e:
            st.error(f"Conversion error for {url}: {e}")
            attempt += 1
            if attempt >= retries:
                return f"Failed after {retries} attempts for {url}: {e}"
            st.warning(f"Retrying conversion for {url} ({attempt}/{retries})...")
            time.sleep(2)

# Function to handle Streamlit app logic
async def handle_downloads(url_list, format='mp4'):
    tasks = [async_download_video(url, format=format) for url in url_list]
    results = await asyncio.gather(*tasks)
    return results

if page == translate_text("YouTube Video Downloader", st.session_state.language):
    st.header(translate_text("YouTube Video Downloader", st.session_state.language))
    urls = st.text_area(translate_text("Enter YouTube Video URLs (comma-separated)", st.session_state.language))
    if urls:
        url_list = [url.strip() for url in urls.split(',')]
        if st.button(translate_text("Download Videos", st.session_state.language)):
            if len(url_list) > 5:
                st.warning(translate_text("You can download up to 5 videos at a time.", st.session_state.language))
                url_list = url_list[:5]

            # Run asynchronous tasks
            results = asyncio.run(handle_downloads(url_list))
            for result in results:
                st.success(result)

elif page == translate_text("YouTube to MP3", st.session_state.language):
    st.header(translate_text("YouTube to MP3 Converter", st.session_state.language))
    urls = st.text_area(translate_text("Enter YouTube Video URLs (comma-separated)", st.session_state.language))
    if urls:
        url_list = [url.strip() for url in urls.split(',')]
        if st.button(translate_text("Convert and Download MP3s", st.session_state.language)):
            if len(url_list) > 5:
                st.warning(translate_text("You can convert up to 5 videos to MP3 at a time.", st.session_state.language))
                url_list = url_list[:5]

            # Run asynchronous tasks
            results = asyncio.run(handle_downloads(url_list, format='mp3'))
            for result in results:
                st.success(result)

elif page == translate_text("YouTube to MP4", st.session_state.language):
    st.header(translate_text("YouTube to MP4 Converter", st.session_state.language))
    urls = st.text_area(translate_text("Enter YouTube Video URLs (comma-separated)", st.session_state.language))
    if urls:
        url_list = [url.strip() for url in urls.split(',')]
        if st.button(translate_text("Download MP4s", st.session_state.language)):
            if len(url_list) > 5:
                st.warning(translate_text("You can download up to 5 videos at a time.", st.session_state.language))
                url_list = url_list[:5]

            # Run asynchronous tasks
            results = asyncio.run(handle_downloads(url_list, format='mp4'))
            for result in results:
                st.success(result)

elif page == translate_text("About Us", st.session_state.language):
    st.header(translate_text("About AmnaDev Video Download", st.session_state.language))
    st.write(
        """
        <style>
        .about-page {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: Arial, sans-serif;
        }
        .section {
            margin-bottom: 20px;
        }
        .section h2 {
            color: #007BFF;
        }
        .section p {
            line-height: 1.6;
        }
        </style>
        <div class="about-page">
            <div class="section">
                <h2>About AmnaDev Video Download</h2>
                <p>
                    **AmnaDev Video Download** - Free Online at AmnaDev.com
                </p>
                <p>
                    Are you tired of struggling to download and convert your favorite YouTube videos to various formats? Do you want a fast, reliable, and user-friendly solution to enjoy your beloved content offline? Look no further! AmnaDev Video Download (Converter) is here to revolutionize your YouTube video downloading and converting experience.
                </p>
            </div>
            <div class="section">
                <h2>Multiple Format Support</h2>
                <p>
                    AmnaDev supports a wide range of video and audio formats. Convert YouTube videos to MP4, 3GP, WEBM, MP3, OGG, and M4A. This versatility ensures that you can enjoy your downloaded content on any device, be it a PC, tablet, iPhone, or Android smartphone.
                </p>
            </div>
            <div class="section">
                <h2>High-Quality Video Downloads</h2>
                <p>
                    Our platform allows you to download YouTube videos in various resolutions, including 720p, 1080p, 2k, and even 4k. This means you can enjoy your content in the highest quality possible, just as the creator intended.
                </p>
            </div>
            <div class="section">
                <h2>User-Friendly Interface</h2>
                <p>
                    AmnaDev is designed for ease of use. Our simple and intuitive interface allows you to download and convert YouTube videos in just a few clicks, without the need for any technical knowledge or expertise.
                </p>
            </div>
            <div class="section">
                <h2>No Software Installation Required</h2>
                <p>
                    Unlike many other YouTube video downloaders and converters, AmnaDev is an online tool that doesn't require you to install any software on your device. Simply visit our website, enter the video URL, and start downloading your favorite YouTube content.
                </p>
            </div>
            <div class="section">
                <h2>Fast Download Speeds</h2>
                <p>
                    We understand that time is precious, so we have optimized our platform to provide you with the fastest download speeds possible. Say goodbye to long waiting times and hello to instant access to your content!
                </p>
            </div>
            <div class="section">
                <h2>Why Choose AmnaDev Video Download?</h2>
                <ul>
                    <li>100% Free to Use: AmnaDev Video Download is completely free. No hidden fees or premium subscriptions—enjoy unlimited downloads and conversions without spending a dime.</li>
                    <li>High-Quality Downloads: We prioritize quality, ensuring your downloads are in the best possible resolution, whether you're saving a video or extracting audio.</li>
                    <li>Compatible with Major Platforms: Whether you're using a PC, tablet, iPhone, or Android device, our platform supports all major platforms, allowing you to enjoy your content anywhere, anytime.</li>
                    <li>Safe and Secure: Your privacy and security are our top priorities. AmnaDev uses the latest encryption technologies to keep your data safe while you use our platform.</li>
                    <li>Regular Updates: We're constantly improving AmnaDev to offer you new features, better performance, and an enhanced user experience.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
