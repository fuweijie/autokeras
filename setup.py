from distutils.core import setup
from setuptools import find_packages

setup(
    name='autokeras',
    packages=find_packages(exclude=('tests',)),
    install_requires=['scipy==1.1.0',
                      'torch==1.0.1.post2',
                      'torchvision==0.2.2.post3',
                      'numpy==1.15.4',
                      'keras==2.2.4',
                      'scikit-learn==0.20.1',
                      'scikit-image==0.15.0',
                      'tqdm==4.28.1',
                      'tensorflow==1.13.1',
                      'imageio==2.4.1',
                      'requests==2.21.0',
                      'lightgbm==2.0.2',
                      'pandas==0.23.4',
                      'opencv-python==4.1.0.25'],
    version='0.3.5',
    description='AutoML for deep learning',
    author='DATA Lab at Texas A&M University',
    author_email='jhfjhfj1@gmail.com',
    url='http://autokeras.com',
    download_url='https://github.com/jhfjhfj1/autokeras/archive/0.3.5.tar.gz',
    keywords=['AutoML', 'keras'],
    classifiers=[]
)
