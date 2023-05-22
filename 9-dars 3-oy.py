# class C:
#     pass

# class A:
#     pass

# class B:
#     pass
# class D:
#     pass

# class E:
#     pass

# class K1(C,A,B):
#     pass

# class K3(A,D):
#     pass

# class K2(B,D,E):
#     pass

# class Z(K1,K3,K2):
#     pass
# a=Z.mro()
# print(a)

# class D:
#     pass

# class E:
#     pass

# class F:
#     pass

# class B(D,E):
#     pass

# class C(D,F):
#     pass

# class A(B,C):
#     pass

# a=A.mro()
# print(a)

# class H:
#     pass

# class G:
#     pass

# class F:
#     pass

# class E (H):
#     pass

# class C (G):
#     pass

# class D(F):
#     pass

# class B (C,H):
#     pass

# class A (D,E,B):
#     pass

# a=A.mro()
# print(a)

class A:
    pass


class B:
    pass


class C(A, B):
    pass


class D(C, B):
    pass


a = D.mro()
print(a)




