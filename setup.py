from setuptools import setup

setup(
    name='sphinx_huzzler',
    version='0.1.0',
    description='Huzzler is Guzzler with Huntr.',
    long_description=open('README.rst').read(),
    author='Carlos Jenkins',
    author_email='carlos@jenkins.co.cr',
    url='https://github.com/carlos-jenkins/sphinx_huzzler',
    packages=['sphinx_huzzler'],
    include_package_data=True,
    install_requires=['Sphinx>=1.2b1'],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ),
)
