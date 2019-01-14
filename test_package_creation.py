from mypackage import inside_main
from mypackage.subpackage import inside_submain

inside_main.call()
inside_submain.call() 
print(__name__)