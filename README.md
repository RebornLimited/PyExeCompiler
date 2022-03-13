# PyExeCompiler
### Compile py files to exe right in the code.

# Getting started
Install the library:
<ul>
	<li>Installing with pip:</li>
</ul>

```$ pip install pyExeCompiler```

<ul>
	<li>Installing with git:</li>
</ul>

```
$ git clone https://github.com/RebornLimited/PyExeCompiler
$ cd PyExeCompiler
$ python setup.py install
```

# Usage
```python
import pyExeCompiler as pec

# Your code if needed

pec.compile(file_name, icon_path)
```
Then run your file through the console.<br>
```$ python your_file.py```<br>

# Variables
### file_name - The name of the file you are compiling. You must specify with the extension!
### icon_path - Path to your program's icon file. The icon extension must be .ico! If you don't need an icon, write ```None``` instead of the path.
