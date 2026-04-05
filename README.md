# Blogger Portable Archiver

A lightweight Python utility designed to backup your Blogger posts into completely standalone HTML files. Unlike standard web saves, this tool embeds all images directly into the HTML code using Base64 encoding. This ensures your archived posts remain fully intact and readable even if the original blog is taken down or the images are deleted from the host.

## ✨ Key Features

- **True Portability**: Images are converted into data strings and embedded directly inside the .html file. No "images" folder required.
- **User-Friendly GUI**: Built with tkinter for a simple, no-code-required interface.
- **Modern Styling**: Generates clean, responsive HTML layouts for every post.
- **Smart Sanitization**: Automatically handles special characters in post titles to ensure safe and organized file naming.

## 🚀 Getting Started

### 1. Prerequisites

  You will need Python 3.x installed. You also need to install the required external libraries:

```bash
pip install requests beautifulsoup4
 ```

> [!NOTE]
    If you are on Linux, you may also need to install the python3-tk package via your package manager if the GUI doesn't open.

### 2. Getting your Blogger API Credentials
To use this tool, you need a Google Cloud API Key and your Blog ID:
* API Key:

   * Go to the Google Cloud Console.
   * Create a new project.
   * Search for and Enable the Blogger API v3.
   * Navigate to Credentials -> Create Credentials -> API Key.

 * Blog ID:

    * Log into your Blogger dashboard.
    * Look at the URL in your browser. It will look like: https://www.blogger.com/blog/posts/1234567890 ...
    * The digits following /posts/ are your Blog ID.

## 🛠️ How to Use

  1. Run the script:

  
    python blogger_downloader.py


 * Enter Credentials: Paste your API Key and Blog ID into the respective text fields.
 * Initiate Download: Click the "Generate Portable HTML Files" button.
 * Select Location: A folder picker will appear. Choose where you want to save your archive.
 * Success: The script will loop through your posts, fetch images, encode them, and save individual .html files to your chosen directory.

## 📂 Project Structure

    blogger_downloader.py: The main Python script containing the GUI logic and the archiving engine.
    README.md: Project documentation.

## ⚠️ Important Notes
 * **API Quotas**: Google imposes daily limits on API requests. While unlikely to be hit by a single blog archive, be mindful if archiving dozens of high-frequency blogs.
 * **Private Blogs**: This tool is designed for public blogs. Private blogs may require OAuth2 authentication, which is not supported in this lightweight version.
 * **Security**: Never share your API Key or commit it to a public GitHub repository.
    

## 📜 License
This project is open-source and available under the MIT License.
