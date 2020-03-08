"""if __name__ == '__main__'"""
import testpackage

# Runs when we import it
print(testpackage.__name__)
print(__name__)

if __name__ == '__main__':
    print('I got invoked directly!')
