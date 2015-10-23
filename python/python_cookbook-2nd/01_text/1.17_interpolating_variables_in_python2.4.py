#!/usr/bin/env python

import string

# make a template from a string where some identifiers are marked with $
new_style = string.Template('This is $thing')
print type(new_style), new_style.substitute({'thing': 5})
# alternatively, you can pass keyword-arguments to 'substitue':
print new_style.substitute(thing=5)

# double $ signs make escape
# ${}
form_letter = '''Dear $customer,
I hope you are having a great time.
If you do not find Room $room to your satisfaction,
let us know. Please accept this $$5 coupon.
Sincerely,
$manager
${name}Inn'''
letter_template = string.Template(form_letter)
print letter_template.substitute({'name': 'Sleepy', 'customer': 'Fred Smith',
                                  'manager': 'Barney Mills', 'room': 307,
                                  })

# use local(), an artificial dict whose keys are the local variables
msg = string.Template('the square of $number is $square')
for number in range(10):
    square = number * number
    print msg.substitute(locals())
