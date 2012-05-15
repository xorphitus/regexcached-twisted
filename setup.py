"""
Distutuis file.
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    pass

import os
README = os.path.join(os.path.dirname(__file__), "README.md")

setup(name = "regexcached",
      version = "0.0.1",
      author = "xorphitus / T. Matsu",
      author_email = "xorphitus@gmail.com",
      description = "A replica of memcached, that accepts a regular expression key.",
      long_description = open(README).read() + "\n\n",
      url = "https://github.com/xorphitus/regexcached-twisted",
      packages = find_packages(),
      namespace_packages = [],
      install_requires = [
          "Twisted"
          ],
      classifiers = [
          "Framework :: Twisted",
          "Programing Language :: Python :: 2.7"
          ],
      test_suite = "nose.collector",
      test_require = ["Nose"],
      )
