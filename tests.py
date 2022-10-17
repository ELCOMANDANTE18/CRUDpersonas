import unittest
from unittest.mock import patch
from main import persona

class TestPersona(unittest.TestCase):
    def test_constructor(self):
        persona = Persona()
        self.assertEqual(persona._dict_, {'documento':1,'apellido':'Fernandez', 'nombre':'Anabel'})

    @patch('builtins.input', side_effect=[3, 'Trump', 'Donald'])
    def test_input(self, mock_input):
        persona = Persona()
        persona.input()
        self.assertEqual(persona._dict_, {'documento':3,'apellido':'Trump', 'nombre':'Donald'})

if __name__ == '__main__':
    unittest.main()