def check_kth_power(n1, k1):
        while n1%k1 == 0:
            n1 = n1/k1

        if n1 != 1:
            return False
        return True


print check_kth_power(128, 5)

