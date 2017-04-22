from setuptools import setup

setup(
    name='laxis_made_projects',
    version='0.0.1',
    url='http://github.com/aarondizele/python/setuptools.py',
    license='MIT',
    author='Aaron Dizele',
    author_email='aldizele@gmail.com',
    description='Lorem ectums...',
    py_modules=['ab_test'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'docopt >= 0.6.0',
        'numpy >= 1.10.0'
    ],
    entry_points="""
    [console_scripts]
    laxis_made_projetcs = cli:main
    """
)