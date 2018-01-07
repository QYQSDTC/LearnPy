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
import re
import time
from multiprocessing.dummy import Pool
from typing import Dict, List, Set, Union

import bs4
import requests as req
from tqdm import tqdm
from xxhash import xxh64

import ujson as json

ARXIV = "https://arxiv.org"
URL = "https://arxiv.org/list/{sub}/new"
TODAY = time.ctime()

subject = re.compile(r"/list/(.+)/new")

PP = Dict[str, Dict[str, Union[str, List[str]]]]


class Arxiv:
    """Arxiv new list crawer."""

    @staticmethod
    def get_subs() -> Set[str]:
        """Get all subs."""
        arxiv = bs4.BeautifulSoup(req.get("https://arxiv.org").content, "lxml")
        lst = arxiv.select("#content li a")
        subs = set()
        for a in lst:
            sj = subject.findall(a.attrs["href"])
            if sj:
                subs.add(sj[0])
        with open("subs", "w") as f:
            f.write("\n".join(subs))
        return subs

    @staticmethod
    def load_olds() -> PP:
        """Load old papers."""
        papers = {}  # type: PP
        if os.path.exists("papers.json"):
            papers = json.load(open("papers.json"))
        return papers

    def __init__(
            self, sub: str = None, update: bool = True, multi: int = 5
    ) -> None:
        """Initialize Arxiv."""
        if os.path.exists("subs"):
            with open("subs") as f:
                self.subs = set(f.read().split("\n")[:-1])
        else:
            self.subs = self.get_subs()

        while sub not in self.subs or not sub:
            print("please input your sub from list:", " ".join(self.subs))
            sub = input("> ")

        self.url = URL.format(sub = sub)
        self.update = update
        self.papers = self.load_olds()  # type: PP
        self.new_papers = set()  # type: Set[str]
        self.multi = multi
        self.downloads = set()  # type: Set[str]

    def save(self) -> None:
        """Save papers' info."""
        with open("papers.json", "w") as f:
            json.dump(self.papers, f, indent = 3)

    def save_new(self) -> None:
        """Save only new papers."""
        with open("papers_new.json", "w") as f:
            papers = {}
            for k, v in self.papers.items():
                if k in self.new_papers:
                    papers[k] = v
            json.dump(papers, f)

    def update_papers(self) -> None:
        """Update subject papers."""
        content = bs4.BeautifulSoup(req.get(self.url).content, "lxml")
        dds, dts = content.select("dl dd"), content.select("dl dt")
        assert len(dds) == len(dts)  # dd, dt must have the same length
        papers = {}
        for dd, dt in zip(dds, dts):
            fn = dt.select("a[title='Abstract']")[0].text
            if xxh64(fn).hexdigest() in self.papers:
                continue
            url = ARXIV + dt.select("a[title='Download PDF']")[0].attrs["href"]
            title = dd.select(".list-title")[0].text.replace("\n", "").replace(
                "Title: ", ""
            )
            author = dd.select(".list-authors")[0].text.replace(
                "\n", ""
            ).replace("Authors: ", "")
            try:
                comment = dd.select(".list-comments")[0].text.replace(
                    "\n", ""
                ).replace("Comments: ", "")
            except IndexError:
                comment = "None"
            subjects = dd.select(".list-subjects")[0].text.replace(
                "\n", ""
            ).replace("Subjects: ", "")
            primary_subject = dd.select(".primary-subject")[0].text
            try:
                abstract = dd.select("p.mathjax")[0].text
            except IndexError:
                cc = bs4.BeautifulSoup(
                    req.get(url.replace("pdf", "abs")).content, "lxml"
                )
                abstract = cc.select(".abstract")[0].text

            papers[xxh64(fn).hexdigest()] = {
                "url": url,
                "title": title,
                "author": author,
                "comment": comment,
                "subjects": subjects,
                "primary subject": primary_subject,
                "abstract": abstract
            }
        if self.papers:
            self.new_papers = set(papers.keys()) & set(self.papers.keys())
        else:
            self.new_papers = set(papers.keys())
        if self.update:
            self.papers.update(papers)
            self.save()

    def download_pdf(self) -> None:
        """Download PDFs."""
        t = tqdm(total = len(self.downloads))
        if not os.path.exists("papers"):
            os.mkdir("papers")

        def multi(hs: str) -> None:
            """Craw it with multiprocessing."""
            res = req.get(str(self.papers[hs]["url"]), stream = True)
            with open(f"papers/{self.papers[hs]['title']}.pdf", "wb") as f:
                for chunk in res.iter_content(chunk_size = 64):
                    f.write(chunk)
            t.update()

        pool = Pool(self.multi)
        pool.map(multi, self.downloads)
        pool.close()
        pool.join()

    def run(self) -> None:
        """Run this crawer."""
        print("updating newest papers")
        self.update_papers()
        self.save_new()


def main() -> None:
    """Yooo, here is the main function."""
    arxiv = Arxiv(sub = "astro-ph")
    arxiv.run()
    print("All papers:")
    for i in arxiv.papers:
        print(
            i,
            arxiv.papers[i]["title"],
            arxiv.papers[i]["abstract"],
            sep = "\n"
        )
    if arxiv.new_papers:
        print("new papers:")
        for i in arxiv.new_papers:
            print(
                i,
                arxiv.papers[i]["title"],
                arxiv.papers[i]["abstract"],
                sep = "\n"
            )
    else:
        print("No new papers")
    print("which paper would you like to download?(c/hash?)")
    ipt = input("> ").lower()
    ta = False
    if ipt != "c" and ipt not in arxiv.papers:
        ta = True
    while ipt in arxiv.papers or ta:
        if ta:
            ta = False
            print("Error! Try again!")
            ipt = input("> ").lower()
            continue
        arxiv.downloads.add(ipt)
        print(ipt, arxiv.papers[ipt]["title"], "and next?(c/hash)?")
        ipt = input("> ").lower()
        if ipt != "c" and ipt not in arxiv.papers:
            ta = True

    arxiv.download_pdf()
    print("see u next time")


if __name__ == "__main__":
    main()
