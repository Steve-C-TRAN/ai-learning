import os
from gitignore_parser import parse_gitignore

files_to_concatenate = [
    # Core application files
    'app/__init__.py',           # Flask app initialization
    'run.py',                    # Application entry point
    'config.py',                 # Main configuration
    'requirements.txt',          # Python dependencies

    # Routes and Views
    'app/routes/__init__.py',    # Routes initialization
    'app/routes/main.py',        # Main route handlers

    # Content (per-course packages)
    'app/content/loader.py',     # Course discovery and quiz helpers
    'app/content/ai_intro/modules.py',   # Course 1 content
    'app/content/ai_intro/quizzes.py',   # Course 1 quizzes
    'app/content/ai_advanced/modules.py',# Course 2 content
    'app/content/ai_advanced/quizzes.py',# Course 2 quizzes

    # Models and Data
    'app/models/__init__.py',    # Models initialization
    'app/models/progress.py',    # Anonymous progress tracking
    'app/models/quiz.py',        # Quiz attempts
    'app/models/course.py',      # (legacy placeholder, safe to keep)

    # Forms and Auth (legacy, currently unused)
    'app/forms/__init__.py',     # Forms initialization
    'app/forms/forms.py',        # Form definitions
    'app/auth.py',               # Authentication logic

    # Agents (legacy, currently unused)
    'app/agents/__init__.py',    # Agents initialization

    # Utils
    'app/utils/__init__.py',     # Utils initialization
    'app/utils/errors.py',       # Error handling
    'app/utils/logging.py',      # Standard logging functions

    # Templates
    'app/templates/base.html',   # Base template
    'app/templates/index.html',  # Courses landing
    'app/templates/course.html', # Course detail page
    'app/templates/module.html', # Module detail page with quiz

    # Frontend Assets (exclude images and generated CSS)
    'app/static/js/htmx.min.js', # Vendor JS
    'app/static/js/main.js',     # Main JavaScript file

    # Build/Tooling Config
    'tailwind/config.js',        # Tailwind custom config
    'tailwind/input.css',        # Tailwind source CSS
    'tailwind.config.js',        # Tailwind configuration
    'postcss.config.js',         # PostCSS configuration
    'package.json',              # NPM scripts and deps

    # Documentation
    'README.md',
    'README_setup.md',
    'README_next.md',

    # Tests
    'tests/__init__.py',
]

# Define the output file
output_file = 'combined.txt'

def create_directory_tree(startpath):
    """Generate a string representation of the directory tree, excluding .gitignore files, migrations/, and .git/."""
    tree = []
    
    # Parse .gitignore file
    gitignore_file = os.path.join(startpath, '.gitignore')
    if os.path.exists(gitignore_file):
        ignorer = parse_gitignore(gitignore_file)
    else:
        ignorer = lambda f: False  # If no .gitignore, don't ignore anything
    
    # Additional directories to exclude
    exclude_dirs = {'migrations', '.git', 'scripts', 'data', 'prompts'}
    
    for root, dirs, files in os.walk(startpath, topdown=True):
        # Remove ignored and explicitly excluded directories
        dirs[:] = [d for d in dirs if not ignorer(os.path.join(root, d)) and d not in exclude_dirs and not d.startswith('zzz')]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not ignorer(os.path.join(root, f)) and not f.startswith('zzz'):
                tree.append(f"{subindent}{f}")
    return '\n'.join(tree)

def concatenate_files(file_list, output_file):
    tree = create_directory_tree('.')  # Adjust '.' to the root of your project if necessary
    with open(output_file, 'w') as outfile:
        outfile.write("# Project Directory Structure\n")
        outfile.write(tree + "\n\n# End of Directory Structure\n\n")
        for file_name in file_list:
            if os.path.exists(file_name):
                with open(file_name, 'r') as infile:
                    outfile.write(f'# Start of {file_name}\n')
                    outfile.write(infile.read())
                    outfile.write(f'\n# End of {file_name}\n\n')
            else:
                print(f"File {file_name} does not exist.")

if __name__ == '__main__':
    concatenate_files(files_to_concatenate, output_file)
    print(f"Files concatenated into {output_file}")
