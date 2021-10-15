"""
1. Given a text finding the number of times a numerical digit (0-9) appeared
2. Finding what all are those numerical values

sample text source courtesy : https://www.lipsum.com/
"""

import re

text = """ The standard chunk of Lorem Ipsum used since the 1500s is 
reproduced below for those interested. Sections 1.10.32 and 1.10.33 
from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in 
their exact original form, accompanied by English versions from the 1914 
translation by H. Rackham.
"""

count_numerical_digits = len(re.sub(r"\D", "", text))

show_numerical_digits = re.findall(r"\d[\.,-]?\d+[\.,-]?\d+", text)

print("Extracted numerical text is :", show_numerical_digits)

print("Numerical number count is :", count_numerical_digits)
