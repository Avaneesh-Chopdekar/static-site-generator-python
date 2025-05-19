from utils import get_markdown_files


if __name__ == "__main__":
    content_directory = "content"
    output_directory = "dist"
    template_file = "template/blog.html"
    get_markdown_files(content_directory, template_file, output_directory)
