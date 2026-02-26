from collections import OrderedDict
import bisect

class SummaryRanges:

    def __init__(self):
        self.intervals = OrderedDict() # key: start, value: list[start,end]

    def addNum(self, value: int) -> None:
        # binary search for the first equal/larger than value
        keys = list(self.intervals.keys())
        if len(keys) == 0:
            self.intervals[value] = [value, value]
            return            
        idx = bisect.bisect_left(keys, value)
        is_last = idx == len(keys)
        if is_last:
            last_key = keys[-1]
            prev_interval = self.intervals[last_key]
            if prev_interval[1] >= value: return
            elif prev_interval[1] == value-1:
                self.intervals[last_key] = [self.intervals[last_key][0], value]
            else:
                self.intervals[value] = [value, value]
                self.intervals.move_to_end(value)
            return            

        next_start = keys[idx]
        if next_start == value: return
        is_first = idx == 0
        next_interval = self.intervals[next_start]

        if is_first:
            if next_start == value+1:
                self.intervals[value] = [value, next_interval[1]]
                self.intervals.move_to_end(value, last=False)
                del self.intervals[next_start]
            else:
                self.intervals[value] = [value, value]
                self.intervals.move_to_end(value, last=False)
            return

        prev_start = keys[idx-1]
        prev_interval = self.intervals[prev_start]
        prev_end = prev_interval[1]

        if prev_end >= value: return

        if next_start == value+1:
            if prev_end == value-1:
                # merge!
                next_end = next_interval[1]
                self.intervals[prev_start] = [prev_start, next_end]
            else:
                items = list(self.intervals.items())
                items.insert(idx, (value, [value, next_interval[1]]))
                self.intervals = OrderedDict(items)

            del self.intervals[next_start]
            return
        
        elif prev_end < value:
            if prev_end == value-1:
                self.intervals[prev_start] = [prev_start, value]
            else:
                # insert between prev & next new interval
                items = list(self.intervals.items())
                items.insert(idx, (value, [value, value]))
                self.intervals = OrderedDict(items)
            return

        return          

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals.values())


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()