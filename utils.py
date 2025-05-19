import os


def convert_markdown_to_html(file_name, file_content):
    """
    This function receives converts the markdown file to html

    Args:
        file_name (str): The name of the markdown file.
        file_content (str): The content of the markdown file.
    """
    file_name = file_name.replace(".md", ".html")
    print(f"Processing file: {file_name}")
    print(f"First 100 characters: {file_content[:100]}...")


def get_markdown_files(directory):
    """
    Gets all markdown files from the specified directory and processes them.

    Args:
        directory (str): The directory to search for markdown files.
    """
    for file_name in os.listdir(directory):
        if file_name.endswith(".md"):
            file_path = os.path.join(directory, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                convert_markdown_to_html(file_name, file_content)
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
