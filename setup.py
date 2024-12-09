from setuptools import setup, find_packages

setup(
    name='prueba_python_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',  # Required for visualization
        'pandas',      # Required for DataFrame handling
    ],
    author='Montserrat Diaz',
    description='Prueba: crear libraria sencilla',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
    #url='https://github.com/yourusername/simple_python_library'
)