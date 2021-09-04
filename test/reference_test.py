from harvard.collection import Collection
from harvard.reference_book import BookReference
from harvard.reference_ebook import EbookReference
from harvard.reference_chapter import ChapterEditedBookReference
from harvard.reference_vitalsource import VitalsourceReference
from harvard.reference_journal import ArticleReference
from harvard.reference_journal_online import ArticleOnlineReference
from harvard.reference_website import WebsiteReference
from harvard.reference_newspaper import ArticleNewpaperReference
from harvard.reference_electronic_newspaper import ArticleElectronicNewpaperReference
from harvard.reference_research import ResearchReportReference
from harvard.reference_research_online import ResearchReportOnlineReference
from harvard.reference_conference import ConferencePapersReference
from harvard.reference_correspondence import CorrespondenceReference
from harvard.reference_lecture import LectureReference
from harvard.reference_un_resolution import UNResolutionReference
from harvard.reference_treaty import TreatyReference

import unittest

class TestReference(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.maxDiff = None

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

    def test_journal(self):
        self.assertEqual('Backhaus, K., Mell, B. & Sabel, T. (2007) Business-to-Business Marketing Textbooks: A Comparative Review. \x1B[3mJournal of Business-to-Business Marketing\x1B[0m 14(4): 11-65.',
        ArticleReference(
            authors = 'Backhaus, K., Mell, B. & Sabel, T.',
            year = '2007',
            title = 'Business-to-Business Marketing Textbooks: A Comparative Review',
            journal = 'Journal of Business-to-Business Marketing',
            volume= '14',
            issue = '4',
            pages = '11-65'
        ).format_console())

    def test_journal_online(self):
        self.assertEqual('Kilpatrick, C., Saito, H., Allegranzi, B. & Pittet, D. (2018) Preventing sepsis in health care – It’s in your hands: A World Health Organization call to action. \x1B[3mJournal of Infection Prevention\x1B[0m 19(3): 104-106. DOI: https://doi.org/10.1177%2F1757177418769146',
        ArticleOnlineReference(
            authors = 'Kilpatrick, C., Saito, H., Allegranzi, B. & Pittet, D.',
            year = '2018',
            title = 'Preventing sepsis in health care – It’s in your hands: A World Health Organization call to action',
            journal = 'Journal of Infection Prevention',
            volume= '19',
            issue = '3',
            pages = '104-106',
            doi = 'https://doi.org/10.1177%2F1757177418769146'
        ).format_console())

    def test_journal_online2(self):
        self.assertEqual('Kilpatrick, C., Saito, H., Allegranzi, B. & Pittet, D. (2018) Preventing sepsis in health care – It’s in your hands: A World Health Organization call to action. \x1B[3mJournal of Infection Prevention\x1B[0m 19(3): 104-106. Available from: https://doi.org/10.1177%2F1757177418769146 [Accessed 01 Sep. 2021]',
        ArticleOnlineReference(
            authors = 'Kilpatrick, C., Saito, H., Allegranzi, B. & Pittet, D.',
            year = '2018',
            title = 'Preventing sepsis in health care – It’s in your hands: A World Health Organization call to action',
            journal = 'Journal of Infection Prevention',
            volume= '19',
            issue = '3',
            pages = '104-106',
            url = 'https://doi.org/10.1177%2F1757177418769146',
            accessed = '01 Sep. 2021'
        ).format_console())

    def test_website(self):
        self.assertEqual('Tobak, S. (2015) 15 Business Tips Every Entrepreneur Should Know. Available from: https://www.entrepreneur.com/article/253143 [Accessed 30 July 2018].',
        WebsiteReference(
            authors = 'Tobak, S.',
            year = '2015',
            title = '15 Business Tips Every Entrepreneur Should Know',
            url = 'https://www.entrepreneur.com/article/253143',
            accessed = '30 July 2018'
        ).format_console())

    def test_website(self):
        self.assertEqual('Wood, Z. (May 23, 2018) Marks & Spencer reports sharp drop in annual profits. \x1B[3mThe Guardian\x1B[0m.',
        ArticleNewpaperReference(
            authors = 'Wood, Z.',
            year = 'May 23, 2018',
            title = 'Marks & Spencer reports sharp drop in annual profits',
            newspaper = 'The Guardian'
        ).format_console())

    def test_website2(self):
        self.assertEqual('Wood, Z. (May 23, 2018) Marks & Spencer reports sharp drop in annual profits. \x1B[3mThe Guardian\x1B[0m. 1-2.',
        ArticleNewpaperReference(
            authors = 'Wood, Z.',
            year = 'May 23, 2018',
            title = 'Marks & Spencer reports sharp drop in annual profits',
            newspaper = 'The Guardian',
            pages = '1-2'
        ).format_console())

    def test_electronic_newspaper(self):
        self.assertEqual('Davis, K. (May 23, 2018) Ready for GDPR? 5 Tips for Marketing Leaders. \x1B[3mForbes\x1B[0m. Available from: https://www.forbes.com/sites/forbescontentmarketing/2018/05/23/ready-for-gdpr-5-tips-for-marketing-leaders/#367991b0c2af [Accessed 24 May 2018].',
        ArticleElectronicNewpaperReference(
            authors = 'Davis, K.',
            year = 'May 23, 2018',
            title = 'Ready for GDPR? 5 Tips for Marketing Leaders',
            newspaper = 'Forbes',
            url = 'https://www.forbes.com/sites/forbescontentmarketing/2018/05/23/ready-for-gdpr-5-tips-for-marketing-leaders/#367991b0c2af',
            accessed = '24 May 2018'
        ).format_console())

    def test_electronic_newspaper2(self):
        self.assertEqual('Davis, K. (May 23, 2018) Ready for GDPR? 5 Tips for Marketing Leaders. \x1B[3mForbes\x1B[0m. 1-2. Available from: https://www.forbes.com/sites/forbescontentmarketing/2018/05/23/ready-for-gdpr-5-tips-for-marketing-leaders/#367991b0c2af [Accessed 24 May 2018].',
        ArticleElectronicNewpaperReference(
            authors = 'Davis, K.',
            year = 'May 23, 2018',
            title = 'Ready for GDPR? 5 Tips for Marketing Leaders',
            newspaper = 'Forbes',
            url = 'https://www.forbes.com/sites/forbescontentmarketing/2018/05/23/ready-for-gdpr-5-tips-for-marketing-leaders/#367991b0c2af',
            accessed = '24 May 2018',
            pages = '1-2'
        ).format_console())

    def test_report(self):
        self.assertEqual('Dye, C. et al. (2013) \x1B[3mResearch for universal health coverage: World health report 2013\x1B[0m. Luxembourg: World Health Organization.',
        ResearchReportReference(
            authors = 'Dye, C. et al.',
            year = '2013',
            title = 'Research for universal health coverage: World health report 2013',
            place = 'Luxembourg',
            publisher = 'World Health Organization'
        ).format_console())

    def test_report_online(self):
        self.assertEqual('Bradshaw, J. et al. (2013) \x1B[3mA minimum income standard for Britain: what people think\x1B[0m. Available from: http://www.jrf.org.uk/sites/files/jrf/2226-income-poverty-standards.pdf [Accessed 24 May 2018].',
        ResearchReportOnlineReference(
            authors = 'Bradshaw, J. et al.',
            year = '2013',
            title = 'A minimum income standard for Britain: what people think',
            url = 'http://www.jrf.org.uk/sites/files/jrf/2226-income-poverty-standards.pdf',
            accessed = '24 May 2018'
        ).format_console())

    def test_conference(self):
        self.assertEqual('Cook, D. (2000) \'Developing franchised business in Scotland\', \x1B[3mSmall firms: adding the spark: the 23rd ISBA national small firms policy and research conference\x1B[0m. Robert Gordon University, Aberdeen, 15–17 November. Leeds: Institute for Small Business Affairs. 127–136.',
        ConferencePapersReference(
            authors = 'Cook, D.',
            year = '2000',
            title = 'Developing franchised business in Scotland',
            conference_title = 'Small firms: adding the spark: the 23rd ISBA national small firms policy and research conference',
            conference_date = '15–17 November',
            conference_location = 'Robert Gordon University, Aberdeen',
            place = 'Leeds',
            publisher = 'Institute for Small Business Affairs',
            pages = '127–136'
        ).format_console())

    def test_conference2(self):
        self.assertEqual('Cook, D. (2000) \'Developing franchised business in Scotland\', \x1B[3mSmall firms: adding the spark: the 23rd ISBA national small firms policy and research conference\x1B[0m. Robert Gordon University, Aberdeen, 15–17 November. Leeds: Institute for Small Business Affairs.',
        ConferencePapersReference(
            authors = 'Cook, D.',
            year = '2000',
            title = 'Developing franchised business in Scotland',
            conference_title = 'Small firms: adding the spark: the 23rd ISBA national small firms policy and research conference',
            conference_date = '15–17 November',
            conference_location = 'Robert Gordon University, Aberdeen',
            place = 'Leeds',
            publisher = 'Institute for Small Business Affairs'
        ).format_console())

    def test_correspondence(self):
        self.assertEqual('Walters, F. (2018) Conversation with John Stephens, 13 August.',
        CorrespondenceReference(
            authors = 'Walters, F.',
            year = '2018',
            title = 'Conversation with John Stephens',
            date = '13 August'
        ).format_console())

    def test_lecture(self):
        self.assertEqual('Smith, J. (2018) \x1B[3mMSc BS Lecturecast 1\x1B[0m [Lecturecast]. MBS JUNE 2018 Business Strategy June 2018. University of Essex Online.',
        LectureReference(
            authors = 'Smith, J.',
            year = '2018',
            title = 'MSc BS Lecturecast 1',
            format = 'Lecturecast',
            module = 'mbs june 2018',
            module_title = 'Business Strategy June 2018',
            organization = 'University of Essex Online'
        ).format_console())

    def test_un_resolution(self):
        self.assertEqual('United Nations General Assembly (1994) \x1B[3mUnited Nations framework convention on climate change\x1B[0m. Resolution A/RES/48/189. Available from: http://daccess-dds-ny.un.org/doc/UNDOC/GEN/N94/036/43/PDF/N9403643.pdf?OpenElement [Accessed 15 September 2015].',
        UNResolutionReference(
            general_assembly=True,
            year = '1994',
            title = 'United Nations framework convention on climate change',
            resolution_number = '48/189',
            url = 'http://daccess-dds-ny.un.org/doc/UNDOC/GEN/N94/036/43/PDF/N9403643.pdf?OpenElement',
            accessed = '15 September 2015'
        ).format_console())

    def test_treaty(self):
        self.assertEqual('Convention relating to the status of refugees (1951) Treaty no. 2545. \x1B[3mUnited Nations Treaty Series\x1B[0m, 189: 137-221. Available from: https://treaties.un.org/doc/Publication/UNTS/Volume%20189/v189.pdf [Accessed 17 September 2015].',
        TreatyReference(
            year = '1951',
            title = 'Convention relating to the status of refugees',
            treaty_number = '2545',
            publication_title = 'United Nations Treaty Series',
            volume = '189',
            pages = '137-221',
            url = 'https://treaties.un.org/doc/Publication/UNTS/Volume%20189/v189.pdf',
            accessed = '17 September 2015'
        ).format_console())