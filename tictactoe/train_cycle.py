from dual_network import dual_network
from self_play import self_play
from train_network import train_network
from evaluate_network import evaluate_network, update_best_player
from evaluate_best_player import evaluate_best_player


dual_network()
for i in range(10):
    print('Train', i, '====================')
    self_play()

    train_network()

    update_best_player = evaluate_network()

    if update_best_player:
        evaluate_best_player()