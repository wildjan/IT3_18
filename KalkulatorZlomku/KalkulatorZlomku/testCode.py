"""
Zde otestujte funkcnost vasich magickych metod
"""

from zlomky import Zlomek

# Test
zl1 = Zlomek(0, 1)
zl2 = Zlomek()
add = zl1 + zl2
sub = zl1 - zl2
mul = zl1 * zl2
div = zl1 / zl2

print "%s + %s = %s" %(zl1, zl2, add)
print "%s - %s = %s" %(zl1, zl2, sub)
print "%s * %s = %s" %(zl1, zl2, mul)
print "%s / %s = %s" %(zl1, zl2, div)