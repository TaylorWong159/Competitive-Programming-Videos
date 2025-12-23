import argparse
import os
import sys

def main() -> None:
    if '-h' in sys.argv or '--help' in sys.argv:
        print(
            'Usage: python create_video_project.py project_name [output_dir] [options]\n'
            'Options:\n'
            '  -h, --help            Show this help message and exit'
        )
        exit(0)
    if len(sys.argv) == 2:
        project_name = sys.argv[1]
        output_dir = '.'
    elif len(sys.argv) == 3:
        project_name, output_dir = sys.argv[1:]
    else:
        print('Improper usage: Use -h or --help for help.')
        exit(1)

    # Create project directory
    project_dir = os.path.join(output_dir, project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Create the Manim scene file
    scene_file_path = os.path.join(project_dir, f'{project_name}.py')
    with open(scene_file_path, 'w') as scene_file:
        scene_file.write(
            'from manim import *\n\n'
            f'class {project_name}(Scene):\n\n'
            '    def init(self) -> None:\n'
            '        ...\n\n'
            '    def construct(self) -> None:\n'
            '        # Initialize variables\n'
            '        self.init()\n\n'
            '        # Animate Scene\n'
            '        ...\n'
        )
    print(f'Created video project at: "{project_dir}"')

    # Create script file
    script_file_path = os.path.join(project_dir, 'script.md')
    with open(script_file_path, 'w') as script_file:
        script_file.write(
            f'# {project_name}\n\n'
            '...\n'
        )


if __name__ == '__main__':
    main()