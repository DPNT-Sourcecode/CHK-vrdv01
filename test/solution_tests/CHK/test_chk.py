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