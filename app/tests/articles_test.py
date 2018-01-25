import unittest
from app.models import Articles

class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Article class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_article = Articles('BBC News','EU acts against Poland judiciary reforms', 'Unprecedented disciplinary measures are taken as the EU says the reforms threaten the rule of law.', 'https://ichef.bbci.co.uk/news/1024/cpsprodpb/F046/production/_98901516_2efffed4-d4a6-486a-8a78-112232b92faa.jpg','http://www.bbc.co.uk/news/world-europe-42420150', '2017-12-20T13:36:14Z')

    def test_instance(self):
        '''
        Test case to check if self.new_article is an instance of Article
        '''
        self.assertTrue( isinstance( self.new_article, Articles ) )
