pametis - Sitemap Analyzer/Parser/Iterator
===

The `pametis` package provides a single function, `sitemap`, that iterates over all leaf urls in
a [sitemap](http://sitemaps.org), even if the sitemap is nested and even if the nested sitemaps
are compressed.

Usage is simple:

    from pametis import sitemap

    for url in sitemap( 'http://example.com/sitemap.xml' ):
        print( url, url.lastmod, url.changefreq, url.priority )

The url can be used as a regular string. In addition it has three attributes, `lastmod`, `changefreq` and
`priority`, which correspond with their respective value in the sitemap, or `None` for any value not
provided by the sitemap.

`pametis` can be used also as a command line utility, and it will print to stdout all leaf urls:

    $ pametis http://example.com/sitemap.xml

Or, if installed on the module path:

    $ python -m pametis http://example.com/sitemap.xml

Installation
---

There are several options for installing `pametis`:

- Copy the file `pametis.py` to your project. It is just a single file with no dependencies. Or,

- Install using `pip install pametis`. Or,

- Clone the project from GitHub - `git clone https://github.com/avnr/pametis`.

License
---

MIT License


Revisions History:
---

Version 0.3, 2015-12-14:

- Return per leaf the lastmod, changefreq and priority attributes

- Change sitemap proccessing to ignore namespaces, thus increasing speed, reducing memory footprint, reducing code complexity

