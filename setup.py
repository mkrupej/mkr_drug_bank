from setuptools import setup

setup(
    name="Local DrugBank DB search engine",
    version="0.0.4",
    author="Michal Krupej",
    author_email="michal.krupej@student.uj.edu.pl",
    description="Search engine for local copy of DrugBankDB",
    keywords="drugBank drug db disease",
    packages=['Parser', 'Loader', 'Model'],
    requires=['xmltodict', 'lxml']
    #long_description=read('README'),
)
