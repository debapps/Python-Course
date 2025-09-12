from proj.sample_module import add2num
import pytest


class TestAdd2Num:

    def test_sum_2pos_num(self):
      assert add2num(6, 7)==13

    # @pytest.mark.skip('No Reason')
    def test_sum_1pos_and_1neg_num(self):
      assert add2num(-10, 9)==-1

    def test_sum_exception(self):
       with pytest.raises(TypeError):
          add2num(2, '3')