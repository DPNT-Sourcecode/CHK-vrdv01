from solutions.HLO import hello_solution


class TestHlo():
    def test_hlo(self):
        assert hello_solution.hello("Peter") == "Hello, Peter!"
