import setuptools
from pathlib import Path

setuptools.setup(
        version="149",
        name="vinca",
        author="Oscar Laird", 
        autor_email = "olaird25@gmail.com",

        description = "simple spaced repetition",
        long_description = (Path(__file__).parent / 'README.md').read_text(),
        long_description_content_type="text/markdown",

        url = 'https://github.com/oscarlaird/vinca-SRS',
        project_urls={
                "Bug Tracker": "https://github.com/oscarlaird/vinca-SRS/issues",
                "Man Page": "https://oscarlaird.github.io/vinca-SRS/vinca.1.html",
        },

        data_files = [('man/man1', ['vinca/docs/vinca.1'])],
        # include_package_data = True,
        package_data = {'':['docs/*.txt', 'docs/*.md']},
        install_requires = ['fire'],
        packages=setuptools.find_packages(),
        scripts=[
            'scripts/vinca',
            'scripts/vinca_debug',
           ]
)