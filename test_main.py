import unittest
import csv
from main import Worker
test_data_file_path = '/home/punit/PycharmProjects/pythonProject1/Workerinformation.csv'
test_data_file_object = None
test_data_row_list = list()
def load_test_data():
    global test_data_file_object, test_data_row_list
    test_data_file_object = open(test_data_file_path,'r')
    csv_reader = csv.reader(test_data_file_object, delimiter=',')
    for row in csv_reader:
        test_data_row_list.append(row)
    print('open and load data from Workerinformation.csv complete.')

class TestWorker(unittest.TestCase):

    def testAdd_Employ(self):
        print('')
        print('*************Insert_test***************')
        for row in test_data_row_list:

            expected_result = row[6]
            result = self.worker.Add_Employ()
            self.assertEqual(result, expected_result)
    def testAdd1_Employ(self):
        print('')
        print("**************Negative Test Case****************")
        for row in test_data_row_list:
            if row not in test_data_row_list:
                expected1_result = row
            result = self.Worker.Add_Employ()
            self.assertNotEqual(result, expected1_result)
    def testAdd2_Employ(self):
        for row in test_data_row_list:
            self.assertEqual(self.Worker.Add_Employ(), row[1])
    def testAdd3_Employ(self):
        for row in test_data_row_list:
            if row == None:
                self.assertNotEqual(self.Worker.Add_Employ(), None)
    def testSearch(self):
        for row in test_data_row_list:
            if row not in test_data_row_list:
                self.assertNotEqual(self.worker.Search(), "row")
    def testSearch1(self):
        for row in test_data_row_list:
            self.assertEqual(self.worker.Search(), sel.worker.Add_Employ())
    def testsearch(self):
        for row in test_data_row_list:
            self.assertEqual(self.worker.Add_Employ(name), row[0])
    def testUpdate1(self):
        for row in test_data_row_list :
            self.assertNotEqual(self.worker.Update(), row[1])
    def testUpdate(self):
        for row in test_data_row_list:
            self.assertEqual(self.worker.update(), row)
    def testDelete1(self):
        for row in test_data_row_list:
            self.assertNotEqual(self.worker.Add_employ(), row)
    def testDelete(self):
        for row in test_data_row_list:
            self.assertEqual(self.worker.Delete(), row)


            


if __name__ == '__main__':
    unittest.main()
if __name__ == '__main__' :
    unittest.main()


