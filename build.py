import os
import shutil
import glob

if __name__ == '__main__':
    if os.path.exists('build'):
        shutil.rmtree('build')

    os.mkdir('build')
    shutil.copytree('static', 'build/static')

    # Copy all HTML files from templates to build
    for html_file in glob.glob('templates/*.html'):
        shutil.copy(html_file, 'build/')

    shutil.copy('CNAME', 'build/CNAME')  # Add this line to copy CNAME file