import pyperclip
from cssselect import GenericTranslator, HTMLTranslator

# https://lxml.de/xpathxslt.html: "lxml supports XPath 1.0 (...)"
# https://cssselect.readthedocs.io/en/latest/: "(...) parse CSS3 selectors and translate them to XPath 1.0 expressions."
if __name__ == "__main__":
    css_selector = "table.dataframe"

    generic_expression = GenericTranslator().css_to_xpath(css_selector)
    html_expression = HTMLTranslator().css_to_xpath(css_selector)

    print("Via GenericTranslator:", generic_expression)
    print("Via HTMLTranslator:", html_expression)

    pyperclip.copy(html_expression)
