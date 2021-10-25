from setuptools import setup, find_packages

setup(name='apiautotest',
      version='1.0',
      description="Test API Automation",
      author='Maaz Ahmed',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
            "pytest==6.2.5",
            "pytest-html==3.1.1",
            "requests==2.26.0",
            "requests-oauthlib==1.3.0",
            "PyMySQL==1.0.2"
      ]
      )