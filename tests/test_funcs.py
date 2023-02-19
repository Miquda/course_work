import funcs

def test_hide_digits():
    assert funcs.hide_digits('1324987612349876') == ' 1324987******9876'
    assert funcs.hide_digits('13249876123498769898') == 'Счет **9898'


#    filter_transactions(filename):
#    sort_dict(operations):
#    hide_digits(account):
#    get_transactions(filename):