import json
import torch
import os
import pandas as pd

from torch import  nn
from termcolor import colored

from project1 import *

def main():
    print(colored('Project 1 running ...', 'cyan'))

    epochs = 75
    models = [ResNet(), DeepFCNet(), BasicCNN_bn(0.25)]
    weight_sharings = [True, False]
    auxiliary_losses = [True, False]
    dropout_siamese = 0.25
    repeats = 25

    result_list = []

    for model in models:
        for weight_sharing in weight_sharings:
            for auxiliary_loss in auxiliary_losses:
                for i in range(repeats):
                    model_cloned = type(model)()
                    train, test, train_target, test_target, train_classes, test_classes = generate_data()

                    siamese_model = train_model(model_cloned, train, train_target, train_classes,
                        test, test_target, test_classes, mini_batch_size=100, eta=1e-2, criterion=nn.CrossEntropyLoss(),
                        nb_epochs=epochs, momentum=0, optimizer_name='SGD', weight_sharing=weight_sharing,
                        auxiliary=auxiliary_loss, dropout=dropout_siamese, result_list=result_list)

    results_df = pd.DataFrame(result_list)
    results_df.to_csv("results.csv")

    print(colored('Project 1 done', 'cyan'))

if __name__ == "__main__":
    main()
