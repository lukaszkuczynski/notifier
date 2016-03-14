from model.diff import Diff

class ListComparator():
    '''
    classdocs
    '''

    def compare(self, previous_state, current_state):
        diff_value = self.get_diff_from_lists(previous_state, current_state)
        return Diff(diff_value)

    def get_diff_from_lists(self, previous_list, current_list):
        # print('previous', previous_list)
        # print('current', current_list)
        if (previous_list == None) :
            previous_set = set()
        else:
            previous_set = set(previous_list)
        current_set = set(current_list)
        return list(current_set - previous_set)


