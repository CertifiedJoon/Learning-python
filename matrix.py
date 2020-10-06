from numpy import *

m = array([['Mon',1,2,3,4],['Mon',1,2,3,4],['Mon',1,2,3,4],['Mon',1,2,3,4]])

m_r = append(m, [["Tue",1,2,3,4]], 0)
print(m_r)

m_c = insert(m, [5], [[1],[2],[3],[4]], 1)
print(m_c)

m_dr = delete(m,[2], 0)
print(m_dr)

m_dc = delete(m, s_[2], 1)
print(m_dc)