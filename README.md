# Static Site Generator

This Python script generates a static blog from Markdown files with frontmatter, using an HTML template for individual posts and a separate template for the landing page (index.html). It supports featured posts and sorts posts by date.

## Features

- **Markdown to HTML Conversion:** Converts Markdown files to HTML using the `markdown` library.
- **Frontmatter Support:** Parses YAML frontmatter from Markdown files using the `python-frontmatter` library to extract metadata like title, description, date, and featured status.
- **Template Rendering:** Uses HTML templates to generate the final HTML files, replacing placeholders with dynamic content.
- **Landing Page Generation:** Creates a landing page (`index.html`) with featured posts and a list of recent posts, dynamically populated from the Markdown files.
- **Featured Posts:** Allows you to designate certain posts as "featured" in the frontmatter, which will be displayed prominently on the landing page.
- **Date-Based Sorting:** Sorts posts by date (specified in the frontmatter) in descending order, displaying the most recent posts first.
- **Regular Expression Template Replacement:** Uses regular expressions for template replacement to handle variations in placeholder syntax (e.g., `{{title}}`, `{{ title }}`, etc.).
- **Automatic Directory Creation:** Creates the output directory (`dist` by default) if it doesn't exist.
- **UTF-8 Encoding:** Handles UTF-8 encoding for proper character display.

## Requirements

- Python 3.9+
- `python-frontmatter` library: `pip install python-frontmatter`
- `markdown` library: `pip install markdown`

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Avaneesh-Chopdekar/static-site-generator-python
    cd static-site-generator-python
    ```

2.  **Install dependencies:**

    ```bash
    pip install python-frontmatter markdown
    ```

3.  **Create directories and files:**

    - **`content/` directory:** This directory should contain your Markdown files.
    - **`template/blog.html` file:** This file should contain the HTML template for individual blog posts, with placeholders for `{{ title }}`, `{{ description }}`, and `{{ content }}`. You can customize the template to your liking.
    - **`template/index.html` file:** This file should contain the HTML template for the landing page (`index.html`). It must contain the following placeholders:
      - `<!-- Dynamically add featured blog posts -->`: This is where the featured posts will be inserted.
      - `<!-- Dynamically add recent blog posts -->`: This is where the recent posts will be inserted.
        Remove any existing `article` tags, ensuring only the placeholder comments remain where you want the content inserted.

4.  **Configure the script:**

    - Edit the `main.py` file to set the following variables:
      - `content_directory`: The path to your `content/` directory.
      - `template_file`: The path to your `template/blog.html` file.
      - `output_directory`: The path to the directory where you want the generated HTML files to be saved (default is `dist`).

## Markdown Frontmatter

Your Markdown files should include YAML frontmatter at the beginning of the file, enclosed in `---` delimiters. The frontmatter should include at least the following fields:

```yaml
---
title: My Blog Post Title
description: A brief description of my blog post.
date: 2025-05-19 #YYYY-MM-DD format
featured: true # or false
---
Below here is the actual content of the blog post...
```

- **`title`:** The title of the blog post.
- **`description`:** A brief description of the blog post (used in the landing page).
- **`date`:** The date of the blog post in `YYYY-MM-DD` format. This is used for sorting.
- **`featured`:** Set to `true` to display the post in the "Featured Posts" section of the landing page. Set to `false` or omit the field to exclude it from the featured section.

## Usage

1.  **Run the script:**

    ```bash
    python main.py
    ```

2.  **View the generated website:**

    Open the `index.html` file in the `dist/` directory in your web browser to view the generated blog.

## Customization

- **Templates:** Customize the `template/blog.html` and `template/index.html` files to change the look and feel of your blog.
- **CSS:** Add CSS styles to the generated HTML files by linking to a stylesheet in your templates. A basic `style.css` example is provided in previous responses.
- **Content:** Add or modify Markdown files in the `content/` directory to update the content of your blog.
- **Configuration:** Adjust the `content_directory`, `template_file`, and `output_directory` variables in `main.py` to match your project structure.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
