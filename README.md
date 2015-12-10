pametis - Sitemap Analyzer/Parser
===

The `pametis` package provides a single function, `sitemap`, that iterates over all leaf urls in
a [sitemap](http://sitemaps.org), even if the sitemap is nested and even if the nested sitemaps
are compressed.

Usage is simple:

    from pametis import sitemap

    for url in sitemap( 'http://example.com/sitemap.xml' ):
        ... do something with url ...

`pametis` can be used also as a command line utility, and it will print to stdout all leaf urls:

    $ pametis http://example.com/sitemap.xml

Installation
---

You have several options for installing `pametis`:

- Copy the file `pametis.py` to your project. It is just a single file with no dependencies. Or,

- Install using `pip install pametis`. Or,

- Clone the project from GitHub - `git clone https://github.com/avnr/pametis`.

License
---

MIT License

