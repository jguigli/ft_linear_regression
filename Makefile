all: train predict accuracy graph

train:
	@cd srcs && python3 ./training_model.py
predict:
	@cd srcs && python3 ./predict.py
graph:
	@cd srcs && python3 ./graph.py
accuracy:
	@cd srcs && python3 ./algorithm_accuracy.py
clean:
	@rm ./data/thetas.csv