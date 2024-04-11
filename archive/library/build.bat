cd ./library

py -m build
py -m twine upload --repository testpypi dist/*
pip uninstall arcade-cabinet-LeftOverDefault
pip install -i https://test.pypi.org/simple/ arcade-cabinet-LeftOverDefault==0.0.0.8