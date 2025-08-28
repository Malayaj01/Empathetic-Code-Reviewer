from setuptools import setup, find_packages

setup(
    name='empathetic-code-reviewer',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to transform harsh code review comments into constructive feedback.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/empathetic-code-reviewer',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openai',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)