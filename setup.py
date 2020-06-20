from setuptools import setup, find_packages

setup(name='anndb',
    version='0.0.1',
    description='AnnDB Client',
    author='Marek Galovic',
    author_email='galovic.galovic@gmail.com',
    license='MIT',
    url='https://github.com/marekgalovic/anndb-client-python',
    download_url='https://github.com/marekgalovic/anndb-client-python/archive/0.0.1.tar.gz',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'grpc'
    ],
)