import cm1k
import random
import unittest

class TestCM1K(unittest.TestCase):
    def test_category(self):
        cm1k = cm1k.CM1K()
        random.random()
        category = random.randint(1, 0x7FFE)

        cm1k.write(REG_NSR, 0x10)
        cm1k.write(REG_CAT, category)

        cm1k.write(REG_RESETCHAIN)
        n_count = 0
        while True:
            cat = cm1k.read(REG_CAT)
            if cat == 0xFFFF:
                self.assertEqual(n_count, 1024)
                break
            self.assertEqual(cat, category)
            n_count += 1

if __name__ == '__main__':
    unittest.main()
