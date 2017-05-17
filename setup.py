from distutils.core import setup

setup(
    name='contracts',
    version='1.0',
    packages=[
        'contracts',
        'contracts.nodes',
        'contracts.tokens',
        'contracts.parser',
        'contracts.visitors'
    ],
    url='https://github.com/DeveloperHacker/contracts',
    license='MIT',
    author='HackerMadCat',
    author_email='hacker.mad.cat@gmail.com',
    description='Tiny contract contracts'
)
