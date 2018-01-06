#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              '
    |         =\  -  /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

* author: Nasy
* date: Jan 6, 2017
* email: echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
* file: main.py
* license: MIT

Copyright © 2017 by Nasy. All Rights Reserved.
"""
import os
import time
from multiprocessing.dummy import Pool

import bs4
import requests as req
from tqdm import tqdm

URL = "https://arxiv.org/list/astro-ph/new"
BASE_URL = "https://arxiv.org"
TODAY = time.ctime()

def main() -> None:
    """Yooo, here is the main function."""
    content = bs4.BeautifulSoup(req.get(URL).content, "lxml")
    pdf_paths = content.select(".list-identifier a[title='Download PDF']")
    t = tqdm(total = len(pdf_paths))
    os.mkdir(TODAY)

    def multi(path: bs4.element.Tag) -> None:
        """Craw it multiprocessing."""
        href = BASE_URL + path.attrs["href"]
        with open(path.attrs["href"].replace("/pdf/", TODAY) + ".pdf", "wb") as f:
            f.write(req.get(href).content)
        t.update()

    pool = Pool(5)

    pool.map(multi, pdf_paths)


if __name__ == "__main__":
    main()
