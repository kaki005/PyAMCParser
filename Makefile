# .PHONYで定義することで、タスクランナーを簡単に定義できます

# install
.PHONY: install
install:
	rye pin 3.10
	rye sync
	rye run pre-commit install

# main.pyを実行する
.PHONY: run
run:
	rye run python amc_test.py

# pre-commitを明示的に実行する
.PHONY: pre-commit
pre-commit:
	rye run pre-commit run --all-files

.PHONY: test
test:
	rye run pytest tests

.PHONY: sweep
sweep:
	rye run wandb src/config/sweep.yaml
