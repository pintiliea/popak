import unittest
import pathlib
import popak_installer as pi


class TestPopakInstaller(unittest.TestCase):
    def test_backup(self):
        f = open(TEST_FILE, 'w')  # create a file
        pi.backup(f.name)  # backup the file
        # check that the backup file now exists
        test_bak = pathlib.Path(pi.name_backup_file(TEST_FILE))
        self.assertTrue(test_bak.is_file(), "expected backup file '" + test_bak.name + "' to exist but it's missing")
        # backup the file again and check that test_file.backup2 exists
        # test_bak = pathlib.Path(pi.name_backup_file(TEST_FILE))

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


TEST_FILE = 'test_file'

if __name__ == '__main__':
    unittest.main()
