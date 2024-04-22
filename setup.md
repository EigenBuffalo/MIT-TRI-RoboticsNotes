```
python3 -m pip install --upgrade pip
pip install ipykernel
python3 -m iphkernel install --user --name=venv
pip install pydrake
pip install manipulation --extra-index-url https://drake-packages.csail.mit.edu/whl/nightly/  
pip install nbformat nbconvert
```


you might have to mannually copy the utils.py from github master to your virtual environment /lib/python3.XX/site-packages/manipulation/utils.py
