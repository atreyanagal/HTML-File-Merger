# HTML Files Merger with Python

This Python script facilitates the merging of multiple HTML files into a single HTML document using iframes. It's particularly useful for consolidating various web-based reports or summaries into a unified format.

## Features

- **Merge HTML Files**: Combine multiple HTML files into one.
- **Embed with Iframes**: Utilize iframes for seamless embedding.
- **Customizable Styling**: Easily adjust styling to fit your needs.
- **Straightforward Usage**: Simple and intuitive process.

## Usage

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your_username/html-files-merger.git
    ```

2. **Navigate to the Directory**:

    ```bash
    cd html-files-merger
    ```

3. **Modify the Script**:

    - Open `merge_html_with_iframes.py`.
    - Adjust `folder_path` variable to point to the directory containing your HTML files.

4. **Run the Script**:

    ```bash
    python merge_html_with_iframes.py
    ```

5. **Access Merged HTML**:

    Once the script is executed, the merged HTML file (`merged_reports.html`) will be created in the specified directory. Open it in any web browser to view the consolidated report.

## Requirements

- Python 3.x
- Standard library: os

## Example

Suppose you have the following HTML files in your specified directory (`folder_path`):

- report1.html
- report2.html
- report3.html

After running the script, a file named `merged_reports.html` will be generated, containing iframes with each HTML report embedded.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or features you'd like to see.

## License

This project is licensed under the [MIT License](LICENSE).
