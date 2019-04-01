from solutions.CHK import checkout_solution
"""
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""
class TestChk():

    def test_invalid_input(self):
        assert checkout_solution.checkout('1') == -1
        assert checkout_solution.checkout('E') == -1

    def test_individual_sku(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15

    def test_special_offers(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('AAAAA') == 230
        assert checkout_solution.checkout('AAAAAA') == 260

    def test_combined(self):
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('ABCBD') == 120

