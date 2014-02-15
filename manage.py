from flask.ext.script import Manager
from jason import app
import nose

manager = Manager(app)

def test():
	nose.main(argv=['jason', '--failed'])

def main():
	manager.run()

if __name__ == '__main__':
	main()