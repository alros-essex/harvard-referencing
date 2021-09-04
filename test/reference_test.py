from harvard.collection import Collection
from harvard.reference import *

import unittest

class TestReference(unittest.TestCase):

    def test_book(self):           
        self.assertEqual(
            "Armstrong, G., Kotler, P. & Opresnik, O. (2016) \x1B[3mMarketing: An Introduction\x1B[0m. 13th ed. Harlow: Pearson Education Limited.",
            BookReference(
                authors = 'Armstrong, G., Kotler, P. & Opresnik, O.',
                year = '2016',
                title = 'Marketing: An Introduction', 
                place = 'Harlow',
                publisher = 'Pearson Education Limited',
                edition = '13th').format_console())

    def test_ebook(self):
        self.assertEqual(
            'Raff, D. & Scranton, P. (2016) \x1B[3mThe Emergence of Routines: Entrepreneurship, Organization and Business History\x1B[0m. Oxford: Oxford University Press. Available from: http://0-www.oxfordscholarship.com.serlib0.essex.ac.uk/view/10.1093/acprof:oso/9780198787761.001.0001/acprof-9780198787761# [Accessed 23 May 2018].',
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
            'Tosey, P. & Gregory, J. (2001) \x1B[3mDictionary of Personal Development\x1B[0m. Brisbane: Wiley Blackwell. Available via the Vitalsource Bookshelf. [Accessed 23 May 2018].',
            VitalsourceReference(
                authors = 'Tosey, P. & Gregory, J.',
                year = '2001',
                title = 'Dictionary of Personal Development',
                place= 'Brisbane',
                publisher = 'Wiley Blackwell',
                last_access = '23 May 2018').format_console())

    def test_chapter_edited_book(self):
        self.assertEqual('Malunguza, N., Dube, S., Tchuenche, J., Hove-Musekwa, S. & Mukandavire, Z. (2009) \'Two Strain HIV/AIDS Model and the Effects of Superinfection\', in: Tchuenche, J. & Mukandavire, Z. (eds) Advances in Disease Epidemiology. Hauppauge: Nova Science Publishers.171-195.',
        ChapterEditedBookReference(
            authors = 'Malunguza, N., Dube, S., Tchuenche, J., Hove-Musekwa, S. & Mukandavire, Z.',
            year = '2009',
            title = 'Two Strain HIV/AIDS Model and the Effects of Superinfection',
            original_authors = 'Tchuenche, J. & Mukandavire, Z.',
            original_title = 'Advances in Disease Epidemiology',
            place = 'Hauppauge',
            publisher = 'Nova Science Publishers',
            pages = '171-195'
        ).format_console())
