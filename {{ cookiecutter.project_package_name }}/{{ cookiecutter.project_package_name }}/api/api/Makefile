

VIRTUALENV_PATH=./venv

REQUIREMENTS_FILE_PATH=./requirements.frozen
TEST_REQUIREMENTS_FILE_PATH=./requirements.test.frozen


install_venv:
	@echo "Installing virtualenv..."
	sudo apt install python3.10-venv
	@echo "Done!"


create_venv:
	@echo "Creating virtualenv..."
	python3 -m venv "${VIRTUALENV_PATH}"
	@echo "Done!"


install_reqs_in_venv:
	@echo "Installing requirements..."
	${VIRTUALENV_PATH}/bin/pip install -r "${REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


install_test_reqs_in_venv:
	@echo "Installing test requirements..."
	${VIRTUALENV_PATH}/bin/pip install -r "${TEST_REQUIREMENTS_FILE_PATH}"
	@echo "Done!"


run_unit_tests:
	@echo "Running unit tests..."
	. ${VIRTUALENV_PATH}/bin/activate && ./scripts/run_unit_tests.sh && deactivate
	@echo "Done!"
