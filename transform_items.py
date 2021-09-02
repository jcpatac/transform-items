from collections import defaultdict

def create_item_list(depth, parent_id, parent_id_grouping):
    """
        This is an auxiliary function that groups the items
        into their respective parent nodes
    """
    
    # Sort siblings
    curr_list = sorted(parent_id_grouping[parent_id], key=lambda x: (x.get('seqId')))
    item_list = []
    
    for item in curr_list:
        item['depth'] = depth
        item_list.append(item)
        if (item['id'] in parent_id_grouping):
            item_list += create_item_list(depth + 1, item['id'], parent_id_grouping)
    return item_list

def transform_items(items):
    """
        This function structures a given list of dictionaries
        into a directory-like format
    """
    
    # Sort items based on parent key (with parent None at top)
    sorted_items = sorted(items, key=lambda x: (x.get('parent') is None, x.get('parent')), reverse=True)
    
    # Group items with common parent into an array
    # and put these groupings into a dictionary with the
    # parent id as key
    groups = defaultdict(list)
    for item in sorted_items:
        groups[item['parent']].append(item)
    new_dict = {}
    for item in groups.values():
        new_dict[item[0].get('parent') or 0] = item
    
    return create_item_list(0, 0, new_dict)


items = [
  { 'id': 2, 'seqId': 4, 'parent': 5, 'name': "index.tsx" },
  { 'id': 3, 'seqId': 3, 'parent': 1, 'name': "Sidebar" },
  { 'id': 4, 'seqId': 5, 'parent': 1, 'name': "Table" },
  { 'id': 7, 'seqId': 5, 'parent': 5, 'name': "SelectableDropdown.tsx" },
  { 'id': 5, 'seqId': 2, 'parent': 1, 'name': "AssignmentTable" },
  { 'id': 1, 'seqId': 1, 'parent': None, 'name': "components" },
  { 'id': 6, 'seqId': 2, 'parent': None, 'name': "controllers" },
]


if __name__ == "__main__":
    result = transform_items(items)
    for item in result:
        print(item)
