import os

def create_html_with_iframes():
    folder_path = "C:\Merge HTML files using Python"  # Change this to your desired folder path
    
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cucumber</title>
        <style>
            body {
                background-color: #222;
                color: white;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            h1, p {
                text-align: center;
            }
            iframe {
                width: 100vw; 
                height: 100vh; 
                border: none; 
            }
        </style>
    </head>
    <body>
        <h1>Cucumber Reports Summery</h1> 
        <p>release notes</p>
    """

    html_files = [file for file in os.listdir(folder_path) if file.endswith(".html")]

    for file in html_files:
        html_content += f"""
        <h2>{file}</h2>
        <iframe src="{os.path.join(folder_path, file)}"></iframe>
        """

    html_content += """
    </body>
    </html>
    """

    with open(os.path.join(folder_path, "merged_reports.html"), "w") as f: # Generated merged output html file
        f.write(html_content)

if __name__ == "__main__":
    create_html_with_iframes()
