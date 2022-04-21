from main_querry import *
from intersection import *
import unittest


class TestBooleanQuery(unittest.TestCase):
    path = 'C:/Users/alies/PycharmProjects/Insk/Assignment1/Resources/'
    test_dictionary = make_dic_postings(path)
    test_q1 = test_dictionary['baby']
    test_q2 = test_dictionary['mother']
    inters = Intersection(test_q1, test_q2)

    def test_boolean_and(self):
        self.assertEqual(self.inters.intersect_and(), ['BleakHouseFullBookSummarySparkNotes.txt', 'Midnight’sChildrenFullBookSummarySparkNotes.txt'])

    def test_boolean_or(self):
        self.assertEqual(self.inters.intersect_or(), {'AllQuietontheWesternFrontFullBookSummarySparkNotes.txt', 'EthanFromeFullBookSummarySparkNotes.txt', 'HarryPotterandTheOrderofthePhoenixFullBookSummarySparkNotes.txt', 'HarryPotterandtheHalfBloodPrinceFullBookSummarySparkNotes.txt', 'TheAmericanFullBookSummarySparkNotes.txt', 'HarryPotterandtheSorcerer’sStoneFullBookSummarySparkNotes.txt', 'BleakHouseFullBookSummarySparkNotes.txt', 'HarryPotterandtheGobletofFireFullBookSummarySparkNotes.txt', 'OneFlewOvertheCuckoo’sNestFullBookSummarySparkNotes.txt', 'TheKitchenGodsWifeFullBookSummarySparkNotes.txt', 'BridesheadRevisitedFullBookSummarySparkNotes.txt', 'DivergentFullBookSummarySparkNotes.txt', 'DuneFullBookSummarySparkNotes.txt', 'Midnight’sChildrenFullBookSummarySparkNotes.txt', 'HarryPotterandtheDeathlyHallowsFullBookSummarySparkNotes.txt', 'DiaryofaWimpyKidFullBookSummarySparkNotes.txt', 'FlowersforAlgernonFullBookSummarySparkNotes.txt'})

    def test_boolean_not(self):
        self.assertEqual(self.inters.intersect_not(), {'HarryPotterandtheSorcerer’sStoneFullBookSummarySparkNotes.txt'})