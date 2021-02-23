from binarytree import bst


def search(bin_search_tree, number, path=''):
    if bin_search_tree.value == number:
        return f'Number {number} has been detected on way:\nRoot{path}'
    if number < bin_search_tree.value and bin_search_tree.left is not None:
        return search(bin_search_tree.left, number, path=f'{path}\nGo left')
    if number > bin_search_tree.value and bin_search_tree.right is not None:
        return search(bin_search_tree.right, number, path=f'{path}\nGo right')
    return f'Number {number} is not in tree!'


bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Enter number to find it: '))
print(search(bt, num))





