import cm1k
import random
import unittest

class TestCM1K(unittest.TestCase):
    def test_category(self):
        cm = cm1k.CM1K()
        random.random()
        category = random.randint(1, 0x7FFE)

        cm.write(cm1k.REG_NSR, 0x10)
        cm.write(cm1k.REG_TESTCAT, category)

        cm.write(cm1k.REG_RESETCHAIN)
        n_count = 0
        while True:
            cat = cm.read(cm1k.REG_CAT)
            if cat == 0xFFFF:
                self.assertEqual(n_count, 1024)
                break
            self.assertEqual(cat, category)
            n_count += 1

if __name__ == '__main__':
    unittest.main()
