from utils import process_all_markdown_files


if __name__ == "__main__":
    content_directory = "content"
    output_directory = "dist"
    template_file = "template/blog.html"
    process_all_markdown_files(content_directory, template_file, output_directory)
