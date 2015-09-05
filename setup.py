from setuptools import setup
import os
import io

def read(fname):
    return io.open(os.path.join(os.path.dirname(__file__), fname), encoding="UTF-8").read()

setup(
    name='django-compressor-autoprefixer',
    version='0.1.0',
    author='Yuri Shikanov',
    author_email='dizballanze@gmail.com',
    packages=['django_compressor_autoprefixer'],
    # scripts=[],
    url='https://github.com/dizballanze/django-compressor-autoprefixer',
    license='MIT',
    description='Django Compressor CSS filter for autoprefixer',
    long_description=read('README.rst'),
    install_requires=[
        "django_compressor",
    ],
    data_files=[('', ['LICENSE', 'README.rst'])]
)
