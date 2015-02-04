from setuptools import setup, find_packages

version = '0.1.3'

try:
    readme = open('README.rst').read()
    readme = readme.replace('.. image:: _static', '.. figure:: https://github.com/collective/collective.twittercards/raw/master/docs/_static')
except:
    readme = ''

long_description = (
    readme
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.twittercards',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='plone, twitter cards',
      author='Goldmund, Wyldebeast & Wunderliebe',
      author_email='info@gw20e.com',
      url='https://github.com/collective/collective.twittercards',
      license='GPL 2.0',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.z3cform.datagridfield',
          'five.grok',
          'plone.directives.form',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.api',
              'plone.app.testing[robot]>=4.2.2',
              'plone.testing',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
)
