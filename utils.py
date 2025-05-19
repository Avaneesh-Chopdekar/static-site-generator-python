import os
import re
import frontmatter
from markdown import markdown
from datetime import datetime


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
        date = metadata.get("date", datetime.now())

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


def generate_article_html(title: str, description: str, filename: str) -> str:
    """
    Generates the HTML for a single article.

    Args:
        title (str): The title of the article.
        description (str): The description of the article.
        filename (str): The filename of the article.

    Returns:
        str: The HTML for the article.
    """
    return f"""
            <article>
                <h3><a href="{filename}.html">{title}</a></h3>
                <p>
                    {description}
                </p>
                <a href="{filename}.html">Read more &rarr;</a>
            </article>
"""


def process_all_markdown_files(
    content_dir: str, template_path="template.html", output_dir="dist"
):
    """
    Processes all markdown files in a directory using the specified template and generates
    the index.html.

    Args:
        content_dir (str): The directory to search for markdown files.
        template_path (str): The path to the HTML template file.
        output_dir (str): The directory to save the HTML files.
    """
    all_posts = []
    for filename in os.listdir(content_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(content_dir, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    post = frontmatter.load(f)
                all_posts.append(
                    {
                        "title": post.metadata.get("title", "Default Title"),
                        "description": post.metadata.get(
                            "description", "Default Description"
                        ),
                        "date": post.metadata.get("date", datetime.now()),
                        "featured": post.metadata.get("featured", False),
                        "filename": os.path.splitext(filename)[0],
                        "file_path": file_path,
                    }
                )
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    all_posts.sort(key=lambda x: x["date"], reverse=True)

    featured_posts = [post for post in all_posts if post["featured"]]
    recent_posts = all_posts

    featured_posts_html = "".join(
        generate_article_html(post["title"], post["description"], post["filename"])
        for post in featured_posts
    )

    recent_posts_html = "".join(
        generate_article_html(post["title"], post["description"], post["filename"])
        for post in recent_posts
    )

    with open("dist/index.html", "r", encoding="utf-8") as f:
        landing_page_template = f.read()

    landing_page_html = landing_page_template.replace(
        "<!-- Dynamically add featured blog posts -->", featured_posts_html
    ).replace("<!-- Dynamically add recent blog posts -->", recent_posts_html)

    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(landing_page_html)

    for post in all_posts:
        render_markdown_to_html(post["file_path"], template_path, output_dir)
