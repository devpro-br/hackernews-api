db_test_up:
	docker-compose -f docker-compose.test.yml up -d

db_test_down:
	docker-compose -f docker-compose.test.yml down

run_tests:
	docker-compose -f docker-compose.test.yml up -d && \
	sleep 1 && pytest && \
	docker-compose -f docker-compose.test.yml down

linter:
	pylint hackernews/**/*.py

clean:
	find ./ -name '*.pyc' -exec rm -f {} \;
	find ./ -name '__pycache__' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf .pytest_cache
