<!--
 * @Author: unibeam98 beyondevery@live.com
 * @Date: 2025-07-25 17:34:18
 * @LastEditors: unibeam98 beyondevery@live.com
 * @LastEditTime: 2025-07-25 17:50:50
 * @FilePath: \PyPeridyno_package\README.md
-->
# PyPeridyno_package

## 1.Install twine
``` shell
pip install twine
```

## 2.Use Token

Using this token
To use this API token:

Set your username to __token__
Set your password to the token value, including the pypi- prefix
For example, if you are using Twine to upload your projects to PyPI, set up your $HOME/.pypirc file like this:
```

[testpypi]
  username = __token__
  password = pypi**

[pypi]
  username = __token__
  password = pypi-**

```

## 3.Build PyPeridyno

To configure PeriDyno's asset path, modify the CMake file to redirect PERDYNO_ASSET_PATH to C:/ProgramData/Peridyno/data/ before compiling。

Place the files that need to be packaged and uploaded in the `src` directory.

## 4.Modify File Information

Modify ```setup.py```

## 5.Package

```
python setup.py sdist build
```
A tar.gz file will be generated in the dist directory.

## 6. Upload

Test-pypi:
```
python -m twine upload --repository testpypi dist/*
```

Pypi:
```
python -m twine upload dist/*
```