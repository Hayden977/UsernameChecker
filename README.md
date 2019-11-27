[![Build Status][build-shield]]()
[![GNU License][license-shield]][license-url]
[![Release][release-shield]]()
[![Version][version-shield]]()
[![Custom][custom-shield]]()

# Username Finder 

## Table of Contents

* [About](#about)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Exceptions](#usage)
* [Contributing](#contributing)
  * [Features](#features)
  * [TODO](#features)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

## About


### Built With

This project was created with [Python 3](https://www.python.org/downloads/release/python-380/) 
and is [PEP 8](https://www.python.org/dev/peps/pep-0008/) compatible as of November 26th, 2019.

This repository was built by [PyCharm Community Edition](https://www.jetbrains.com/pycharm/) 
and maintained by [Hayden977](https://github.com/Hayden977).

## Getting Started



### Prerequisites

As of November 26th, 2019, the only external prerequisite is [selenium](https://pypi.org/project/selenium/) and the accompanying browser drivers. 
See [Installation](#installation) for more detail.

```Bash
pip install selenium
```

### Installation

The browser drivers can be found on the [PyPI](https://pypi.org/project/selenium/) page. From the webpage, popular browser drivers are:

| Browser | Download Link |
| ------- | ------------- |
| Chrome  | [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
| Edge    | [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
| Firefox | [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
| Safari  | [https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

Note: if the browser driver is not in the `PATH` variable, the `_PATH` variable will need to be set to the path of the driver.

## Usage

As of November 26th, 2019, running `main.py` will result in the following input field. 

```
Username(s): 
```

This field will accept a single username or a list of usernames separated by commas and spaces. 
Invalid usernames (see [Exceptions](#exceptions) below) should be caught before a query is executed. 

#### Exceptions

From [Mojang](https://help.mojang.com/customer/en/portal/articles/928638-minecraft-usernames), usernames must obey by the following rules:

* Must be between 3-16 characters in length
* Characters from A-Z (upper and lowercase) are allowed
* Characters from 0-9 are allowed
* The only special character allowed is **_** (underscore) 
  * Spaces are not allowed
  * All other characters are not allowed
 

Examples of valid input, followed by examples of invalid inputs, are shown below.

```
VALID INPUTS
Username(s): Python123
Username(s): Python123, Python456

INVALID INPUTS
Username(s): Space Character
Username(s): TwentyCharacterNames
Username(s): 2c
Username(s): русский
```

## Contributing

The Username Finder is currently hindered by the limitations of [selenium](https://pypi.org/project/selenium/). 
Designed as an application tester, it needs to load all elements of a page first. This results in much slower query rates, and downtime for the program.
This downtime could be taken advantage of by a library like [beautifulsoup4](https://pypi.org/project/beautifulsoup4/),
which can read the source of the page instead of rendering the full site. This will likely bring the query rate down from 20 seconds to 5 seconds,
which will allow the following [Features](#features) to be implemented.

#### Features

* CSV support
* Find all available usernames of length `n`
* Username 'sniping'
* **Full [Mojang API](https://wiki.vg/Mojang_API) support**

#### TODO

* Implement [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) or an alternative
* Improve general performance
  * Implement ideas listed in [Features](#features) 
* Improve code readability
  * Remove redundant exception handlers
  * Ensure [PEP 8](https://www.python.org/dev/peps/pep-0008/) compatibility

## License

Released under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.

This project is not affiliated with [NameMC](https://namemc.com/).

## Contact

Maintained by [Hayden977](https://github.com/Hayden977).

## Acknowledgements
* [GitHub Pages](https://pages.github.com)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html)
* [NameMC](https://namemc.com/)
* [Kalle Hallden's](https://github.com/KalleHallden/ProjectInitializationAutomation/commit/0486c1bccc412581bdd6b4f4689842a1b495d087#diff-3c73a31effabccb097e906342a0b9aa0)
source code for the idea and framework
* [StackOverflow](https://stackoverflow.com/a/44593228) for string-replace code snippet

[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-GNU_GPLv3-orange.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/gpl-3.0/
[release-shield]: https://img.shields.io/github/v/release/Hayden977/NameMC?style=flat-square
[version-shield]: https://img.shields.io/pypi/pyversions/selenium?style=flat-square
[custom-shield]: https://img.shields.io/badge/hayden-977-blue.svg?style=flat-square