import os
import copy
from torch import nn
from project1 import *

# Uncomment if you want the output in csv format.
# import pandas as pd


def main():

    print('Project 1 running ...')

    # defining the parameters of the execution
    epochs = 75
    models = [LeNet4(dropout=0.25)]
    weight_sharings = [True, False]
    # defines the use of auxliary loss. The first parameter of the tuple
    # is the weight of the auxiliary loss and the second parameter is the weight
    # of the primary loss
    auxiliary_losses = [(1, 1), (0, 1))]
    dropout_siamese=0.25
    repeats=25

    result_list=[]

    for model in models:
        for weight_sharing in weight_sharings:
            for auxiliary_loss in auxiliary_losses:
                for i in range(repeats):
                    model_cloned=copy.deepcopy(model)
                    train, test, train_target, test_target, train_classes, test_classes=generate_data()
                    siamese_model=train_model(model_cloned, train, train_target, train_classes,
                                                test, test_target, test_classes, mini_batch_size = 50, eta = 1e-2, criterion = nn.CrossEntropyLoss(),
                                                nb_epochs = epochs, momentum = 0, optimizer_name = 'SGD', weight_sharing = weight_sharing,
                                                auxiliary = auxiliary_loss, dropout = dropout_siamese, result_list = result_list)

    # Uncomment for csv output
    # results_df = pd.DataFrame(result_list)
    # results_df.to_csv("results.csv")

    print('Project 1 done')


if __name__ == "__main__":
    main()
