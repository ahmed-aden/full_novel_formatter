# Define virtual environment directory and requirements
VENV_DIR = myenv
REQUIREMENTS = requirements.txt
SCRIPT= page_format.py
PYCACHE = __pycache__

# default setup
all: setup run

# create virtual environment
setup:
	@echo "Creating virtual environment"
	python3 -m venv {VENV_DIR}
	${VENV_DIR}/bin/pip install -r ${REQUIREMENTS}

# Run the script
run: ${VENV_DIR}/bin/activate/install
	@echo "Running script"
	${VENV_DIR}/bin/python3 SCRIPT
	
# Clean up by removing virtual environment 
Clean:
	@echo "Cleaning up virtual environment & pycache"
	rm -rf ${VENV_DIR}
	rm -rf ${PYCACHE}

#TODO: ammend makefile by removing pycache as well

# Requirements.txt not present 
${REQUIREMENTS}:
	@echo "requests" >> REQUIREMENTS
	@echo "beautifulsoup" >> REQUIREMENTS







