
import io
import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
    try:
        long_description = readme.read()
    except IOError:
        long_description = ''


setup_params = dict(
    name='a2m.itertools',
    author='Alex Malykh',
    author_email='a2m.dev@yandex.ru',
    description='A collection of convenient interator functions',
    long_description=long_description,
    url='about:blank',
    license='MIT',
    packages=setuptools.find_packages(exclude=['tests']),
    namespace_packages=['a2m'],

    keywords='itertools iterators',
    test_suite='tests',

    setup_requires=['setuptools_scm'],
    use_scm_version=dict(root='.', relative_to=__file__),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)


if __name__ == '__main__':
    setuptools.setup(**setup_params)