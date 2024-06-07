import os
import shutil

if __name__ == '__main__':
    if os.path.exists('build'):
        shutil.rmtree('build')

    os.mkdir('build')
    shutil.copytree('static', 'build/static')
    shutil.copy('templates/index.html', 'build/index.html')

    shutil.copy('CNAME', 'build/CNAME')  # Add this line to copy CNAME file