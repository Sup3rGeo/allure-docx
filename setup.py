from setuptools import setup, find_packages


setup(
    name="allure-docx",
    description="docx report generator based on allure-generated json files",
    author="Victor Maryama (Typhoon HIL, Inc)",
    version="0.3.2",
    license="MIT",
    install_requires=[
        'cairosvg',
        'click',
        'pygal',
        'python-docx',
    ],
    extras_require={
        'dev': ['pyinstaller'],
    },

    packages=find_packages('src'),
    package_dir={'': 'src'},

    # Should be present so MANIFEST.in is taken into account. However only adds files that are inside package.
    include_package_data=True,

    entry_points={
        'console_scripts': ['allure-docx = allure_docx.commandline:main'],
    },
)
