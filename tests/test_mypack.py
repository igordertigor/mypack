from mypack import super_sum


class TestSuperSum:
    def test_5_and_1_is_6(self):
        assert super_sum(5, 1) == 6

    def test_2_and_3_is_5(self):
        assert super_sum(2, 3) == 5

    def test_cummutes(self):
        assert super_sum(2, 3) == super_sum(3, 2)

    def test_only_single_number(self):
        assert super_sum(1) == 1
