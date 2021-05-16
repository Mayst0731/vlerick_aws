from pprint import pprint

import tabula
import requests
import io
import pandas as pd

url = 'https://www.gibs.co.za/Documents/Executive%20Education%20Short%20Courses.pdf'
page = requests.get(url).content
with io.BytesIO(page) as f:
    df = tabula.read_pdf(f,multiple_tables=True,pages=1)
    # print(df)
    print(type(df))


for item in df:
    if not item.empty:
        header = item.head()
        print(header)
