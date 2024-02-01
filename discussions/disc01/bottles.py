"""Answer the following questions with your group. Step through the diagram to
check your answers.

1) What determines how many different frames appear in an environment diagram?

    - The number of functions defined in the code
    - The number of call expressions in the code
    - The number of return statements in the code
    - The number of times user-defined functions are called when running the
      code

2) What happens to the return value of pass(bottles)?

    - It is used as the new value of remaining in the global frame
    - It is used as the new value of bottles in the global frame
    - It is used as the new value of pass in the global frame
    - None of the above

3) What effect does the line bottles = 98 have on the global frame?

    - It temporarily changes the value bound to bottles in the global frame.
    - It permanently changes the value bound to bottles in the global frame.
    - It has no effect on the global frame.

ANSWERS:
    1) The number of times user-defined functions are called when running the
       code
    2) None of the above
    3) It has no effect on the global frame
"""

bottles = 99
take = 1

def pass_it(around):
    bottles = 98
    return take

remaining = bottles - pass_it(bottles)
bottles = remaining
