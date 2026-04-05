import os
import requests
import base64
import tkinter as tk
from tkinter import messagebox, filedialog
from bs4 import BeautifulSoup

def download_posts():
    api_key = api_entry.get().strip()
    blog_id = blog_entry.get().strip()
    
    if not api_key or not blog_id:
        messagebox.showerror("Error", "Please enter both API Key and Blog ID")
        return

    save_dir = filedialog.askdirectory(title="Select Folder to Save Posts")
    if not save_dir:
        return

    url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts"
    params = {'key': api_key}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if 'items' not in data:
            messagebox.showinfo("Result", "No posts found.")
            return

        for post in data['items']:
            title = post['title'].replace("/", "-").replace("\\", "-")[:50]
            if not title: title = f"Untitled_Post_{post['id']}"
            
            soup = BeautifulSoup(post['content'], 'html.parser')
            
            # Find all images and embed them
            img_tags = soup.find_all('img')
            for img in img_tags:
                original_url = img.get('src')
                if not original_url:
                    continue
                
                try:
                    # Fetch image data
                    img_resp = requests.get(original_url, timeout=10)
                    if img_resp.status_code == 200:
                        content_type = img_resp.headers.get('Content-Type', 'image/jpeg')
                        # Convert to Base64
                        b64_data = base64.b64encode(img_resp.content).decode('utf-8')
                        # Replace the URL with the Data URI
                        img['src'] = f"data:{content_type};base64,{b64_data}"
                except Exception as e:
                    print(f"Could not embed image {original_url}: {e}")

            # Final HTML structure
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>{post['title']}</title>
                <style>
                    body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 20px; background: #f9f9f9; }}
                    article {{ background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
                    img {{ max-width: 100%; height: auto; display: block; margin: 20px 0; border-radius: 4px; }}
                    .meta {{ color: #666; font-size: 0.9em; margin-bottom: 20px; }}
                    h1 {{ color: #222; margin-top: 0; }}
                </style>
            </head>
            <body>
                <article>
                    <h1>{post['title']}</h1>
                    <p class="meta">Published: {post['published']}</p>
                    <hr>
                    {soup.decode_contents()}
                </article>
            </body>
            </html>
            """

            file_path = os.path.join(save_dir, f"{title}.html")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)

        messagebox.showinfo("Success", f"All {len(data['items'])} posts have been archived with embedded images!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed: {str(e)}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Blogger Portable Archiver")
root.geometry("400x250")

tk.Label(root, text="Blogger API Key:", font=("Arial", 10, "bold")).pack(pady=(20, 0))
api_entry = tk.Entry(root, width=45)
api_entry.pack(pady=5)

tk.Label(root, text="Blog ID:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
blog_entry = tk.Entry(root, width=45)
blog_entry.pack(pady=5)

download_btn = tk.Button(root, text="Generate Portable HTML Files", command=download_posts, 
                         bg="#9C27B0", fg="white", font=("Arial", 10, "bold"), pady=10)
download_btn.pack(pady=20)

root.mainloop()