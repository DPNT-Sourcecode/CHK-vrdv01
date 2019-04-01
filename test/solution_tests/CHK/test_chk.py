from solutions.CHK import checkout_solution
"""
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+"""
class TestChk():

    def test_invalid_input(self):
        assert checkout_solution('1') == -1
        assert checkout_solution('E') == -1

    def test_individual_sku(self):
        assert checkout_solution('A') == 50
        assert checkout_solution('B') == 30
        assert checkout_solution('C') == 20
        assert checkout_solution('D') == 15

    def test_special_offers(self):
        assert checkout_solution('AAA') == 130
        assert checkout_solution('BB') == 45
        assert checkout_solution('AAAA') == 180
        assert checkout_solution('AAAAA') == 230
        assert checkout_solution('AAAAAA') == 260