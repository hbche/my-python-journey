import pickle

def store_decision_tree(decision_tree, filename):
    with open(filename, "wb") as fw:
        pickle.dump(decision_tree, fw)
        
        
def grab_decision_tree(filename):
    with open(filename, "rb") as fr:
        return pickle.load(fr)