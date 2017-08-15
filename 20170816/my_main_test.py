# python 3.5.2

from unittest.mock import patch

import my_main


class TestFunction:
    def test(self):
        assert my_main.function('Python') == 'My Python'

    def test_patch_return_value(self):
        with patch('my_class.MyClass.my_method') as mock:
            mock.return_value = 'Hi! Perl'
            assert my_main.function('Python') == 'Hi! Perl'

    def test_patch_side_effect(self):
        with patch('my_class.MyClass.my_method') as mock:
            mock.side_effect = lambda x: 'OLA! {}'.format(x)
            assert my_main.function('Python') == 'OLA! Python'

    def test_called(self):
        with patch('my_class.MyClass.my_method') as mock:
            my_main.function('Python')

        assert mock.called
        assert mock.call_count == 1
        mock.assert_called_with('Python')
