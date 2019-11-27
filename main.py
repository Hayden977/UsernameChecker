from selenium import webdriver as driver

_PATH = "./chromedriver.exe"


class InvalidCharacterError(Exception):
    """Raised when there are invalid characters in username"""
    pass


class SpaceCharacter(InvalidCharacterError):
    """Raised when there are spaces in username"""
    pass


class TooManyChars(InvalidCharacterError):
    """Raised when there are too many characters in username"""
    pass


class TooFewChars(InvalidCharacterError):
    """Raised when there are too few characters in username"""
    pass


class NonAsciiChars(InvalidCharacterError):
    """Raised when there is a non-ASCII character in username"""
    pass


def print_e(es):
    print(len(es) * "-")
    print(es)
    print(len(es) * "-")


def try_name(un, retry=False):
    try:
        if " " in un:
            raise SpaceCharacter
        elif len(un) > 16:
            raise TooManyChars
        elif len(un) < 3:
            raise TooFewChars
        elif not un.isascii():
            raise NonAsciiChars
    except SpaceCharacter:
        print_e("SPACE character in username, replacing with UNDERSCORE")
        try_name(un.replace(" ", "_"))
        return
    except TooManyChars:
        print_e("Too MANY CHARS in username, aborting")
        return
    except TooFewChars:
        print_e("Too FEW CHARS in username, aborting")
        return
    except NonAsciiChars:
        print_e("Non-ASCII character(s) in username, aborting")
        return
    else:
        browser = driver.Chrome(_PATH)
        browser.get("https://namemc.com/search?q=" + un)

        div_xpath = "//*[@id='status-bar']/div/div/div[2]/div/div[1]/div[2]"
        status_xpath = "//*[@id='status-bar']/div/div/div[2]/div/div[2]/div[2]"

        status_div = browser.find_element_by_xpath(div_xpath)
        status = status_div.text
        views_div = browser.find_element_by_xpath(status_xpath)
        views = views_div.text[:-8]

        browser.close()

        print(un, status, views)
        if not status == "Available*" and retry:
            leet = [("A", "4"),
                    ("E", "3"),
                    ("I", "1"),
                    ("L", "1"),
                    ("O", "0"),
                    ("S", "5"),
                    ("T", "7"),
                    ("Z", "2")]
            leet_un = un.upper()
            for char in leet:
                leet_un = leet_un.replace(*char)
            try_name(leet_un)


if __name__ == "__main__":
    username = input("Username(s): ")
    if "," not in username:
        try_name(username, True)
    else:
        names = username.split(", ")
        for name in names:
            try_name(name, True)
