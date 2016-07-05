
import six
import types
import unittest
from a2m.itertools import isplit


class ISplitFailureTestCase(unittest.TestCase):
    '''
    Test :py:func:`isplit` for failures.
    '''
    def test_text_typeerror(self):
        '''should raise a TypeError if called with non-string ``text``.'''
        non_string_value = 100500

        with self.assertRaises(TypeError) as cm:
            next(isplit(non_string_value))

        self.assertEqual(cm.exception.args[0], 'a string is expected')

    def test_maxsplit_typeerror(self):
        '''should raise a TypeError if called with non-integer ``maxsplit``.'''
        with self.assertRaises(TypeError) as cm:
            next(isplit('lorem ipsum', maxsplit='non-integer-value'))

        self.assertEqual(cm.exception.args[0],
                         '``maxpsplit``: an integer is required')

    def test_sep_typeerror(self):
        '''should raise a TypeError if called with non-string ``sep``.'''
        non_string_value = 100500

        with self.assertRaises(TypeError) as cm:
            next(isplit('lorem ipsum', non_string_value))

        self.assertEqual(cm.exception.args[0],
                         '``sep`` parameter must be a string or None')

    def test_sep_valueerror(self):
        '''should raise a ValueError if ``sep`` is empty string.'''
        with self.assertRaises(ValueError) as cm:
            next(isplit('lorem ipsum', ''))

        self.assertEqual(cm.exception.args[0], '``sep``: empty separator')


class ISplitSuccessTestCase(unittest.TestCase):
    '''
    Test :py:func:`isplit` for success.
    '''
    def test_return_type(self):
        '''should return generator iterator'''
        self.assertIsInstance(isplit('lorem ipsum'), types.GeneratorType)

    def test_empty_source_null_sep(self):
        ('should return empty sequence '
         'when given string is empty and ``sep`` is None')

        t = tuple(isplit(''))
        self.assertSequenceEqual(t, [])

    def test_empty_text_non_null_sep(self):
        ('should wrap empty string into single-item sequence '
         'if ``sep`` is not None')

        t = tuple(isplit('', 'some-separator'))
        self.assertSequenceEqual(t, [''])

    def test_strsplit_result_equality(self):
        '''should return the same sequences as str.split() does'''
        DATA = [

            [
                ('lorem ipsum dolor sit amet',),
                ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
            ],

            [
                (' lorem   ipsum\tdolor sit amet\t',),
                ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
            ],

            [
                (' lorem   ipsum\tdolor sit amet\t', None, 0),
                ['lorem   ipsum\tdolor sit amet\t']
            ],

            [
                (' lorem \r  ipsum \ndolor sit amet\t', None, 2),
                ['lorem', 'ipsum', 'dolor sit amet\t']
            ],

            [
                ('Programming Language :: Python :: 2.7', '::'),
                ['Programming Language ', ' Python ', ' 2.7']
            ],

            [
                ('Programming Language :: Python :: 3.4', '::', 1),
                ['Programming Language ', ' Python :: 3.4']
            ],

            [
                ('aaaaa', 'aa'),
                ['', '', 'a']
            ],

            [
                ('aaa', 'aaaa'),
                ['aaa']
            ],

            [
                ('aaaaa', 'aa', 1),
                ['', 'aaa']
            ]

        ]
        strsplit = str.split
        text = six.text_type
        for input_, output_ in DATA:
            seq = strsplit(*input_)
            iseq = list(isplit(*input_))
            self.assertSequenceEqual(iseq, seq)
            self.assertSequenceEqual(iseq, list(map(text, output_)))
