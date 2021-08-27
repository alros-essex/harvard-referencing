from harvard.reference import Reference

import unittest

class TestReference(unittest.TestCase):

    def test_book(self):
        ref = Reference.new_book("My User", "My Collection")          \
            .with_authors('Armstrong, G., Kotler, P. & Opresnik, O.') \
            .with_year('2016')                                        \
            .with_title('Marketing: An Introduction')                 \
            .with_edition('13th')                                     \
            .with_place_of_publication('Harlow')                      \
            .with_publisher('Pearson Education Limited')              \
            .build()
            
        self.assertEqual(
            "<span>Armstrong, G., Kotler, P. & Opresnik, O. (2016) <i>Marketing: An Introduction</i>. 13th ed. Harlow: Pearson Education Limited.</span>",
            ref.format_html())

    def test_ebook(self):
        ref = Reference.new_ebook("My User", "My Collection")                                            \
            .with_authors('Raff, D. & Scranton, P.')                                                     \
            .with_year('2016')                                                                           \
            .with_title('The Emergence of Routines: Entrepreneurship, Organization and Business History') \
            .with_place_of_publication('Oxford')                                                         \
            .with_publisher('Oxford University Press')                                                   \
            .with_available_from_url('http://0-www.oxfordscholarship.com.serlib0.essex.ac.uk/view/10.1093/acprof:oso/9780198787761.001.0001/acprof-9780198787761#')\
            .with_date_of_access('23 May 2018')                                                          \
            .build()

        self.assertEqual(
            '<span>Raff, D. & Scranton, P. (2016) <i>The Emergence of Routines: Entrepreneurship, Organization and Business History</i>. Oxford: Oxford University Press. Available from: <a href="http://0-www.oxfordscholarship.com.serlib0.essex.ac.uk/view/10.1093/acprof:oso/9780198787761.001.0001/acprof-9780198787761#">http://0-www.oxfordscholarship.com.serlib0.essex.ac.uk/view/10.1093/acprof:oso/9780198787761.001.0001/acprof-9780198787761#</a> [Accessed 23 May 2018].</span>',
            ref.format_html())
        