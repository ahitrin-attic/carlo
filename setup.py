from carlo import __version__ as carlo_version
from pip.req import parse_requirements
from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


install_requires = [str(r.req) for r in parse_requirements('requirements.txt', session=False)]


setup(name='carlo',
    version=carlo_version,
    description="declare a model and generate a list of events following this model",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ],
    keywords='random data generation',
    author='Andrey Hitrin',
    author_email='andrey.hitrin@gmail.com',
    url='https://github.com/ahitrin/carlo',
    license='MIT',
    packages=find_packages('carlo'),
    package_dir = {'': 'carlo'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['carlo=carlo:main']
    }
)
