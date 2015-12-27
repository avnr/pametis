from pametis import sitemap

for url in sitemap( 'https://raw.githubusercontent.com/avnr/pametis/master/test/sm10.xml' ):
    print( url )