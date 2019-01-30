import unittest
from picoyplaca import Pico_placa

class TestPicoPlaca(unittest.TestCase):
# This class evaluates the correct function of the algorithm picoyplaca.py
    def test_picoplaca(self):
	# The expected outputs are:
	expected_yes = 'Can be on the road: YES'
	expected_no = 'Can be on the road: NO'
	expected_check = 'Check the given license'
	# Use the function assertEqual to campare equality between funtion output and expected output
	self.assertEqual(str(Pico_placa('PBM4499','lunes','9.59').request()), expected_yes);
	self.assertEqual(str(Pico_placa('AD9','martes','16.59').request()), expected_check);
	self.assertEqual(str(Pico_placa('PKM0891','viernes','10.15').request()), expected_yes);
	self.assertEqual(str(Pico_placa('PRT4592','sabado','12.00').request()), expected_yes);
	self.assertEqual(str(Pico_placa('POK7893','martes','8.45').request()), expected_no);
	self.assertEqual(str(Pico_placa('AFR0504','enero','13.29').request()), expected_check);
	self.assertEqual(str(Pico_placa('GTY0975','a','16.59').request()), expected_check);
	self.assertEqual(str(Pico_placa('HTR3473','martes','22.00').request()), expected_yes);
	self.assertEqual(str(Pico_placa('ADF5677','jueves','17.10').request()), expected_no);
	self.assertEqual(str(Pico_placa('PYR2978','domingo','16.59').request()), expected_yes);
	self.assertEqual(str(Pico_placa('APF0479','viernes','16').request()), expected_no);
	self.assertEqual(str(Pico_placa('KGY0870','miercoles','59').request()), expected_check);

if __name__ == '__main__':
    unittest.main()
