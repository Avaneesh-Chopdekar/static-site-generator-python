import os
import re
import frontmatter
from markdown import markdown


def render_markdown_to_html(
    markdown_file_path, template_file_path="template.html", output_dir="dist"
):
    """
    Renders a markdown file to HTML using a template.

    Args:
        markdown_file_path (str): Path to the markdown file.
        template_file_path (str): Path to the HTML template file.
        output_dir (str): Directory to save the rendered HTML.
    """
    try:
        with open(markdown_file_path, "r", encoding="utf-8") as f:
            post = frontmatter.load(f)
        content = post.content
        metadata = post.metadata

        title = metadata.get("title", "Default Title")
        description = metadata.get("description", "Default Description")
        date = metadata.get("date", "Unknown Date")

        html_content = markdown(content, extensions=["fenced_code", "tables"])

        with open(template_file_path, "r", encoding="utf-8") as f:
            template = f.read()

        template = re.sub(r"\{\{\s*title\s*\}\}", title, template)
        template = re.sub(r"\{\{\s*description\s*\}\}", description, template)
        template = re.sub(r"\{\{\s*content\s*\}\}", html_content, template)

        output_file_name = (
            os.path.splitext(os.path.basename(markdown_file_path))[0] + ".html"
        )
        output_file_path = os.path.join(output_dir, output_file_name)

        os.makedirs(output_dir, exist_ok=True)
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(template)

        print(f"Rendered {markdown_file_path} to {output_file_path}")

    except Exception as e:
        print(f"Error processing {markdown_file_path}: {e}")


def get_markdown_files(
    content_dir: str, template_path="template.html", output_dir="dist"
):
    """
    Gets all markdown files from the specified directory and converts them to HTML.

    Args:
        content_dir (str): The directory to search for markdown files.
        template_path (str): The path to the HTML template file.
        output_dir (str): The directory to save the HTML files.
    """
    for filename in os.listdir(content_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(content_dir, filename)
            render_markdown_to_html(file_path, template_path, output_dir)
