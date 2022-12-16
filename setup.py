from setuptools import setup, find_packages


setup(
    name = 'bayes_nets_sample',
    version = '0.6',
    license = 'MIT',
    description = 'A class to represent a Bayes Network. And apply all the different sampling strategies to the calculate a given query.',
    author = "Srajan Chourasia",
    author_email = 'srajanstark.ash@gmail.com',
    packages = find_packages('bayes'),
    package_dir = {'': 'bayes'},
    url = 'https://github.com/srajan-kiyotaka/bayesNetSample',
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords = ['bayes'],
    install_requires = [
          'random',
      ],
    classifiers = [
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Student_Teachers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.6',
  ],
)
