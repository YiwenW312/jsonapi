import unittest
import jsonapi


class test_jsonapi(unittest.TestCase):

    def test_complex_encoder(self):
        complex_num = complex(3, 4)
        encoded = jsonapi.dumps(complex_num)
        expected = '{"__complex__": true, "a": 3.0, "b": 4.0}'
        self.assertEqual(encoded, expected)

    def test_complex_decoder(self):
        json_string = '{"__complex__": true, "a": 3.0, "b": 4.0}'
        decoded = jsonapi.loads(json_string)
        expected = complex(3, 4)
        self.assertEqual(decoded, expected)

    def test_range_serialization_error(self):
        with self.assertRaises(TypeError):
            jsonapi.dumps(range(5))

    def test_dumps_and_loads_integration(self):
        complex_num = complex(5, 6)
        encoded = jsonapi.dumps(complex_num)
        decoded = jsonapi.loads(encoded)
        self.assertEqual(decoded, complex_num)


if __name__ == '__main__':
    unittest.main()
