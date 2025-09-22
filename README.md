## Python version

Version used in project - Python 3.12

## Generate exe using cxfreeze Windows, MacOs

Coming soon...

## For Developers

1. Use poetry for creating venv.
2. Use black code formatter with line length 110 characters.
3. Use flake8 for best code quality.
4. To run app type HDZero_programmer_2.py

### Compile resources

If you add resources into the UI designer, remember to recompile resources. Otherwise, images may be not correctly 
displayed. 

```shell
pyside6-rcc resource/resources.qrc -o resource/resources.py
```