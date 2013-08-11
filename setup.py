from distutils.core import setup

setup(
    name='git-mnemonic',
    version='0.1.0dev',
    description='Human friendly git hashes',
    author='Glen Mailer',
    author_email='glenjamin@gmail.com',
    url='https://github.com/glenjamin/git-mnemonic',
    license='MIT',
    scripts=['git-mnemonic'],
    packages=['git_mnemonic'],
    package_data={'git_mnemonic': ['words.txt']},
)