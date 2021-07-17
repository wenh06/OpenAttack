import OpenAttack as oa
import datasets
import torch


def dataset_mapping(x):
    return {
        "x": x["sentence"],
        "y": 1 if x["label"] > 0.5 else 0,
    }


def main():
    # choose a trained victim classification model
    # victim = oa.DataManager.load("Victim.BERT.SST")
    print("Build model")
    victim = oa.DataManager.load("Victim.ROBERTA.SST")
    print(f"type(victim) = {type(victim).__name__}")
    
    # choose device (deprecated, already on GPU)
    # device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    # victim = victim.to(device)
    
    # choose an evaluation dataset 
    dataset = datasets.load_dataset("sst", split="train[:100]").map(function=dataset_mapping)
    
    # choose Genetic as the attacker and initialize it with default parameters
    print("New Attacker")
    attacker = oa.attackers.GeneticAttacker()

    print("Start attack")
    options = {
        # TO ADD
    }
    # prepare for attacking
    attack_eval = oa.attack_evals.DefaultAttackEval(attacker, victim, **options)
    # launch attacks and print attack results 
    attack_eval.eval(dataset, visualize=True)


if __name__ == "__main__":
    main()
