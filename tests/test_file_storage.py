import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.fs = FileStorage()

    def test_new(self):
        self.fs.new(FileStorage())
        self.assertIn('FileStorage', self.fs.__objects.keys())

    def test_save(self):
        with patch('builtins.open', new_callable=StringIO) as mock_open:
            self.fs.new(FileStorage())
            self.fs.save()
            mock_open.assert_called_once_with('file.json', 'w')

    def test_reload(self):
        with patch('builtins.open', new_callable=StringIO) as mock_open:
            mock_open.return_value.write.return_value = '{"FileStorage": {"id": "123"}}'
            self.fs.reload()
            self.assertEqual(len(self.fs.__objects), 1)

    def test_all(self):
        self.fs.new(FileStorage())
        self.fs.all()
        self.assertEqual(len(self.fs.__objects), 1)

    def test_new_existing_object(self):
        obj = FileStorage()
        self.fs.new(obj)
        self.fs.new(obj)
        self.assertEqual(len(self.fs.__objects), 1)

    def test_save_empty_file(self):
        with patch('builtins.open', new_callable=StringIO) as mock_open:
            mock_open.return_value.read.return_value = '{}'
            self.fs.reload()
            self.fs.save()
            mock_open.assert_called_with('file.json', 'w')

    def test_reload_nonexistent_file(self):
        with patch('builtins.open', new_callable=StringIO) as mock_open:
            mock_open.side_effect = FileNotFoundError
            self.fs.reload()
            self.assertEqual(len(self.fs.__objects), 0)

if __name__ == '__main__':
    unittest.main()