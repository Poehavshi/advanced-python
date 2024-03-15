
## Help command: 
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  nl    The nl utility reads lines from the named file,applies a...
  tail  output the last N lines, instead of the last 10, if we have input...
  wc    print newline, word, and byte counts for each file, and a total...
```

## NL command for file:
### expected result:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ nl pyproject.toml 
     1  [tool.poetry]
     2  name = "homework-1"
     3  version = "0.1.0"
     4  description = ""
     5  authors = ["arkadiysotnikov <cotnikoarkady@gmail.com>"]
     6  packages = [{include = "filescli"}]
        
     7  [tool.poetry.dependencies]
     8  python = "^3.12"
     9  click = "^8.1.7"
        
        
    10  [build-system]
    11  requires = ["poetry-core"]
    12  build-backend = "poetry.core.masonry.api"
        
        
    13  [tool.poetry.scripts]
    14  file = "filescli.main:main"
```
### our:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py nl pyproject.toml 
     1  [tool.poetry]
     2  name = "homework-1"
     3  version = "0.1.0"
     4  description = ""
     5  authors = ["arkadiysotnikov <cotnikoarkady@gmail.com>"]
     6  packages = [{include = "filescli"}]
    
     7  [tool.poetry.dependencies]
     8  python = "^3.12"
     9  click = "^8.1.7"
    
    
    10  [build-system]
    11  requires = ["poetry-core"]
    12  build-backend = "poetry.core.masonry.api"
    
    
    13  [tool.poetry.scripts]
    14  file = "filescli.main:main"
```

## Nl command with stdin: 
### reference:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ nl
1
     1  1
2
     2  2
3
     3  3
 
     4   
```

### Our:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py nl 
1
     1  1
2
     2  2
3
     3  3
 
     4   

```


## tail command for file: 
### reference:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ tail pyproject.toml 
click = "^8.1.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


[tool.poetry.scripts]
file = "filescli.main:main"
```

### our:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py tail pyproject.toml 
click = "^8.1.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


[tool.poetry.scripts]
file = "filescli.main:main"
```

## Tail command for stdin: 
### reference:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ tail
1
2
3
4
5
6
7
8
9
10
11
12
3D
4
5
6
7
8
9
10
11
12
```

### our (we have -n 17 by default according to the task):
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py tail 
1
2
3
4
5
6
7
8
9
10
11
12
1D
2
3
4
5
6
7
8
9
10
11
12
```

## tail command with several files:
### reference:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ tail pyproject.toml poetry.lock 
==> pyproject.toml <==
click = "^8.1.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


[tool.poetry.scripts]
file = "filescli.main:main"

==> poetry.lock <==
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[metadata]
lock-version = "2.0"
python-versions = "^3.12"
content-hash = "c6202e701e6597827ef3a157ef21b519e1011941877efb14bbb77502a0796dd0"
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ tail pyproject.toml poetry.lock 
```

### our:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py tail pyproject.toml poetry.lock 
==> pyproject.toml <==
click = "^8.1.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


[tool.poetry.scripts]
file = "filescli.main:main"
==> poetry.lock <==
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[metadata]
lock-version = "2.0"
python-versions = "^3.12"
content-hash = "c6202e701e6597827ef3a157ef21b519e1011941877efb14bbb77502a0796dd0"
```

## WC command for file: 
### reference:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ wc pyproject.toml 
      19      37     361 pyproject.toml
```
### our:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py wc pyproject.toml 
      19      37     361 pyproject.toml
```

## WC command with stdin: 
### reference:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ wc
1
2
3
       3       3       6
```

### our:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py wc 
1
2
3
       3       3       6
```

## WC command with several files: 
### reference:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ wc pyproject.toml poetry.lock 
      19      37     361 pyproject.toml
      31     108    1198 poetry.lock
      50     145    1559 total
```
### our:
```
(homework-1-py3.12) Arkadiys-MacBook-Pro:homework-1 arkadiysotnikov$ python filescli/main.py wc pyproject.toml poetry.lock 
      19      37     361 pyproject.toml
      31     108    1198 poetry.lock
      50     145    1559 total
```
