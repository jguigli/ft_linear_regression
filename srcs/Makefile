all: train predict accuracy graph

train:
	@python3 ./training_model.py
predict:
	@python3 ./predict.py
graph:
	@python3 ./graph.py
accuracy:
	@python3 ./algorithm_accuracy.py
clean:
	@rm ../data/thetas.csv