import unittest
import checkout_system


class TestCheckoutSystem(unittest.TestCase):
    # Given Test Cases
    def test_BOGO(self):
        items = ['CF1', 'CF1']
        result = checkout_system.main(items)
        self.assertEqual(11.23, result)

    def test_CHMK(self):
        # Chai Comes before Milk
        items = ['CH1', 'AP1', 'CF1', 'MK1']
        result = checkout_system.main(items)
        self.assertEqual(20.34, result)

    def test_APPL(self):
        items = ['AP1', 'AP1', 'CH1', 'AP1']
        result = checkout_system.main(items)
        self.assertEqual(16.61, result)

    def test_APOM(self):
        # Apple comes after Oatmeal
        items = ['OM1', 'AP1', 'CH1', 'OM1', 'AP1']
        result = checkout_system.main(items)
        self.assertEqual(16.49, result)

    # Testing Special case functions
    def test_special_case_chai(self):
        # Chai Comes after Milk
        items = ['MK1', 'AP1', 'CF1', 'CH1']
        result = checkout_system.main(items)
        self.assertEqual(20.34, result)

    def test_special_case_oatmeal(self):
        # Apple comes before Oatmeal
        items = ['AP1', 'OM1']
        result = checkout_system.main(items)
        self.assertEqual(6.69, result)


if __name__ == '__main__':
    unittest.main()
