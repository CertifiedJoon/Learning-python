from collections import defaultdict
import pysnooper
@pysnooper.snoop()
def build_order(dependencies, projects):
    mapped = defaultdict(list)
    STATUS_STARTED = 1
    STATUS_FINISHED = 2
    order = []
    for prerequisite, eligible in dependencies:
        mapped[prerequisite].append(eligible)
    
    statuses = {}
    for project in projects:
        to_visit = [project]
    
        while to_visit:
            v = to_visit.pop()
            if v in statuses:
                if statuses[v] == STATUS_STARTED:
                    statuses[v] = STATUS_FINISHED
                    order.append(v)
            else:
                statuses[v] = STATUS_STARTED
                to_visit.append(v)
            
            for eligible in mapped.get(v, []):
                if eligible in statuses:
                    if statuses[eligible] == STATUS_STARTED:
                        return None
                else:
                    to_visit.append(eligible)
                    
    order.reverse()
    return order


if __name__ == "__main__":
    dependencies = [('a','d'), ('f','b'), ('b','d'), ('f', 'a'), ('d','c'), ('c', 'a')]
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    print(build_order(dependencies, projects))