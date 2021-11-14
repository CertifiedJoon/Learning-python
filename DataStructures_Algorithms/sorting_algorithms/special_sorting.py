class _Item:
    __slots__ = '_key', 'element'
    def __init__(self, key, element):
        self._key = key
        self._element = element

def deco_sort(data, key=None):
    if k is not None:
        for i in range(len(data)):
            data[i] = _Item(key(data[i]), data[j])
    merge_sort(data)
    if k is not None:
        for i in range(len(data)):
            data[i] = data[i]._element