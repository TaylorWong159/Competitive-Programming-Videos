import argparse
from datetime import datetime as dt
import os

def copy_file(
    src: str,
    dest: str,
    *,
    replacements: dict[str, str] | None = None
) -> None:
    """
    Copy a file from src to dest, replacing placeholders with actual values.

    Args:
        src (str): Source file path.
        dest (str): Destination file path.
        replacements (optional dict[str, str]): Dictionary of placeholders and their replacements.
    """
    with open(src, 'r', encoding='utf-8') as f_src:
        content = f_src.read()

    if replacements is not None:
        for placeholder, actual in replacements.items():
            content = content.replace(f'%%{placeholder}%%', actual)

    with open(dest, 'w', encoding='utf-8') as f_dest:
        f_dest.write(content)

def title_case(name: str) -> str:
    """
    Convert a string to title case, replacing underscores and hyphens with spaces.

    Args:
        name (str): The string to convert.
    Returns:
        str: The title-cased string.
    """
    return ' '.join(word.capitalize() for word in name.replace('_', ' ').replace('-', ' ').split())

def pascal_case(name: str) -> str:
    """
    Convert a string to PascalCase, removing underscores and hyphens.

    Args:
        name (str): The string to convert.
    Rreturns:
        str: The PascalCase string.
    """
    return ''.join(word.capitalize() for word in name.replace('_', ' ').replace('-', ' ').split())

def main() -> None:
    parser = argparse.ArgumentParser(description='Create a new Manim video project.')
    parser.add_argument(
        'project_name',
        type=str,
        help='Name of the new project'
    )
    parser.add_argument(
        '--output_dir', '-o',
        type=str,
        default='videos',
        help='Directory to create the project in (default: "videos")',
        required=False
    )
    parser.add_argument(
        '--template', '-t',
        type=str,
        default='templates',
        help='Directory containing the template files (default: "templates")',
        required=False
    )
    parser.add_argument(
        '--author', '-a',
        type=str,
        default='',
        help='Author name for the project',
        required=False
    )
    args = parser.parse_args()

    project_name: str = args.project_name
    output_dir: str = args.output_dir
    template_dir: str = args.template
    author: str = args.author

    # Create project directory
    project_dir = os.path.join(output_dir, project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Replacements
    replacements = {
        'project': project_name,
        'project_class': pascal_case(project_name),
        'project_title': title_case(project_name),
        'date': dt.now().isoformat(),
        'author': author,
    }

    # Create the Manim scene file
    scene_file_path = os.path.join(project_dir, f'{project_name}.py')
    scene_template_path = os.path.join(template_dir, 'video.py')
    copy_file(scene_template_path, scene_file_path, replacements=replacements)
    # Create script file
    script_file_path = os.path.join(project_dir, 'script.tex')
    script_template_path = os.path.join(template_dir, 'script.tex')
    copy_file(script_template_path, script_file_path, replacements=replacements)

if __name__ == '__main__':
    main()