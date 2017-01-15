class AP(object):
    def __init__(self,prvni, diference):
        self.prvni = prvni
        self.diference = diference
    
    def __str__(self):
        return "AP({0}, {1})".format(self.prvni, self.diference)

    def a(self, n):
        return self.prvni + (n - 1) * self.diference

    def s(self, n):
        return (self.prvni + self.a(n)) * n / 2 

# Test
ap = AP(2, 5)
print ap

print ap.a(8), ap.a(13)