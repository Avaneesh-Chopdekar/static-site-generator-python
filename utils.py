import os


def convert_markdown_to_html(file_name, file_content, output_dir="dist"):
    """
    Converts a markdown file to HTML and saves it in the specified output directory.

    Args:
        file_name (str): The name of the markdown file.
        file_content (str): The content of the markdown file.
        output_dir (str): The directory to save the HTML file.
    """
    html_file_name = os.path.splitext(file_name)[0] + ".html"
    output_path = os.path.join(output_dir, html_file_name)

    # Change this later
    html_content = f"<h1>{file_name}</h1>\n<pre>{file_content}</pre>"

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)
        print(f"Converted {file_name} to {html_file_name}")
    except Exception as e:
        print(f"Error creating HTML file for {file_name}: {e}")


def get_markdown_files(directory, output_dir="dist"):
    """
    Gets all markdown files from the specified directory and converts them to HTML.

    Args:
        directory (str): The directory to search for markdown files.
        output_dir (str): The directory to save the HTML files.
    """
    for file_name in os.listdir(directory):
        if file_name.endswith(".md"):
            file_path = os.path.join(directory, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                convert_markdown_to_html(file_name, file_content, output_dir)
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
