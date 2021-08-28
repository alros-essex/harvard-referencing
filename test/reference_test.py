from harvard.collection import Collection
from harvard.reference import BookReference
from harvard.reference import EbookReference
from harvard.reference import VitalsourceReference

import unittest

class TestReference(unittest.TestCase):

    def test_book(self):           
        self.assertEqual(
            "Armstrong, G., Kotler, P. & Opresnik, O. (2016) _Marketing: An Introduction_. 13th ed. Harlow: Pearson Education Limited.",
            BookReference(
                authors = 'Armstrong, G., Kotler, P. & Opresnik, O.',
                year = '2016',
                title = 'Marketing: An Introduction', 
                place = 'Harlow',
                publisher = 'Pearson Education Limited',
                edition = '13th').format_console())

    def test_ebook(self):
        self.assertEqual(
            'Raff, D. & Scranton, P. (2016) _The Emergence of Routines: Entrepreneurship, Organization and Business History_. Oxford: Oxford University Press. Available from: http://0-www.oxfordscholarship.com.serlib0.essex.ac.uk/view/10.1093/acprof:oso/9780198787761.001.0001/acprof-9780198787761# [Accessed 23 May 2018].',
            EbookReference(
                authors = 'Raff, D. & Scranton, P.',
                year = '2016',
                title = 'The Emergence of Routines: Entrepreneurship, Organization and Business History',
                place = 'Oxford',
                publisher = 'Oxford University Press',
                url = 'http://0-www.oxfordscholarship.com.serlib0.essex.ac.uk/view/10.1093/acprof:oso/9780198787761.001.0001/acprof-9780198787761#',
                last_access = '23 May 2018').format_console())
        
    def test_vitalsource(self):
        self.assertEqual(
            'Tosey, P. & Gregory, J. (2001) _Dictionary of Personal Development_. Brisbane: Wiley Blackwell. Available via the Vitalsource Bookshelf. [Accessed 23 May 2018].',
            VitalsourceReference(
                authors = 'Tosey, P. & Gregory, J.',
                year = '2001',
                title = 'Dictionary of Personal Development',
                place= 'Brisbane',
                publisher = 'Wiley Blackwell',
                last_access = '23 May 2018').format_console())