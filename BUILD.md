# For developers

Readme:

    pip3 install m2r
    m2r README.md

Build:

    python3 setup.py sdist bdist_wheel
    
Upload:

    pip3 install twine
    twine upload dist/*
